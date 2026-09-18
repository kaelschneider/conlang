# Status

**Last updated:** 2026-09-17  
**Phase:** Core morphology and syntax established; lexical/semantic edge cases remain under testing  
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
7. **Early sequence repair:** `wu > u` is general; morphologically generated `yi > ye` precedes the major weakening series.
8. **Palatalization trace:** orthographic merger to `c` is complete, but former `*t` may retain a transitional [t] component in phonetic realization such as `/ru(t)ɕi/`; this is not a separate phoneme.
9. **Lexicalized cluster reduction:** `*ndt > nt:` is later and independent of the general weakening series.
10. **Conditioning model:** the outcome is shaped jointly by syllable structure and neighboring-vowel transition class. **OPEN** means `CV`; **CLOSED** means `CVC`. Vowel classes are `F = /e i/` and `B = /a u/`; `F_F`, `F_B`, `B_F`, and `B_B` identify the transition between the vowels flanking the target. The four classes are independent conditioning environments; there is no universal lenition hierarchy. Closure is a structural factor, not an `n`-specific rule, and its effect is environment-specific.

### Resolved design decisions — second phonology pass

- Stress is **rightmost heavy, otherwise penultimate**; `CVV` and `CVC` count as heavy.
- Late sonorant reduction targets **homorganic sonorant clusters**, is favored across morphological boundaries, and can spread into lexicalized material.
- `nm > m:`; `nr > nn > n:` is treated as nasal-dominant assimilation within the sonorant cluster.
- Resulting `m:`/`n:` length is phonetic/metrical rather than a new synchronic phonemic contrast.
- `yi > ye` is a morphologically generated boundary repair; `wu > u` is a general phonological repair.
- Historical `pp/tt/kk` are not a modern consonant-length contrast; modern surface forms conform to `(C)V(C)`.
- `ada > da` is ordered as `*ata > ada > da`, with the vowel-loss rule applying after `t > d`.


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
- Late sonorant-cluster reduction includes `nm > mm > m:` and `nr > nn > n:`, with phonetic rather than phonemic length
- Stress is rightmost-heavy otherwise penultimate; IPA must mark primary stress with `ˈ`

### Morphology
- Finite verb template: `(DIRECTION) (OBJECT) STEM (AUX/DERIV) AGENT (NEG) (DISCOURSE) TENSE (ASPECT)`
- Finite verbs require person agreement; agreement follows the semantic agent where one exists and otherwise the stative/agentless S
- Stem grades: `-a-` NONFINITE, `-e-` LINKING/ATTRIBUTIVE, `-u-` REALIS, `-i-` IRREALIS
- Direction: `i-` toward, `a-` away, `Ø` neutral; direction is verbal rather than nominal
- Object slot: `n-` local, `Ø` nonlocal, `s-` reflexive, `r-` reciprocal; LOCAL/NLOC is distinct from nominal LOC (`-te`)
- AUX/DERIV: `-re-` progressive, `-ke-` continuative, `-me-` habitual, `-se-` inchoative; `-te-` remains ANALYZED/unresolved
- NEG is a suffixal polarity exponent after AGENT and before optional DISCOURSE/TENSE/ASPECT; its exact short CV/VC form remains unselected
- Agreement: `-k-` 1, `-t-` 2, `-p-` 3; person-only
- Discourse: `-h-` exclamative, `-y-` interrogative
- Tense: `-i-` nonpast, `-a-` past
- Aspect: `Ø` imperfective, `-n` perfect
- Eight base nominal cases: ABS, ERG, GEN, LOC, SUPER, INE, PATH, COM
- Common-noun number is restricted rather than obligatory; an archaic dual survives in conventionalized natural-pair nouns
- Dedicated verbal applicatives eliminated
- COM `-me` has a core association/accompaniment reading with contextual instrumental, benefactive, and malefactive extensions; `i-` marks the benefactive directional construction and `a-` marks the malefactive directional construction
- Restricted but productive GEN + spatial stacking: GEN+LOC, GEN+SUPER, GEN+INE
- LOC + verbal direction has two distinct constructions: ALL (`O-te i-VERB`) and DAT-like (`O-te i-(LOCAL/NLOC)-VERB`); NLOC DAT-like is zero-marked and therefore segmentally identical to ALL
- Converbs are nominalization + case; same-subject continuity is unmarked and overt GEN-marking marks switch-reference
- Participles `-ri`, `-na`, `-mu` are productive agentive, patientive, and resultative forms
- `-nu` nominalizer; `keranu`, `keranka`, `kerande` working family

