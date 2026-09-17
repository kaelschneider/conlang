# Status

**Last updated:** 2026-09-17  
**Phase:** Morphology established; syntax testing underway  
**Repository structure:** Minimal LLM-oriented structure

## Canonical files

- `GRAMMAR.md` — current synchronic grammar and established diachronic evidence
- `LEXICON.tsv` — canonical lexical/root inventory
- `EXAMPLES.tsv` — example and test corpus

## Established

### Phonology
- Vowels: `/a e i u/`; long vowels are `aa ee ii uu` when established
- Consonants: `/p t k c m n s h w j r/` as the synchronic inventory, with `c = /ts/` and `j = /j/`
- Surface syllable: `(C)V(C)`
- Historical `*p > h`; historical `*p` remains distinct from `*h`
- `t, k > c` before `/i/`; `tc > c`
- `*ndt > nt:` is attested historically/lexically, not established as a productive synchronic rule
- `wu > u`; `yi > ye` in established developments
- `ku-p-i > kupi > kuhi > kui` is established
- `mente > mende`; `menta > menda`
- `menme` and `menra` have unresolved conditioning and possible reduced realizations
- Stress is weight-sensitive: rightmost heavy syllable, otherwise penultimate; exact weight definition remains open
- IPA is recorded explicitly in lexical and example data rather than inferred from spelling

### Morphology
- Finite verb template: `(DIRECTION) (OBJECT) STEM (AUX/DERIV) AGENT (DISCOURSE) TENSE (ASPECT)`
- Stem grades: `-a-` NONFINITE, `-e-` LINKING/ATTRIBUTIVE, `-u-` REALIS, `-i-` IRREALIS
- Stem-grade vowel is final in the root/stem; grades are independent of directional `i-` and `a-`
- Direction: `i-` toward, `a-` away, `Ø` neutral; direction is verbal rather than nominal
- Spatial case polarity is compositional: five spatial cases combine with `Ø/i-/a-`
- Object markers: `Ø` local, `n-` nonlocal, `s-` reflexive, `r-` reciprocal; exactly one object slot
- If a vowel is required for NONLOCAL without direction, `e-` may serve as support
- AUX/DERIV: `-re-` progressive, `-ke-` continuative, `-me-` habitual, `-se-` inchoative, `-te-` opposite of inchoative
- AUX/DERIV forms take linking `-e-`; AUX/DERIV and final aspect are separate slots and may co-occur
- `-we-` and productive `-w-` dropped from canonical system
- Agreement: `-k-` 1SG, `-t-` 2SG, `-p-` 3SG; no verbal plural agreement
- Discourse: `-h-` exclamative, `-y-` interrogative
- Tense: `-i-` nonpast, `-a-` past
- Aspect: `Ø` imperfective, `-n` perfect
- Eight base nominal cases: ABS, ERG, GEN, LOC, SUPER, INE, PATH, COM
- Spatial directional expansion: LOC→ALL/ABL, SUPER→SUBLATIVE/DELATIVE, INE→ILLATIVE/ELATIVE, PATH→directional path readings
- COM polysemy: animate neutral COM, inanimate INST, animate + direction BEN
- Dedicated verbal applicatives eliminated; instrumental and benefactive meanings use nominal case constructions
- Constructional readings include partitive via GEN, dative-like via LOC + `i-`, essive via LOC + stative predicate, and translative via ESSIVE + `i-ra`
- Converbs are intended through nominalizers + case endings; participial relatives combine stem grades with dedicated participial morphology; exact inventories remain unresolved
- Established complex forms include `kerurekin`, `kui`, `kutye`, and `hukka`
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

These forms occur in the existing test corpus but their lexical/derivational analyses are not yet normalized. They are retained as experimental lexical entries.

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
