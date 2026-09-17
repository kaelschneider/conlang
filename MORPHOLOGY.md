# Morphology

Status: canonical where stated; unresolved items remain in `STATUS.md`.

## G-MORPH — Morphology

### G-MORPH-01 — Morphological profile

The language has compact, consonant-heavy morphology with historically fused/reduced forms and inherited monoconsonantal roots. The overall morphological type is mixed rather than assigned a single typological label.

### G-MORPH-02 — Verb template

Finite verbs follow:

`(DIRECTION) (OBJECT) STEM (AUX/DERIV) AGENT (DISCOURSE) TENSE (ASPECT)`

There is no dedicated verbal applicative slot. Finite verbs require an AGENT/person agreement marker.

### G-MORPH-03 — Stem grades

| Grade | Form | Function | Leipzig gloss |
|---|---|---|---|
| NONFINITE | `-a-` | nonfinite / citation form | `NFIN` |
| LINKING | `-e-` | linking / attributive | `LINK` |
| REALIS | `-u-` | realis | `REAL` |
| IRREALIS | `-i-` | irrealis | `IRR` |

The alternating stem vowel is final in the root/stem. A lexical root such as `kat` becomes verbal `kata`; subsequent grades produce forms such as `kate`, not an internally altered root followed by another stem-vowel suffix.

These grades are independent of directional `i-` and `a-`.

For HOLD, the citation/nonfinite form is `ka`. The realis stem is `ku`:

`ka` → `k-u` → `k-u-k-i` → `kuci`

For BE.BIG, the citation/nonfinite form is `sara` and the linking form is `sare`:

`sara` → `sar-e`

### G-MORPH-04 — Direction

`i-` = toward / goalward; `a-` = away / sourceward; `Ø` = neutral.

Directional morphology is verbal. It is not a prefix attached to the noun. In case constructions the noun retains its nominal case suffix and the finite verb carries `i-` or `a-`.

If a vowel is required for NONLOCAL without direction, `e-` may serve as support.

### G-MORPH-05 — Object slot

There is exactly one object slot:

| Marker | Function | Leipzig gloss |
|---|---|---|
| `Ø` | local object | — |
| `n-` | nonlocal object | `NLOC` |
| `s-` | reflexive | `REFL` |
| `r-` | reciprocal | `RECP` |

The overt object remains a separate noun phrase in SOV clauses. Nominal case suffixes likewise remain on the overt noun phrase.

### G-MORPH-06 — AUX/DERIV

The following light roots occur in the AUX/DERIV slot and take the linking `-e-` grade:

| Root | Basic lexical meaning | AUX form | Semantic value | Leipzig gloss |
|---|---|---|---|---|
| `*r` | go | `-re-` | progressive | `PROG` |
| `*k` | hold | `-ke-` | continuative | `CONT` |
| `*m` | live / dwell / stay | `-me-` | habitual | `HAB` |
| `*s` | cut / remove | `-se-` | inchoative | `INCH` |
| `*t` | transfer | `-te-` | analyzed; semantic value unresolved | `TE` |

AUX/DERIV morphology and final verbal aspect are separate slots and may co-occur. `-we-` and productive `-w-` were considered during development but are dropped from the canonical system.

### G-MORPH-07 — Agreement

| Person | Marker | Leipzig gloss |
|---|---|---|
| 1 | `-k-` | `1` |
| 2 | `-t-` | `2` |
| 3 | `-p-` | `3` |

Agreement is person-only: the markers do not distinguish singular from plural. Finite verbs require one person marker. Number is expressed independently, including by pronouns.

The 3rd-person marker `-p-` participates in the established historical development to `kui` and related forms; the full conditioned historical system is documented in `PHONOLOGY.md`.

### G-MORPH-08 — Discourse / mood

| Marker | Function | Leipzig gloss |
|---|---|---|
| `-h-` | exclamative | `EXCL` |
| `-y-` | interrogative | `INT` |

`-h-` is historically associated with `*h` 'say/blow'; it is not a realis marker.

### G-MORPH-09 — Tense

`-i-` = nonpast (`NPST`); `-a-` = past (`PST`).

### G-MORPH-10 — Aspect

`Ø` = imperfective (`IPFV`); `-n` = perfect (`PRF`).

### G-MORPH-11 — Noun cases

| Case | Suffix | Core meaning | Semantic domain | Leipzig gloss |
|---|---|---|---|---|
| ABS | `Ø` | patient / S | core argument | `ABS` |
| ERG | `-ku` | agent / A | core argument | `ERG` |
| GEN | `-se` | possessor / dependent | relational | `GEN` |
| LOC | `-te` | at / in / static | spatial | `LOC` |
| SUPER | `-ta` | on / against / surface | spatial | `SUPER` |
| INE | `-ci` | inside / containment | spatial | `INE` |
| PATH | `-ra` | along / through / medium | spatial | `PATH` |
| COM | `-me` | with / associate | participant | `COM` |

