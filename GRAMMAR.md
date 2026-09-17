# Grammar

## Phonology

Status: canonical where stated; unresolved conditions remain in `STATUS.md`.

## G-PHON — Phonology

### G-PHON-01 — Syllable structure

Surface syllable structure is `(C)V(C)`. Productive onset clusters are not established. Complex sequences may arise historically or morphologically and subsequently reduce or fuse.

For historical conditioning, **OPEN** means a target consonant belongs to a syllable of shape `CV`; **CLOSED** means it belongs to a syllable of shape `CVC`. The distinction is structural and is not specific to any one coda consonant. Historical syllabification determines which syllable is relevant at the stage where a sound law applies.

Representative historical shapes for testing include `*pVpV`, `*pVpVn`, `*pVnpV`, and `*pVnpVn`; these are diagnostic configurations rather than separate lexical rules.

### G-PHON-02 — Vowels

The synchronic vowel inventory is `/a e i u/`. Long vowels are written `aa ee ii uu` and represented phonemically as `/aː eː iː uː/` when their quantity is established.

For historical vowel-environment notation:

- **F** = front vowel (`/e i/`)
- **B** = back vowel (`/a u/`)

Thus the four vowel-transition classes are:

| Class | Meaning |
|---|---|
| `F_F` | front → front |
| `F_B` | front → back |
| `B_F` | back → front |
| `B_B` | back → back |

The four classes are evaluated independently. No universal lenition hierarchy is assumed; the concrete outcomes are given by the historical matrix in G-PHON-04/G-PHON-05.

### G-PHON-03 — Consonants

The synchronic consonant inventory is `/p t k m n s h w j r/`. In the established orthography, `c` is a context-dependent spelling: it represents `/ɕ/` from historical `-ki > -ci`, and `/tɕ/` from historical `-ti > -ci`. The spellings `v` and `y` represent `/w/` and `/j/`, respectively.

Conditioned phonetic realization is not exhaustively specified. Historical-source distinctions may survive as phonetic traces without creating additional synchronic phonemes.

### G-PHON-04 — Historical conditioning

The principal historical weakening system is conditioned by the interaction of:

1. the syllable containing the target consonant (**OPEN / CLOSED**), and
2. the neighboring-vowel transition class (**F_F / F_B / B_F / B_B**).

OPEN syllables permit a later stage of weakening than CLOSED syllables in the environments where the consonant has more than one weakening stage. The four vowel-transition classes are otherwise independent rather than ordered on a single scale.

The matrix below is the concrete current system. It applies to historical singleton `p, t, k` targets that reach the general weakening stage. A dash for `B_F` with `t/k` means that pre-/i/ palatalization has priority and the consonant does not enter the ordinary lenition path.

| Syllable | Target | `F_F` | `F_B` | `B_F` | `B_B` |
|---|---|---|---|---|---|
| OPEN | `p` | `h` | `h` | `Ø` | `Ø` |
| OPEN | `t` | `d` | `d` | PAL | `d` |
| OPEN | `k` | `g` | `k` | PAL | `Ø` |
| CLOSED | `p` | `p` | `p` | `h` | `h` |
| CLOSED | `t` | `t` | `t` | PAL | `d` |
| CLOSED | `k` | `k` | `k` | PAL | `g` |

`PAL` is the independently ordered pre-/i/ pathway in G-PHON-05. The written `c` is retained in both outcomes, but its surface pronunciation depends on the historical source.

This matrix is a concrete design completion of cells that are not all directly instantiated by the small current corpus. Attested developments constrain the cells containing `reruka`, `reruta`, `rerupa`, `rupi`, `mente`, and `menta`; unsupported cells are completed by extending the same consonant-specific stage logic without introducing a new lenition series.

### G-PHON-05 — Historical sound laws and relative chronology

`>` denotes a successive historical stage. Later rules apply to the outputs of earlier rules unless an environment explicitly limits the rule.

#### Stage I — Pre-/i/ palatalization

**1. `t, k > c / _i`**

Historical `t` and `k` become orthographic `c` before `/i/`. This `c` is a written merger, not a synchronic phoneme.

**2. `-ti > -ci` in 2P verb morphology**

The 2P agreement sequence `-ti` becomes orthographic `-ci`. In an open syllable, `-ci` is realized `/tɕi/`; when the syllable is closed, the affricate reduces to `/ɕ/`. Thus `-ci` is `/tɕi/`, while `-cin` is `/ɕin/`.

**3. `-ki > -ci > /ɕi/`**

The historical `k` outcome deaffricates to `/ɕ/` before `/i/`.

Established developments include `ruki > ruci > /ruɕi/` and `ruti > ruci > /rutɕi/`. The written forms merge as `ruci`, but their surface pronunciations remain distinct by historical source; `/tɕ/` in the latter is not a separate synchronic phoneme.

