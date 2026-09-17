# Status

**Last updated:** 2026-09-17  
**Phase:** Morphology established; syntax testing underway  
**Repository structure:** Minimal LLM-oriented structure

## Canonical files

- `GRAMMAR.md` — current synchronic grammar
- `LEXICON.tsv` — canonical lexical/root inventory
- `EXAMPLES.tsv` — example and test corpus

## Established

### Phonology
- Vowels: `/a e i u/`
- Consonants: `/p t k c m n s h w j r/`
- Surface syllable: `(C)V(C)`
- Word-initial `*p > h`
- `t, k > c` before `/i/`
- `tc > c`
- `wu > u`
- `yi > ye`
- Stress is weight-sensitive: rightmost heavy syllable, otherwise penultimate

### Morphology
- Finite verb template: `(DIRECTION) (OBJECT) STEM (AUX/DERIV) AGENT (DISCOURSE) TENSE (ASPECT)`
- Stem grades: `-a-` NONFINITE, `-e-` LINKING/ATTRIBUTIVE, `-u-` REALIS, `-i-` IRREALIS
- Direction: `i-` toward, `a-` away, `Ø` neutral
- Object markers: `Ø` local, `n-` nonlocal, `s-` reflexive, `r-` reciprocal
- AUX/DERIV: `-re-` progressive, `-ke-` continuative, `-me-` habitual, `-se-` inchoative, `-te-` opposite of inchoative
- Agreement: `-k-` 1SG, `-t-` 2SG, `-p-` 3SG; no verbal plural agreement
- Discourse: `-h-` exclamative, `-y-` interrogative
- Tense: `-i-` nonpast, `-a-` past
- Aspect: `Ø` imperfective, `-n` perfect
- Eight base nominal cases: ABS, ERG, GEN, LOC, SUPER, INE, PATH, COM
- Dedicated verbal applicatives eliminated; instrumental/benefactive meanings use nominal case constructions

### Syntax
- SOV is the current canonical order.
- Attributive modifiers precede nouns.
- Stative predicates follow subjects.
- Mixed Split-S alignment is established in broad terms, with exact conditioning unresolved.
- Participial relatives precede nouns; finite relatives follow nouns.
- Converbs and nominalized clauses are the intended primary clause-combining strategy.

## Known inconsistencies / cleanup needed

### Q-001 — `ka` vs. `ku` 'hold'

The historical root inventory identifies `*k` with modern `ka` 'hold', while existing test clauses use `ku` as the surface hold stem (`kui`, `kutye`, `kerurekin` contains a separate `keru` 'carry'). This must be resolved rather than inferred.

### Q-002 — `kerande`, `sare`, `keru`

These forms occur in the existing test corpus but their lexical/derivational analyses were not present in the root inventory. They are retained as experimental lexical entries until their analyses are normalized.

## Open questions

### Phonology
- Q-003: precise definition of syllable weight for stress
- Q-004: conditioning of remaining historical developments such as `menme` and `menra`

### Morphology
- Q-005: exact nominalizer inventory and converb/case mappings
- Q-006: dedicated participial forms
- Q-007: whether any additional productive derivational morphology exists

### Syntax
- Q-008: exact person/animacy/volitionality conditioning of Split-S
- Q-009: genitive position
- Q-010: negative marker and position in the verb template
- Q-011: independent adposition system, if any
- Q-012: converb switch-reference / subject continuity
- Q-013: information-structure mechanisms

## Immediate testing priorities

1. Resolve `ka`/`ku` hold-stem discrepancy.
2. Generate matched Split-S clauses across person, animacy, and volitionality.
3. Test pre- vs. post-nominal genitives.
4. Design and test negative morphology.
5. Test reflexive and reciprocal object marking.
6. Test all 18 nominal case/polarity forms in natural clauses.
7. Normalize `kerande`, `sare`, and `keru` lexical analyses.
8. Expand the lexicon only after productive derivational patterns are sufficiently clear.
