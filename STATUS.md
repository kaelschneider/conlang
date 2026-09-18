# Status

**Last updated:** 2026-09-18  
**Phase:** Relational grammar integrated and matrix-tested; lexicon semantic audit and first construction-first corpus rebuild completed; active work is lexical valency/construction coverage and independent syntax validation
**Repository structure:** Consolidated grammar source; minimal flat structure

## Canonical files

- `GRAMMAR.md` — canonical consolidated grammar: phonology, morphology, syntax, prosody, and historical sound change
- `LEXICON.tsv` — canonical lexical/root inventory
- `EXAMPLES.tsv` — example and test corpus
- `SCHEMA.json` — structural validation schema
- `AGENTS.md` — repository maintenance instructions

## Corpus migration / grammar reconciliation — 2026-09-18

The corpus has now been reconciled with the integrated relational grammar.

- The GEN/PATH surface-form conflict is resolved in favor of **GEN -se**, consistent with the established pronominal pattern sese and the pre-existing corpus. The former PATH exponent -ra is retired from synchronic case morphology; former PATH converbial/route meanings migrate to **COM/ASSOCIATIVE -me**.
- Existing corpus glosses and notes using **INE** are migrated to **CONTAINMENT** (CONTAIN in Leipzig-style glosses), and **SUPER** to **POSITION**.
- The five former PATH converb examples (E-0017, E-0018, E-0032, E-0033, E-0113) now use -me and are analyzed as COM/ASSOCIATIVE converbs.
- E-0118 is corrected to a genuine **GEN → LOC** stack (-se-te); the previous unstacked GEN form did not instantiate the documented stack.
- Benefactive, malefactive, and recipient examples using a promoted relational participant now use productive **APPL -ka-**. For the existing 2P examples, the promoted participant receives the **LOCAL n-/en-** object index, matching the current verb-template and APPL analysis.
- The obsolete NLOC description in E-0027 is replaced by the current ordinary 3P-inanimate zero-index analysis; E-0029 and recipient examples use LOCAL explicitly to distinguish object indexing from nominal LOC case.
- All 120 example IDs are preserved. No lexicon entries were added or changed.

Validation checks on the migrated corpus: 120 rows retained; no stale PATH, INE, SUPER, or NLOC labels remain in segmentation/gloss/notes; segmentation/gloss word counts remain aligned; grammar references and lexical-entry references resolve against the branch; no duplicate IDs were introduced.

This reconciliation treats GRAMMAR.md as authoritative for the resulting system while preserving the superseded PATH analysis in historical/status provenance where relevant.
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
| GEN | `-se` | inherent/identifying relation between one nominal entity and another |

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
- single general applicative (`-ka-`)
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

There are no unresolved core parameters among the relational-system decisions already tested. The remaining uncertainties are **lexical or construction-level tests**, not reasons to reopen the settled relational architecture.

Current open areas are concentrated in lexical valency and in a small set of independent syntax families. In particular, the corpus still needs targeted evidence for exact speech-complement behavior, naming, filling/loading, material/source relations, and the remaining non-relational clause systems. Genuine lexical gaps are not to be converted into grammatical rules merely to make an English test sentence expressible.

## Relational-system roadmap — 2026-09-18

The relational system has moved from architectural design into **validated constructional coverage**. The original roadmap is retained here as a state record, with completed phases updated rather than treated as pending.

**1 — Corpus migration and grammar reconciliation — COMPLETE.**

The active corpus has been reconciled with the reorganized seven-value case system, productive APPL, current object indexing, and the COM/ASSOCIATIVE replacement for the former PATH domain. Historical/deprecated material remains explicitly marked for provenance.

**2 — Argument-structure / multi-complement validation — COMPLETE FOR THE CURRENT EXPERIMENTAL SYSTEM.**

`E-0122`–`E-0131` established the APPL hierarchy, candidate selection, tie-breaking, object-index realizations, and the APPL/non-APPL distinction.

**3 — Full relational construction matrix — COMPLETE FOR THE CURRENT EXPERIMENTAL SYSTEM.**

