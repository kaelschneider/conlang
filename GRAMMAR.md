# Grammar

## Phonology

Status: canonical where stated; unresolved conditions remain in `STATUS.md`.

## G-PHON — Phonology

### G-PHON-01 — Syllable structure

Surface syllable structure is `(C)V(C)`. Productive onset clusters are not established. Complex sequences may arise historically or morphologically and subsequently reduce or fuse. A productive morphophonological repair applies at the verbal object-stem boundary: `n + C → enC`, so the LOCAL object marker surfaces as `en-` before consonant-initial stems.

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

This matrix is a concrete design completion of cells that are not all directly instantiated by the small current corpus. Attested developments constrain the cells containing `reruka`, `reruta`, `rerupa`, `rupi`, `mente`, and `menta`; unsupported cells are completed by extending the same consonant-specific stage logic without introducing a new lenition series. In particular, OPEN F_B is an independent retention environment for `k`, while CLOSED F_F/F_B retention reflects the additional blocking effect of syllable closure; neither pattern is intended as a universal lenition hierarchy.

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

Because the stop has been restructured as a historical geminate, it is no longer an intervocalic singleton target for the later weakening series. The geminate stage is historical rather than a productive synchronic consonant-length contrast; modern surface forms conform to the `(C)V(C)` phonotactics and may realize the outcome as a single stop.

**5. `tc > c`**

Consonant-sequence simplification reduces `tc` to `c`. This belongs to the early cluster-coalescence period rather than the later lexicalized `*ndt > nt:` development.

**6. `wu > u`**

The prohibited sequence `wu` is repaired to `u` wherever the sequence occurs. This is a general phonological repair rather than a morphologically restricted alternation.

**7. `yi > ye` across a morpheme boundary**

The prohibited sequence `yi` is repaired to `ye` when it arises across a morpheme boundary. The grammatical identity of the final NONPAST marker is unchanged; `e` is the phonological repair rather than a replacement tense exponent.

Thus `ku-t-y-i > kutyi > kutye` retains `-i` as NONPAST historically. The rule is a phonological boundary repair, not a lexicalized replacement of the tense marker.

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

Sonorant clusters with strong similarity undergo late simplification, especially across morphological boundaries, with phonetic lengthening of the surviving sonorant. The process is historically favored at morpheme boundaries but may spread into lexicalized material. The attested `nm` outcome proceeds by ordinary nasal place assimilation, while `nr` proceeds by the nasal-dominant assimilation described below.

The currently established outcomes are:

**14. `nm > mm > m:`**

**15. `nr > nn > n:`**

The `nm > mm` step is ordinary nasal place assimilation; the `nr > nn` step is nasal-dominant assimilation within a highly similar sonorant cluster rather than a general rule turning `r` into `n`.

Thus:

```text
menme > mem:e
menra > menna > men:a
```

The resulting `m:` and `n:` represent phonetic/metrical duration, not a new synchronic phonemic length contrast. In synchronic phonemic analysis, the surviving consonants remain /m/ and /n/. These are members of a generalized historical cluster-reduction process, not lexical exceptions.

#### Stage V — Later initial-vowel reduction

**16. `a > Ø / #_dV`**

An initial unstressed `a` is lost before `d`.

Thus the established lexical chain is:

```text
*ata > ada > da
```

The later vowel-loss rule is independent of the main stop-weakening matrix and follows `t > d`.

#### Stage VI — Later lexicalized and morphological reduction

**17. `-anute > -ante` in nominalizer + LOC sequences**

In the historical `kera + -nu + -te` sequence, the unstressed vowel of the `-nu-te` sequence is lost:

`keranute > kerante`

The contraction was historically productive in this morphological environment.

**18. `nt > nd` in the same lexicalized sequence**

Post-nasal voicing yields:

`kerante > kerande`

This is a localized historical development of the nominalizer-plus-LOC sequence, not a general modern alternation.

**19. `*ndt > nt:`**

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

Stress falls on the **rightmost heavy syllable**. If a word contains no heavy syllable, stress falls on the **penultimate syllable**. IPA fields must mark the assigned primary stress with `ˈ`, including monosyllables.

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

Status: canonical where stated; residual lexical/phonetic edge cases remain in `STATUS.md`.

## G-MORPH — Morphology

### G-MORPH-01 — Morphological profile

The language has compact, consonant-heavy morphology with historically fused/reduced forms and inherited monoconsonantal roots. The overall morphological type is mixed rather than assigned a single typological label.

