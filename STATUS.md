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
- Consonants: `/p t k c m n s h w j r/` as orthographic inventory, with `c = /ts/` and `j = /j/`
- Surface syllable: `(C)V(C)`
- Word-initial `*p > h`
- `t, k > c` before `/i/`
- `tc > c`
- `wu > u`
- `yi > ye`
- Stress is weight-sensitive: rightmost heavy syllable, otherwise penultimate; exact weight definition remains open
- IPA is now recorded explicitly in lexical and example data rather than inferred from spelling

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
- Leipzig Glossing Rules are the default interlinear glossing convention

### Hold-form analysis

The previous `ka` vs. `ku` inconsistency is resolved as a morphological distinction rather than two competing lexical forms:

- `L-0016 ka` is the canonical lexeme/citation form for HOLD.
- `k-u` → `ku` is the REALIS stem form.
- `k-u-i` → `kui` is REALIS + NONPAST.
- `ku` and `kui` are predictable inflected forms and are not separate lexicon entries.

This analysis should be revisited only if later evidence demonstrates lexicalization or an irregular paradigm.

## Known inconsistencies / cleanup needed

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

1. Generate matched Split-S clauses across person, animacy, and volitionality.
2. Test pre- vs. post-nominal genitives.
3. Design and test negative morphology.
4. Test reflexive and reciprocal object marking.
5. Test all 18 nominal case/polarity forms in natural clauses.
6. Normalize `kerande`, `sare`, and `keru` lexical analyses.
7. Expand the lexicon only after productive derivational patterns are sufficiently clear.
