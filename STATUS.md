# Status

**Last updated:** 2026-09-17  
**Phase:** Morphology established; syntax testing underway  
**Repository structure:** Consolidated grammar source; minimal flat structure

## Canonical files

- `GRAMMAR.md` — canonical consolidated grammar: phonology, morphology, syntax, prosody, and historical sound change
- `LEXICON.tsv` — canonical lexical/root inventory
- `EXAMPLES.tsv` — example and test corpus
- `SCHEMA.json` — structural validation schema
- `AGENTS.md` — repository maintenance instructions

## 10-question phonological recovery audit — 2026-09-17

1. **Generalized weakening:** each `>` is a successive historical stage. The designed regression forms are to be explained by general historical developments, not isolated example-specific rules.
2. **Unified initial weakening:** historical `*p`, `*t`, and `*k` participate in one related weakening process, with consonant-specific first-stage outcomes: `p > h`, `t > d`, `k > g`.
3. **Pre-/i/ palatalization precedes general weakening:** `t, k > c / _i`, followed by `c > tɕ / _i` and `tɕ > ɕ / _i`.
4. **Stop + h fusion precedes general weakening:** `ph > pp`, `th > tt`, `kh > kk`.
5. **Intervocalic loss is unified at later stages:** `h, ɣ > Ø / V_V` where the conditioned historical environment permits the endpoint.
6. **Initial `*p > h`:** word-initial `*p > h` is historically continuous with the broader `p` weakening, but remains environmentally distinct from intervocalic weakening. Historical `*p` remains distinct from historical `*h`.
7. **Early sequence repair:** `wu > u` and `yi > ye` precede the major weakening series.
8. **Palatalization trace:** orthographic merger to `c` is complete, but former `*t` may retain a transitional [t] component in phonetic realization such as `/ru(t)ɕi/`; this is not a separate phoneme.
9. **Lexicalized cluster reduction:** `*ndt > nt:` is later and independent of the general weakening series.
10. **Conditioning model:** the outcome is shaped jointly by syllable structure and neighboring-vowel transition class. **OPEN** means `CV`; **CLOSED** means `CVC`. Vowel classes are `F = /e i/` and `B = /a u/`; `F_F`, `F_B`, `B_F`, and `B_B` identify the transition between the vowels flanking the target. `F_F` and `B_B` are the stronger lenition class in the working hierarchy; `F_B` and `B_F` are intermediate. Closure is a structural factor, not an `n`-specific rule, and its effect is environment-specific.

The exact OPEN/CLOSED × F_F/F_B/B_F/B_B outcomes remain to be determined from corpus testing. Conventional historical sound-law notation should be used when individual conditioned rules are promoted; the matrix is a testing/analysis framework rather than a required final notation.

## Grammar consolidation — 2026-09-17

The grammar sources have been consolidated into `GRAMMAR.md`:

- `GRAMMAR.md` — phonology, morphology, syntax, prosody, and historical sound change

Existing `G-PHON`, `G-MORPH`, and `G-SYN` section IDs are retained so existing `EXAMPLES.tsv` references remain stable.


## Repository structure rule

Agents must not add, remove, rename, move, split, merge, or otherwise alter repository files or directories unless the user explicitly instructs them to change the repository structure.

## Established

### Phonology
- Vowels: `/a e i u/`; long vowels are `aa ee ii uu` when established
- Consonants: `/p t k m n s h w j r/`; `c` is orthographic and has `/ɕ/` or `/tɕ/` surface realization depending on historical source (`-ki > -ci` vs. `-ti > -ci`); `v = /w/`, `y = /j/`
- Surface syllable: `(C)V(C)`
- Historical conditioning uses OPEN/CLOSED syllable structure plus F_F/F_B/B_F/B_B vowel-transition class
- Historical `*p > h`; historical `*p` remains distinct from historical `*h`
- Pre-/i/ `t, k > c`; orthographic `c` is `/ɕ/` from `-ki > -ci` and `/tɕ/` from `-ti > -ci`
- `ph > pp`, `th > tt`, `kh > kk`
- `wu > u`; `yi > ye`
- `*ndt > nt:` is attested historically/lexically, not established as a productive synchronic rule
- `ku-p-i > kupi > kuhi > kui` is established
- `mente > mende`; `menta > menda`
- `menme` and `menra` have unresolved conditioning
- Stress is weight-sensitive; IPA must mark primary stress with `ˈ`

