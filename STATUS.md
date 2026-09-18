# Status

**Last updated:** 2026-09-18  
**Phase:** Core grammar established; remaining work is validation, corpus growth, and lexical expansion  
**Repository structure:** Consolidated grammar source; minimal flat structure

## Canonical files

- `GRAMMAR.md` — canonical consolidated grammar: phonology, morphology, syntax, prosody, and historical sound change
- `LEXICON.tsv` — canonical lexical/root inventory
- `EXAMPLES.tsv` — example and test corpus
- `SCHEMA.json` — structural validation schema
- `AGENTS.md` — repository maintenance instructions

## Experimental relational case / directional / applicative system — 2026-09-18

**Status: EXPERIMENTAL.** This section records the current working system developed for continued testing. It is intentionally **not canonical** and does not replace the morphology, syntax, lexicon, or examples currently established in `GRAMMAR.md`, `LEXICON.tsv`, or `EXAMPLES.tsv`. The experiment is isolated on branch `experimental-relational-case-system`; `main` remains unchanged.

### Experimental architecture

Working clause template:

`NOUN-[NUMBER]-[CASE] DIRECTIONAL-[OBJECT]-VERB-[APPL/DERIVATION]-[AUX1]-[SUBJECT]-[TENSE]-[NEG/DISCOURSE]-[ASPECT]`

Semantic order:

`CASE → relational frame → DIRECTIONAL → event vector → APPL → core-argument addition → OBJECT → participant indexing → VERB → event structure → ASPECT → temporal contour`

The system is intended for an SOV language with active-stative / ERG-ABS alignment and substantial historical fusion.

### Experimental nominal case inventory

Seven case values are proposed: six overt cases plus ABS zero.

| Case | Form | Core meaning |
|---|---:|---|
| ABS | `Ø` | unmarked patient/theme; patientive S |
| ERG | `-ku` | agent/controller; agentive S |
| LOC | `-te` | spatial landmark/reference |
| CONTAINMENT | `-ci` | bounded interior/domain |
| POSITION | `-ta` | positional/contact/support configuration |
| COM / ASSOCIATIVE | `-me` | association, accompaniment, medium, instrument, route |
| GEN | `-ra` | inherent/identifying relation between one nominal entity and another |

GEN is deliberately distinct from COM. GEN is noun-to-noun and covers possession, kinship, part-whole, attribution, origin, material/composition, and related identifying relations. COM is event-oriented association and can extend to accompaniment, means/instrument, and route/medium.

The experimental system therefore **absorbs PATH into COM/ASSOCIATIVE** and does not posit a separate PATH case.

### Experimental number

Number remains independent of case and precedes case:

`NOUN-[NUMBER]-[CASE]`

| Noun class | Plural |
|---|---|
| Animate | `-i` |
| Inanimate | `-n` |

An archaic dual remains a possible lexicalized residue but is not part of the productive system.

### Experimental directional system

`i-`, `a-`, and zero form a general relational-vector opposition:

| Form | Core contribution |
|---|---|
| `Ø` | relation holds without directed change |
| `i-` | convergence / increasing orientation toward the relational frame |
| `a-` | divergence / decreasing orientation away from the relational frame |

This is not restricted to physical motion. It can orient communication, perception, influence, possession/control change, association, inclusion/exclusion, acquisition/relinquishment, and state transition.

The directional remains invariant in semantic principle across the four spatial/relational frames:

| Base frame | `Ø` | `i-` | `a-` |
|---|---|---|---|
| LOC | at/by frame | toward frame | away/from frame |
| CONTAINMENT | within domain | into domain | out of domain |
| POSITION | configuration holds | into/establish configuration | out of/terminate configuration |
| COM | association | convergent association | divergent association |

Traditional terms such as LOCATIVE, ALLATIVE, ABLATIVE, INESSIVE, ILLATIVE, ELATIVE, SUPERESSIVE, SUBLATIVE, DELATIVE, COMITATIVE, INSTRUMENTAL, and PERLATIVE are descriptive labels for recurring interpretations, not basic morpheme meanings.

### Experimental applicative

One general applicative is proposed and **promoted as a single productive operation within the experimental system**.

**APPL = add the participant expressed by a relational NP to the verb's core argument structure.**

It does not intrinsically mean dative, benefactive, malefactive, locative, instrumental, or any other semantic role.

The productive applicative exponent is **`-ka-`**, selected as a verbal suffix immediately after AUX/DERIV and before AGENT.

One APPL adds one relational participant. **Unrestricted APPL stacking is rejected.** Multiple APPLs are not established as a productive mechanism. When more than one relational NP could supply the applied participant, the remaining open issue is how the language selects among those candidates.

### Experimental object indexing

The object slot is reorganized around participant status:

| Object status | Form | Meaning |
|---|---:|---|
| LOCAL | `-n-` | 1P or 2P |
| 3P.ANIMATE | `-m-` | ordinary nonlocal animate |
| 3P.INANIMATE | `Ø` | ordinary nonlocal inanimate |
| OBV | `-v-` | obviative/further nonlocal |
| RECIP | `-r-` | reciprocal |
| REFL | `-s-` | reflexive |