`E-0188`–`E-0194` closed the seven previously untested `CASE × DIRECTION × APPL` cells. The four productive relational frames now have explicit neutral, `i-`, `a-`, and APPL behavior, with lexical semantic licensing remaining the normal constraint.

**4 — Construction-first corpus redevelopment — COMPLETE FOR THE CURRENT LAYER.**

The active corpus now includes relational, argument-structure, information-structure, causative, participial, converbial, and core syntax coverage. Further construction-first growth continues as targeted valency gaps are discovered.

**5 — Remaining independent syntax gaps — NEXT MAJOR GRAMMATICAL LAYER.**

Priority remains:

`imperative/hortative → modality → content questions → impersonal predicates → secondary predication → finite speech complements → comparison → passive`

These should be designed and tested only after lexical valency distinctions are sufficiently understood.

**6 — Lexical valency and family expansion — CURRENT.**

Run construction-first tests on neutral and diagnostic predicates whose argument structures remain under-specified. Priorities are experiencer, speech, search/hunt, acquisition, naming, filling/loading, and material/source relations. New lexicon should be added only for genuine semantic gaps.

### Current promotion gate

Before the relational system is promoted wholesale across the repository:

1. `GRAMMAR.md` and active `EXAMPLES.tsv` must agree on case inventory and segmentation;
2. APPL `-ka-` must be represented consistently;
3. multi-complement/object-index behavior must remain consistent across additional valency frames;
4. the four-frame × three-direction relational matrix must remain contradiction-free;
5. historical analyses must remain distinct from synchronic productive rules;
6. lexical valency tests must not silently establish universal case frames from single predicates.

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
## Argument-structure and multi-complement validation — 2026-09-18

Added matched experimental examples `E-0122`–`E-0131` to test the already-settled APPL hierarchy and its concrete clause behavior.

Results:

- In lexical-patient + recipient + beneficiary clauses, the recipient is selected and receives the single object index even when the beneficiary is ordered first. This confirms that semantic rank, not linear order, controls selection across different-ranked APPL candidates.
- A pure event-setting relation does not become APPL-eligible merely because additional relational NPs are present. Three relational NPs can coexist with one APPL.
- The APPL/non-APPL contrast is now explicit: `O-LOC + i-VERB` remains a non-applied goal-oriented relation, while `O-LOC + i-VERB-APPL` promotes that participant and indexes it.
- Same-rank beneficiary ties behave as specified: discourse prominence selects the applied participant; when discourse does not distinguish the candidates, linear order is the final fallback.
- Object-index behavior is exercised for LOCAL (`n-`), ordinary 3P animate (`m-`), ordinary 3P inanimate (`Ø`), and OBV (`v-`). The `m-` and `v-` tests use a vowel-initial stem so that no unestablished consonant-initial boundary repair is asserted.
- The lexical patient/theme is not an object-index competitor in these APPL constructions. The working role hierarchy therefore remains intact, but its APPL-selection domain is now explicit in `G-MORPH-06A`.

Multi-complement **ordering itself is not promoted to a rigid clause-wide rule**. The tests establish that APPL selection survives changes in relational-NP order, while neutral examples continue to place the lexical theme before relational complements. Further ordering work belongs in the full relational-construction matrix rather than being inferred from these ten examples alone.

A remaining morphophonological gap is explicit: only `n + C → enC` is established for object-slot boundary repair. `m-`, `v-`, `s-`, and `r-` before consonant-initial stems remain unestablished and must not be generated as canonical surface forms until tested.

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
## Lexicon semantic audit — 2026-09-18

The first semantic audit pass is complete for the inherited core. The audit treats the lexicon as a semantic system rather than as a list of English glosses and separates neutral constructional probes from inherently diagnostic/specialized vocabulary.

### Adopted inherited semantic centers