### G-MORPH-02 — Verb template

Finite verbs follow:

`(DIRECTION) (IMPERATIVE) (OBJECT) STEM (AUX/DERIV) APPL AGENT (NEG) (DISCOURSE) TENSE (ASPECT)`

NEG is the invariant suffix `-su-` in the right-edge inflectional zone, immediately after person agreement and before optional discourse marking. It is a dedicated polarity exponent (`NEG`). Negation does not alter stem grade, direction, object status, or the positions of discourse, tense, or aspect.

APPL is a dedicated verbal suffixal slot immediately after AUX/DERIV. Its productive exponent is `-ka-`. APPL adds one selected relational participant to the verb's core argument structure. It is available to overt relational NPs and to inherently relational arguments that are lexically licensed by the predicate. Finite verbs require a person-agreement marker. The agreement controller is the semantic agent where an agentive argument exists; in agentless/stative predicates, the single S argument controls agreement.

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


### G-MORPH-05 — Object slot

There is exactly one object slot. In the experimental relational system, the slot is organized by participant status:

| Marker | Function | Leipzig gloss |
|---|---|---|
| `n-` | 1P or 2P object | `LOCAL` |
| `m-` | ordinary 3P animate object | `3P.ANIM` |
| `Ø` | ordinary 3P inanimate object | `3P.INAN` |
| `v-` | obviative object | `OBV` |
| `s-` | reflexive | `REFL` |
| `r-` | reciprocal | `RECP` |

The overt object remains a separate noun phrase in SOV clauses, and the noun retains its nominal case suffix. Object indexing is distinct from nominal LOC case (`-te`). The LOCAL form intentionally merges 1P and 2P objects; speaker/addressee interpretation is recovered from discourse.

The `n- + C → enC` repair remains productive before consonant-initial verb stems. Before vowel-initial stems, `n-` remains `n-`.

OBV is a discourse-status category rather than a fourth person. When a third-person referent is obviative, `v-` replaces the ordinary third-person index rather than stacking with `m-`.

### G-MORPH-06 — AUX/DERIV

The following light roots occur in the AUX/DERIV slot and take the linking `-e-` grade:

| Root | Basic lexical meaning | AUX form | Semantic value | Leipzig gloss |
|---|---|---|---|---|
| `*r` | go | `-re-` | progressive | `PROG` |
| `*k` | hold | `-ke-` | continuative | `CONT` |
| `*m` | live / dwell / stay | `-me-` | habitual | `HAB` |
| `*s` | cut / remove | `-se-` | inchoative | `INCH` |
| `*t` | transfer | `-te-` | change-of-state / transformative | `CHG` |

AUX/DERIV morphology and final verbal aspect are separate slots and may co-occur. `-te-` is synchronically productive but semantically restricted, favoring predicates involving a change into a new state or condition. `-we-` and productive `-w-` were considered during development but are dropped from the canonical system.

### G-MORPH-06A — Applicative

The productive applicative exponent is `-ka-`.

APPL is a single productive valency operation. It adds **one** relational participant to the verb's core argument structure; unrestricted APPL stacking is not productive.

The APPL-selected participant must be either:

- an overt relational NP marked by a productive relational case;
- an inherently relational argument independently licensed by the lexical predicate.

When several relational NPs are eligible, selection proceeds by:

1. semantic argument hierarchy;
2. discourse prominence for genuine same-rank ties;
3. linear word order for any remaining genuine tie.

The working hierarchy is **patient/theme > recipient/goal > beneficiary/maleficiary > other applied participant**.

APPL selection occurs before object indexing. Once selected, the applied relational participant occupies the single object-index position. The lexical patient/theme remains an overt ABS core participant and is not separately indexed in these APPL constructions. The object slot therefore does not function as a general competition among all core arguments; it is the single participant-index position used by the APPL-promoted relational argument.

The hierarchy is evaluated only over participants that are actually eligible for APPL. A lexical patient/theme is not an APPL candidate merely because it is already a core argument. Multiple relational NPs may therefore coexist, but only one is promoted and indexed; unselected relational NPs remain ordinary case-marked relations.

With stative predicates, APPL is available only where the predicate independently licenses an affected participant. Direction and aspect remain independent of APPL.

APPL follows the complete AUX/DERIV material and precedes AGENT:

`STEM (AUX/DERIV) APPL AGENT`

No APPL-specific allomorphy is currently established.

### G-MORPH-07 — Agreement