### Syntax
- Declarative SOV
- Attributive modifiers precede nouns
- Stative predicate follows subject
- Active-stative / Split-S: 1st/2nd-person S is agentive; 3rd-person S is conditioned by animacy and volitionality
- Established pronouns include `ne`, `se`, `er`, `men`, `sen`, `en`; ERG forms include `neku`, `seku`, `erku`, `menku`, `senku`, `enku`
- Questions use verbal `-y-`
- Participial relatives precede the noun; finite relative clauses follow the noun and use a gap
- Converbs and nominalized clauses are the primary strategy for subordination and clause chaining
- Independent coordination is primarily juxtaposed, with a small secondary conjunction class
- A small independent postposition class may coexist with case morphology
- GEN-marked possessors precede the head noun

## Morphology and syntax resolution — 2026-09-17

The 20-question morphology/syntax pass resolved the following structural points:

- Split-S: 1st/2nd-person S is agentive; 3rd-person S is conditioned by animacy and volitionality. Agentive S and A take ERG; patientive S and O take ABS.
- Finite agreement indexes the semantic agent when one exists; otherwise a stative or otherwise agentless S controls agreement. Agreement remains person-only.
- Verbal object status is discourse-based: LOCAL `n-` is marked, while zero is NLOC by default.
- Common-noun number is restricted rather than obligatory; an archaic dual survives in conventionalized natural-pair nouns.
- GEN possessors are prenominal. GEN + LOC/SUPER/INE stacking is productive within its established semantic domain but is not freely extended to arbitrary case combinations.
- A small, historically derived postposition class may coexist with case morphology.
- Negation is a verbal suffix in the right-edge inflectional zone: after AGENT and before optional DISCOURSE/TENSE/ASPECT. The exponent is a dedicated short CV/VC form; its exact phonological shape remains a separate lexicalization detail. No negative stem grade is used.
- `-ri`, `-na`, and `-mu` are productive agentive, patientive, and resultative participles.
- The productive derivational core remains compact, while older derivational strata may be partially productive, lexicalized, or opaque; deeper historical layering is permitted through reanalysis rather than unrestricted synchronic stacking.
- Converbs are nominalization + case. Same-subject continuity is unmarked; an overt GEN-marked nominalized subject marks switch-reference. Case meanings remain broadly polyfunctional.
- Finite relative clauses use a gap. Coordination is primarily juxtaposition, with a small secondary conjunction class.
- Information structure remains the main unresolved syntactic domain.

## Known inconsistencies / cleanup needed

The conditioned historical system is documented in `GRAMMAR.md`, including the resolved OPEN/CLOSED × F_F/F_B/B_F/B_B matrix. Existing lexical and example forms have been checked against the resolved stress and historical rules; no lexical/example rewrite was required by this pass.

The earlier regression forms (`apa`, `ita`, `teta`, `keka`, `neku`, `seku`, `kerande-te`, and related forms) remain useful diagnostic evidence for historical strata and conditioning rather than being declared exceptions.

Zero-marked verbal objects are now canonically NLOC by default; overt LOCAL `n-` should be used when discourse accessibility/salience makes the object local. Local `n-` retains the established surface repair `n + C → enC` before consonant-initial verb stems.

## Open questions

### Morphology
- Q-019: exact discourse conditions favoring COM accompaniment, instrumental, benefactive, and malefactive readings
- Q-014: exact phonological fusion and independent exponent boundaries in `kera + -nu + -te > kerande`
- Q-016: exact semantic value and productivity of AUX/DERIV `-te-`
- NEG: exact phonological exponent form remains to be selected; syntactic position is established.

### Syntax
- Q-013: information-structure mechanisms

## Immediate testing priorities

1. Test the nominalizer + case structure underlying `kerande`.
2. Test the productive participles and converb/switch-reference system with matched examples.
3. Develop information-structure and discourse tests; do not promote a construction from frequency alone.

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

These generation decisions do not by themselves promote unresolved morphology such as `-te-` to rule status. The productive participles `-ri`, `-na`, and `-mu` are now established independently by the morphology/syntax pass. Existing lexical entries are not retroactively reclassified from this generation model alone.
