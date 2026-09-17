# AGENTS.md — Conlang Project Guide

This file describes how to work on the repository. It is a maintainer/development guide, not part of the language grammar.

## Project purpose

This repository develops a naturalistic a priori constructed language. The goal is a coherent language system rather than an English-to-word substitution list: phonology, morphology, syntax, lexical structure, historical development, and usage should constrain one another.

Changes should therefore be evaluated both synchronically and diachronically. A form that works mechanically is not automatically a lexical item, and a plausible historical explanation is not automatically a productive modern rule.

## Repository structure

The repository is deliberately small and flat:

| File | Authority / purpose |
|---|---|
| `GRAMMAR.md` | Primary source for the current synchronic grammar and established historical evidence. |
| `LEXICON.tsv` | Primary lexical/root inventory, including status and historical relationships. |
| `EXAMPLES.tsv` | Provenance-bearing examples, tests, and analyses. Examples support testing but do not override grammar. |
| `STATUS.md` | Current development state, open questions, recovered decisions, and testing priorities. Not itself grammar. |
| `README.md` | Public-facing overview of the language and repository. Keep it descriptive rather than procedural. |
| `AGENTS.md` | Development and maintenance instructions for contributors and coding/automation agents. |

Do not add new top-level source files merely for convenience. Extend the existing sources unless the project's information architecture has genuinely become a bottleneck.

## Source authority

Use this precedence when interpreting the repository:

1. Explicitly established rules in `GRAMMAR.md`.
2. Stable lexical data in `LEXICON.tsv`.
3. Established examples in `EXAMPLES.tsv` as evidence of usage.
4. `STATUS.md` for current decisions, uncertainty, and unresolved questions.
5. Git history for provenance and superseded analyses.

When these sources disagree, do not silently resolve the disagreement. Preserve the evidence, identify the conflict, and record the unresolved issue in `STATUS.md` unless the requested change explicitly resolves it.

## Development status

Keep these analytical levels distinct:

- **ESTABLISHED / RULE** — explicitly adopted as part of the current language description.
- **ANALYZED** — an interpretation supported by evidence but not yet promoted to a productive rule.
- **EXPERIMENTAL** — a form or construction being tested.
- **UNRESOLVED / `?`** — evidence is insufficient to choose an analysis.
- **DEPRECATED** — retained for historical/provenance reasons but no longer current.

Do not promote an analyzed or experimental feature simply because it is typologically plausible, aesthetically attractive, frequent in generated examples, or easy to implement.

## Language-development principles

### Naturalism

Prefer interacting systems with plausible acquisition, processing, lexicalization, analogy, and historical development. Rare typological features are acceptable when their consequences are coherent.

Do not add isolated exotic features merely to increase typological novelty.

### Synchrony and diachrony

Keep modern grammar separate from historical explanation. Historical forms may motivate an analysis, but historical reconstruction does not by itself create a modern productive rule.

When developing a change, prefer ordinary historical mechanisms such as:

- sound change and conditioned allophony;
- morphological reanalysis;
- grammaticalization;
- analogy and paradigm leveling;
- lexicalization and semantic specialization;
- frequency-driven reduction or fusion;
- borrowing, when supported by the project's setting.

Preserve uncertain chronology as uncertain rather than inventing an ordering.

### Lexical structure

Build semantic families and lexical networks rather than treating the lexicon as a direct translation dictionary. Track polysemy, derivation, compounds, lexicalization, semantic drift, and historical relationships.

Do not create a separate lexical entry for a predictable inflected form. Create one when the form has become an independent lexeme, has an established lexical derivation, has irregular or unpredictable behavior, or has another documented reason to be lexicalized.

### Grammar-first testing

Before introducing a new rule, test it against existing:

- phonotactics and morphophonology;
- argument structure and alignment;
- case marking;
- verbal morphology and stem grades;
- NP structure;
- clause structure;
- pronouns and agreement;
- lexical derivation;
- historical sound laws;
- existing examples.

Use matched examples to distinguish competing analyses. Prefer the smallest change that explains the evidence without creating new exceptions.

## Editing rules

