# AGENTS.md — Conlang Project Guide

This file describes how to work on the repository. It is a maintainer/development guide, not part of the language grammar.

## Purpose

This repository develops a naturalistic a priori constructed language. The goal is a coherent language system rather than an English-to-word substitution list: phonology, morphology, syntax, lexical structure, historical development, and usage should constrain one another.

Changes should be evaluated both synchronically and diachronically. A form that works mechanically is not automatically a lexical item, and a plausible historical explanation is not automatically a productive modern rule.

## Repository structure

The repository is deliberately small and flat:

| File | Authority / purpose |
| --- | --- |
| `GRAMMAR.md` | Primary source for current synchronic grammar and established historical evidence. |
| `LEXICON.tsv` | Primary lexical/root inventory, including status and historical relationships. |
| `EXAMPLES.tsv` | Provenance-bearing examples, tests, and analyses. Examples support testing but do not override grammar. |
| `STATUS.md` | Current development state, open questions, recovered decisions, and testing priorities. Not itself grammar. |
| `README.md` | Public overview of the language and repository. Descriptive rather than procedural. |
| `AGENTS.md` | Development and maintenance instructions for contributors and coding/automation agents. |

Do not add new top-level source files merely for convenience. Extend existing sources unless the project's information architecture has genuinely become a bottleneck.

## Source authority and conflict resolution

Use this precedence when interpreting the repository:

1. Explicitly established rules in `GRAMMAR.md`.
2. Stable lexical data in `LEXICON.tsv`.
3. Established examples in `EXAMPLES.tsv` as evidence of usage.
4. `STATUS.md` for current decisions, uncertainty, and unresolved questions.
5. Git history for provenance and superseded analyses.

**When sources disagree:** Do not silently resolve the disagreement. Preserve the evidence, identify the conflict, and record it in `STATUS.md` with the label `CONFLICT: [source A] vs [source B] — [brief description]`. Link from both affected sections. Do not change either source until the conflict is explicitly resolved via a documented decision.

## Development status levels

Keep these analytical levels distinct:

- **ESTABLISHED / RULE** — Explicitly adopted as part of the current language description. Productive in at least one established paradigm or documented lexical family.
- **ANALYZED** — An interpretation supported by evidence (≥2 independent examples, no phonological/grammatical contradictions). Not yet promoted to a productive rule.
- **EXPERIMENTAL** — A form or construction being tested. May appear in examples but should not be treated as canonical.
- **UNRESOLVED / `?`** — Evidence is insufficient to choose an analysis. Preserve all candidate interpretations.
- **DEPRECATED** — Retained for historical/provenance reasons but no longer current. Mark clearly.

**Promotion criteria:**

- EXPERIMENTAL → ANALYZED: Supported by ≥2 independent examples with no phonological or grammatical contradictions found during testing.
- ANALYZED → RULE: Productive in ≥1 morphological paradigm or lexical family; integrated into GRAMMAR with documented consequences; all downstream effects traced (examples, lexicon, historical analysis).

Do not promote an analyzed or experimental feature simply because it is typologically plausible, aesthetically attractive, frequent in generated examples, or easy to implement.

## Development principles

### Naturalism

Prefer interacting systems with plausible acquisition, processing, lexicalization, analogy, and historical development. Rare typological features are acceptable when their consequences are coherent.

Do not add isolated exotic features merely to increase typological novelty.

### Synchrony and diachrony

Keep modern grammar separate from historical explanation. Historical forms may motivate an analysis, but historical reconstruction does not by itself create a modern productive rule.

When developing a historical change, prefer ordinary mechanisms such as:

- Sound change and conditioned allophony
- Morphological reanalysis
- Grammaticalization
- Analogy and paradigm leveling
- Lexicalization and semantic specialization
- Frequency-driven reduction or fusion
- Borrowing (when supported by the project's setting)

Preserve uncertain chronology as uncertain rather than inventing an ordering.

### Lexical structure

Build semantic families and lexical networks rather than treating the lexicon as a direct translation dictionary. Track polysemy, derivation, compounds, lexicalization, semantic drift, and historical relationships.

Do not create a separate lexical entry for a predictable inflected form. Create one when the form has become an independent lexeme, has an established lexical derivation, has irregular or unpredictable behavior, or has another documented reason to be lexicalized.

### Grammar-first testing

Before introducing a new rule, test it against:

- Phonotactics and morphophonology
- Argument structure and alignment
- Case marking and agreement
- Verbal morphology and stem grades
- NP and clause structure
- Pronouns and person marking
- Lexical derivation patterns
- Historical sound laws
- Existing examples (no contradictions)

Use matched examples to distinguish competing analyses. Prefer the smallest change that explains the evidence without creating new exceptions.

## Data conventions

### `LEXICON.tsv`

Required columns:

```
id	form	ipa	type	pos	gloss	derived_from	status	notes
```

Use established controlled vocabularies. Use `?` for unknown/unresolved information and `—` for not applicable.

`derived_from` identifies immediate lexical parents only, not the full ancestry chain.

### `EXAMPLES.tsv`

Required columns:

```
id	text	ipa	translation	segmentation	gloss	grammar_refs	entry_refs	status	notes
```

Each example should be traceable to the grammar and lexical material it tests when those references are established.

### Glossing conventions

Use Leipzig-style segmentation and grammatical glossing. Keep segmentation and gloss aligned. Project-specific abbreviations should be defined in GRAMMAR, not invented ad hoc in examples.

### IPA conventions

Use only established phonemic contrasts. Do not manufacture phonetic detail to appear more complete. Historical reconstructions belong in the historical analysis section, not in the modern IPA field.

Keep orthographic form, phonemic IPA, phonetic IPA, and reconstructed forms distinctly labeled.

## Editing rules

1. Read `STATUS.md` and the relevant section of `GRAMMAR.md` before making substantive changes.
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
12. Avoid unrelated cleanup in the same change unless necessary to prevent a real contradiction.

## Red flags: When not to commit

- **Creating a lexical entry for an inflected form** — If it's predictable from morphology, it shouldn't be in LEXICON.
- **Adding IPA or morphology that isn't established** — Inferences belong in STATUS or notes, not in canonical fields.
- **Promoting experimental forms by frequency alone** — High frequency in examples does not create a rule.
- **Rewriting historical analysis to fit current grammar** — Preserve historical evidence even when it complicates modern description.
- **Changing a root's status without updating its derivatives** — A root change cascades through LEXICON and EXAMPLES.
- **Breaking example segmentation without updating grammar references** — Broken references make examples worthless.
- **Resolving a conflict silently** — Conflicts require explicit documented decisions in STATUS.

## Workflow for substantive changes

### 1. Identify the dependency surface

Determine which of grammar, lexicon, examples, status, and historical analysis are affected. A change to one system may have mechanical consequences elsewhere.

Create a mental map:

- Does this change existing morphology? → Check all affected roots and derivatives.
- Does this add a new rule? → What examples test it? What exceptions exist?
- Does this change a lexical entry? → Are there examples using it? Does it affect derived words?
- Does this affect historical analysis? → Does the current grammar still follow from it?

### 2. Establish the evidence

Separate directly established facts from interpretations or proposals. If evidence underdetermines the result, preserve multiple candidate analyses rather than forcing a single choice.

Write down:

- What examples or data motivated this change?
- Are there alternative analyses? If so, why did you choose this one?
- What existing rules does this interact with?

### 3. Stress-test with examples

Generate or inspect representative examples. For larger mechanical systems, test paradigms or balanced lexical samples rather than isolated cases.

Before committing:

- Does the form follow current phonotactics?
- Does its morphology match an established template?
- Does its argument structure fit existing alignment/case behavior?
- Are there contradictions in existing examples?

### 4. Update authoritative sources in order

1. **GRAMMAR.md** — Synchronic rules, established morphophonology, documented consequences.
2. **LEXICON.tsv** — Lexical facts, status, historical relationships.
3. **EXAMPLES.tsv** — Provenance-bearing examples and tests.
4. **STATUS.md** — Unresolved issues, recovered decisions, conflicts, and project state.
5. **Git commit message** — Link to STATUS if resolving an open question.

### 5. Check downstream effects

Look for:

- Broken segmentation in examples
- Invalid forms or contradictions
- Changed argument frames affecting other entries
- Stale references in grammar sections
- Historical analyses that no longer fit the data

### 6. Review the diff before committing

Verify that the diff contains only the intended changes. Confirm that:

- No experimental material has been promoted accidentally
- All affected examples have been updated
- Conflicts are documented, not hidden
- No IDs were renumbered or reused

## Pre-commit validation checklist

**Fast check (before every commit):**

- Does the new form obey current phonotactics?
- Does its morphology match an established template?
- Are unresolved questions still marked as unresolved?
- Are IDs and references preserved?
- Is the change minimal and focused?

**Thorough check (for grammar or lexical changes):**

- Does the analysis require an unsupported new rule?
- Does an existing example contradict it?
- Have all affected derivatives been updated?
- Is the change productive, lexicalized, historical, or merely experimental?
- If historical, is the chronology actually supported or marked uncertain?
- Are lexical entries limited to genuinely lexical material (not predictable inflection)?
- If removing material, is it marked DEPRECATED rather than deleted?

The desired outcome is not maximal regularity. Naturalistic irregularity is welcome when it has a recoverable lexical, morphological, phonological, frequency, or historical motivation.

## Common mistakes

- **Treating frequency as productivity.** An experimental form appearing in many generated examples is still experimental until explicitly tested and promoted.
- **Inferring intermediate steps.** If a form's etymology or derivation is unclear, mark it unresolved rather than inventing a plausible chain.
- **Silently updating one side of a conflict.** Conflicts must be resolved explicitly in STATUS and documented in the commit.
- **Over-normalizing the lexicon.** If an entry has irregular behavior with good historical reasons, keep it irregular.
- **Assuming historical forms are modern rules.** A sound change or reanalysis explains how a form arose, not whether it's still productive.
- **Creating multiple lexical entries for the same root in different statuses.** One entry per root; use the `status` column to track its development.

## For automation and coding agents

Validation scripts should enforce:

- TSV syntax and column presence (LEXICON, EXAMPLES)
- IDs are stable and not reused
- All `grammar_refs` in EXAMPLES point to documented sections in GRAMMAR.md
- All `entry_refs` in EXAMPLES point to valid IDs in LEXICON.tsv
- No example contains both a status field and contradicts a RULE in GRAMMAR.md
- Segmentation and gloss are length-aligned in examples
- No lexical entry has a form that is a predictable inflection of another entry (without justification in notes)

Cross-file consistency checks:

- All roots in EXAMPLES exist in LEXICON.tsv or are marked as reconstructed/proposed
- All morphological processes mentioned in GRAMMAR.md appear in at least one example
- No deprecated entries are referenced in active examples without a note
- Conflicts logged in STATUS.md are traceable to diffs in GRAMMAR/LEXICON/EXAMPLES