### Morphology
- Finite verb template: `(DIRECTION) (OBJECT) STEM (AUX/DERIV) AGENT (DISCOURSE) TENSE (ASPECT)`
- Finite verbs require person agreement
- Stem grades: `-a-` NONFINITE, `-e-` LINKING/ATTRIBUTIVE, `-u-` REALIS, `-i-` IRREALIS
- Direction: `i-` toward, `a-` away, `Ø` neutral; direction is verbal rather than nominal
- Object markers: `Ø` local, `n-` nonlocal, `s-` reflexive, `r-` reciprocal
- AUX/DERIV: `-re-` progressive, `-ke-` continuative, `-me-` habitual, `-se-` inchoative; `-te-` remains ANALYZED/unresolved
- Agreement: `-k-` 1, `-t-` 2, `-p-` 3; person-only
- Discourse: `-h-` exclamative, `-y-` interrogative
- Tense: `-i-` nonpast, `-a-` past
- Aspect: `Ø` imperfective, `-n` perfect
- Eight base nominal cases: ABS, ERG, GEN, LOC, SUPER, INE, PATH, COM
- Dedicated verbal applicatives eliminated
- COM `-me` has a core association/accompaniment reading with contextual instrumental and directional extensions; `i-/a-` remains verbal
- Restricted GEN + spatial stacking: GEN+LOC, GEN+SUPER, GEN+INE
- Converbs are nominalization + case; same-subject/switch-reference unresolved
- Participles `-ri`, `-na`, `-mu` remain ANALYZED
- `-nu` nominalizer; `keranu`, `keranka`, `kerande` working family

### Syntax
- Declarative SOV
- Attributive modifiers precede nouns
- Stative predicate follows subject
- Active-stative / Split-S analysis under testing
- Established pronouns include `ne`, `se`, `er`, `men`, `sen`, `en`; ERG forms include `neku`, `seku`, `erku`, `menku`, `senku`, `enku`
- Questions use verbal `-y-`
- Participial relatives precede the noun; finite relative clauses follow the noun
- Converbs and nominalized clauses are intended primary clause-combining strategy
- Independent adposition system unresolved
- Genitive position unresolved

## Known inconsistencies / cleanup needed

The conditioned historical system is now documented in `GRAMMAR.md`, but the exact environment-by-environment outcomes have not yet been assigned. Existing lexical and example forms must not be rewritten until those conditions are resolved.

The previous regression also identified forms whose outcomes under an unconditional `V_V` rule were problematic (`apa`, `ita`, `teta`, `keka`, `neku`, `seku`, `kerande-te`, and related forms). These remain diagnostic evidence for the conditioned system rather than being declared exceptions.

The historical development `ada > da` remains to be placed in the chronology.

## Open questions

### Phonology
- Q-003: precise definition of syllable weight for stress
- Q-004: conditioning of remaining historical developments such as `menme` and `menra`
- Q-015: exact OPEN/CLOSED × F_F/F_B/B_F/B_B outcomes and conventional rule formulation
- Q-018: placement and conditioning of `ada > da`

### Morphology
- Q-005: exact converb-to-case mappings and subject-continuity/switch-reference behavior
- Q-006: whether `-ri`, `-na`, `-mu` can be promoted from ANALYZED to RULE
- Q-007: whether any additional productive derivational morphology exists
- Q-019: exact discourse conditions favoring COM accompaniment, benefactive, and instrumental readings in directional constructions
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

1. Build the complete OPEN/CLOSED × F_F/F_B/B_F/B_B regression matrix from `LEXICON.tsv` and `EXAMPLES.tsv`.
2. Determine which existing forms instantiate each environment.
3. Infer conditioned historical endpoints without rewriting modern forms prematurely.
4. Resolve `ada > da` placement.
5. Update affected examples only after the conditioned historical system is explicit.
6. Test the nominalizer + case structure underlying `kerande`.
7. Continue syntax testing after the grammar split.

## Lexical derivation generation decisions — 2026-09-17

The lexical-generation strategy was parameterized through the 20-question morphology/lexicon design pass. The resulting model is documented in `GRAMMAR.md` as ANALYZED methodology rather than promoted as additional synchronic grammar.

Key decisions:

- Root shapes: C 15%, VC 25%, CVC 60%; CVCC is derived only from CVC + C.
- Roots are category-neutral by default, with weak category biases and weak root-shape/category correlations.
- Semantic families are deliberately seeded alongside independently generated roots.
- Approximately 55% of roots remain morphologically simple; family size has a long tail associated with frequency and semantic centrality.
- Derivation is balanced between category change and semantic extension; verb → noun is favored.
- CVC + C → CVCC is primarily verbal/eventive, but may develop secondary lexicalized functions.
- The productive derivational core is approximately 4–5 mechanisms, with mixed formal mechanisms and limited two-layer composition.
- Limited noun ↔ verb conversion is permitted.
- Potential derivatives are candidates rather than automatic lexical entries; lexicalization is selected through staged phonological, morphological, semantic, frequency, and collision filters.
- The working added-consonant prior for CVCC is t:4, k:4, n:3, p:2, m:2, s:2, r:2.
- The LLM is used as semantic curator/critic, not as the primary phonological word-form generator.

These decisions do not promote `-ri`, `-na`, `-mu`, `-te-`, or any other currently ANALYZED/UNRESOLVED morphology to RULE status. Existing lexical entries are not retroactively reclassified from this generation model alone.