| Person | Marker | Leipzig gloss |
|---|---|---|
| 1 | `-k-` | `1` |
| 2 | `-t-` | `2` |
| 3 | `-p-` | `3` |

Agreement is person-only: the markers do not distinguish singular from plural. Finite verbs require one person marker. Agreement follows the semantic agent when an agentive argument exists; a stative or otherwise agentless single S argument controls agreement. Number is expressed independently, including by pronouns.

The 3rd-person marker `-p-` participates in the established historical development to `kui` and related forms; the full conditioned historical system is documented in `GRAMMAR.md`.

### G-MORPH-08 — Discourse / mood

| Marker | Function | Leipzig gloss |
|---|---|---|
| `-h-` | exclamative | `EXCL` |
| `-y-` | interrogative | `INT` |
| `ka-` | imperative | `IMP` |

The imperative is a dedicated verbal prefix. Its structural position is after any directional prefix and before the ordinary object slot:

`(DIRECTION) ka- (OBJECT) STEM ...`

Imperative clauses suppress ordinary person agreement. The addressee is pragmatically understood unless an overt subject is independently required for contrast, deixis, or discourse reasons. Number is therefore not encoded on the imperative verb.

The default imperative uses the existing citation/nonfinite stem rather than the realis or irrealis stem. A distinct special imperative grade is not synchronically productive; lexicalized exceptional forms may develop historically.

Thus the default relationship is:

`ka- + STEM-NFIN`

and with direction:

`i- + ka- + STEM-NFIN`
`a- + ka- + STEM-NFIN`

The imperative prefix `ka-` is distinct from APPL `-ka-` in both position and function. Adjacent identical material is permitted; an imperative of HOLD, whose citation form is `ka`, therefore yields `kaka`.

Hortatives reuse the imperative construction with an overt 1PL subject where needed for disambiguation or emphasis. No dedicated hortative exponent is established.

Prohibitives are compositional NEG + IMP. NEG retains its ordinary right-edge position; the imperative continues to suppress ordinary person agreement. The exact surface pattern of NEG in commands is therefore morphological composition rather than a separate prohibitive construction.

The exclamative `-h-` and interrogative `-y-` remain in the discourse slot. Imperative is a separate outer mood prefix and is not equivalent to either discourse marker.

### G-MORPH-09 — Tense

`-i-` = nonpast (`NPST`); `-a-` = past (`PST`).

### G-MORPH-10 — Aspect

`Ø` = imperfective (`IPFV`); `-n` = perfect (`PRF`).

### G-MORPH-11 — Nominal number and case

Common nouns do not obligatorily inflect for number. A restricted productive plural category is available where overt number is useful. The plural is animacy-sensitive:

| Noun class | Plural exponent | Status |
|---|---|---|
| Animate | `-i` | productive |
| Inanimate | `-n` | productive |

Number morphology precedes nominal case suffixes. An archaic dual survives in a small lexicalized set of conventionalized natural-pair nouns; it is not synchronically productive.

The experimental nominal case inventory contains seven values, six overt and ABS zero:

| Case | Suffix | Core relational meaning | Semantic domain | Leipzig gloss |
|---|---|---|---|---|
| ABS | `Ø` | patient / S | core argument | `ABS` |
| ERG | `-ku` | agent / controller | core argument | `ERG` |
| LOC | `-te` | spatial landmark / reference frame | relational | `LOC` |
| CONTAINMENT | `-ci` | bounded interior / domain | relational | `CONTAIN` |
| POSITION | `-ta` | positional / contact / support configuration | relational | `POSITION` |
| COM / ASSOCIATIVE | `-me` | association / accompaniment / means / medium / route | relational | `COM` |
| GEN | `-se` | identifying relation between nominals | relational | `GEN` |

GEN is a noun-to-noun relation covering possession, kinship, part-whole, attribution, origin, material/composition, and related identifying relations. The productive GEN exponent is `-se`, consistent with the established pronominal pattern `se-se`; the former PATH exponent `-ra` is not a synchronic case exponent. Former PATH meanings are represented by COM/ASSOCIATIVE `-me`. COM is event-oriented association and is distinct from GEN.

The former PATH domain is absorbed into COM/ASSOCIATIVE and is not a separate synchronic case. Traditional labels such as ALLATIVE, ABLATIVE, INESSIVE, ILLATIVE, SUPERESSIVE, SUBLATIVE, DELATIVE, COMITATIVE, INSTRUMENTAL, and PERLATIVE describe recurring constructional interpretations rather than additional case morphemes.