Historical proposal for the LOCAL form:

`*-nk > *-ŋ- > -n-`  
`*-nt > -n-`

Historical proposal for 3P animate:

`*-np > -m-`

LOCAL intentionally merges 1P and 2P. Speaker vs. addressee is resolved by discourse rather than by separate object morphology.

OBV is primarily a discourse-status category rather than a simple fourth person.

### Experimental object hierarchy

When an ordinary lexical patient and applicatively added participants coexist, the working hierarchy is:

**patient/theme > recipient/goal > beneficiary/maleficiary > other applied participant**

APPL selection precedes object indexing: the selected relational participant is promoted into core argument structure and receives the single object index.

RECIP and REFL are special coreference constructions rather than ordinary competing semantic roles.

### Experimental relational constructions

The four productive relational frames are:

**LOC**

- `LOC + Ø`: event anchored at/by the landmark
- `LOC + i-`: event converges toward the landmark
- `LOC + a-`: event diverges from the landmark
- `LOC + i- + APPL`: convergent landmark becomes a core participant
- `LOC + a- + APPL`: divergent landmark becomes a core participant

**CONTAINMENT**

- `CONTAINMENT + Ø`: relation within bounded domain
- `CONTAINMENT + i-`: convergence into domain
- `CONTAINMENT + a-`: divergence out of domain
- `CONTAINMENT + Ø + APPL`: domain becomes a core participant
- `CONTAINMENT + i- + APPL`: participant enters/is brought into domain
- `CONTAINMENT + a- + APPL`: participant exits/is removed from domain

**POSITION**

- `POSITION + Ø`: positional/contact configuration holds
- `POSITION + i-`: enter/establish configuration
- `POSITION + a-`: leave/terminate configuration
- `POSITION + i- + APPL`: participant enters/establishes configuration
- `POSITION + a- + APPL`: participant leaves/terminates configuration

**COM / ASSOCIATIVE**

- `COM + Ø`: association/accompaniment; contextually means/instrument/route
- `COM + i-`: convergent association
- `COM + a-`: divergent association
- `COM + i- + APPL`: convergent associated core participant; beneficiary-type readings may arise
- `COM + a- + APPL`: divergent/adversely oriented associated core participant; maleficiary-type readings may arise

Benefactive and malefactive are constructional interpretations of COM plus direction plus APPL, not separate morphemes. APPL remains a single productive operation; it does not license unrestricted stacking.

### Experimental case stacking

Case stacking is restricted and compositional. The working principle is:

> **Inner case constructs a relational domain; outer case relates that constructed domain to something else.**

Promoted productive core after the stacking stress test:

| Stack | Function | Status |
|---|---|---|
| **CONTAINMENT → LOC** | locate a region/place within the bounded domain | promoted |
| **GEN → CONTAINMENT** | construct a bounded domain belonging to/defined by X | promoted |
| **GEN → LOC** | locate something in/at X's domain | promoted |

The promotion is structural. The experimental `STATUS.md` inventory still conflicts with the case inventory in `GRAMMAR.md` (`GEN = -ra` here versus `GEN = -se` and `PATH = -ra` there); that conflict remains unresolved. Corpus forms therefore follow `GRAMMAR.md`'s currently authoritative surface inventory rather than silently resolving the discrepancy.

Retained experimental tests:

| Stack | What it tests | Status |
|---|---|---|
| **POSITION → LOC** | locating a positional/contact configuration | experimental |
| **COM → LOC** | locating a point/event along a route or medium | experimental |
| **GEN → CONTAINMENT → LOC** | recursive compositional stacking | experimental |
| reversed case order | whether stacking is semantically ordered rather than freely permutable | unresolved test |
| repeated identical case | whether formally possible repetition has any productive meaning | unresolved test |
| **ERG** stacking | whether core-agent marking can participate in nested relations | unresolved test |

Repeated identical cases are not promoted; unrestricted stacking remains unsupported. ERG does not freely stack.

### Experimental multiple relational NPs and scope

Multiple relational NPs are permitted. Each can establish an independent relation to the event.

This is distinct from case stacking:

- **case stacking** = one NP carries nested relational relations
- **multiple relational NPs** = several NPs independently relate to the event

There is one clause-level directional. It can orient all compatible relational frames simultaneously.

A single APPL adds one relational participant. When several relational NPs are simultaneously eligible, selection proceeds in this order:

1. semantic argument hierarchy selects among different-ranked candidates;
2. discourse prominence resolves genuine same-rank ties;
3. linear word order resolves any remaining genuine tie.

APPL selection precedes OBJ indexing: the selected relational participant is first promoted into the core argument structure, after which the single OBJ slot is assigned.

The current hierarchy remains **patient/theme > recipient/goal > beneficiary/maleficiary > other applied participant**. A pure relational setting does not become APPL-eligible merely by being a relational NP.

Unrestricted APPL-to-all or arbitrary APPL stacking is rejected. Multiple-candidate APPL selection is now resolved within the experimental model.

