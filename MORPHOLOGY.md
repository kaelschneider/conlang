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
