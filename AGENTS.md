# AGENTS.md — Conlang Project Guide
Maintenance guide for contributors and coding agents. Not part of the language description.

**Do not add, remove, rename, move, split, or merge files or directories unless explicitly instructed to change repository structure.** No convenience files, no derived-note files, no self-directed reorganization. This rule has no exceptions elsewhere in this document.

## Files

| File | Authority |
| --- | --- |
| `GRAMMAR.md` | Authoritative for phonology, morphology, syntax, prosody, historical sound change. Cite by `G-PHON` / `G-MORPH` / `G-SYN` section. |
| `LEXICON.tsv` | Authoritative lexical/root inventory: forms, status, historical relationships. |
| `EXAMPLES.tsv` | Provenance-bearing examples and tests. Evidence only — examples never override grammar. |
| `STATUS.md` | Current state, open questions, recovered decisions, testing priorities. Not grammar. |
| `SCHEMA.json` | Authoritative structure spec for the two TSVs. Used by automated validation. |
| `README.md` | Public overview. Descriptive, not procedural. |
| `AGENTS.md` | This file. |

## Task routing

Read only what the task requires initially. Apply mandatory downstream checks when the change affects dependent material. Do not run unrelated parts of the workflow merely for completeness.

| Task | Read first | Then |
| --- | --- | --- |
| Add / edit a lexeme | `G-PHON` + existing rows of the same `type` | Checklist → commit |
| Add / edit an example | The `G-` sections it tests + its referenced lexicon rows | Checklist → commit |
| Change or add a grammar rule | `STATUS.md` + the full affected domain section | Full workflow below |
| Answer an open design question | `STATUS.md` + relevant `G-` section | 3–5 options → recommend one → record in authoritative source + `STATUS.md` → move on |
| Resolve a source conflict | Both sources + `STATUS.md` | Document the decision, then apply it |

## Dependency checks

Every change triggers its downstream checks. These are mandatory and stated once:

```text
GRAMMAR.md changed         → inspect LEXICON.tsv + EXAMPLES.tsv for affected
                             forms, analyses, segmentations, refs, IPA, derivations
LEXICON/EXAMPLES changed   → validate the complete modified file against SCHEMA.json,
                             then check linguistically against GRAMMAR.md
any substantive change     → review README.md and STATUS.md before committing
```

## Source authority and conflicts

Domain source is authoritative for established grammar; lexicon and examples supply evidence; `STATUS.md` records decisions and uncertainty; Git history holds provenance and superseded analyses.

When sources disagree, **do not silently resolve it.** Preserve both analyses and record the conflict in `STATUS.md` as:

```text
CONFLICT: [source A] vs [source B] — [brief description]
```

For a factual/source conflict, do not change either source until the conflict has been resolved by a documented decision. For a genuinely creative design question, use the decision process under **Design principles** instead of treating underdetermination as a source conflict.

## Status levels

Keep these distinct and never blur them:

- **ESTABLISHED / RULE** — adopted as part of the current description.
- **ANALYZED** — supported interpretation, not yet a productive rule.
- **EXPERIMENTAL** — under test.
- **UNRESOLVED / `?`** — evidence insufficient to choose.
- **DEPRECATED** — retained for provenance, no longer current.

Do not promote a feature because it is typologically plausible, aesthetically attractive, frequent in generated examples, or easy to implement.

## Data conventions

`LEXICON.tsv` columns:

```text
id	form	ipa	type	pos	gloss	derived_from	status	notes
```

`EXAMPLES.tsv` columns:

```text
id	text	ipa	translation	segmentation	gloss	grammar_refs	entry_refs	status	notes
```

- Surface forms (`form`, `text`) contain no hyphens. Hyphens belong in `segmentation` and other analysis fields.
- `?` = unknown/unresolved. `—` = not applicable. Use established controlled vocabularies.
- Preserve IDs. Never renumber or reuse.
- Keep orthographic, phonemic, phonetic, and reconstructed forms distinctly labeled. Orthographic `c` is never an IPA phoneme.

### IPA