### Experimental converb system — 2026-09-18

The converb test is promoted within the experimental relational system. Converbial clauses continue to be formed by verbal nominalization plus case; the case supplies the subordinate relational frame.

Four case-based converb relations are productive:

| Converb case | Productive relation |
|---|---|
| **LOC `-te`** | event situated relative to a spatial/relational frame; supports situative/temporal overlap |
| **CONTAINMENT `-ci`** | event within a bounded domain; directional forms support entry into or exit from that domain |
| **POSITION `-ta`** | event in a positional/contact/support configuration |
| **COM / ASSOCIATIVE `-me`** | association, accompaniment, means, medium, route, or co-participation |

The experimental directional system remains active inside converbal morphology. Direction is therefore expressed on the subordinate verb before nominalization:

> **`DIRECTIONAL–VERB–NMLZ–CASE`**

For each productive converb frame:

- `Ø` = the subordinate event holds in the case-defined relation;
- `i-` = the subordinate event converges toward / increasingly orients into the case-defined relation;
- `a-` = the subordinate event diverges from / increasingly orients away from the case-defined relation.

A directional may instead occur only in the finite main clause, and subordinate and main clauses may independently carry directionals. Nominalization does not neutralize the relational-vector contribution of the subordinate verb.

**GEN `-ra` on the nominalized clause is not promoted as a general converb relation.** GEN remains available for the overt subject of a nominalized clause where it marks switch-reference, as established by the nominalization system. Bare ABS nominalization remains available for content/event nominalization rather than functioning as a general converb relation; ERG is likewise not a general converb relation.

The promoted system therefore supports productive LOC, CONTAINMENT, POSITION, and COM converbs, each with independent `Ø / i- / a-` directional combinations. This promotion remains experimental and does not alter canonical `GRAMMAR.md`.
### Experimental stative and aspect interaction

The directional system has been promoted beyond physical motion.

With stative predicates:

| Direction | IMPERFECTIVE | PERFECT |
|---|---|---|
| `Ø` | state/relation ongoing | state/relation established/relevant |
| `i-` | convergence toward/entry into the relation ongoing | convergence completed/attained |
| `a-` | divergence from/withdrawal from the relation ongoing | divergence completed/terminated |

The directional does not become an inchoative or terminative marker. Aspect remains independently responsible for temporal contour.

Thus:

> `i-` + stative = orientation toward establishment of the state/relation

> `a-` + stative = orientation toward withdrawal from the state/relation

### Experimental event-boundary analysis

No BOUNDARY or TERMINATIVE case is currently proposed.

Event boundaries are distributed across existing morphology:

- **Case** defines the relevant spatial/relational frame.
- **Directional** defines orientation toward/away from that frame.
- **Verb** defines event structure such as trajectory, approach, endpoint attainment, crossing, or departure.
- **Aspect** defines temporal presentation/completion.

Abstract event schemas under test include:

- **MOVE** — trajectory, endpoint unspecified
- **APPROACH** — convergence without required attainment
- **REACH** — endpoint attained
- **PASS** — reference crossed
- **LEAVE** — departure from a source relation
- **BEGIN** — onset
- **END** — cessation
- **REMAIN** — persistence

This supports deriving boundary and endpoint interpretations without adding a new nominal case.

### Experimental stative/dynamic generalization

The directional opposition is treated as a general relational-vector system, not as a motion-only prefix system:

> `i-` = convergence / increasing orientation toward the relational frame

> `a-` = divergence / decreasing orientation away from the relational frame

With stative predicates, directional morphology may construe transition toward or away from a state; it does not itself encode aspect or inchoativity.

### Experimental causative argument structure

For:

> **CAUSER causes CAUSEE to act on PATIENT**

the working structure is:

> **CAUSER-ERG CAUSEE-ERG PATIENT-ABS**

when the causee remains agentive.

Hierarchy:

> **CAUSER > CAUSEE > PATIENT**

The causer always controls the SUBJECT index. An agentive causee outranks the patient for the single OBJ index.

If the caused participant is non-agentive, it does not retain ERG; ABS is the current default candidate.

No dedicated causee case is proposed.

### Experimental status and remaining tests

The following have been promoted within this experimental model:

- general relational-vector direction
- single general applicative
- LOCAL vs. NONLOCAL object-index organization
- OBV `-v-`
- patient > recipient/goal > beneficiary/maleficiary > other applied participant hierarchy
- four spatial/relational base frames
- COM absorbing PATH/medium
- no BOUNDARY case
- stative × directional × aspect interaction
- agentive-causee causative hierarchy
- restricted productive case stacking
- multiple relational NPs with one clause-level directional

The following remain to be tested before any possible canonical promotion:

No changes to `GRAMMAR.md`, `LEXICON.tsv`, or `EXAMPLES.tsv` are made by this experimental record.

## Stacked case + APPL decision — 2026-09-18

The stacked-case + APPL stress test is resolved within the experimental relational system:

