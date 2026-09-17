# Conlang

A naturalistic a priori constructed language project. This repository contains the current grammatical description, lexical inventory, and example corpus for the language.

## Language overview

The language is being developed as a coherent linguistic system: phonology, morphology, syntax, lexicon, usage, and historical development are intended to constrain one another.

Current work includes:

- a four-vowel system with established long vowels;
- a consonant system with `c = /ts/`, `v = /w/`, and `y = /j/` in the established orthography;
- weight-sensitive stress and established morphophonological processes;
- consonant-final verbal roots with distinct stem grades for nonfinite, linking/attributive, realis, and irrealis functions;
- verbal direction marking, object marking, person agreement, discourse marking, tense, and aspect;
- an active–stative / Split-S alignment system under continued testing;
- nominal case marking with constructional extensions;
- nominalization and case-based converb constructions;
- lexical derivation, compounds, and lexicalized complexes;
- a developing historical account based on conditioned sound change, reduction, reanalysis, analogy, and lexicalization.

Exact rules, forms, and unresolved conditions belong in `GRAMMAR.md`, with lexical/data structures in the TSV files and project-state notes in `STATUS.md`.

## Repository structure

| File | Role |
|---|---|
| `GRAMMAR.md` | Current consolidated grammar: phonology, morphology, syntax, prosody, and historical sound change. |
| `LEXICON.tsv` | Canonical lexical and root inventory, including lexical relationships and status. |
| `EXAMPLES.tsv` | Provenance-bearing examples and test corpus. |
| `STATUS.md` | Current development state, uncertainty, and testing priorities. |
| `AGENTS.md` | Development and maintenance guide for contributors and automation. |
| `SCHEMA.json` | JSON Schema for structural validation of LEXICON.tsv and EXAMPLES.tsv. |

The repository is intentionally small and flat. Repository structure must not be altered by agents unless the user explicitly instructs the agent to add, remove, rename, move, split, or merge files or directories.

## Source authority

1. `GRAMMAR.md` is authoritative for phonology, morphology, syntax, prosody, and historical sound change.
4. `LEXICON.tsv` is authoritative for lexical entries and root data.
5. `EXAMPLES.tsv` records evidence and testing; examples do not override established grammar.
6. `STATUS.md` records development state and uncertainty; it is not itself grammar.
7. Git history records change history and superseded analyses.

When sources conflict, do not silently choose one. Preserve the conflict and record it in `STATUS.md` until it is explicitly resolved.

## Evidence and status

The project distinguishes established rules from analyses and experiments. In particular:

- **RULE / established** — explicitly adopted as part of the current language description.
- **ANALYZED** — supported interpretation that has not yet been promoted to a rule.
- **EXPERIMENTAL** — form or construction being tested.
- **`?` / unresolved** — evidence does not currently determine the analysis.
- **DEPRECATED** — retained for historical or provenance reasons but no longer current.

Typological plausibility, resemblance to another language, generated frequency, or intuition does not by itself make a form canonical.

## Lexicon

`LEXICON.tsv` contains lexical material, not every possible grammatical form. Predictable inflection normally does not receive a separate lexical entry.

Lexical derivation, lexicalization, historical independence, irregularity, or other established lexical behavior may justify a separate entry. When a derivational relationship is uncertain, the uncertainty should be preserved rather than replaced by an invented etymology.

## Examples

`EXAMPLES.tsv` is both a corpus and a regression-testing resource. Examples should preserve their status and provenance. Experimental examples can test proposed grammar, but repeated experimental usage does not automatically establish a rule.

## Working on the language

Changes should be checked against the relevant grammar domain, phonology/morphology/syntax dependencies, lexical patterns, examples, and historical analysis. See `AGENTS.md` for the detailed development workflow and maintenance rules.

The project favors explicit evidence, reversible analysis, and historically motivated naturalistic development over arbitrary regularization or isolated novelty.