- `r` / `ra`: broader **MOVE / GO** semantic center; the historical `GO` gloss remains a normal lexical interpretation.
- `m` / `ma`: broader **REMAIN / STAY** semantic center; `LIVE / DWELL` remains lexicalized.
- `n` / `na`: broader **OBTAIN / ACQUIRE** semantic center; `GET / FIND` and `RECEIVE` remain available through lexical semantics.
- `j` / `ya`: broader **PERCEIVE** semantic center; `SEE / KNOW` polysemy is retained.
- `h` / `ha`: **SAY** is the neutral probe sense; `BLOW` remains a lexicalized sense.
- `v` / `va`: broader **GROW / INCREASE** semantic center.
- `t` / `transfer`: remains a deliberately neutral **TRANSFER** predicate rather than being specialized toward GIVE or TAKE.
- Existing specialized lexical items remain specialized; semantic broadening does not flatten the lexicon.

### Neutral probe principle

A neutral probe is not simply a frequent word. It is a lexeme whose inherent semantics leave the target construction free to contribute its own relational, aspectual, argument-structural, or discourse meaning.

The current verbal probe core is centered on:
`TRANSFER, MOVE, HOLD/RETAIN, REMAIN/STAY, PERCEIVE, SAY, HEAR, THINK, WORK/ACT, SLEEP, MAKE/CREATE, OPEN, CLOSE, WRITE, READ, WASH, COOK`.

Predicates with strongly directional or endpoint-fixed semantics such as `ENTER`, `FALL`, `RISE`, `PUT`, `GIVE`, and `TAKE` are retained as **diagnostic predicates**, not excluded from the language.

## Lexical-class generation strategy — 2026-09-18

The same audit logic will be extended to nominals and other lexical classes. The intended procedure is:

1. establish semantic domains and conceptual families before assigning individual forms;
2. generate category-neutral roots independently of English part-of-speech labels;
3. assign lexical-category biases from semantic behavior, derivational history, and expected frequency rather than from root shape alone;
4. construct balanced **probe inventories** for nominals, statives/adjectives, and other open classes;
5. retain specialized vocabulary outside the probe inventories so the language does not become an artificial set of generic words;
6. use construction-first corpus needs to identify genuine semantic gaps rather than adding words merely to translate an English sentence list;
7. permit light sound symbolism as a **probabilistic semantic prior** in candidate generation/selection, never as a deterministic mapping from sound to meaning;
8. distinguish productive lexical semantics from later lexicalization, metaphor, and sound-symbolic specialization.

### Nominal probe coverage target

`CONTAINER` should no longer function as the default nominal test object. The nominal probe set should cover contrasting referential types relevant to the grammar, including at minimum:

- animate/person;
- animal or other sentient being;
- plant;
- natural landmark;
- artifact/tool;
- bounded enclosure/container;
- substance/mass entity;
- food/material;
- body/object of manipulation;
- place/region/domain;
- abstract/eventive nominal;
- relationally dependent entity.

The five principal nominal probe gaps identified in the audit are now filled by `L-0087`–`L-0091`: `ren` PERSON/HUMAN, `mur` ANIMAL, `tak` TOOL/ARTIFACT, `nim` BODY PART, and `sur` PLACE/DOMAIN. These remain experimental, category-neutral roots.

### Sound-symbolism policy — provisional

Sound shape may bias candidate meanings where a plausible association is culturally and phonetically coherent. The generator should prefer **soft tendencies** over fixed correspondences and should allow multiple lexical outcomes within the same semantic domain.

A sound-symbolic association may influence candidate ranking, but semantic-family coherence, phonological legality, derivational behavior, frequency, and lexical collision checks remain stronger constraints.

This audit does not establish any new synchronic sound-meaning rule.
## Lexical-class generation and neutral probe inventory — 2026-09-18

The lexical-class design pass is resolved as follows:

- Nominal probes are selected through a balanced semantic/referential matrix rather than by frequency alone.
- The nominal matrix deliberately contrasts person/animate, animal, plant, natural object, artifact/tool, bounded enclosure, substance/mass, food/material, body/object of manipulation, place/region/domain, abstract/eventive nominal, and relationally dependent entity.
- `kerande` CONTAINER remains a specialized noun but is no longer the default or principal nominal probe.
- Category-neutral roots remain the default starting point. Noun/verb/adjective/adverb behavior may emerge through zero conversion, derivation, semantic specialization, and lexicalization.
- Stative/adjectival probes will cover dimension, temperature, physical property, age/state, quantity, evaluation, disposition, and sensory quality rather than relying on `sara` BE.BIG alone.
- Dedicated lexical classes are minimized; additional parts of speech arise where semantic, derivational, or historical evidence supports them.
- Sound symbolism is a weak probabilistic prior: broad phonetic/root-shape associations may break ties when assigning candidate meanings, but never determine meaning or override semantic-family coherence, phonological legality, derivational compatibility, frequency, or lexical evidence.