- **Single APPL is productive.** One APPL may promote one relational participant into the verb's core argument structure.
- **Unrestricted APPL stacking is rejected.** The system does not permit arbitrary multiple APPL operations.
- **Multiple-candidate APPL selection remains open.** When multiple relational NPs are simultaneously eligible, the criteria for choosing which one is applied remain to be specified/tested.

The result does not select an APPL exponent and does not promote the experimental relational system into canonical grammar.

## Multiple-candidate APPL selection decision — 2026-09-18

The selection test is resolved within the experimental relational system:

- **Semantic hierarchy is the primary selector.** Among simultaneously eligible relational NPs, the higher-ranked semantic argument is selected.
- **Discourse prominence resolves genuine same-rank ties.**
- **Linear word order resolves only remaining genuine ties.**
- **APPL selection precedes OBJ indexing.** The selected relational participant is promoted first; the resulting core arguments then compete for the single OBJ slot under the established hierarchy.

The working selection hierarchy remains:

> **patient/theme > recipient/goal > beneficiary/maleficiary > other applied participant**

A relational NP that functions only as an event setting/domain is not automatically APPL-eligible.

## OBV/discourse behavior decision — 2026-09-18

The OBV/discourse stress test is resolved within the experimental relational/object system:

- **OBV is a discourse-status category, not a fourth person.** It distinguishes a discourse-peripheral/further-nonlocal 3P participant from the currently proximate or otherwise more prominent participant.
- **Animacy supplies a strong hierarchy bias.** Among eligible 3P participants, animate participants are preferentially available to the proximate/OBV contrast, but discourse prominence can override the animacy bias.
- **Initial status is discourse-driven.** A discourse context may establish one participant as proximate without a rigid first-mention, subject, or agent rule.
- **Newness is a defeasible OBV bias.** A newly introduced participant commonly enters as OBV when an established discourse center already exists, but immediate topical or focal prominence can make the new participant proximate instead.
- **OBV can persist across clauses.** An OBV participant normally retains that status while remaining backgrounded within the same discourse segment.
- **Topic shifts can reassign status.** A previously OBV participant can become proximate when it becomes the new discourse center; the former proximate may consequently become OBV.
- **Multiple OBV participants are permitted.** The system is not limited to a single proximate-vs-obviative pair, and OBV does not require exactly two 3P participants.
- **OBV is independent of grammatical role.** Subject/object status does not mechanically determine proximate vs. OBV; grammatical role may interact with discourse prominence rather than replacing it.
- **Contrastive focus can override prior OBV status.** Strong new discourse prominence can promote an OBV participant to proximate status.
- **Topic/focus word order does not itself assign OBV.** Clause-initial topicalization or immediately preverbal focus can signal information structure without mechanically changing the object's discourse status.
- **Genuine same-rank ties remain secondary.** When discourse prominence does not distinguish candidates, an independently motivated semantic/grammatical hierarchy may break the tie; linear order is only a final fallback. No new fixed ranking is introduced solely for OBV.
- **A solitary 3P participant may still be OBV.** OBV does not require a simultaneously competing proximate 3P participant, although contrast with an established discourse center is a major licensing environment.