### G-MORPH-12 — Relational frames, directional constructions, and case stacking

Nominal case establishes a relational frame; direction is verbal and supplies the relational vector. The experimental system has four productive relational frames:

| Frame | `Ø` | `i-` | `a-` |
|---|---|---|---|
| LOC | relation holds at/by frame | convergence toward frame | divergence away from frame |
| CONTAINMENT | relation holds within domain | convergence into domain | divergence out of domain |
| POSITION | configuration holds | enter/establish configuration | leave/terminate configuration |
| COM | association/accompaniment | convergent association | divergent association |

The ordinary construction is `O-CASE (i-/a-) VERB`. The noun retains its case suffix; direction remains verbal.

Each relational frame can, where the lexical predicate licenses the relation, combine with the single productive APPL. APPL adds the relational participant to the verb's core argument structure; the selected participant then occupies the single object-index position. The full frame × direction × APPL space is productive at the constructional level, subject to lexical semantic licensing.

#### LOC series

`O-te` anchors the event at/by a landmark. `O-te i-VERB` orients the event toward the landmark; `O-te a-VERB` orients it away from the landmark.

With APPL:

| Direction | Construction | Function |
|---|---|---|
| neutral | `O-te Ø-VERB-APPL` | the landmark is promoted as a core participant; the relation remains statically anchored |
| toward | `O-te i-VERB-APPL` | the landmark is promoted as a convergent goal/reference |
| away | `O-te a-VERB-APPL` | the landmark is promoted as a divergent source/reference |

The neutral construction does not require a directed transition: direction is absent while the LOC relation supplies the anchoring frame. In the away construction, the promoted landmark is construed as the source/reference from which the event diverges.

Object-index realization follows the general object-slot inventory in G-MORPH-05. Thus an ordinary 3P animate landmark uses `m-`, while an ordinary 3P inanimate landmark uses zero.

Bare `O-te i-VERB` remains the non-applied allative/goal-oriented construction; recipient/landmark promotion is signaled by APPL rather than by a separate case.

#### CONTAINMENT series

`O-ci` expresses a relation within a bounded domain. `O-ci i-VERB` orients an event into the domain; `O-ci a-VERB` orients it out of the domain.

With APPL:

| Direction | Construction | Function |
|---|---|---|
| neutral | `O-ci VERB-APPL` | the bounded domain itself is promoted as a core participant without directional change |
| toward | `O-ci i-VERB-APPL` | the relevant participant/domain relation converges into the bounded domain |
| away | `O-ci a-VERB-APPL` | the relevant participant/domain relation diverges out of the bounded domain |

The neutral APPL construction therefore treats the bounded domain as an argument-bearing relational participant while retaining the static containment relation.

#### POSITION series

`O-ta` expresses a positional, contact, or support configuration. `O-ta i-VERB` establishes or enters the configuration; `O-ta a-VERB` leaves or terminates it.

With APPL:

| Direction | Construction | Function |
|---|---|---|
| neutral | `O-ta VERB-APPL` | the participant in the existing support/contact configuration is promoted without directed change |
| toward | `O-ta i-VERB-APPL` | the participant enters or establishes the support/contact configuration |
| away | `O-ta a-VERB-APPL` | the participant leaves or terminates the support/contact configuration |

The vector is constructionally independent of APPL: APPL adds the participant, while `i-` and `a-` specify the direction of change relative to the POSITION frame.

#### COM / ASSOCIATIVE series

`O-me` expresses association or accompaniment. With a means-, instrument-, medium-, or route-like participant, the same case supports those contextual interpretations.

With APPL:

| Direction | Construction | Function |
|---|---|---|
| neutral | `O-me VERB-APPL` | the associated participant is promoted as a core participant without inherent benefit/harm or directed divergence/convergence |
| toward | `O-me i-VERB-APPL` | the associated participant is promoted with convergent orientation; beneficiary-type readings may arise |
| away | `O-me a-VERB-APPL` | the associated participant is promoted with divergent orientation; maleficiary-type readings may arise |

Neutral COM APPL therefore remains semantically associative rather than automatically benefactive or malefactive. Directional COM extensions remain constructional consequences of the independent vector.

#### Case stacking

Case stacking is restricted and compositional:

> **The inner case constructs a relational domain; the outer case relates that constructed domain to something else.**

