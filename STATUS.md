# Status

**Last updated:** 2026-09-17  
**Phase:** Morphology established; syntax testing underway  
**Repository structure:** Minimal LLM-oriented structure

## Canonical files

- `GRAMMAR.md` — current synchronic grammar and established diachronic evidence
- `LEXICON.tsv` — canonical lexical/root inventory
- `EXAMPLES.tsv` — example and test corpus

## 10-question recovery audit — 2026-09-17

The recovery audit was used to distinguish current decisions from older analyses.

1. **Applicatives:** dedicated verbal applicatives are eliminated. Instrumental and benefactive meanings remain nominal case constructions.
2. **`-w-`:** productive `-w-` is dropped from the canonical discourse/mood system.
3. **Participles:** `-ri` agentive, `-na` patientive, and `-mu` resultative are recovered as ANALYZED, not yet RULE-level morphology.
4. **Converbs:** converbial clauses are analyzed through nominalization plus case; the case supplies the relation. Same-subject/switch-reference behavior remains unresolved.
5. **Nominalization:** `-nu` is recovered as the nominalizer. `keranu`, `keranka`, and `kerande` are recovered as the working derivational family; exact fusion remains to be formalized.
6. **GEN + spatial stacking:** recovered as restricted constructional morphology. GEN+LOC, GEN+SUPER, and GEN+INE are established domains, but free productivity over all cases is not established.
7. **Sound laws:** relative chronology is recovered where supported; unresolved ordering remains explicitly `?` rather than being invented.
8. **Pronouns:** full case evidence and plural reductions are recovered; uncertain reduced realizations remain unresolved.
9. **Examples:** additional examples from the session are recovered as experimental unless their analysis is already secure.
10. **Alignment/AUX:** active-stative/Split-S analysis is recovered, with exact person/animacy/volitionality conditioning unresolved. `-te-` remains an ANALYZED AUX/DERIV value rather than a settled semantic rule.

## Established

### Phonology
- Vowels: `/a e i u/`; long vowels are `aa ee ii uu` when established
- Consonants: `/p t k c m n s h w j r/`; established orthography uses `c = /ts/`, `v = /w/`, and `y = /j/`
- Surface syllable: `(C)V(C)`
- Historical `*p > h`; historical `*p` remains distinct from historical `*h`
- Historical `p > h` before `/i/` in the relevant environment; `h > Ø` between vowels in developments such as `kuhi > kui`
- `t, k > c` before `/i/`; `tc > c`
- `*ndt > nt:` is attested historically/lexically, not established as a productive synchronic rule
- `wu > u`; `yi > ye` in established developments
- `ku-p-i > kupi > kuhi > kui` is established
- `mente > mende`; `menta > menda`
- `menme` and `menra` have unresolved conditioning and possible reduced realizations
- Stress is weight-sensitive: rightmost heavy syllable, otherwise penultimate; exact weight definition remains open

### Morphology
- Finite verb template: `(DIRECTION) (OBJECT) STEM (AUX/DERIV) AGENT (DISCOURSE) TENSE (ASPECT)`
- Finite verbs require person agreement
- Stem grades: `-a-` NONFINITE, `-e-` LINKING/ATTRIBUTIVE, `-u-` REALIS, `-i-` IRREALIS
- Stem-grade vowel is final in the root/stem; grades are independent of directional `i-` and `a-`
- Direction: `i-` toward, `a-` away, `Ø` neutral; direction is verbal rather than nominal
- Object markers: `Ø` local, `n-` nonlocal, `s-` reflexive, `r-` reciprocal; exactly one object slot
- AUX/DERIV: `-re-` progressive, `-ke-` continuative, `-me-` habitual, `-se-` inchoative; `-te-` remains ANALYZED/unresolved
- `-we-` and productive `-w-` dropped from canonical system
- Agreement: `-k-` 1, `-t-` 2, `-p-` 3; agreement is person-only and does not distinguish singular/plural
- Discourse: `-h-` exclamative, `-y-` interrogative
- Tense: `-i-` nonpast, `-a-` past
- Aspect: `Ø` imperfective, `-n` perfect
- Eight base nominal cases: ABS, ERG, GEN, LOC, SUPER, INE, PATH, COM
- Directional readings are compositional constructions rather than additional nominal cases
- COM polysemy: animate neutral COM, inanimate INST, animate + direction BEN; exact semantic boundaries remain under testing
- Dedicated verbal applicatives eliminated
- Constructional readings include partitive via GEN, dative-like via LOC + `i-`, essive via LOC + stative predicate, and translative via ESSIVE + `i-ra`
- Restricted GEN + spatial stacking: GEN+LOC, GEN+SUPER, GEN+INE
- Converbs are nominalization + case; converb relation inventory and switch-reference remain unresolved
- Participles: `-ri` agentive, `-na` patientive, `-mu` resultative, ANALYZED
- `-nu` nominalizer recovered; `keranu`, `keranka`, `kerande` are the working derivational family
- `kerande` remains the canonical CONTAINER lexeme
- Established complex forms include `kerurekin`, `kui`, `kutye`, and `hukka`

### Pronouns
- `ne` = 1SG
- `se` = 2SG
- `er` = 3SG
- `men` = 1PL
- `sen` = 2PL
- `en` = 3PL
- ERG forms include `neku`, `seku`, `erku`, `menku`, `senku`, `enku`
- `mente > mende`; `menta > menda`
- `menme` → `/menme/` or `/mem:e/` remains unresolved
- `menra` → `/menra/` or `/men:a/` remains unresolved
- Formal `sese` and reduced `sa/si` variants remain unresolved in distribution

## Known inconsistencies / cleanup needed

The 10-question audit resolves the major case/applicative, discourse-slot, nominalization, participle, converb, case-stacking, chronology, pronoun, and alignment recovery decisions. `GRAMMAR.md` still needs to be synchronized with this audit where its older wording remains.

## Open questions

### Phonology
- Q-003: precise definition of syllable weight for stress
- Q-004: conditioning of remaining historical developments such as `menme` and `menra`
- Q-015: exact relative ordering/conditioning of the recovered historical sound laws where not directly established

### Morphology
- Q-005: exact converb-to-case mappings and subject-continuity/switch-reference behavior
- Q-006: whether `-ri`, `-na`, `-mu` can be promoted from ANALYZED to RULE
- Q-007: whether any additional productive derivational morphology exists
- Q-014: exact phonological fusion and independent exponent boundaries in `kera + -nu + -te > kerande`
- Q-016: exact semantic value and productivity of AUX/DERIV `-te-`

### Syntax
- Q-008: exact person/animacy/volitionality conditioning of Split-S
- Q-009: genitive position
- Q-010: negative marker and position in the verb template
- Q-011: independent adposition system, if any
- Q-013: information-structure mechanisms
- Q-017: productivity limits of GEN + spatial case stacking

## Immediate testing priorities

1. Generate matched Split-S clauses across person, animacy, and volitionality.
2. Test pre- vs. post-nominal genitives.
3. Design and test negative morphology.
4. Test reflexive and reciprocal object marking.
5. Test all nominal case/polarity constructions in natural clauses.
6. Test the nominalizer + case structure underlying `kerande`.
7. Test `-ri`, `-na`, `-mu` in matched participial relatives.
8. Test converb case relations and subject continuity.
9. Test the productivity limits of GEN + spatial stacking.
10. Expand the lexicon only after productive derivational patterns are sufficiently clear.