This preserves a genuinely discourse-sensitive obviation system while keeping semantic/participant hierarchy primary where an independent hierarchy already exists. The result remains experimental and does not by itself promote the -v- exponent into canonical GRAMMAR.md.

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
- Finite verb template: `(DIRECTION) (OBJECT) STEM (AUX/DERIV) APPL AGENT (NEG) (DISCOURSE) TENSE (ASPECT)`
- Finite verbs require person agreement; agreement follows the semantic agent where one exists and otherwise the stative/agentless S
- Stem grades: `-a-` NONFINITE, `-e-` LINKING/ATTRIBUTIVE, `-u-` REALIS, `-i-` IRREALIS
- Direction: `i-` toward, `a-` away, `Ø` neutral; direction is verbal rather than nominal
- Object slot: `n-` 1P/2P, `m-` ordinary 3P animate, `Ø` ordinary 3P inanimate, `v-` obviative, `s-` reflexive, `r-` reciprocal; object indexing is distinct from nominal LOC (`-te`)
- AUX/DERIV: `-re-` progressive, `-ke-` continuative, `-me-` habitual, `-se-` inchoative, and semantically restricted productive `-te-` change-of-state / transformative
- NEG is the invariant suffix `-su-` after AGENT and before optional DISCOURSE/TENSE/ASPECT; no special NEG allomorphy is established
- Agreement: `-k-` 1, `-t-` 2, `-p-` 3; person-only
- Discourse: `-h-` exclamative, `-y-` interrogative
- Tense: `-i-` nonpast, `-a-` past
- Aspect: `Ø` imperfective, `-n` perfect
- Seven base nominal cases: ABS, ERG, LOC, CONTAINMENT, POSITION, COM/ASSOCIATIVE, GEN; the former PATH domain is absorbed into COM/ASSOCIATIVE
- Common-noun number is restricted rather than obligatory; animate nouns have productive `-i` plural and inanimate nouns have productive `-n` plural; an archaic dual survives in conventionalized natural-pair nouns
- APPL `-ka-` is a single productive verbal suffix after AUX/DERIV and before AGENT
- COM `-me` has association/accompaniment as its core reading; instrumental use is contextual and means-like; `i-` + COM yields benefactive when the associated participant benefits, and `a-` + COM yields malefactive when the associated participant is harmed or opposed
- Restricted productive case stacking: CONTAINMENT→LOC, GEN→CONTAINMENT, and GEN→LOC; reversed order, repeated identical case, and free ERG stacking are not productive
- LOC + verbal direction has distinct allative and recipient/goal constructions; recipient/goal uses the single object-index slot and may be zero-marked for ordinary 3P inanimate recipients
- Converbs are nominalization + case; same-subject continuity is unmarked and overt GEN-marking marks switch-reference
- Participles `-ri`, `-na`, `-mu` are productive agentive, patientive, and resultative forms
- `-nu` nominalizer; `keranu` is productive, `keranka` is lexicalized, and `kerande` is a partially fossilized lexicalized nominal

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
- Common-noun number is restricted rather than obligatory; animate nouns have productive `-i` plural and inanimate nouns have productive `-n` plural; an archaic dual survives in conventionalized natural-pair nouns.
- GEN possessors are prenominal. GEN + LOC/SUPER/INE stacking is productive within its established semantic domain but is not freely extended to arbitrary case combinations.
- A small, historically derived postposition class may coexist with case morphology.
- Negation is the invariant suffix `-su-` in the right-edge inflectional zone after AGENT and before optional DISCOURSE/TENSE/ASPECT; no negative stem grade or special allomorphy is used.
- `-ri`, `-na`, and `-mu` are productive agentive, patientive, and resultative participles
- AUX/DERIV `-te-` is synchronically productive but semantically restricted as a change-of-state / transformative marker.
- The productive derivational core remains compact, while older derivational strata may be partially productive, lexicalized, or opaque; deeper historical layering is permitted through reanalysis rather than unrestricted synchronic stacking.
- Converbs are nominalization + case. Same-subject continuity is unmarked; an overt GEN-marked nominalized subject marks switch-reference. Case meanings remain broadly polyfunctional.
- Finite relative clauses use a gap. Coordination is primarily juxtaposition, with a small secondary conjunction class.
- Information structure is established as constituent-order plus prosodic prominence: topics may occur clause-initially; narrow/contrastive focus favors the immediately preverbal position.

## OPEN/CLOSED × vowel-transition matrix refinement — 2026-09-17

The 10-question matrix refinement retained the current 24-cell outcomes. The decisions establish: OPEN vs. CLOSED is a primary conditioning factor; F_F/F_B/B_F/B_B remain independent conditioning classes; pre-/i/ palatalization has priority in B_F for `t/k`; OPEN F_B retains `k`; OPEN `p` in B_F/B_B reaches `Ø` through `h`; `t` stops at `d`; CLOSED B_B `t` still weakens to `d`; CLOSED `p` in B_F/B_B reaches `h`; CLOSED `k` in F_F/F_B remains `k`; and the matrix is historical rather than a productive synchronic alternation.

The F_B `k` retention and CLOSED F_F/F_B `k` retention are treated as language-specific conditioning effects within the historical system, not as universal phonetic implications.

## OPEN/CLOSED × vowel-transition matrix testing — 2026-09-17

The refined matrix was stress-tested across all 24 cells using diagnostic historical forms representing each OPEN/CLOSED × F_F/F_B/B_F/B_B combination for `p`, `t`, and `k`.

Results:

- All 24 cells have defined outcomes.
- B_F `t/k` consistently bypass ordinary weakening through pre-/i/ palatalization.
- No CLOSED cell produces greater weakening than its corresponding OPEN cell.
- All currently attested diagnostic forms (`rupi`, `ku-p-i`, `reruka`, `reruta`, `rerupa`, `mente`, `menta`, `neku`, `seku`, `keka`) match their assigned matrix cells.
- OPEN F_B `k` retention and CLOSED F_F/F_B `k` retention remain distinct conditioning effects rather than a universal lenition hierarchy.
- The resulting system remains historical rather than a productive synchronic alternation.

The 24-cell diagnostic set is a validation test, not additional corpus evidence, so no synthetic forms were added to `EXAMPLES.tsv`.

## Nominalizer family testing — 2026-09-17

Added three experimental regression examples to `EXAMPLES.tsv`:

- `E-0011` tests productive `keranu` + LOC (`keranu-te`) as a same-subject converb, contrasted with fossilized `kerande`.
- `E-0012` tests `keranu-te` with an overt GEN-marked nominalized subject (`sese`) for switch-reference.
- `E-0013` tests lexicalized `keranka` as a normal noun with ERG case and regular 3rd-person agreement, while `kerande` remains the object noun.

All three examples pass structural/schema-field checks, ID and cross-file reference checks, IPA/stress checks, and segmentation/gloss alignment. The family remains experimentally tested; no new productive morphology is promoted beyond the existing grammar.

## Productive morphology, converb, and information-structure testing — 2026-09-17