| Stack | Function | Status |
|---|---|---|
| `CONTAINMENT → LOC` | locate a region/place within the bounded domain | productive experimental |
| `GEN → CONTAINMENT` | construct a bounded domain belonging to/defined by X | productive experimental |
| `GEN → LOC` | locate something at/in X's relational domain | productive experimental |

Reversed case order is not productive. Repeated identical case is not productive. ERG does not freely participate in case stacking. Additional combinations remain constructional tests rather than part of the productive core.

### G-MORPH-13 — COM constructions and semantic extensions

COM (`-me`) is the core event-oriented associative case. It covers association and accompaniment and can extend contextually to means/instrument and route/medium. The former PATH domain is therefore represented inside COM rather than by a separate case.

| Direction | Construction | Typical interpretation |
|---|---|---|
| neutral | `O-me VERB` | accompaniment / association; means or medium where licensed |
| toward | `O-me i-VERB` | convergent association; with APPL, the selected associated participant may be promoted as beneficiary |
| away | `O-me a-VERB` | divergent association; with APPL, the selected associated participant may be promoted as maleficiary |

Benefactive and malefactive are constructional interpretations of COM + direction + APPL; they are not separate case morphemes. Direction remains the general relational vector, and APPL remains the independent valency operation.

### G-MORPH-14 — Constructional extensions

Some grammatical functions arise compositionally from existing cases and other established morphology. They are not additional nominal cases.

| Function | Source construction | Interpretation |
|---|---|---|
| PART | GEN (`-se`) | partitive use in divisible/mass contexts |
| ESSIVE | LOC (`-te`) + stative predicate | being at/in a state or location |
| TRANSLATIVE | LOC (`-te`) + `i-` + stative predicate | becoming / coming into a state or relation |

The dative-like construction is distinct from the allative: allative describes orientation toward a location, while the dative-like construction introduces a recipient/goal participant through the verbal object slot. Its object-index realization is defined in G-MORPH-12.

`COMP` is not treated as a separate constructional function here because ordinary accompaniment is the core function of COM and is described under G-MORPH-13.

### G-MORPH-14A — Mood and modality

The imperative is marked by the dedicated prefix `ka-`, after any directional prefix and before the ordinary object slot. Imperatives suppress ordinary person agreement and default to the citation/nonfinite stem. The imperative prefix is distinct from APPL `-ka-`.

Hortatives reuse the imperative construction with an overt 1PL subject when pragmatically useful. Prohibitives are NEG + IMP compositionally; there is no separate prohibitive exponent.

Modal auxiliaries are finite preverbal operators. They carry the ordinary finite morphology (stem grade, agreement, tense, and aspect), while the lexical predicate appears in the nonfinite/citation form. The auxiliary is positioned immediately before the lexical predicate, after the ordinary object and other overt clause arguments.

Clause-level modal particles precede the clause and carry broad scope. The current epistemic/evidential particle is `hi`.

The experimental modal inventory is:

| Form | Type | Meaning | Source |
|---|---|---|---|
| `kera` | modal AUX | necessity / must | CARRY lexical domain; grammaticalized |
| `ure` | modal AUX | possibility / may | DREAM lexical domain; grammaticalized |
| `nete` | modal AUX | intention / intend | THINK lexical domain; grammaticalized |
| `hi` | modal PART | epistemic/evidential uncertainty | SAY/BLOW lexical domain; grammaticalized |

`kera` as a necessity auxiliary is synchronically homonymous with lexical `kera` CARRY. The distinction is established by syntactic category and the auxiliary construction rather than by a new phonological form.

Modal auxiliary clauses retain ordinary verbal direction and relational structure on the nonfinite lexical predicate. Object indexing and APPL remain associated with the clause's lexical argument structure; their interaction with modal auxiliaries is a dedicated stress-test area rather than an automatic reassignment.

Modal meaning scopes over negation by default. When a lexical complement is negated, NEG precedes the nonfinite/citation ending on that complement (`STEM-NEG-NFIN`), yielding modal > negation by default. NEG on the finite modal auxiliary instead yields negation of the modal proposition (`NEG > MOD`). Thus the two scope readings are compositionally distinguishable without a new scope morpheme.

Modal auxiliaries and particles form no single transparent synchronic paradigm. Their partially related forms reflect independent grammaticalization histories; sound symbolism may bias future lexicalized modal developments only weakly.
### G-MORPH-15 — Converbs, participles, and nominalization