Every non-`?` IPA field must carry primary stress (`ˈ`) per the current stress rule. Analyze each field against `GRAMMAR.md` — segment legality, stress placement, word boundaries, conditioned realizations — rather than regex-checking characters. Use only established contrasts; invent no phonetic detail. Reconstructions belong in historical analysis, not modern IPA fields.

For conditioned realizations, consult the applicable `G-PHON` section. Do not duplicate grammar rules here.

## Pre-commit checklist

Run the applicable portions before every commit. Do not perform unrelated checks merely for completeness.

- [ ] Form obeys current phonotactics; morphology matches an established template.
- [ ] If `LEXICON.tsv` or `EXAMPLES.tsv` changed, the complete modified file validates against `SCHEMA.json`; IDs and references preserved.
- [ ] Every non-`?` IPA field affected by the change is analyzed against the phonology, stress included.
- [ ] No lexical entry for a form predictable from productive morphology.
- [ ] No IPA, morphology, or historical form asserted beyond what is established.
- [ ] Root status changes propagated to all derivatives.
- [ ] Affected examples updated; no broken segmentation or stale `grammar_refs`.
- [ ] Nothing experimental promoted by frequency alone; nothing historical rewritten to fit current analysis.
- [ ] Unresolved material still marked unresolved; any factual/source conflict documented, not resolved silently.
- [ ] `STATUS.md` updated if a question was resolved, reopened, or materially changed.
- [ ] Repository structure unchanged unless explicitly authorized.
- [ ] Diff contains only the intended change. No unrelated cleanup.

The goal is not maximal regularity. Naturalistic irregularity is welcome when it has a recoverable lexical, morphological, phonological, frequency, or historical motivation.

## Workflow for substantive changes

For grammar-rule changes and anything with mechanical consequences elsewhere.

1. **Scope.** Identify which domain and data sources the change touches.
2. **Evidence.** Separate established facts from interpretation. When evidence is insufficient to resolve a factual/source conflict, preserve the competing analyses. When the issue is genuinely a creative design choice, use the decision process below to make a bounded decision.
3. **Test.** Stress-test against matched examples and the dependencies below. Prefer the smallest change that explains the evidence without creating new exceptions.
4. **Update.** Apply the documented decision to the authoritative source, then update affected TSVs and `STATUS.md` as required.
5. **Check.** Run the dependency checks and the applicable pre-commit checklist above.

Dependencies to test a new rule against: phonotactics and morphophonology; argument structure and alignment; case and agreement; verbal morphology and stem grades; NP and clause structure; pronouns and person marking; derivation patterns; historical sound laws; existing examples.

## Post-push check

After pushing any repository change, re-read `STATUS.md` against the resulting repository state. If the push changes established decisions, open questions, testing priorities, or recovered decisions, update `STATUS.md` in a follow-up change before treating the work as complete.

## Design principles

### Naturalism

Prefer interacting systems with plausible acquisition, processing, lexicalization, analogy, and historical development. Rare features are fine when their consequences are coherent. Do not add isolated exotic features to increase typological novelty.

### Decisions over methodology

When the language is underdetermined, decide. Present 3–5 genuinely distinct options, each with its typological motivation and its creative consequence; recommend one on grounds of plausibility, internal coherence, and established direction; record it and move on.

The recommendation is a well-motivated proposal, not an objectively required answer, and never overrides the user's creative authority. Do not reopen a settled question to build a more elaborate framework. Use tests and matrices only where they can distinguish viable alternatives or expose a contradiction. Prefer a simple, explicitly provisional canon over unresolved scaffolding when the stakes are low. Mark results as design decisions rather than manufacturing certainty.

When evidence is insufficient to resolve a factual/source conflict, preserve the competing analyses rather than forcing a decision. When the issue is creative underdetermination, do not mistake the absence of unique evidence for a reason to defer indefinitely.

### Synchrony and diachrony

Keep modern grammar separate from historical explanation. History may motivate an analysis; reconstruction alone never creates a modern productive rule.

Preferred mechanisms for historical development: sound change, conditioned allophony, morphological reanalysis, grammaticalization, analogy, paradigm leveling, lexicalization, semantic specialization, frequency-driven reduction or fusion, and setting-supported borrowing.