Added seven experimental regression examples to `EXAMPLES.tsv`:

- `E-0014`–`E-0016` test productive agentive `-ri`, patientive `-na`, and resultative `-mu` participles in attributive/relative use.
- `E-0017`–`E-0018` form a matched same-subject / switch-reference converb pair using nominalization plus PATH; the switch-reference member uses an overt GEN-marked nominalized subject.
- `E-0019` tests clause-initial topicalization without changing the object's case or the agent's ERG marking.
- `E-0020` is a matched information-structure case with the same segmental sequence but narrow contrastive focus assigned prosodically to the immediately preverbal subject.

All seven examples remain `experimental` and do not promote any additional grammar. Structural validation, lexical/grammar reference resolution, IPA/stress checks, and segmentation/gloss alignment pass for the new material.

## Known inconsistencies / cleanup needed

The conditioned historical system is documented in `GRAMMAR.md`, including the resolved OPEN/CLOSED × F_F/F_B/B_F/B_B matrix. The principal lexical and example forms have been reconciled against the current grammar.

The earlier regression forms (`apa`, `ita`, `teta`, `keka`, `neku`, `seku`, `kerande-te`, and related forms) remain useful diagnostic evidence for historical strata and conditioning rather than being declared exceptions.

The object slot distinguishes `n-` (1P/2P), `m-` (ordinary 3P animate), `Ø` (ordinary 3P inanimate), and `v-` (OBV), with `s-` and `r-` reserved for reflexive/reciprocal constructions. `n-` retains the established surface repair `n + C → enC` before consonant-initial verb stems.

## Open questions

None among the current core grammar decisions. Residual lexical creation/testing may add entries as needed, but no unresolved grammatical parameter from the recovery audits remains open.

## Immediate testing priorities

1. **Completed 2026-09-17:** Validate `LEXICON.tsv` against `SCHEMA.json` and check all affected IPA/derivation fields against `GRAMMAR.md`; the blank-row defect was removed and the complete populated file now passes structural validation.
2. **Completed 2026-09-17:** Test the nominalizer family (`keranu`, `keranka`, `kerande`) with additional examples.
3. **Completed 2026-09-17:** Test productive participles, converb/switch-reference constructions, and information-structure contrasts with matched experimental examples.
4. **Completed 2026-09-17:** Stress-test the OPEN/CLOSED × F_F/F_B/B_F/B_B historical matrix across all 24 cells and reconcile the attested diagnostic forms.
5. **Completed 2026-09-18:** Stress-test OBV/discourse behavior, including proximate selection, persistence, reassignment, multiple OBV participants, animacy effects, focus/topic interaction, and grammatical-role independence.
6. Continue corpus growth with additional matched tests for productive morphology, subordination, and discourse structure.

### Relational-system roadmap — 2026-09-18

The experimental relational system is now being integrated into the grammar. The remaining roadmap is:

**A — Case-space reconciliation — completed.** Adopt the reorganized seven-value semantic inventory: ABS, ERG, LOC, CONTAINMENT, POSITION, COM/ASSOCIATIVE, and GEN; absorb the former PATH domain into COM/ASSOCIATIVE.

**B — APPL/object architecture — completed.** Canonicalize `-ka-` as the productive APPL suffix; place it after AUX/DERIV and before AGENT; use the single object-index slot for the APPL-selected participant.

**C — Argument-hierarchy stress test — next.** Build matched tests with multiple eligible relational NPs, especially transitive clauses containing patient/theme + recipient/goal + beneficiary/maleficiary, and test the hierarchy, discourse tie-breaking, object indexing, direction, and APPL with statives where the predicate independently licenses an affected participant.

**D — Construction-first corpus redevelopment — following C.** Redevelop the regression corpus from language-internal construction schemas rather than English sentence translation, systematically crossing CASE × DIRECTION × APPL × ARGUMENT STRUCTURE and retaining English only as a translation/paraphrase layer.

## Leipzig valency-frame coverage audit — 2026-09-17

The 70-frame Leipzig Valency Classes sample was tested against the current grammar as a constructional coverage audit. The source defines valency in terms of argument roles, coding properties, behavioral properties, and cross-clausal behavior; this pass focuses on whether the listed role frames can be expressed with the current case, direction, object-slot, agreement, and clause-combining systems.

Results:

- No listed frame is categorically impossible under the current system.
- Core S/A, transitive A–P, locative, source, instrument, surface, reflexive/reciprocal, and recipient/goal patterns are structurally expressible with existing morphology.
- Recipient/goal frames (`show`, `give`, `send`, `tell`, `ask`) can use LOC plus verbal direction/dative-like object-slot marking while the theme remains an overt ABS NP. The relative ordering of multiple non-subject NPs is not yet established.
- Experiencer predicates (`like`, `fear`, `smell`, `see`) are expressible, but their choice between ERG experiencer + ABS stimulus and another alignment requires lexical testing; the grammar does not assign all experiencers one universal case.
- `rain` requires an explicit decision about default 3rd-person agreement on an impersonal finite verb, since finite verbs require person agreement but no dummy subject construction is currently documented.
- `talk`, `think about`, `search for`, and similar semantically oblique complements can be lexicalized as ordinary ABS objects or use existing COM/PATH/LOC relations, but the exact lexical selection is not yet established.
- `say` can use an ABS nominalized complement plus a LOC recipient, but finite speech-complement syntax has not yet been directly tested.
- `name` can be represented by a recipient/goal analysis (`X-LOC` + `Y-ABS`), but an object-complement naming construction is not yet established.
- `build ... out of`, `fill ... with`, and the inverse `load L with T` frame are expressible through existing case resources only with construction-specific semantic interpretations; these should receive targeted corpus tests before being treated as established.