Converbial clauses are analyzed through nominalization plus case; the case supplies the converbial relation. Same-subject continuity is the unmarked interpretation. An overt GEN-marked subject inside the nominalized clause marks a switch to a different subject. This gives an explicit switch-reference contrast without a dedicated switch-reference affix.

The productive converb relations use LOC, CONTAINMENT, POSITION, and COM/ASSOCIATIVE; case meaning remains recognizable while temporal, causal, purposive, manner/means, and related readings arise from constructional context. Independent conjunctions are not the primary strategy for subordination or clause chaining.

Participles are productive and are formed from the nonfinite/citation stem:

| Form | Function | Leipzig gloss |
|---|---|---|
| `-ri` | agentive participle | `AG.PTCP` |
| `-na` | patientive participle | `PAT.PTCP` |
| `-mu` | resultative participle | `RES.PTCP` |

`-nu` is the recovered nominalizer. The working derivational family is:

- `keranu` = carrying / carrying event
- `keranka` = carrier / person associated with carrying
- `kerande` = container / place, instrument, or means associated with carrying

`kerande` remains the canonical CONTAINER lexeme. Its historical pathway is `kera + -nu + -te > keranute > kerante > kerande`: the `-nu-te` sequence undergoes vowel syncope (`keranute > kerante`) followed by localized post-nasal voicing (`nt > nd`). The historical contraction was productive in the nominalizer-plus-LOC environment, but the modern result is partially fossilized. `keranu` remains a productive nominalization rather than a required lexical entry; `keranka` is a lexicalized carrier noun. The final `-de` in `kerande` preserves a weak semantic association with LOC but is not a freely productive synchronic suffix.

### G-MORPH-16 — Established complex verbal forms

`kerurekin` = `keru-re-k-i-n` (CARRY.REAL-PROG-1-NONPAST-PERF). It demonstrates co-occurrence of AUX/DERIV, agreement, tense, and aspect.

`ku-p-i > kupi > kuhi > kui` demonstrates the 3rd-person realis/nonpast form `kui` through historical `p > h > Ø` development.

`ku-t-y-i > kutyi > kutye` demonstrates interrogative `-y-` plus NONPAST `-i`, with phonological repair because `-yi` is prohibited.

`hukka < hu-k-h-a` is a lexicalized verbal derivative preserving productive `-h-` EXCL morphology; its lexicalized meaning is fixed, while the historical segmentation remains transparent enough to identify the discourse exponent.

## Lexical derivation and generation model — ANALYZED

The following is the current **lexical-generation model** derived from the morphology decisions of 2026-09-17. It describes how new lexical material is to be generated and filtered; it does not by itself promote unestablished derivational exponents to productive grammar.

### Root inventory

Inherited lexical roots use a mixed mono-/disyllabic shape system. The base distribution below is global; semantic-domain shape biases may make small local deviations in which semantic centers receive which shapes, while capacity-aware allocation preserves the global target as far as legal capacity permits.

| Root shape | Base frequency |
|---|---:|
| V | 0.25% |
| C | 0.50% |
| CV | 2.00% |
| VC | 2.00% |
| CVC | 15.25% |
| VCV | 8.00% |
| CVCV | 72.00% |

Thus, at the default 1,600-root target, **20% of roots are short/monosyllabic shapes** and the remainder are disyllabic. Short forms are deliberately preserved as a compact lexical core rather than exhausted indiscriminately.

The inherited-root generator treats `V, C, CV, VC, CVC, VCV,` and `CVCV` as explicit legal root shapes. `CVCV` is a genuine two-syllable inherited root shape here; this is distinct from the separate morphological process `CVC + stem vowel → CVCV`, which produces the same surface sequence from a shorter root.

When the configured target exceeds the capacity of a primary root shape, the generator redistributes only the shortfall into explicitly configured fallback shapes. The current emergency fallback is `CVCVC`, still composed of ordinary `(C)V(C)` syllables. No unconfigured shape is ever introduced silently.

`CVCC` is not an independent root shape. It is derived by adding a consonant to a CVC root:

`CVC + C → CVCC`

A stem grade is then added after the root or derived root:

- `C + stem vowel → CV`
- `VC + stem vowel → VCV`
- `CVC + stem vowel → CVCV`
- `CVC + C + stem vowel → CVCCV`

### Syllable-final phonotactic filter

Newly generated roots exclude `h` and `j` from **every syllable-final consonant position**. This is a root-generation constraint, not a universal ban on `h` or `j` in word-final or derived forms.