#### Stage II — Early sequence restructuring

These changes precede the general weakening process.

**4. `p, t, k + h > pp, tt, kk`**

A stop immediately followed by `h` coalesces as a geminate stop.

Examples:

- `r-u-k-h-a > rukha > rukka`
- `r-u-t-h-a > rutha > rutta`
- `r-u-p-h-a > rupha > ruppa`

Because the stop has been restructured as a geminate, it is no longer an intervocalic singleton target for the later weakening series.

**5. `tc > c`**

Consonant-sequence simplification reduces `tc` to `c`. This belongs to the early cluster-coalescence period rather than the later lexicalized `*ndt > nt:` development.

**6. `wu > u`**

The prohibited sequence `wu` is repaired to `u`.

**7. `yi > ye`**

The prohibited sequence `yi` is repaired to `ye`. The grammatical identity of the final NONPAST marker is unchanged; `e` is the phonological repair rather than a replacement tense exponent.

Thus `ku-t-y-i > kutyi > kutye` retains `-i` as NONPAST historically.

#### Stage III — Conditioned consonant weakening

The three voiceless stops participate in one historically related weakening process, but their first-stage outcomes are consonant-specific. The stage reached is determined by the matrix in G-PHON-04.

**8. `p > h`**

**9. `t > d`**

**10. `k > g`**

The later stages are consonant-specific:

**11. `h > Ø`** in the matrix cells where `p` reaches complete loss.

**12. `g > ɣ`** in the cells where `k` reaches the fricative stage.

**13. `ɣ > Ø`** in the cells where `k` reaches complete loss.

The historical paths therefore remain:

```text
*p > h > Ø
*t > d
*k > g > ɣ > Ø
```

but each consonant reaches only the endpoint permitted by its OPEN/CLOSED × vowel-transition cell.

Established regression paths are now fully represented by the matrix:

```text
reruka > reruga > reruɣa > rerua
reruta > reruda
rerupa > reruha > rerua
rupi > ruhi > rui
ku-p-i > kupi > kuhi > kui
mente > mende
menta > menda
```

`neku`, `seku`, and `keka` also remain unchanged in the general matrix because their `k` occurs in the weak `F_B` environment. Other stable forms whose apparent modern intervocalic stop does not fit the historical exposure of the weakening layer (`apa`, `ita`, and `teta`) are retained as later lexical/structural formations rather than being created as exceptions to the sound law.

Word-initial `*p > h` is historically continuous with the broader `p` weakening but has a distinct environment from intervocalic weakening. Historical `*p` remains distinct from historical `*h`.

#### Stage IV — Generalized sonorant-cluster reduction

Complex sonorant clusters undergo late simplification with compensatory lengthening of the surviving consonant. The currently established cluster-specific outcomes are:

**14. `nm > m:`**

**15. `nr > n:`**

Thus:

```text
menme > mem:e
menra > men:a
```

These are members of a generalized historical cluster-reduction process, not lexical exceptions.

#### Stage V — Later initial-vowel reduction

**16. `a > Ø / #_dV`**

An initial unstressed `a` is lost before `d`.

Thus the established lexical chain is:

```text
*ata > ada > da
```

The later vowel-loss rule is independent of the main stop-weakening matrix and follows `t > d`.

#### Stage VI — Later lexicalized cluster reduction

**17. `*ndt > nt:`**

This is an independent later development attested in lexicalized material. It is not part of either the general weakening series or the generalized sonorant-cluster reduction, and is not established as a productive synchronic rule.

### G-PHON-06 — Historical/synchronic scope

Historical sound laws explain how modern forms arose; they are not automatically productive synchronic alternations.

Lexicalization, morphological reanalysis, analogical restoration, later grammaticalization, and other restructuring may preserve or obscure historical outputs. A modern form should not be changed merely because an older rule could have applied to an earlier stage.

The current modern lexical and example forms are retained while their historical derivations are tested against the concrete matrix.

### G-PHON-07 — Orthography and IPA

The established orthography uses `v = /w/`, `y = /j/`, and context-dependent `c`. IPA records pronunciation rather than orthographic spelling: orthographic `c` is transcribed `/ɕ/` when it derives from `-ki > -ci`, and `/tɕ/` when it derives from `-ti > -ci`.

Long vowels are written doubled and transcribed with IPA length `ː` when established.

When IPA is typed on a standard keyboard, `:` may be used as the plain-text substitute for IPA `ː` for length/gemination. In morphological glossing/segmentation, `:` retains its project/Leipzig use for morphophonological or grammatical fusion.

### G-PHON-08 — Prosody

Stress is predictable rather than contrastive and is mora-weighted:

- `CV` = light (1 mora)
- `CVV` = heavy (2 morae)
- `CVC` = heavy (2 morae)
- `CVVC` = superheavy but treated as heavy for stress assignment

