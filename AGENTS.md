# AGENTS.md — Conlang Project Guide

This file describes how to work on the repository. It is a maintainer/development guide, not part of the language grammar.

## Repository structure

The repository is deliberately small and flat. **Do not add, remove, rename, move, split, merge, or otherwise alter files or directories unless the user explicitly instructs you to change the repository structure.** Do not create new files merely for convenience, to hold derived notes, or to reorganize information on your own.

| File | Authority / purpose |
| --- | --- |
| `GRAMMAR.md` | Primary source for synchronic phonology, prosody, and historical sound change. |
| `GRAMMAR.md` | Primary source for synchronic morphology and morphological constructions. |
| `GRAMMAR.md` | Primary source for synchronic syntax and syntactic constructions. |
| `LEXICON.tsv` | Primary lexical/root inventory, including status and historical relationships. |
| `EXAMPLES.tsv` | Provenance-bearing examples, tests, and analyses. Examples support testing but do not override grammar. |
| `STATUS.md` | Current development state, open questions, recovered decisions, and testing priorities. Not itself grammar. |
| `README.md` | Public overview of the language and repository. Descriptive rather than procedural. |
| `AGENTS.md` | Development and maintenance instructions for contributors and coding/automation agents. |
| `SCHEMA.json` | Authoritative JSON Schema for the structural representation of LEXICON.tsv and EXAMPLES.tsv used by automated validation. |

### Grammar authority

`GRAMMAR.md` is the single authoritative source for established phonology, morphology, syntax, prosody, and historical sound change. Use the relevant `G-PHON`, `G-MORPH`, or `G-SYN` section.

`LEXICON.tsv`, `EXAMPLES.tsv`, and `STATUS.md` retain their respective evidence/status roles.

## Source authority and conflict resolution

Use the applicable domain source as authoritative for established grammar, followed by stable lexical data and established examples for evidence. `STATUS.md` records current decisions and uncertainty; Git history records provenance and superseded analyses.

**When sources disagree:** Do not silently resolve the disagreement. Preserve the evidence, identify the conflict, and record it in `STATUS.md` with the label `CONFLICT: [source A] vs [source B] — [brief description]`. Link from affected sections. Do not change either source until the conflict is explicitly resolved via a documented decision.

## Development status levels

Keep these analytical levels distinct:

- **ESTABLISHED / RULE** — Explicitly adopted as part of the current language description.
- **ANALYZED** — Supported interpretation not yet promoted to a productive rule.
- **EXPERIMENTAL** — A form or construction being tested.
- **UNRESOLVED / `?`** — Evidence is insufficient to choose an analysis.
- **DEPRECATED** — Retained for historical/provenance reasons but no longer current.

Do not promote an analyzed or experimental feature simply because it is typologically plausible, aesthetically attractive, frequent in generated examples, or easy to implement.

## Development principles

### Naturalism

Prefer interacting systems with plausible acquisition, processing, lexicalization, analogy, and historical development. Rare typological features are acceptable when their consequences are coherent.

Do not add isolated exotic features merely to increase typological novelty.

### Synchrony and diachrony

Keep modern grammar separate from historical explanation. Historical forms may motivate an analysis, but historical reconstruction does not by itself create a modern productive rule.

When developing a historical change, prefer ordinary mechanisms such as sound change, conditioned allophony, morphological reanalysis, grammaticalization, analogy, paradigm leveling, lexicalization, semantic specialization, frequency-driven reduction or fusion, and borrowing when supported by the setting.

## Grammar-first testing

Before introducing a new rule, test it against the relevant domain and its dependencies:

- Phonotactics and morphophonology
- Argument structure and alignment
- Case marking and agreement
- Verbal morphology and stem grades
- NP and clause structure
- Pronouns and person marking
- Lexical derivation patterns
- Historical sound laws
- Existing examples

Use matched examples to distinguish competing analyses. Prefer the smallest change that explains the evidence without creating new exceptions.

## Data conventions

### `LEXICON.tsv`

Required columns:

