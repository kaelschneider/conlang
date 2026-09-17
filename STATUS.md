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
- Consonants: `/p t k c m n s h w j r/`; established orthography uses `c = /ts/`, `v = /w/`, and `y = /j/`
- Surface syllable: `(C)V(C)`
- Historical `*p > h`; historical `*p` remains distinct from historical `*h`
- Historical `p > h` before `/i/` in the relevant historical environment; `h > Ø` between vowels in developments such as `kuhi > kui`
- `t, k > c` before `/i/`; `tc > c`
- `*ndt > nt:` is attested historically/lexically, not established as a productive synchronic rule
- `wu > u`; `yi > ye` in established developments
- `ku-p-i > kupi > kuhi > kui` is established
- `mente > mende`; `menta > menda`
- `menme` and `menra` have unresolved conditioning and possible reduced realizations
- Stress is weight-sensitive: rightmost heavy syllable, otherwise penultimate; exact weight definition remains open
- In IPA fields, keyboard `:` may represent IPA `ː` for length/gemination

### Morphology
- Finite verb template: `(DIRECTION) (OBJECT) STEM (AUX/DERIV) AGENT (DISCOURSE) TENSE (ASPECT)`
- Finite verbs require person agreement
- Stem grades: `-a-` NONFINITE, `-e-` LINKING/ATTRIBUTIVE, `-u-` REALIS, `-i-` IRREALIS
- Stem-grade vowel is final in the root/stem; grades are independent of directional `i-` and `a-`
- Direction: `i-` toward, `a-` away, `Ø` neutral; direction is verbal rather than nominal
- Directional readings of cases are compositional constructions, not additional nominal cases
- Object markers: `Ø` local, `n-` nonlocal, `s-` reflexive, `r-` reciprocal; exactly one object slot
- If a vowel is required for NONLOCAL without direction, `e-` may serve as support
- AUX/DERIV: `-re-` progressive, `-ke-` continuative, `-me-` habitual, `-se-` inchoative, `-te-` opposite of inchoative
- AUX/DERIV forms take linking `-e-`; AUX/DERIV and final aspect are separate slots and may co-occur
- `-we-` and productive `-w-` dropped from canonical system
- Agreement: `-k-` 1, `-t-` 2, `-p-` 3; agreement is person-only and does not distinguish singular/plural
- Discourse: `-h-` exclamative, `-y-` interrogative
- Tense: `-i-` nonpast, `-a-` past
- Aspect: `Ø` imperfective, `-n` perfect
- Eight base nominal cases: ABS, ERG, GEN, LOC, SUPER, INE, PATH, COM
- LOC, SUPER, INE, PATH, and COM can participate in compositional directional constructions; ABS, ERG, and GEN do not currently directionalize
- COM polysemy: animate neutral COM, inanimate INST, animate + direction BEN
- Dedicated verbal applicatives eliminated; instrumental and benefactive via nominal case constructions
- Constructional readings include partitive via GEN, dative-like via LOC + `i-`, essive via LOC + stative predicate, and translative via ESSIVE + `i-ra`
- Converbs are intended through nominalizers + case endings; participial relatives combine stem grades with dedicated participial morphology; exact inventories remain unresolved
- `kerande` is established as `kera + NOM + CASE`; the exact independent NOM and CASE exponents remain to be formalized
- Established complex forms include `kerurekin`, `kui`, `kutye`, and `hukka`
- Leipzig Glossing Rules are the default interlinear glossing convention

### Hold-form analysis

- `L-0016 ka` is the canonical lexeme/citation form for HOLD.
- `k-u` → `ku` is the REALIS stem form.
- Finite 1st-person forms include `k-u-k-i` → `kuci`.
- `ku` and finite forms such as `kuci` are predictable inflected forms and are not separate lexicon entries.

### Carry-form analysis

- The canonical lexical item is `L-0034 kera`, derived from `ka + ra` and functioning as the nonfinite stem for CARRY.
- `keru` is the predictable REALIS form of `kera` and is not a separate lexicon entry.
- `kerurekin` is analyzed from `ker-u-re-k-i-n`, with `kera` as the lexical stem and `-u-` as REALIS.

### Karande / be.big analysis

- `L-0032 kerande` is the canonical lexical noun meaning CONTAINER, derived from `kera + NOM + CASE`.
- `L-0033 sara` is the canonical lexical verb meaning BE.BIG.
- `sare` is the predictable LINK/attributive form of `sara`, not a separate lexicon entry.
- The attributive construction is `sare kerande` = 'large container'.

### Pronouns

- `ne` = 1SG
- `se` = 2SG
- `er` = 3SG
- `men` = 1PL
- `sen` = 2PL
- `en` = 3PL

## Known inconsistencies / cleanup needed

The ten-question audit resolved the previous agreement, orthography, segmentation, case-direction, 3SG, and container-form conflicts. Remaining uncertainty is confined to the open questions below and to explicitly unresolved historical conditioning.

## Open questions

### Phonology
- Q-003: precise definition of syllable weight for stress
- Q-004: conditioning of remaining historical developments such as `menme` and `menra`

### Morphology
- Q-005: exact nominalizer inventory and converb/case mappings
- Q-006: dedicated participial forms
- Q-007: whether any additional productive derivational morphology exists
- Q-014: exact independent exponents/segmentation of NOM + CASE in `kerande`

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
5. Test all 18 nominal case/polarity constructions in natural clauses.
6. Test the nominalizer + case structure underlying `kerande`.
7. Expand the lexicon only after productive derivational patterns are sufficiently clear.