### Current neutral verbal probe inventory

The construction-first verbal core is:

`L-0002 TRANSFER; L-0005 MOVE; L-0003 HOLD/RETAIN; L-0009 REMAIN/STAY; L-0006 PERCEIVE; L-0007 SAY; L-0041 HEAR; L-0075 THINK; L-0076 WORK/ACT; L-0037 SLEEP; L-0077 MAKE/CREATE; L-0042 OPEN; L-0052 CLOSE; L-0066 WRITE; L-0067 READ; L-0064 WASH; L-0065 COOK`.

Strongly directionally or endpoint-fixed predicates remain available as diagnostic predicates rather than being used as the primary neutral probes: `ENTER, FALL, RISE, PUT, GIVE, TAKE`, and similar lexicalized predicates.

### Current nominal probe anchors

Existing vocabulary already supplies useful nominal anchors across several semantic domains:

| Semantic role | Current anchor | Status |
|---|---|---|
| plant | `L-0050 et` TREE | experimental |
| natural object | `L-0051 at` STONE | experimental |
| substance/mass | `L-0040 am` WATER | experimental |
| natural phenomenon/material-like entity | `L-0043 ir` RAIN; `L-0072 rir` SNOW | experimental |
| bounded enclosure | `L-0032 kerande` CONTAINER | stable, specialized |
| natural spatial/domain concept | `L-0081 mam` SHADE | experimental |
| fire/elemental entity | `L-0049 ek` FIRE | experimental |
| human/animate participant | `L-0036 keranka` CARRIER | stable, specialized |

The current anchors are deliberately not treated as a complete nominal probe lexicon. Genuine gaps remain for a semantically neutral PERSON/HUMAN noun, ANIMAL noun, TOOL/ARTIFACT noun, BODY-PART noun, and a more neutral PLACE/DOMAIN noun. These gaps should be filled through new root generation or justified semantic extension rather than by overusing `CONTAINER`.

### Other lexical-class probe policy

Category-neutral roots may supply nominal, verbal, and stative uses where the semantic relationship is natural. Eventive nominal uses, result/product nouns, abstract nouns, and sensory-property nouns should be especially useful for testing derivation and conversion. The corpus should distinguish ordinary lexical category flexibility from productive morphological nominalization, rather than treating every noun-like interpretation as evidence of a dedicated noun-forming rule.
## Construction-first corpus rebuild — 2026-09-18

The first corpus redevelopment pass is complete after the semantic audit.

- The five new nominal probes `ren, mur, tak, nim, sur` are exercised across core transitivity, relational cases, direction, APPL, stacking, stative/dynamic predicates, derivation, and clause combining.
- The prior 115 experimental example rows are retained as `deprecated` regression/provenance material rather than treated as the active construction corpus. The nine stable examples and three analyzed/three unresolved rows remain preserved.
- 56 new active experimental examples (`E-0132`–`E-0187`, excluding the removed malformed probe) form the first construction-first corpus layer.
- The new corpus deliberately reduces dependence on `kerande` CONTAINER and distributes nominal roles across human, animal, artifact, body-part, place/domain, substance, and natural referents.
- Construction generation begins from the language-internal system: relational frame, directional vector, APPL eligibility, argument hierarchy, case stacking, converb relation, stative interaction, and information-structural contrasts. English remains a translation/paraphrase layer.
- Neutral probes are used first; strongly directional or endpoint-fixed predicates remain diagnostic rather than serving as the default evidence for constructional meaning.
- Sound symbolism is applied only as a weak probabilistic prior in lexical assignment; no deterministic sound-to-meaning rule has been introduced.

### Current rebuild boundary