1. Read `STATUS.md` and the relevant part of `GRAMMAR.md` before making substantive changes.
2. Inspect the relevant lexical rows and examples before changing a lexical or grammatical analysis.
3. Preserve existing IDs.
4. Make the smallest change needed for the requested task.
5. Do not silently rewrite historical evidence to fit a current analysis.
6. Keep unresolved material explicitly unresolved.
7. Do not infer IPA, morphology, or historical forms that are not established.
8. Keep orthographic form, phonemic IPA, phonetic IPA, and reconstructed forms distinct.
9. Keep productive morphology distinct from lexicalized or historical material.
10. Update affected examples when a grammatical rule changes.
11. Update `STATUS.md` when a question is resolved, reopened, or materially changed.
12. Avoid unrelated cleanup in the same change unless it is necessary to prevent a real contradiction.

## Data conventions

### `LEXICON.tsv`

Required columns:

```text
id	form	ipa	type	pos	gloss	derived_from	status	notes
```

Use the established controlled vocabularies already documented in the repository. Use `?` for unknown or unresolved information and `—` for not applicable information.

`derived_from` should identify immediate lexical parents, not an entire ancestry chain.

### `EXAMPLES.tsv`

Required columns:

```text
id	text	ipa	translation	segmentation	gloss	grammar_refs	entry_refs	status	notes
```

Each example should be traceable to the grammar and lexical material it tests when those references are established.

### Glossing

Use Leipzig-style segmentation and grammatical glossing. Keep segmentation and gloss aligned as closely as possible. Project-specific abbreviations should be defined in the grammar rather than invented ad hoc in examples.

### IPA

Use only established phonemic contrasts. Do not manufacture phonetic detail to make a transcription look more complete. Historical reconstructions belong to the historical analysis, not the modern IPA field.

## Recommended workflow for substantive changes

### 1. Identify the dependency surface

Determine which of grammar, lexicon, examples, status, and historical analysis are affected. A change to one system may have mechanical consequences elsewhere.

### 2. Establish the evidence

Separate what is directly established from what is an interpretation or proposal. If the evidence underdetermines the result, preserve multiple analyses rather than forcing a choice.

### 3. Stress-test

Generate or inspect a small set of representative examples. For larger mechanical systems, test paradigms or balanced lexical samples rather than isolated examples.

### 4. Update authoritative sources

Put settled synchronic rules in `GRAMMAR.md`, lexical facts in `LEXICON.tsv`, and provenance-bearing examples in `EXAMPLES.tsv`. Use `STATUS.md` for unresolved issues and project state.

### 5. Check downstream effects

Look for broken segmentation, invalid forms, changed argument frames, stale references, contradictory examples, and historical analyses that no longer fit.

### 6. Review the diff

Before committing, verify that the diff contains only the intended changes and that no experimental material has been promoted accidentally.

## Linguistic architecture currently represented in the repository

The current working description includes:

- a four-vowel system with established long vowels;
- a consonant inventory including the orthographic correspondences `c = /ts/`, `v = /w/`, and `y = /j/`;
- weight-sensitive stress, with some weight details still under investigation;
- consonant-final lexical roots with distinct stem grades for nonfinite, linking/attributive, realis, and irrealis functions;
- verbal direction marking, object marking, person agreement, discourse marking, tense, and aspect;
- an active–stative / Split-S alignment under continued testing;
- a compact nominal case system with constructional extensions;
- mixed nominal and verbal strategies for property concepts and possession;
- nominalization and case-based converb constructions under development;
- lexicalized and derivational complexes whose behavior must be distinguished from productive morphology;
- a growing historical account involving conditioned sound change, reduction, reanalysis, and lexicalization.

These descriptions summarize the current repository state. The source files remain authoritative for exact forms, rules, and unresolved conditions.

## Validation checklist

Before considering a change complete, ask:

- Does the new form obey current phonotactics?
- Does its morphology correspond to an established template?
- Does its argument structure fit existing alignment/case behavior?
- Is it productive, lexicalized, historical, or merely experimental?
- Does the analysis require an unsupported new rule?
- Does an existing example contradict it?
- Are unresolved questions still marked as unresolved?
- Are IDs and references preserved?
- Are lexical entries limited to genuinely lexical material?
- If the change is historical, is its chronology actually supported?

The desired outcome is not maximal regularity. Naturalistic irregularity is welcome when it has a recoverable lexical, morphological, phonological, frequency, or historical motivation.