This audit is evidence about constructional coverage, not a promotion of any new lexical valencies or grammatical rules. No new lexicon entries or grammar rules were added.


## Stacked-case stress test — 2026-09-18

Added six examples (`E-0116`–`E-0121`) after testing stacked-case composition with verbal direction.

- `E-0116` promotes **CONTAINMENT → LOC** as productive within the experimental model.
- `E-0117` promotes **GEN → CONTAINMENT** as productive within the experimental model.
- `E-0118` promotes **GEN → LOC** as productive within the experimental model.
- `E-0119` retains **POSITION → LOC** as an unresolved semantic/productivity test.
- `E-0120` retains **COM → LOC** as an unresolved route/medium test.
- `E-0121` retains **GEN → CONTAINMENT → LOC** as a recursive three-case test.

The experimental seven-value case inventory is now canonical in `GRAMMAR.md`; the former PATH case is absorbed into COM/ASSOCIATIVE.

No new lexicon entries were required; the six examples are reference-valid and segmentation/gloss aligned.
## TAM interaction and construction-first corpus stress test — 2026-09-17

Added 39 experimental examples (`E-0083`–`E-0121`).

- The five AUX/DERIV values were exhaustively crossed with NONPAST/PAST and IMPERFECTIVE/PERFECT, yielding a complete 20-cell finite TAM matrix. Every cell is morphologically formable under the current verb template.
- PERFECT combines without special allomorphy after both NONPAST and PAST, and progressive, continuative, habitual, inchoative, and change-of-state morphology remain available with PERFECT. Their semantic compatibility varies by context, but no grammatical incompatibility was found.
- Additional tests cover NEG + PROGRESSIVE + PERFECT, NEG + INTERROGATIVE + PERFECT, directional TRANSFER, directional-COM benefactive/malefactive readings, the LOCAL-recipient dative-like construction, secondary predication with a resultative participle, content nominalization, case-based temporal subordination, switch-reference, and the newly tested productive/retained stacked-case constructions.
- The construction-first examples show why the language should not be modeled as English predicate + translated arguments: TRANSFER plus `i-/a-`, case stacking, converbial case choice, and COM direction can organize meanings in ways not captured by one-to-one English lexical glosses.
- Remaining exact syntax/valency gaps are not papered over: imperative/hortative, modal/necessitative/ability, comparison, passive, content-question syntax, impersonal finite predicates, and fully specified secondary predication/direct-speech syntax still require dedicated design work.

The corpus remains somewhat English-centered because many examples retain English-style event descriptions. Future corpus growth should therefore begin from language-internal construction schemas and semantic contrasts, using English only as a translation/paraphrase layer.

## New-root grammar testing — 2026-09-17

Added 46 experimental examples (`E-0037`–`E-0082`) testing all 50 new roots `L-0037`–`L-0086` in actual grammatical environments. Coverage includes intransitive and transitive predicates, stative predicates, nominal use of category-neutral roots, LOC/INE/SUPER case frames, verbal direction, ordinary COM accompaniment, directional-COM benefactive and malefactive readings, and several provisional valency frames.

All 50 new roots occur in at least one new example. The corpus deliberately retains experimental status where a root's exact lexical valency or semantic complement relation is not yet established, notably experiencer predicates, speech targets, `think about`, and multiple-complement ordering. No new grammatical rule was promoted from these tests.

A stricter IPA pass also corrected finite-form stress so the heavy VC/CVC root syllable receives primary stress under the current rightmost-heavy rule, with directional prefixes remaining unstressed. The complete modified `EXAMPLES.tsv` passed field-count, ID uniqueness, grammar-reference, lexicon-reference, and segmentation/gloss alignment checks.

## Fiziwig syntax-test audit — 2026-09-17

The 218-sentence Fiziwig/Conlang Syntax Test Cases list was audited against the current grammar. The mirrored list describes itself as a culled set of 218 sentences chosen to test distinct syntactic principles rather than repeated vocabulary patterns.

Using `✓` for a construction directly supported by the current grammar, `△` for a meaning/construction expressible with existing resources but requiring an unestablished lexical or constructional decision, and `✗` for the exact construction requiring a currently absent grammatical resource, the audit yields:

- `✓` 82 / 218: directly supported.
- `△` 86 / 218: structurally possible but not yet canonically specified.
- `✗` 50 / 218: not currently expressible as that exact construction without adding grammar; most meanings remain paraphrasable.