### G-MORPH-12 — Directional constructions with case

Nominal cases remain distinct cases. Directional readings are compositional constructions: the noun keeps its ordinary case suffix and the finite verb carries `i-` toward or `a-` away. These constructions do not create additional nominal cases.

LOC, SUPER, INE, PATH, and COM can participate in directional constructions. ABS, ERG, and GEN do not currently directionalize.

#### LOC series

| Polarity | Construction | Function | Meaning |
|---|---|---|---|
| Ø | `O-te` | LOC | at / in |
| i- | `O-te i-VERB` | ALL construction | to / toward |
| a- | `O-te a-VERB` | ABL construction | from / away |

#### SUPER series

| Polarity | Construction | Function | Meaning |
|---|---|---|---|
| Ø | `O-ta` | SUPER | on / against |
| i- | `O-ta i-VERB` | SUBLATIVE construction | onto / up to surface |
| a- | `O-ta a-VERB` | DELATIVE construction | off / from surface |

#### INE series

| Polarity | Construction | Function | Meaning |
|---|---|---|---|
| Ø | `O-ci` | INE | inside / within |
| i- | `O-ci i-VERB` | ILLATIVE construction | into / in through |
| a- | `O-ci a-VERB` | ELATIVE construction | out of |

#### PATH series

| Polarity | Construction | Function | Meaning |
|---|---|---|---|
| Ø | `O-ra` | PATH | along / through |
| i- | `O-ra i-VERB` | PATH+i- construction | toward along / across |
| a- | `O-ra a-VERB` | PATH+a- construction | away along / back |

COM directional constructions are described under G-MORPH-13.

### G-MORPH-13 — COM polysemy and directional construction

COM is a nominal case. Its directional uses are compositional constructions rather than additional cases.

| Polarity | Animate argument | Inanimate argument | Semantic reading |
|---|---|---|---|
| Ø | COM | INST | with / alongside (COM); with / using (INST) |
| i- | BEN construction | INST construction | toward for / on behalf of (BEN); toward via / using (INST) |
| a- | BEN construction | INST construction | away for / on behalf of (BEN); away via / using (INST) |

The exact semantic boundaries remain subject to testing.

### G-MORPH-14 — Applicatives

Dedicated verbal applicatives have been eliminated. Instrumental and benefactive meanings are expressed through nominal case constructions; no dedicated verbal applicative morphology remains.

### G-MORPH-15 — Constructional functions

| Function | Source | Realization |
|---|---|---|
| PART | GEN, partitive use | `-se` in divisible/mass contexts |
| COMP | COM, comitative + locative anchoring | `-me` + context |
| DAT | LOC + `i-`, recipient / goal participant | `O-te i-VERB` in dative-like contexts |
| ESSIVE | LOC + stative predicate | `-te` in copular/state constructions |
| TRANSLATIVE | ESSIVE + `i-ra` | `-te` + `i-ra` meaning 'become' |

These are constructional readings, not additional nominal cases.

### G-MORPH-16 — GEN + spatial stacking

GEN + spatial stacking is established as restricted constructional morphology.

| Stacking | Function | Status |
|---|---|---|
| `GEN + LOC` | at / in X's domain | established |
| `GEN + SUPER` | on X's surface / domain | established |
| `GEN + INE` | inside X's domain | established |

These stacked constructions are not assumed to be freely productive over all nominal cases. Productivity limits remain under testing.

### G-MORPH-17 — Converbs, participles, and nominalization

Converbial clauses are analyzed through nominalization plus case; the case supplies the converbial relation. The inventory of case-to-relation mappings and same-subject versus switch-reference behavior remains unresolved. Independent conjunctions are not currently established as the primary clause-combining strategy.

Participial morphology is analyzed as follows, but has not yet been promoted to full rule-level canon:

| Form | Function | Status |
|---|---|---|
| `-ri` | agentive participle | ANALYZED |
| `-na` | patientive participle | ANALYZED |
| `-mu` | resultative participle | ANALYZED |

`-nu` is the recovered nominalizer. The working derivational family is:

- `keranu` = carrying / carrying event
- `keranka` = carrier / person associated with carrying
- `kerande` = container / place, instrument, or means associated with carrying

`kerande` remains the canonical CONTAINER lexeme. Its synchronic analysis is `kera + -nu + -te` with surface fusion/reduction; the exact independent exponent boundaries and phonological pathway remain unresolved.

### G-MORPH-18 — Established complex verbal forms

`kerurekin` = `keru-re-k-i-n` (CARRY.REAL-PROG-1-NONPAST-PERF). It demonstrates co-occurrence of AUX/DERIV, agreement, tense, and aspect.

