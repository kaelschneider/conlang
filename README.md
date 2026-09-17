# Conlang

A naturalistic a priori constructed language project. The language is developed as a coherent system in which phonology, morphology, syntax, lexicon, usage, and historical development constrain one another.

## Typological profile

The current language can be described as a **head-final, predominantly agglutinative language with substantial historical fusion and reduction**. Its grammatical profile includes:

- **Basic clause order:** SOV.
- **Alignment:** active-stative / Split-S analysis, with the exact conditioning of person, animacy, and volitionality still under testing.
- **Nominal morphology:** eight basic cases—ABS, ERG, GEN, LOC, SUPER, INE, PATH, and COM—used for core argument marking and spatial/relational functions.
- **Verbal morphology:** finite verbs require person agreement. Person contrasts are 1/2/3, without a singular/plural distinction in the agreement markers.
- **Direction:** verbal `i-` marks movement toward/goalward and `a-` movement away/sourceward. Directional constructions retain the noun's case morphology.
- **Object status:** the verbal object slot distinguishes LOCAL (`n-`) from NLOC (`Ø`), with additional reflexive and reciprocal values. Before consonant-initial stems, LOCAL `n-` surfaces as `en-` by `n + C → enC`.
- **TAM and verbal categories:** stem grades distinguish NONFINITE, LINKING, REALIS, and IRREALIS; tense distinguishes NONPAST and PAST; aspect distinguishes IMPERFECTIVE and PERFECT.
- **Case constructions:** spatial cases participate in directional constructions; LOC plus verbal direction also supports a distinct dative-like construction through the object slot.
- **COM semantics:** `-me` has association/accompaniment as its core value, with contextual instrumental use; `O-me + i-VERB` has a benefactive reading and `O-me + a-VERB` a malefactive reading.
- **Clause combining:** nominalization plus case is the intended basis for converbial constructions.
- **Prosody:** stress is predictable and weight-sensitive.
- **Phonology and historical development:** a four-vowel system, a ten-consonant synchronic inventory, context-dependent orthographic `c`, and a layered history of palatalization, consonant weakening, sequence repair, and cluster reduction.

The language is intended to exhibit ordinary historical consequences—fusion, reduction, lexicalization, analogy, and semantic specialization—rather than a perfectly regular synchronically transparent system.

### Orthography

The established orthography uses:

| Letter | Pronunciation / function |
|---|---|
| `c` | context-dependent spelling: `/ɕ/` from historical `-ki > -ci`; `/tɕ/` from historical `-ti > -ci` |
| `v` | `/w/` |
| `y` | `/j/` |
| `aa ee ii uu` | long vowels |

Orthographic `c` is **not a synchronic phoneme**. IPA records the actual pronunciation rather than the written letter.

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
2. `LEXICON.tsv` is authoritative for lexical entries and root data.
3. `EXAMPLES.tsv` records evidence and testing; examples do not override established grammar.
4. `STATUS.md` records development state and uncertainty; it is not itself grammar.
5. Git history records change history and superseded analyses.

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