The principal coverage gaps are imperative/hortative morphology, modal/necessitative/ability constructions, comparative and superlative degree, passive voice, exact content-question syntax, impersonal finite predicates, multiple-complement ordering, nominal/secondary predication, and several spatial/temporal relational constructions. These are testing priorities rather than automatic grammar changes.

Strongly supported areas include SOV argument structure, ERG/ABS alignment, GEN possession, LOC/SUPER/INE/PATH/COM relations, verbal direction, productive TAM/AUX morphology, reflexive direct objects, participial relatives, finite gap relatives, juxtaposed coordination, switch-reference converbs, and directional recipient/benefactive constructions.

No grammar rule was inferred merely to make the English test sentences translatable. The audit concerns constructional capacity, not English word-order imitation.

## Lexical generation refinement — 2026-09-17

The lexical-generation methodology explicitly evaluates both the literal and metaphorical semantic contribution of verbal direction. Roots should be chosen so that `i-` and `a-` can contribute productive toward/away or goal/source meanings during lexical derivation. A general TRANSFER-type root is therefore preferable to a semantically endpoint-fixed root such as GIVE when both can occupy the same lexical domain: the former preserves neutral, toward-recipient, and away-source derivational space.

The directional opposition is also treated as a source for **metaphorical and constructional semantic extension**. The toward/away schema may motivate readings involving benefit/detriment, support/opposition, acquisition/disposition, inclusion/exclusion, initiation/completion, and related domains when the lexical semantics and construction support the mapping. The established COM pattern provides a model: `O-me + i-VERB` is benefactive when O benefits, while `O-me + a-VERB` is malefactive when O is harmed or opposed. Such meanings are constructional or lexicalized extensions, not automatic free meanings of `i-` and `a-`.

Future root batches must test semantically central candidates against neutral, `i-`, and `a-` frames where their valency permits, then consider plausible metaphorical extensions licensed by the same semantic frame. Roots that duplicate a useful directional construction should be avoided unless lexicalization or semantic specialization supplies an independent motivation. This does not retroactively reclassify the 50 roots already added in `L-0037`–`L-0086`; those remain experimental candidates.


## Root-final generation filter — 2026-09-17

The lexical generator now blocks `h` and `j` from root-final position in newly generated VC/CVC roots. The six affected experimental roots were replaced without changing their IDs or semantic glosses: `ah → an`, `muh → muk`, `jeh → jek`, `kah → kat`, `haj → han`, `pej → pet`. The established one-segment roots `h` and `j` remain valid historical roots; the new filter applies only to newly generated multi-segment roots.

## Lexical root generation pass — 2026-09-17

Added 50 experimental lexical roots (`L-0037`–`L-0086`) to `LEXICON.tsv`.

- The 50 new roots comprise 15 VC and 35 CVC forms. All ten available one-consonant root forms (`p t k v r j h s m n`) were already occupied, so no additional C roots could be added without exact-form collision.
- Including the existing 10 C roots, the 60-root inventory now has 16.7% C, 25.0% VC, and 58.3% CVC roots, close to the generation targets of 15%, 25%, and 60%.
- All new roots are `experimental`, category-neutral (`pos = —`), have `derived_from = —`, and carry no invented historical derivation.
- The complete modified lexicon passes the applicable structural schema constraints, ID/form uniqueness, root-shape checks, and lexical-status checks.
- All 200 basic grade expansions (four stem grades for each root) were tested for legal modern surface shape; no cross-root stem collisions were found. Boundary repairs were considered where relevant.

## Corpus growth pass — 2026-09-17

Added sixteen experimental regression examples (`E-0021`–`E-0036`) to extend matched coverage without adding lexical entries or changing canonical grammar:

- `E-0021`–`E-0025` test the productive AUX/DERIV series (`-re-`, `-ke-`, `-me-`, `-se-`) plus a past/nonpast progressive contrast.
- `E-0026` tests the semantically restricted productive change-of-state `-te-`.
- `E-0027`–`E-0028` test invariant right-edge NEG placement and NEG + interrogative stacking, including the established `yi > ye` repair.
- `E-0029` tests overt LOCAL object marking and the established `n + C > enC` boundary repair.
- `E-0030`–`E-0031` form a matched directional-COM benefactive/malefactive pair.
- `E-0032`–`E-0033` form a matched same-subject/switch-reference PATH-converb pair with a directional finite main clause.
- `E-0034` tests clause-initial subject topicalization without changing grammatical marking; `E-0035` tests narrow contrastive object focus in the immediately preverbal position.
- `E-0036` tests animate `-i` and inanimate `-n` plural marking before nominal case, with unchanged person-only verbal agreement.

All sixteen examples remain `experimental`; they add regression evidence but do not promote any new rule.

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

These generation decisions do not by themselves determine the status of individual grammatical exponents. The productive participles `-ri`, `-na`, and `-mu`, and semantically restricted productive `-te-` change-of-state morphology, are established independently by the morphology/syntax pass. Existing lexical entries are not retroactively reclassified from this generation model alone.