`ku-p-i > kupi > kuhi > kui` demonstrates the 3rd-person realis/nonpast form `kui` through historical `p > h > Ø` development.

`ku-t-y-i > kutyi > kutye` demonstrates interrogative `-y-` plus NONPAST `-i`, with phonological repair because `-yi` is prohibited.

`hukka < hu-k-h-a` is an established example of the discourse slot; its exact lexical/derivational interpretation remains tied to the relevant root history.

## Lexical derivation and generation model — ANALYZED

The following is the current **lexical-generation model** derived from the morphology decisions of 2026-09-17. It describes how new lexical material is to be generated and filtered; it does not by itself promote unestablished derivational exponents to productive grammar.

### Root inventory

Basic lexical roots are generated in three shapes:

| Root shape | Target frequency |
|---|---:|
| C | 15% |
| VC | 25% |
| CVC | 60% |

`CVCC` is not an independent root shape. It is derived by adding a consonant to a CVC root:

`CVC + C → CVCC`

A stem grade is then added after the root or derived root:

- `C + stem vowel → CV`
- `VC + stem vowel → VCV`
- `CVC + stem vowel → CVCV`
- `CVC + C + stem vowel → CVCCV`

The root-shape distribution is a generation target, not a claim that the modern lexicon must exactly match these percentages.

### Lexical category and family formation

Roots are category-neutral by default. A minority may have weak noun- or verb-oriented biases. Root shape has only a weak statistical correlation with lexical category; shape is not a categorical noun/verb marker.

Roots are generated both independently and as members of deliberately seeded semantic families. Semantic-family seeding should emphasize broad semantic domains and culturally salient concepts rather than arbitrary lists of near-synonyms.

Potential derivations are generated for all root shapes. Derivational productivity is frequency-sensitive rather than shape-exclusive: common or semantically central roots may support larger lexical families, while many roots remain simple. Approximately 55% of roots are expected to remain morphologically simple.

### Productive derivation

The productive derivational core is intended to remain compact, with approximately four to five productive mechanisms. The system is mixed: derivation may be category-changing or meaning-extending, and formal mechanisms need not all have the same historical origin.

The following principles are established for generation:

1. Category-changing and meaning-extending derivation are both productive domains.
2. Verb-to-noun derivation is favored over noun-to-verb derivation, but both directions remain available.
3. `CVC + C → CVCC` is primarily associated with event/action verbalization, while individual lexicalized derivatives may develop more specific meanings or secondary functions.
4. Derivational mechanisms are mostly category-oriented, but historical/semantic strata may overlap and produce non-identical functions.
5. Zero derivation/conversion remains available, especially for closely related noun/verb pairs.
6. Derivations may normally compose to two layers; unrestricted stacking is not the default.

No new overt derivational exponent is asserted here. `-nu`, `-ri`, `-na`, and `-mu` retain their statuses in G-MORPH-17 and are not promoted to productive rule by this model.

### Added-consonant derivation

For the `CVC + C → CVCC` pathway, the added consonant is drawn from a restricted weighted set rather than the full consonant inventory uniformly. The working generation weights are:

| Added C | Relative weight |
|---|---:|
| `t` | 4 |
| `k` | 4 |
| `n` | 3 |
| `p` | 2 |
| `m` | 2 |
| `s` | 2 |
| `r` | 2 |

The set is a generation prior, not a claim that every listed consonant is a synchronically productive suffix. The added consonant may acquire weak functional associations statistically, but no consonant is assigned a fixed one-to-one derivational meaning. Historical associations may later account for recurring distributions.

### Candidate-family generation and lexicalization

The generator should normally produce approximately 2–4 potential derivatives per root. These are candidates, not automatic lexical entries.

Candidate derivations are evaluated in stages:

1. phonological legality and root-shape constraints;
2. derivational/category compatibility;
3. semantic plausibility within the root domain or cultural setting;
4. compositional interpretation;
5. frequency and semantic-centrality effects on likely lexicalization;
6. collision filtering, rejecting exact homophones and obvious phonological collisions;
7. lexicalization, after which a derivative may become an independent lexical item.

Family size should have a long tail: most roots have small families, while frequent and semantically central roots are disproportionately likely to develop larger families.

Derived meanings begin compositionally. Lexicalized forms may specialize semantically and can eventually become synchronically independent lexemes.

### LLM role in lexical generation

The LLM is a semantic curator and critic rather than the primary generator of word forms.

The intended division of labor is:

`phonological generator → derivational candidate generator → semantic curation/critique → lexicalization filter → lexical inventory`

The LLM may propose or critique semantic relationships and candidate families, but phonological form generation, phonotactic legality, derivational mechanics, and final collision filtering remain rule- or algorithm-driven.

This model is a generation methodology and analytical parameterization. It must not be used to retroactively declare undocumented historical relationships or unestablished morphology to be canonical.