For ordinary root shapes, this affects the coda of `VC` and `CVC`. If the emergency `CVCVC` fallback is used, both coda positions are restricted. The two-syllable `CV.CV` and `V.CV` shapes have no syllable-final consonant and therefore impose no additional exclusion.

The established historical one-segment roots `h` and `j` remain unaffected.


### Lexical category and family formation

Roots are category-neutral by default. A minority may have weak noun- or verb-oriented biases. Root shape has only a weak statistical correlation with lexical category; shape is not a categorical noun/verb marker.

Roots are generated both independently and as members of deliberately seeded semantic families. Semantic-family seeding should emphasize broad semantic domains and culturally salient concepts rather than arbitrary lists of near-synonyms.

Potential derivations are generated for all root shapes. Derivational productivity is frequency-sensitive rather than shape-exclusive: common or semantically central roots may support larger lexical families, while many roots remain simple. Approximately 55% of roots are expected to remain morphologically simple.

### Productive derivation

The productive derivational core remains compact, with approximately four to five synchronically productive mechanisms. The system is mixed: derivation may be category-changing or meaning-extending, and formal mechanisms need not all have the same historical origin. Older derivational strata coexist with this core and may survive as partially productive, lexically restricted, or opaque patterns.

The following principles are established for generation:

1. Category-changing and meaning-extending derivation are both productive domains.
2. Verb-to-noun derivation is favored over noun-to-verb derivation, but both directions remain available.
3. `CVC + C → CVCC` is primarily associated with event/action verbalization, while individual lexicalized derivatives may develop more specific meanings or secondary functions.
4. Derivational mechanisms are mostly category-oriented, but historical/semantic strata may overlap and produce non-identical functions.
5. Zero derivation/conversion remains available, especially for closely related noun/verb pairs.
6. Synchronically productive derivations normally compose to at most two layers; unrestricted stacking is not the default. Older lexicalized forms may preserve deeper historical layering through reanalysis or fusion.

This generation model does not by itself determine the status of individual grammatical exponents. The productive participles `-ri`, `-na`, and `-mu`, and the semantically restricted `-te-` change-of-state auxiliary, are established independently by the current morphology.

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

### Directional semantics in lexical generation

Root generation must account for the independent semantic contribution of verbal direction. `i-` expresses movement toward/goalward and `a-` movement away/sourceward, so roots should not be selected solely for an English gloss when a directional contrast can supply a more natural lexical organization.

Prefer roots whose semantic frame combines productively with direction. In particular, a general transfer relation is more useful than a root whose lexical meaning already fixes one endpoint relation such as GIVE: a transfer root can yield toward-recipient, away-source, or neutral transfer readings through `i-`, `a-`, or zero direction. Likewise, motion-oriented roots should leave directional meaning available for composition rather than redundantly lexicalizing a single direction.

The same toward/away opposition may acquire **metaphorical and constructional extensions** from the underlying spatial schema. `i-` may develop readings in which an event, action, or participant is oriented toward, for, or into the interest/state of another participant; `a-` may develop readings in which it is oriented away from, against, out of, or to the detriment of another participant. The established COM pattern is an example: `O-me + i-VERB` can be benefactive and `O-me + a-VERB` can be malefactive. Future lexical families should therefore consider not only literal goal/source alternations but plausible semantic extensions involving benefit, harm, acquisition, disposition, support/opposition, inclusion/exclusion, initiation/completion, and other culturally or lexically conventionalized mappings from spatial direction. These are candidate semantic pathways, not automatic meanings of `i-` or `a-`.

During candidate-family generation, test semantically central roots against neutral, `i-`, and `a-` frames where their valency permits them, and separately consider metaphorical readings licensed by the root's semantic frame. Penalize roots that merely duplicate a productive directional construction unless lexicalization or semantic specialization provides an independent motivation. Preserve established constructional meanings such as benefactive/malefactive while distinguishing them from free semantic polysemy. This is a lexical-generation heuristic, not a new rule of synchronic morphology.

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

Status: canonical where stated; residual lexical/phonetic edge cases remain in `STATUS.md`.

## G-SYN — Syntax

### G-SYN-01 — Basic word order

Declarative clauses use SOV order.

### G-SYN-02 — Noun phrase modifier order

Attributive modifiers precede the noun: `sare kerande` = 'large container'. Here `sare` is the LINK form of `sara` 'be.big'.

### G-SYN-03 — Predicative statives

A stative predicate follows its subject: `Kerande sarui` = 'the container is large'.