```text
id\tform\tipa\ttype\tpos\tgloss\tderived_from\tstatus\tnotes
```

Use established controlled vocabularies. Use `?` for unknown/unresolved information and `—` for not applicable.

### `EXAMPLES.tsv`

Required columns:

```text
id\ttext\tipa\ttranslation\tsegmentation\tgloss\tgrammar_refs\tentry_refs\tstatus\tnotes
```

Each example should be traceable to the grammar and lexical material it tests when those references are established.

### IPA conventions

Use only established phonemic contrasts. Do not manufacture phonetic detail to appear more complete. Historical reconstructions belong in historical analysis, not in modern IPA fields.

Keep orthographic, phonemic, phonetic, and reconstructed forms distinctly labeled.

## Editing rules

1. Read `STATUS.md` and the relevant domain source before making substantive changes.
2. Inspect relevant lexical rows and examples before changing a lexical or grammatical analysis.
3. Preserve existing IDs (do not renumber or reuse).
4. Make the smallest change needed for the requested task.
5. Do not silently rewrite historical evidence to fit current analysis.
6. Keep unresolved material explicitly unresolved.
7. Do not infer IPA, morphology, or historical forms that are not established.
8. Keep orthographic, phonemic, phonetic, and reconstructed forms distinct.
9. Keep productive morphology distinct from lexicalized or historical material.
10. Update all affected examples when a grammatical rule changes.
11. Update `STATUS.md` when a question is resolved, reopened, or materially changed.
12. Avoid unrelated cleanup unless necessary to prevent a real contradiction.
13. **Do not alter repository file structure unless the user explicitly instructs the agent to do so.**

## Red flags: When not to commit

- Creating a lexical entry for an inflected form when it is predictable from morphology.
- Adding IPA or morphology that is not established.
- Promoting experimental forms by frequency alone.
- Rewriting historical analysis to fit current grammar.
- Changing a root's status without updating its derivatives.
- Breaking example segmentation without updating grammar references.
- Resolving a conflict silently.
- Creating or moving files without explicit structural authorization.

## Workflow for substantive changes

### 1. Identify the dependency surface

Determine which domain and data sources are affected. A change to one system may have mechanical consequences elsewhere.

### 2. Establish the evidence

Separate directly established facts from interpretations or proposals. If evidence underdetermines the result, preserve multiple candidate analyses rather than forcing a single choice.

### 3. Stress-test with examples

Generate or inspect representative examples. For larger mechanical systems, test paradigms or balanced lexical samples rather than isolated cases.

### 4. Update authoritative sources

Update the applicable domain source first, then affected `LEXICON.tsv` or `EXAMPLES.tsv` data, then `STATUS.md` when a decision changes development state.

### 5. Check downstream effects

Look for broken segmentation, invalid forms, stale grammar references, changed lexical relationships, and historical analyses that no longer fit.

### 6. Review the diff before committing

Verify that the diff contains only the intended changes. Confirm that no experimental material was promoted accidentally, IDs were preserved, conflicts were documented, and no unauthorized structural changes were made.

## Pre-commit validation checklist

**Fast check:**

- Does the new form obey current phonotactics?
- Does its morphology match an established template?
- Are unresolved questions still marked unresolved?
- Are IDs and references preserved?
- Is the change minimal and focused?
- Was repository structure left unchanged unless explicitly authorized?

**Thorough check:**

- Does the analysis require an unsupported new rule?
- Does an existing example contradict it?
- Have all affected derivatives been updated?
- Is the change productive, lexicalized, historical, or experimental?
- If historical, is the chronology supported or marked uncertain?
- Are lexical entries limited to genuinely lexical material?

The desired outcome is not maximal regularity. Naturalistic irregularity is welcome when it has a recoverable lexical, morphological, phonological, frequency, or historical motivation.

## For automation and coding agents

All automated validation should use `SCHEMA.json` as the authoritative specification for valid `LEXICON.tsv` and `EXAMPLES.tsv` structure. Cross-row and cross-file checks remain validation-script responsibilities.
