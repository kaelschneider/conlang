# Status Report
**Last updated:** September 17, 2026  
**Phase:** 3–4 (morphology complete; syntax testing underway)

## Summary

Core morphological and phonological systems are established. Ten initial test clauses have now been generated to stress-test SOV order, case marking, agreement, questions, directional morphology, and morphological stacking. Syntax remains partially specified: Split-S conditioning, genitive position, negation, and several clause-combining mechanisms require further testing.

## Established (Canonical)

### Phonology
- ✓ Core inventory (consonants, vowels)
- ✓ General syllable structure: (C)V(C)
- ✓ Established sound changes (word-initial *p > h, etc.)
- ~ Allophony: environment-driven; historical sound changes may motivate rules; promote rules to canon only after repeated evidence
- ~ Stress/prosody: weight-sensitive where relevant, potentially morphologically conditioned; promote rules after repeated testing

### Morphology: Verbs
- ✓ Finite verb template: (DIR) (OBJ) STEM (AUX) AGENT (DISCOURSE) TENSE (ASPECT)
- ✓ Direction system: i- (toward), a- (away), Ø (neutral)
- ✓ Stem grades: -a- (nonfinite), -e- (linking), -u- (realis), -i- (irrealis)
- ✓ Object marking: Ø (local), n- (nonlocal), s- (reflexive), r- (reciprocal)
- ✓ AUX/DERIV roots: -re-, -ke-, -me-, -se-, -te-
- ✓ Agreement: 1SG -k-, 2SG -t-, 3SG -p-; no plural agreement
- ✓ Discourse/mood: -h- (exclamative), -y- (interrogative)
- ✓ Tense: -i- (nonpast), -a- (past)
- ✓ Aspect: Ø (imperfective), -n (perfect)
- ✓ `-we-` and productive `-w-` dropped from the canonical system

### Morphology: Nouns
- ✓ 8 base cases (ABS, ERG, GEN, LOC, SUPER, INE, PATH, COM)
- ✓ 3 directional expansions on spatial cases (Ø, i-, a-)
- ✓ COM polysemy: animacy + polarity → COM/INST/BEN
- ✓ No dedicated applicative morphology
- ✓ 18 total inflectional forms

### Lexicon
- ✓ 10 historical monoconsonantal roots (*p, *t, *k, *w, *r, *j, *h, *s, *m, *n)
- ✓ Sound-symbolic semantic clustering
- ? Complete inventory of productive nominalizers / converbs
- ? Participial forms beyond stem grades

## In Progress (Not Yet Canonical)

### Syntax
- ~ Basic SOV order is supported by existing examples and the first 10-clause test corpus
- ~ Split-S / mixed alignment specifics (needs animacy/person/volitionality conditions)
- ~ Genitive position (pre- or post-nominal?)
- ~ Adpositions (exist? type?)
- ~ Negative morphology (position in verb template?)
- ~ Converb / switch-reference system
- ~ Information structure / focus mechanisms
- ~ Relative clause formation
- ~ Clause combining (coordination, subordination)

### Testing
- ✓ Initial 10-clause morphosyntax corpus added at `examples/test-clauses.md`
- ~ Need matched person/animacy/volitionality clauses for Split-S testing
- ~ Need matched genitive-position tests
- ~ Need negative clauses once negative morphology is designed
- ~ Need all 18 nominal case forms tested in natural examples
- ~ Need reflexive/reciprocal object tests

## Not Yet Started

- Comprehensive lexicon expansion (target: 50–100+ stems from 10 roots)
- Derivational morphology (agent nouns, abstract nouns, etc.)
- Sound-law documentation (if pursuing diachronic depth)
- Written text examples (running prose in the language)
- Typological summary document

## Decision Points Blocking Progress

| Blocker | Impact | Phase |
|---|---|---|
| Specify animacy/person/volitionality alignment conditions | Validates syntax | 3 |
| Determine genitive position | Constrains phrase order | 3 |
| Define negative morphology | Completes verb template | 3 |
| Test morphosyntax with matched examples | Validates syntax and unlocks lexicon expansion | 4 |

## Next Actions (Ordered by Dependency)

1. Generate matched Split-S test clauses: 1SG/2SG/3SG, animate/inanimate, intentional/non-intentional
2. Test pre- vs. post-nominal genitives in matched pairs
3. Design negative morphology and test its position/scope
4. Test reflexive and reciprocal object marking
5. Test all 18 nominal forms in actual clauses
6. Expand lexicon to 30–50 stems
7. Build running text → 1–2 paragraphs to stress-test morphosyntax
8. Finalize participials and derivational patterns
9. Document validated syntax in canon files