The first rebuild establishes a balanced active probe corpus but does not claim to exhaust every remaining construction family. The next corpus layer should complete the full `CASE × DIRECTION × APPL × ARGUMENT STRUCTURE` matrix, then add matched coverage for information structure, causative argument structure, and secondary predication before promotion review.

## CASE × DIRECTION × APPL matrix closure — 2026-09-18

The remaining seven APPL cells identified in the construction-first coverage audit have now been resolved and instantiated in the active corpus.

### Resolved constructional parameters

- **LOC + Ø + APPL:** the landmark is promoted as a core participant while the spatial relation remains statically anchored.
- **LOC + a- + APPL:** the promoted landmark is construed as a source/reference from which the event diverges.
- **CONTAINMENT + Ø + APPL:** the bounded domain itself becomes a core participant without directional change.
- **POSITION + Ø + APPL:** the participant in an existing support/contact configuration is promoted without directed change.
- **POSITION + i- + APPL:** the promoted participant enters or establishes the support/contact configuration.
- **POSITION + a- + APPL:** the promoted participant leaves or terminates the support/contact configuration.
- **COM + Ø + APPL:** the associated participant is promoted without inherent benefit/harm or directional interpretation.

This closes the previously untested frame × direction × APPL cells. The resulting architecture is now consistently:

**CASE = relational frame → DIRECTION = relational vector → APPL = valency promotion → OBJECT = participant indexing**

The seven new active examples are **E-0188–E-0194**. APPL remains a single productive operation; unrestricted APPL stacking remains rejected.


## Active syntax coverage pass — 2026-09-18

The active corpus now contains direct evidence for the previously underrepresented core syntax constructions:

- **G-SYN-06 / G-SYN-07:** question and negation morphology
- **G-SYN-05:** plural pronouns with person-only verbal agreement
- **G-SYN-11:** prenominal GEN possession
- **G-SYN-08:** finite postnominal relative clause with a gap
- **G-SYN-13:** topic-left and narrow-focus/preverbal information structure
- **G-SYN-12:** clause juxtaposition as the default coordination strategy

The current active corpus still has no dedicated **G-SYN-10 adposition** example because the grammar only permits a small independent postposition class historically derived from relational expressions; no such adposition is presently established in the lexicon. This remains an intentional lexical/grammatical open area rather than a corpus omission.

New active examples: **E-0195–E-0202**.

## Lexical valency / construction audit — 2026-09-18

A construction-first valency pass was run against the current lexical inventory and relational grammar. The goal was to identify where existing predicates already support useful argument structures and where apparent gaps are genuinely lexical rather than grammatical.

### Tested successfully with existing lexical material

- **Experiencer predicates:** `an` FEAR and `yat` SMELL were tested with an ERG experiencer and ABS stimulus. `j` PERCEIVE already has the same basic transitive pattern in the active corpus. This supports lexical variation in experiencer alignment without establishing a universal experiencer case.
- **Speech:** `h` SAY supports an ABS nominalized content plus a LOC recipient/goal in `E-0205`. This is evidence for a viable finite speech frame, but the exact syntax of finite vs. nominalized/direct-speech complements remains open.
- **Search/hunt:** `em` HUNT takes an ABS target in `E-0206`. A separate SEARCH lexeme is not currently required by the grammar, but the lexical distinction remains open.
- **Acquisition/finding:** broadened `n` OBTAIN/ACQUIRE takes an ordinary ABS object in `E-0207`; FIND remains a lexical interpretation rather than a separate grammatical construction.
- **Material/medium:** `at-me` with `kan` BUILD in `E-0208` provides an event-oriented stone material/medium relation under COM. This does not establish a separate MATERIAL or SOURCE case and does not generalize GEN to event arguments.

### Genuine lexical gaps

No current root directly supplies **NAME** or **FILL/LOAD**, so those frames should not yet drive grammatical invention. They remain candidates for future lexical-family generation if construction-first corpus needs demonstrate that the semantic domains are warranted.

### Current conclusion

The existing relational system is sufficient to express the tested valencies without adding a new core case or a new general applicative. The unresolved work is now primarily **lexical semantics and construction-specific syntax**, especially exact finite speech-complement behavior and future NAME/FILL/LOAD predicates.

New active valency probes: **E-0203–E-0208**.