### G-SYN-04 — Alignment

The language has an active-stative / Split-S alignment. Speech-act-participant S arguments (1st/2nd person) pattern agentively. Third-person S is agentive when animacy and volitionality support an agentive interpretation and patientive otherwise.

Agentive S and A take ERG; patientive S and O take ABS. The split therefore has a person-conditioned core and an animacy/volitionality-conditioned third-person extension.

### G-SYN-05 — Pronouns

Established pronouns include `ne` (1SG), `se` (2SG), `er` (3SG), `men` (1PL), `sen` (2PL), and `en` (3PL). ERG forms include `neku`, `seku`, `erku`, `menku`, `senku`, and `enku`. Verbal agreement marks person but not number.

Plural case developments include established `mente > mende` and `menta > menda`. Common nouns have restricted productive number marking rather than obligatory number inflection; animate nouns use productive `-i`, while inanimate nouns use productive `-n`. An archaic dual survives in conventionalized natural-pair nouns as a nonproductive lexical residue. `menme` may surface as `/menme/` or `/mem:e/`; `menra` is retained as a historical former-PATH form for the phonological regression and may surface as `/menra/` or `/men:a/` under prosodically conditioned reduction. Formal `sese` and reduced `sa/si` are likewise prosodically conditioned variants. `sese` is retained under prominence; `sa` is the ordinary unstressed reduction, while `si` represents a more extreme reduction favored in very weak or clitic-like positions.

### G-SYN-06 — Questions

Interrogation is marked by verbal `-y-` in the discourse slot. Example: `Seku kerande kutye?`

### G-SYN-07 — Negation

Negation is verbal morphology in the right-edge inflectional zone. Its slot is after AGENT and before optional DISCOURSE, TENSE, and ASPECT. The exponent is invariant `-su-`; it has no negative stem grade or special agreement/tense allomorphy.

### G-SYN-08 — Relative clauses

Participial relatives precede the noun; finite relative clauses follow the noun. Finite relatives use a gap for the relativized argument rather than a dedicated relative pronoun or obligatory resumptive.

### G-SYN-09 — Clause combining

Converbs and nominalized clauses are the primary strategy for subordination and clause chaining. Same-subject continuity is unmarked; an overt GEN-marked subject in the nominalized clause marks switch-reference. Case meanings remain broadly polyfunctional across converbial relations.

### G-SYN-10 — Adpositions

Nominal relations are primarily expressed through case morphology. A small independent postposition class may coexist with case; these adpositions are expected to arise historically from nouns or case-bearing relational expressions and need not duplicate the core case inventory.

### G-SYN-11 — Genitives

GEN-marked possessors precede the head noun and participate in the general prenominal modifier order. Overt subjects of nominalized clauses are also GEN-marked.


### G-SYN-12 — Coordination

Independent clauses are normally coordinated by juxtaposition. A small closed set of conjunctions is available where overt coordination is useful, especially for contrast, additive linkage, or discourse clarity. Conjunctions are secondary to juxtaposition and are not the primary mechanism for subordination.

### G-SYN-13 — Information structure
### G-SYN-14 — Imperatives and modality

Imperative mood is expressed by verbal `ka-` after any directional prefix and before the object slot. Imperatives suppress ordinary person agreement; the addressee is normally implicit. The default imperative uses the citation/nonfinite stem.

Hortatives reuse the imperative construction with an overt 1PL subject when pragmatically necessary. Prohibitives are formed compositionally from NEG + imperative.

Clause-level modality is structurally distinct from imperative mood. Two modal realization types are permitted:

1. **clause-level modal particles** with broad scope over the clause;
2. **modal auxiliaries** in the immediate preverbal position for tighter association with the event/predicate.

Modal auxiliaries carry ordinary finite morphology; the lexical complement appears in the citation/nonfinite form. Clause-level particles precede the clause.

The initial modal inventory is `kera` NECESSITY, `ure` POSSIBILITY, `nete` INTENTION/VOLITION, and `hi` EPISTEMIC/EVIDENTIAL UNCERTAINTY.

By default, modal meaning scopes over negation. Exact negative-complement morphology under a modal auxiliary remains an explicit stress-test question.



Neutral declaratives retain SOV order. A discourse topic may be placed at the left edge of the clause without changing its grammatical role. Narrow or contrastive focus favors the immediately preverbal position and receives prosodic prominence. No dedicated topic or focus particle is required; information-structural effects are expressed through constituent order plus prosody.