Stress falls on the rightmost heavy syllable. If a word contains no heavy syllable, stress falls on the penultimate syllable. IPA fields must mark the assigned primary stress with `ˈ`, including monosyllables.

### Historical regression notes

The conditioned system replaces the previous blanket `V_V` analysis. The regression evidence now supports the concrete OPEN/CLOSED × F/F transition matrix rather than an unconditional intervocalic rule.

The principal established diagnostic cells are:

- `reruka` — OPEN `B_B`, `k > g > ɣ > Ø`
- `reruta` — OPEN `B_B`, `t > d`
- `rerupa` — OPEN `B_B`, `p > h > Ø`
- `rupi` / `ku-p-i` — OPEN `B_F`, `p > h > Ø`
- `mente` — OPEN `F_F`, `t > d`
- `menta` — OPEN `F_B`, `t > d`
- `neku`, `seku`, `keka` — weak `F_B` `k` environment, no general weakening
- `menme`, `menra` — generalized late sonorant-cluster reduction
- `ada` — later initial-vowel reduction after `t > d`

The stable forms `apa`, `ita`, and `teta` are assigned to a later lexical/structural stratum rather than being used to create exceptions to the productive historical matrix. This preserves the concrete sound laws while allowing historically opaque formations to remain stable.


---

## Morphology

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
| `n-` | local object | `LOC` |
| `Ø` | nonlocal object | `NLOC` |
| `s-` | reflexive | `REFL` |
| `r-` | reciprocal | `RECP` |

The overt object remains a separate noun phrase in SOV clauses. Nominal case suffixes likewise remain on the overt noun phrase. LOCAL/NLOC in this section refers to object status in the verbal object slot and is distinct from nominal LOC case (`-te`).

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

The 3rd-person marker `-p-` participates in the established historical development to `kui` and related forms; the full conditioned historical system is documented in `GRAMMAR.md`.

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

### G-MORPH-11 — Nominal case system

The basic nominal case inventory comprises eight cases:

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

These are the basic nominal cases. Additional semantic functions are constructional extensions of these cases rather than additional nominal cases.

### G-MORPH-12 — Case composition and directional constructions

Nominal cases retain their ordinary suffixes when they participate in larger constructions. Direction is verbal: the finite verb carries `i-` toward/goalward or `a-` away/sourceward, while the noun retains its case suffix.

The ordinary directional construction has no object-slot marking:

`O-CASE i-VERB` → movement toward the case-marked spatial relation  
`O-CASE a-VERB` → movement away from the case-marked spatial relation

The currently established spatial cases participating in directional constructions are LOC, SUPER, INE, and PATH. COM has its own specialized semantic pattern in G-MORPH-13. ABS, ERG, and GEN do not currently directionalize.

#### LOC series

| Polarity | Construction | Function | Meaning |
|---|---|---|---|
| Ø | `O-te` | LOC | at / in |
| i- | `O-te i-VERB` | ALL | to / toward |
| a- | `O-te a-VERB` | ABL | from / away |

The **allative (ALL)** construction expresses movement toward the location itself. It does not by itself introduce a recipient or beneficiary.

A distinct **dative-like (DAT-like)** construction uses the LOC noun phrase together with the verb's object slot. The object slot is interpreted as the recipient/goal participant:

| Object status | Construction | Function | Meaning |
|---|---|---|---|
| LOCAL | `O-te i-n-VERB` | DAT-like | to / for the local recipient |
| NLOC | `O-te i-VERB` | DAT-like | to / for the nonlocal recipient |

ALL and DAT-like are distinct constructions even where their surface segments coincide. ALL is `O-te i-VERB` with no object-slot value; DAT-like is `O-te i-(LOCAL/NLOC)-VERB` and introduces a recipient/goal participant through the object slot. Because NLOC is zero-marked, the NLOC DAT-like form is segmentally identical to ALL; the distinction is syntactic and semantic rather than an additional overt segment. This does not create a new nominal case.

#### SUPER series

| Polarity | Construction | Function | Meaning |
|---|---|---|---|
| Ø | `O-ta` | SUPER | on / against |
| i- | `O-ta i-VERB` | SUBLATIVE | onto / up to surface |
| a- | `O-ta a-VERB` | DELATIVE | off / from surface |

#### INE series

| Polarity | Construction | Function | Meaning |
|---|---|---|---|
| Ø | `O-ci` | INE | inside / within |
| i- | `O-ci i-VERB` | ILLATIVE | into / in through |
| a- | `O-ci a-VERB` | ELATIVE | out of |

#### PATH series

| Polarity | Construction | Function | Meaning |
|---|---|---|---|
| Ø | `O-ra` | PATH | along / through |
| i- | `O-ra i-VERB` | PATH+i- | toward along / across |
| a- | `O-ra a-VERB` | PATH+a- | away along / back |

