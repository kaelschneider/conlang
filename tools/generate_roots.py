#!/usr/bin/env python3
"""Generate reproducible inherited-root lexical candidates from the language architecture.

This is the semantic/phonological candidate engine only. It never edits canonical
LEXICON.tsv, GRAMMAR.md, or EXAMPLES.tsv.

Requires: PyYAML (pip install pyyaml)
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import re
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any

import yaml

GENERATOR_VERSION = "0.1.0"


@dataclass(frozen=True)
class Node:
    id: str
    label: str
    domains: tuple[str, ...]
    features: tuple[str, ...]
    salience: float
    frequency: float
    cultural: float
    grammatical: float


@dataclass(frozen=True)
class Edge:
    source: str
    relation: str
    target: str


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a mapping at top level")
    return data


def require_keys(data: dict[str, Any], keys: list[str], label: str) -> None:
    missing = [k for k in keys if k not in data]
    if missing:
        raise ValueError(f"{label}: missing required keys: {', '.join(missing)}")


def read_tsv_forms(path: Path) -> set[str]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if "form" not in (reader.fieldnames or []):
            raise ValueError(f"{path}: missing 'form' column")
        return {row["form"].strip() for row in reader if row.get("form", "").strip()}


def read_grammar(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_grammar(config: dict[str, Any], grammar_text: str) -> None:
    anchors = config["validation"]["grammar_anchors"]
    checks = [
        ("vowels", anchors["vowels"]),
        ("consonants", anchors["consonants"]),
        ("root_shapes", anchors["root_shapes"]),
        ("final_exclusion_phrase", anchors["final_exclusion_phrase"]),
    ]
    for name, needle in checks:
        if needle not in grammar_text:
            raise ValueError(
                f"GRAMMAR.md reconciliation failed for {name!r}: {needle!r} not found"
            )


def validate_config(config: dict[str, Any]) -> None:
    require_keys(config, ["generator", "inventory", "phonology", "semantic_pressure", "semantic_graph"], "config")
    inv = config["inventory"]
    if not inv["minimum"] <= inv["default_target"] <= inv["maximum"]:
        raise ValueError("inventory target must lie within configured bounds")
    shapes = config["phonology"]["root_shapes"]
    if abs(sum(shapes.values()) - 1.0) > 1e-9:
        raise ValueError("root-shape weights must sum to 1.0")
    excluded = config["phonology"]["root_final_exclude"]
    for shape in ("VC", "CVC"):
        if set(excluded.get(shape, [])) - set(config["phonology"]["consonants"]):
            raise ValueError(f"unknown final-exclusion phoneme in {shape}")
    if config["sound_symbolism"]["deterministic_mapping_forbidden"] is not True:
        raise ValueError("deterministic sound symbolism must remain forbidden")


def parse_graph(config: dict[str, Any]) -> tuple[dict[str, Node], list[Edge], dict[str, list[Edge]]]:
    nodes = {}
    for raw in config["semantic_graph"]["nodes"]:
        node = Node(
            id=raw["id"],
            label=raw["label"],
            domains=tuple(raw["domains"]),
            features=tuple(raw.get("features", [])),
            salience=float(raw["salience"]),
            frequency=float(raw["frequency"]),
            cultural=float(raw["cultural"]),
            grammatical=float(raw["grammatical"]),
        )
        if node.id in nodes:
            raise ValueError(f"duplicate semantic node: {node.id}")
        nodes[node.id] = node

    edges: list[Edge] = []
    out: dict[str, list[Edge]] = defaultdict(list)
    for raw in config["semantic_graph"]["relations"]:
        if len(raw) != 3:
            raise ValueError(f"invalid relation: {raw!r}")
        edge = Edge(str(raw[0]), str(raw[1]), str(raw[2]))
        if edge.source not in nodes or edge.target not in nodes:
            # Seed graph may intentionally mention future expansion nodes; those are forbidden
            # because the architecture should be closed and reviewable.
            raise ValueError(f"relation references unknown semantic node: {edge}")
        edges.append(edge)
        out[edge.source].append(edge)
    return nodes, edges, out


def normalize(values: dict[str, float]) -> dict[str, float]:
    if not values:
        return {}
    lo = min(values.values())
    hi = max(values.values())
    if math.isclose(lo, hi):
        return {k: 1.0 for k in values}
    return {k: (v - lo) / (hi - lo) for k, v in values.items()}


def weighted_pagerank(nodes: dict[str, Node], edges: list[Edge], damping: float = 0.85) -> dict[str, float]:
    n = len(nodes)
    outgoing: dict[str, list[str]] = defaultdict(list)
    incoming: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        outgoing[edge.source].append(edge.target)
        incoming[edge.target].append(edge.source)

    rank = {node_id: 1.0 / n for node_id in nodes}
    for _ in range(100):
        new_rank: dict[str, float] = {}
        sink_mass = sum(rank[node_id] for node_id in nodes if not outgoing[node_id])
        for node_id in nodes:
            incoming_mass = 0.0
            for source in incoming[node_id]:
                denom = len(outgoing[source])
                if denom:
                    incoming_mass += rank[source] / denom
            new_rank[node_id] = (1.0 - damping) / n + damping * (
                incoming_mass + sink_mass / n
            )
        delta = sum(abs(new_rank[k] - rank[k]) for k in nodes)
        rank = new_rank
        if delta < 1e-10:
            break
    return rank


def build_centrality(nodes: dict[str, Node], edges: list[Edge], config: dict[str, Any]) -> dict[str, float]:
    degree = defaultdict(int)
    for edge in edges:
        degree[edge.source] += 1
        degree[edge.target] += 1
    degree_n = normalize({k: float(degree[k]) for k in nodes})
    pr = normalize(weighted_pagerank(nodes, edges))
    pressure = {}
    weights = config["semantic_pressure"]
    for node_id, node in nodes.items():
        centrality = weights["semantic_centrality"] * pr[node_id]
        connectivity = weights["network_connectivity"] * degree_n[node_id]
        frequency = weights["communicative_frequency"] * node.frequency
        cultural = weights["cultural_salience"] * node.cultural
        grammatical = weights["grammatical_utility"] * node.grammatical
        pressure[node_id] = centrality + connectivity + frequency + cultural + grammatical
    return normalize(pressure)


def choose_shape(rng: random.Random, shapes: dict[str, float]) -> str:
    roll = rng.random()
    cumulative = 0.0
    for shape, weight in shapes.items():
        cumulative += float(weight)
        if roll <= cumulative:
            return shape
    return next(reversed(shapes))


def largest_remainder_counts(total: int, weights: dict[str, float]) -> dict[str, int]:
    raw = {k: total * v for k, v in weights.items()}
    base = {k: math.floor(v) for k, v in raw.items()}
    remainder = total - sum(base.values())
    order = sorted(raw, key=lambda k: raw[k] - base[k], reverse=True)
    for key in order[:remainder]:
        base[key] += 1
    return base


def random_weighted(rng: random.Random, items: list[Any], weights: list[float]) -> Any:
    if not items:
        raise ValueError("weighted choice on empty collection")
    return rng.choices(items, weights=weights, k=1)[0]


def domain_weight(node: Node, domain_counts: dict[str, int], total_so_far: int, config: dict[str, Any]) -> float:
    bounds = config["semantic_pressure"]["domain_share"]
    domain = node.domains[0]
    if total_so_far <= 0:
        return 1.0
    share = domain_counts[domain] / total_so_far
    if share < bounds["minimum_soft"]:
        return float(bounds["underweight_factor"])
    if share > bounds["maximum_soft"]:
        return float(bounds["overweight_factor"])
    return 1.0


def make_family_seeds(nodes: dict[str, Node], edges: list[Edge], centrality: dict[str, float]) -> list[dict[str, Any]]:
    families: list[dict[str, Any]] = []
    seen: set[str] = set()
    for node_id, node in nodes.items():
        family_id = f"F-{node_id}"
        seed_key = family_id
        if seed_key not in seen:
            families.append({
                "family_id": family_id,
                "center": node_id,
                "relations": [],
                "neighbors": [],
                "distance": "very_close",
                "affinity": centrality[node_id],
                "family_stage_bias": "initial",
            })
            seen.add(seed_key)
    for edge in edges:
        family_id = f"F-{edge.source}-{edge.relation}-{edge.target}"
        if family_id in seen:
            continue
        families.append({
            "family_id": family_id,
            "center": edge.source,
            "relations": [edge.relation],
            "neighbors": [edge.target],
            "distance": "close",
            "affinity": 0.5 * (centrality[edge.source] + centrality[edge.target]),
            "family_stage_bias": "initial",
        })
        seen.add(family_id)
    # Add selected two-step families. These represent emergent semantic neighborhoods,
    # not claims of lexical derivation.
    by_source: dict[str, list[Edge]] = defaultdict(list)
    for edge in edges:
        by_source[edge.source].append(edge)
    for node_id, first_edges in by_source.items():
        for first in first_edges:
            second_edges = by_source.get(first.target, [])
            for second in second_edges[:6]:
                family_id = f"F-{node_id}-{first.relation}-{first.target}-{second.relation}-{second.target}"
                if family_id in seen:
                    continue
                families.append({
                    "family_id": family_id,
                    "center": node_id,
                    "relations": [first.relation, second.relation],
                    "neighbors": [first.target, second.target],
                    "distance": "moderate",
                    "affinity": 0.45 * centrality[node_id] + 0.275 * centrality[first.target] + 0.275 * centrality[second.target],
                    "family_stage_bias": "specialized",
                })
                seen.add(family_id)
    return families


def distance_band(distance: str) -> str:
    return distance


def lexicalization_bias(distance: str, priors: dict[str, dict[str, float]]) -> dict[str, float]:
    return dict(priors[distance])


def family_stage(rng: random.Random, config: dict[str, Any], family_bias: str) -> str:
    weights = dict(config["family_model"]["family_stage_weights"])
    if family_bias in weights:
        weights[family_bias] *= 1.5
    return random_weighted(rng, list(weights), list(weights.values()))


def category_behavior_for(features: set[str], rng: random.Random, config: dict[str, Any]) -> str:
    weights = dict(config["category_behavior"])
    if "state" in features:
        weights["stative_leaning"] *= 1.5
    if "impact_manipulation" in features or "continuity_change" in features:
        weights["verb_leaning"] *= 1.35
    if "material" in features or "animate" in features:
        weights["noun_leaning"] *= 1.20
    return random_weighted(rng, list(weights), list(weights.values()))


def probe_role_for(features: set[str], rng: random.Random, config: dict[str, Any]) -> str:
    weights = dict(config["probe_policy"])
    # Remove non-probability controls.
    weights.pop("diagnostic_features", None)
    weights.pop("specialized_features", None)
    weights.pop("never_force_generic", None)
    if features.intersection(config["probe_policy"]["diagnostic_features"]):
        weights["diagnostic"] *= 2.5
    if features.intersection(config["probe_policy"]["specialized_features"]):
        weights["specialized"] *= 2.5
    return random_weighted(rng, list(weights), list(weights.values()))


def phonological_features(form: str, config: dict[str, Any]) -> list[str]:
    manner = {
        "p": "stop", "t": "stop", "k": "stop",
        "m": "nasal", "n": "nasal",
        "s": "fricative", "h": "fricative",
        "w": "approximant", "j": "approximant", "r": "liquid",
    }
    return [manner.get(ch, f"vowel:{ch}") for ch in form]


def sound_symbolic_score(form: str, semantic_features: set[str], config: dict[str, Any]) -> float:
    profile = config["sound_symbolism"]["tendencies"]
    manner_map = {
        "stop": {"p", "t", "k"},
        "nasal": {"m", "n"},
        "fricative": {"s", "h"},
        "approximant": {"w", "j"},
        "liquid": {"r"},
    }
    score = 0.0
    applicable = 0
    for feature in semantic_features:
        if feature not in profile:
            continue
        applicable += 1
        pref = profile[feature]
        cm = set().union(*(manner_map[m] for m in pref.get("preferred_consonant_manners", [])))
        pv = set(pref.get("preferred_vowels", []))
        consonants = [ch for ch in form if ch in config["phonology"]["consonants"]]
        vowels = [ch for ch in form if ch in config["phonology"]["vowels"]]
        part = 0.0
        if consonants:
            part += sum(ch in cm for ch in consonants) / len(consonants)
        if vowels:
            part += sum(ch in pv for ch in vowels) / len(vowels)
        score += part / 2.0
    if applicable == 0:
        return 0.0
    return score / applicable


def generate_forms_for_shape(shape: str, rng: random.Random, config: dict[str, Any], count: int) -> list[str]:
    vowels = list(config["phonology"]["vowels"])
    consonants = list(config["phonology"]["consonants"])
    weights = config["phonology"]["phoneme_weights"]
    forms: list[str] = []
    for _ in range(count):
        if shape == "C":
            forms.append(random_weighted(rng, consonants, [weights[c] for c in consonants]))
        elif shape == "VC":
            allowed_final = [c for c in consonants if c not in config["phonology"]["root_final_exclude"]["VC"]]
            forms.append(
                random_weighted(rng, vowels, [weights[v] for v in vowels])
                + random_weighted(rng, allowed_final, [weights[c] for c in allowed_final])
            )
        elif shape == "CVC":
            allowed_final = [c for c in consonants if c not in config["phonology"]["root_final_exclude"]["CVC"]]
            forms.append(
                random_weighted(rng, consonants, [weights[c] for c in consonants])
                + random_weighted(rng, vowels, [weights[v] for v in vowels])
                + random_weighted(rng, allowed_final, [weights[c] for c in allowed_final])
            )
        else:
            raise ValueError(f"unsupported root shape: {shape}")
    return forms


def choose_root_form(
    semantic_features: set[str],
    shape: str,
    rng: random.Random,
    config: dict[str, Any],
    used_forms: set[str],
    candidate_pool_size: int = 32,
) -> str:
    candidates = []
    attempts = 0
    while len(candidates) < candidate_pool_size and attempts < candidate_pool_size * 5:
        attempts += 1
        form = generate_forms_for_shape(shape, rng, config, 1)[0]
        if form not in used_forms and form not in candidates:
            candidates.append(form)
    if not candidates:
        raise RuntimeError(f"phonological space exhausted for shape {shape}")
    effect = float(config["sound_symbolism"]["maximum_effect_on_rank"])
    scored = []
    for form in candidates:
        ss = sound_symbolic_score(form, semantic_features, config)
        scored.append((ss + rng.random() * effect, form))
    scored.sort(reverse=True)
    return scored[0][1]


def orthographic(form: str, config: dict[str, Any]) -> str:
    mapping = config["phonology"]["orthography"]
    return "".join(mapping.get(ch, ch) for ch in form)


def allocate_shape_targets(total: int, config: dict[str, Any]) -> dict[str, int]:
    return largest_remainder_counts(total, config["phonology"]["root_shapes"])


def quantile_bucket(value: float, buckets: list[dict[str, Any]]) -> dict[str, Any]:
    for bucket in buckets:
        if value <= float(bucket["centrality_max"]):
            return bucket
    return buckets[-1]


def plan_family_sizes(
    families: list[dict[str, Any]],
    centrality: dict[str, float],
    config: dict[str, Any],
    target: int,
    rng: random.Random,
) -> dict[str, int]:
    """Assign long-tailed family sizes, then reconcile exactly to the target root count."""
    buckets = config["family_model"]["family_size_buckets"]
    sizes: dict[str, int] = {}

    for family in families:
        c = centrality[family["center"]]
        bucket = quantile_bucket(c, buckets)
        if rng.random() < float(bucket["simple_probability"]):
            size = 1
        else:
            lo = int(bucket["size_min"])
            hi = int(bucket["size_max"])
            size = rng.randint(lo, hi)
        sizes[family["family_id"]] = size

    # Reconcile the stochastic family-size draw with the requested total while
    # preserving each bucket's intended minimum/maximum range.
    minimum_total = len(families)
    if target < minimum_total:
        raise RuntimeError(
            f"target {target} is smaller than the number of semantic families {minimum_total}"
        )

    while sum(sizes.values()) < target:
        eligible = []
        weights = []
        for family in families:
            bucket = quantile_bucket(centrality[family["center"]], buckets)
            cap = int(bucket["size_max"])
            current = sizes[family["family_id"]]
            if current < cap:
                eligible.append(family)
                # Central families are more likely to grow additional members.
                weights.append(max(0.01, centrality[family["center"]] + 0.05))
        if not eligible:
            raise RuntimeError("family-size capacity exhausted before reaching target")
        family = random_weighted(rng, eligible, weights)
        sizes[family["family_id"]] += 1

    while sum(sizes.values()) > target:
        eligible = []
        weights = []
        for family in families:
            current = sizes[family["family_id"]]
            if current > 1:
                eligible.append(family)
                weights.append(max(0.01, 1.05 - centrality[family["center"]]))
        if not eligible:
            raise RuntimeError("cannot reduce family sizes to target without empty families")
        family = random_weighted(rng, eligible, weights)
        sizes[family["family_id"]] -= 1

    return sizes


def root_distance(family_distance: str) -> str:
    return {
        "very_close": "very_close",
        "close": "close",
        "moderate": "moderate",
        "distant": "distant",
        "very_distant": "very_distant",
    }.get(family_distance, "moderate")


def semantic_distance_from_path(family: dict[str, Any]) -> str:
    if family["distance"] == "very_close":
        return "very_close"
    if family["distance"] == "close":
        return "close"
    if family["distance"] == "moderate":
        return "moderate"
    return "distant"


def make_root_id(index: int) -> str:
    return f"R-{index:04d}"


def generate_candidates(
    config: dict[str, Any],
    nodes: dict[str, Node],
    edges: list[Edge],
    seed: int,
    target: int,
    existing_forms: set[str],
) -> dict[str, Any]:
    rng = random.Random(seed)

    centrality = build_centrality(nodes, edges, config)
    families = make_family_seeds(nodes, edges, centrality)
    if not families:
        raise ValueError("semantic graph produced no family seeds")

    shape_targets = allocate_shape_targets(target, config)
    domain_counts: dict[str, int] = defaultdict(int)
    used_forms = set(existing_forms)
    candidates: list[dict[str, Any]] = []
    family_counts: dict[str, int] = defaultdict(int)

    family_sizes = plan_family_sizes(families, centrality, config, target, rng)
    family_remaining = dict(family_sizes)
    family_weights_base = [max(0.001, f["affinity"]) for f in families]
    attempts = 0
    max_attempts = target * 50

    while len(candidates) < target and attempts < max_attempts:
        attempts += 1
        remaining_shapes = []
        remaining_shape_weights = []
        for shape, target_count in shape_targets.items():
            current = sum(1 for c in candidates if c["root_shape"] == shape)
            remaining = target_count - current
            if remaining > 0:
                remaining_shapes.append(shape)
                remaining_shape_weights.append(remaining)
        shape = random_weighted(rng, remaining_shapes, remaining_shape_weights)

        weights = []
        for family, base_weight in zip(families, family_weights_base):
            remaining = family_remaining[family["family_id"]]
            if remaining <= 0:
                weights.append(0.0)
                continue
            node = nodes[family["center"]]
            penalty = domain_weight(node, domain_counts, len(candidates), config)
            weights.append(base_weight * penalty * remaining)

        eligible_families = [f for f in families if family_remaining[f["family_id"]] > 0]
        eligible_weights = [
            weights[i] for i, f in enumerate(families)
            if family_remaining[f["family_id"]] > 0
        ]
        family = random_weighted(rng, eligible_families, eligible_weights)
        node = nodes[family["center"]]
        features = set(node.features)

        # Two-step families inherit the second target's conceptual feature when available.
        for neighbor_id in family["neighbors"]:
            features.update(nodes[neighbor_id].features)

        form = choose_root_form(features, shape, rng, config, used_forms)
        used_forms.add(form)
        ortho = orthographic(form, config)

        band = semantic_distance_from_path(family)
        lex_bias = lexicalization_bias(band, config["lexicalization_priors"])
        stage = family_stage(rng, config, family["family_stage_bias"])
        category = category_behavior_for(features, rng, config)
        probe = probe_role_for(features, rng, config)
        sound_score = sound_symbolic_score(form, features, config)

        semantic_neighbors = [nodes[n].label for n in family["neighbors"]]
        relations = list(family["relations"])
        family_counts[family["family_id"]] += 1
        family_remaining[family["family_id"]] -= 1
        domain_counts[node.domains[0]] += 1

        root_index = len(candidates) + 1
        candidate = {
            "root_id": make_root_id(root_index),
            "root_form": ortho,
            "root_shape": shape,
            "phonological_features": phonological_features(form, config),
            "semantic_center": node.label,
            "semantic_domain": node.domains[0],
            "semantic_subdomain": node.domains[1] if len(node.domains) > 1 else node.domains[0],
            "semantic_neighbors": semantic_neighbors,
            "semantic_relations": relations,
            "semantic_distance": band,
            "conceptual_salience": round(centrality[node.id] * 0.5 + node.salience * 0.5, 6),
            "expected_frequency": round(node.frequency * 0.55 + centrality[node.id] * 0.45, 6),
            "lexicalization_bias": lex_bias,
            "family_affinity": round(family["affinity"], 6),
            "derivational_affinity": round(0.5 * node.grammatical + 0.5 * (1.0 if category != "neutral" else 0.5), 6),
            "sound_symbolic_profile": {
                "semantic_features": sorted(features),
                "soft_match_score": round(sound_score, 6),
                "maximum_rank_effect": config["sound_symbolism"]["maximum_effect_on_rank"],
            },
            "probe_role": probe,
            "family_id": family["family_id"],
            "family_stage": stage,
            "lexicalization_status": "candidate",
            "category_behavior": category,
            "generation_seed": seed,
            "generation_version": config["generator"]["version"],
        }
        candidates.append(candidate)

    if len(candidates) != target:
        raise RuntimeError(
            f"could not generate target count {target}; produced {len(candidates)} after {attempts} attempts"
        )

    meta = {
        "generator": config["generator"],
        "generated_on": str(date.today()),
        "seed": seed,
        "target": target,
        "architecture": {
            "root_shapes": config["phonology"]["root_shapes"],
            "root_final_exclude": config["phonology"]["root_final_exclude"],
            "semantic_pressure_weights": config["semantic_pressure"],
            "semantic_graph_nodes": len(nodes),
            "semantic_graph_edges": len(edges),
            "semantic_graph_families": len(families),
        },
        "candidate_count": len(candidates),
        "shape_counts": {
            shape: sum(1 for c in candidates if c["root_shape"] == shape)
            for shape in shape_targets
        },
        "domain_counts": dict(sorted(domain_counts.items())),
    }
    return {"metadata": meta, "candidates": candidates}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_tsv(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = data["metadata"]["generator"].get("output_fields") or [
        "root_id",
        "root_form",
        "root_shape",
        "semantic_center",
        "semantic_domain",
        "semantic_distance",
        "family_id",
        "family_stage",
        "lexicalization_status",
        "category_behavior",
        "probe_role",
        "generation_seed",
        "generation_version",
    ]
    fields = [f for f in fields if f in data["candidates"][0]]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in data["candidates"]:
            writer.writerow({
                key: json.dumps(row[key], ensure_ascii=False, separators=(",", ":"))
                if isinstance(row[key], (dict, list))
                else row[key]
                for key in fields
            })


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("tools/root_generation.yaml"))
    parser.add_argument("--grammar", type=Path, default=Path("GRAMMAR.md"))
    parser.add_argument("--lexicon", type=Path, default=Path("LEXICON.tsv"))
    parser.add_argument("--output-json", type=Path, default=Path("root_candidates.json"))
    parser.add_argument("--output-tsv", type=Path, default=Path("root_candidates.tsv"))
    parser.add_argument("--seed", type=int, required=True, help="Explicit reproducibility seed.")
    parser.add_argument("--count", type=int, default=None, help="Root count; defaults to configured target.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_yaml(args.config)
    validate_config(config)

    target = args.count if args.count is not None else int(config["inventory"]["default_target"])
    minimum = int(config["inventory"]["minimum"])
    maximum = int(config["inventory"]["maximum"])
    if not minimum <= target <= maximum:
        raise SystemExit(f"count must be between {minimum} and {maximum}")

    grammar_text = read_grammar(args.grammar)
    if config["validation"]["require_grammar_reconciliation"]:
        validate_grammar(config, grammar_text)

    existing_forms = set()
    if config["validation"]["reject_existing_lexicon_collisions"]:
        existing_forms = read_tsv_forms(args.lexicon)

    nodes, edges, _ = parse_graph(config)
    result = generate_candidates(config, nodes, edges, args.seed, target, existing_forms)
    result["metadata"]["input_data_version"] = hashlib.sha256(
        args.config.read_bytes()
    ).hexdigest()[:16]
    result["metadata"]["grammar_version_anchor"] = hashlib.sha256(
        grammar_text.encode("utf-8")
    ).hexdigest()[:16]
    result["metadata"]["lexicon_version_anchor"] = hashlib.sha256(
        args.lexicon.read_bytes()
    ).hexdigest()[:16]

    # Expose configured output fields for the TSV writer.
    result["metadata"]["generator"]["output_fields"] = config["output"]["json_fields"]
    write_json(args.output_json, result)
    write_tsv(args.output_tsv, result)
    print(json.dumps(result["metadata"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