#### Case stacking

GEN may combine with a restricted set of spatial cases:

| Stacking | Function | Status |
|---|---|---|
| `GEN + LOC` | at / in X's domain | established |
| `GEN + SUPER` | on X's surface / domain | established |
| `GEN + INE` | inside X's domain | established |

These stacked constructions are not assumed to be freely productive over all nominal cases. Productivity limits remain under testing.

### G-MORPH-13 — COM constructions and semantic extensions

COM (`-me`) is a nominal case whose core meaning is **association / accompaniment**. It also supports an instrumental reading when the associated participant is a means, tool, or other inanimate entity. These are contextual readings of one case, not separate nominal cases.

| Construction | Core relation | Typical reading |
|---|---|---|
| `O-me` | association | with / alongside O |
| `O-me` + instrument context | means | with / using O |

The distinction is contextual rather than a strict grammatical animacy split: animate nouns favor accompaniment, while tools and other inanimate nouns readily favor the instrumental/means reading.

With directional morphology, the direction remains on the finite verb and `-me` continues to mark the associated participant:

| Direction | Construction | Spatial relation | Constructional extension |
|---|---|---|---|
| neutral | `O-me VERB` | with / alongside O | accompaniment; instrumental/means where context permits |
| toward | `O-me i-VERB` | toward O | **benefactive**: for / toward the benefit of O |
| away | `O-me a-VERB` | away from O | **malefactive**: to / from O's detriment |

Thus:

`O-me` + `i-VERB` → **benefactive**  
`O-me` + `a-VERB` → **malefactive**

`i-` and `a-` do not alter the COM suffix or introduce applicative morphology. Benefactive and malefactive meanings are constructional extensions of COM plus verbal direction. Instrumental/means remains a contextual reading of neutral COM and is not assigned to the directional opposition.

### G-MORPH-14 — Constructional extensions

Some grammatical functions arise compositionally from existing cases and other established morphology. They are not additional nominal cases.

| Function | Source construction | Interpretation |
|---|---|---|
| PART | GEN (`-se`) | partitive use in divisible/mass contexts |
| ESSIVE | LOC (`-te`) + stative predicate | being at/in a state or location |
| TRANSLATIVE | ESSIVE + `i-ra` | become / come into a state |

The dative-like construction is distinct from the allative: allative describes movement to a location, while the dative-like construction introduces a recipient/goal participant through the verbal object slot. Its LOCAL/NLOC distinction is defined in G-MORPH-12.

`COMP` is not treated as a separate constructional function here because ordinary accompaniment is the core function of COM and is described under G-MORPH-13.

### G-MORPH-15 — Converbs, participles, and nominalization

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

### G-MORPH-16 — Established complex verbal forms

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


---

## Syntax

Status: canonical where stated; unresolved items remain in `STATUS.md`.

## G-SYN — Syntax

### G-SYN-01 — Basic word order

Declarative clauses use SOV order.

### G-SYN-02 — Noun phrase modifier order

Attributive modifiers precede the noun: `sare kerande` = 'large container'. Here `sare` is the LINK form of `sara` 'be.big'.

### G-SYN-03 — Predicative statives

A stative predicate follows its subject: `Kerande sarui` = 'the container is large'.

### G-SYN-04 — Alignment

The language is analyzed as active-stative / Split-S. Speech-act participants are strongly agentive; among third persons, animacy and volitionality condition the alignment pattern. Exact conditioning remains unresolved.

### G-SYN-05 — Pronouns

Established pronouns include `ne` (1SG), `se` (2SG), `er` (3SG), `men` (1PL), `sen` (2PL), and `en` (3PL). ERG forms include `neku`, `seku`, `erku`, `menku`, `senku`, and `enku`. Verbal agreement marks person but not number.

Plural case developments include established `mente > mende` and `menta > menda`. `menme` may surface as `/menme/` or `/mem:e/`, and `menra` as `/menra/` or `/men:a/`; their conditioning remains unresolved. Formal `sese` and reduced `sa/si` variants remain unresolved in distribution.

### G-SYN-06 — Questions

Interrogation is marked by verbal `-y-` in the discourse slot. Example: `Seku kerande kutye?`

### G-SYN-07 — Negation

Negation is verbal morphology, but the marker and template position remain unresolved.

### G-SYN-08 — Relative clauses

Participial relatives precede the noun; finite relative clauses follow the noun.

### G-SYN-09 — Clause combining

Converbs and nominalized clauses are the primary intended strategy for clause combining. Independent conjunctions are not currently established as the primary strategy.

### G-SYN-10 — Adpositions

Nominal relations are primarily expressed through case morphology. An independent adposition system is unresolved.

### G-SYN-11 — Genitives

Genitive position is unresolved.
