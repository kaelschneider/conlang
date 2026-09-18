# Status

**Last updated:** 2026-09-18  

**Phase:** Relational grammar and the current construction-first corpus layer are validated; finite speech complements, comparison, and passive are now working developmental constructions. Active work is cross-domain stress testing, generator runtime validation, lexical valency/construction coverage, and promotion review.  
**Repository structure:** Consolidated grammar source; minimal flat structure

## Branch state

- `main` is the canonical reconciled branch.
- `developmental` is the active working branch for experimental analyses, expanded regression coverage, generator development, and pending promotion decisions.
- The repository currently has only the persistent `main` and `developmental` branches.
- The inherited-root generator lives on `developmental`; the workflow entry point is present on `main` and explicitly checks out `developmental`.

## Canonical files

- `GRAMMAR.md` — authoritative grammar: phonology, morphology, syntax, prosody, and historical sound change
- `LEXICON.tsv` — authoritative lexical/root inventory
- `EXAMPLES.tsv` — provenance-bearing examples and regression corpus
- `SCHEMA.json` — structural schema for the two TSV files
- `AGENTS.md` — repository maintenance and development policy
- `STATUS.md` — development state, decisions, open questions, and testing priorities

## Project-wide validation checkpoint — 2026-09-18

Both persistent branches were checked after the recent relational, corpus, syntax, and generator work.

### Structural/data validation

**`main`**

- 86 lexical rows
- 127 example rows
- no duplicate IDs
- no broken lexical references
- no broken grammar references
- no segmentation/gloss word-count mismatches
- no invalid IPA fields under the current schema/phonology checks
- no hyphens in surface example text after cleanup

**`developmental`**

- 98 lexical rows
- 268 example rows
- example status distribution: 9 stable, 3 analyzed, 3 unresolved, 138 experimental, 115 deprecated
- no duplicate IDs
- no broken lexical references
- no broken grammar references
- no segmentation/gloss word-count mismatches
- no invalid IPA fields under the current schema/phonology checks
- no hyphens in surface example text after cleanup
- grammar section identifiers are unique after removal of the duplicate `G-SYN-16` heading

The schema now explicitly accepts the current `AUX` lexical POS and the retained `deprecated` example status used for superseded regression/provenance material.

### Corrections applied during this pass

- Removed the duplicated `G-SYN-16 — Impersonal predicates` section from developmental `GRAMMAR.md`.
- Corrected the remaining surface-form hyphen violations in `E-0227` and `E-0228`.
- Corrected the IPA fields for `E-0165` and `E-0168`.
- Corrected canonical `E-0073` surface text in `main`.
- Corrected the orthographic `v` in the IPA for canonical `E-0126` to phonological /w/.
- Updated `SCHEMA.json` on both branches to match the implemented status/POS vocabulary.

These are validation/consistency repairs; no new grammatical rule was introduced by them.

## Current reconciled grammar architecture

The current `developmental` grammar is organized around:

- seven nominal case values: ABS, ERG `-ku`, GEN `-se`, LOC `-te`, CONTAINMENT `-ci`, POSITION `-ta`, and COM/ASSOCIATIVE `-me`
- PATH absorbed into COM/ASSOCIATIVE rather than retained as a separate synchronic case
- a general relational-vector system: `Ø` = neutral relation, `i-` = convergence/increasing orientation, `a-` = divergence/decreasing orientation
- one productive APPL operation, `-ka-`; unrestricted APPL stacking is not established
- APPL candidate selection by semantic hierarchy, then discourse prominence, then linear order for genuine same-rank ties
- one verbal object-index slot: LOCAL `n-/en-`, ordinary 3P animate `m-`, ordinary 3P inanimate zero, OBV `v-`; reflexive and reciprocal remain special coreference values
- APPL promotion before object indexing; other relational NPs remain oblique unless independently licensed as core arguments
- productive case stacking restricted to the currently promoted core: CONTAINMENT → LOC, GEN → CONTAINMENT, GEN → LOC
- `POSITION → LOC`, `COM → LOC`, recursive three-case stacking, repeated identical case, and unrestricted ERG stacking remain boundary tests rather than promoted general rules
- SOV order, active-stative / Split-S alignment, person-only finite agreement, case-based converbs, constituent-order/prosody information structure, and a compact derivational system
- impersonal finite predicates with working `-v-` agreement for the initial weather/ambient class
- secondary predication using existing `-ri`, `-na`, and `-mu` participles, independent of APPL
- finite speech complements as zero-complementizer finite ABS content clauses, with optional LOC addressees
- comparison as COM-marked standard + verbal direction on gradable predicates, including equative, superior, inferior, and set-based superlative readings
- passive as finite `-na-` voice, promoting the patient to ABS S and optionally demoting the agent to COM
- PASS + APPL as a productive composition: PASS promotes the patient to ABS S and agreement control; APPL independently promotes one remaining eligible relational participant to the single object-index slot; the existing APPL hierarchy and tie-break rules remain unchanged

The relational system is fully integrated into the current `developmental` description, but remains developmental until independently promoted to `main`.

## Corpus state

The first construction-first corpus redevelopment is complete for the current layer.

- Older superseded regression material remains preserved as `deprecated`; it is provenance, not current evidence for productive grammar.
- The active construction-first layer begins with neutral nominal probes and deliberately distributes referential types rather than relying on the historical CONTAINER example.
- Relational, argument-structure, information-structure, causative, converbial, question, modal, impersonal, and secondary-predication probes are represented in the active corpus.
- The full four-frame `CASE × DIRECTION × APPL` matrix is closed for the current experimental architecture.
- Active syntax probes cover content questions, impersonal predicates, and secondary predication in addition to the earlier core syntax set.

## Lexicon semantic state

The semantic audit treats the lexicon as a system of centers, specialization, polysemy, and constructional behavior rather than a flat English-gloss list.

Current neutral semantic centers include:

- `r/ra` MOVE / GO
- `m/ma` REMAIN / STAY
- `n/na` OBTAIN / ACQUIRE
- `j/ya` PERCEIVE
- `h/ha` SAY
- `v/va` GROW / INCREASE
- `t/transfer` TRANSFER

Specialized and lexicalized meanings are retained rather than flattened into generic roots.

Current lexical valency testing has covered experiencer, speech, search/hunt, acquisition, and material/medium relations. NAME and FILL/LOAD remain genuine lexical gaps rather than triggers for new grammatical structure.

## Inherited-root generator

The inherited-root generator is implemented on `developmental`:

- `tools/generate_roots.py`
- `tools/root_generation.yaml`

Current generator/config version: **0.3.0** (candidate-pool architecture).

Current generation profile:

- default candidate pool: 4,000 candidates; intended human-curation target: 1,600 roots
- permitted generation range: 1,200–5,000
- root-shape weights sum to 1.0
- mixed mono-/disyllabic root shapes with a 20% short-root allocation; CVCV remains the principal shape and CVCVC is an emergency fallback only after primary legal forms are exhausted
- final `h/j` exclusion applies to configured syllable-final consonant positions
- orthographic `v/y` are normalized to phonological /w j/ for collision checks
- existing lexicon collisions and within-run collisions are rejected
- semantic graph: 133 nodes and 160 relations
- sound symbolism is a weak ranking prior; deterministic sound-to-meaning mapping is forbidden
- generated candidates remain experimental and are never written automatically to `LEXICON.tsv`\n- the candidate pool deliberately overgenerates; human semantic curation is expected to reduce the pool toward the 1,600-root working target\n- the family model targets 55% of candidate roots as singleton families; the remaining roots are allocated to centrality-weighted non-singleton families with a long-tail size distribution\n- distant/very-distant semantic relationships are reserved for a separate historical-drift stage rather than being generated as direct semantic families

Static configuration and grammar-anchor checks are consistent with the current files. A runtime seeded generator smoke test has **not** been executed in this environment because the repository sandbox cannot resolve external GitHub access; candidate production therefore remains a separate runtime-validation step.

## Independent syntax pass — 2026-09-18

The three remaining independent-syntax gaps were completed as working developmental constructions, then reconciled to the selected 2026-09-18 decisions and interaction-tested in the regression corpus.

### Finite speech complements

- SAY `ha` now directly selects a finite ABS speech-content clause in ordinary preverbal complement position.
- No complementizer is required. The embedded clause remains fully finite, retaining its own subject/case marking, agreement, TAM, negation, and interrogation.
- An overt addressee is an ordinary LOC-marked relational NP; it is not automatically promoted by APPL.
- Direct speech has no obligatory dedicated quotative exponent. Quotation is treated as a discourse/prosodic interpretation of the finite speech-content clause rather than a new grammatical morpheme.

### Comparison

- Comparison uses the existing COM/ASSOCIATIVE case to mark the standard.
- With gradable predicates, neutral direction gives an equative reading; `i-` gives a superior comparison; `a-` gives an inferior comparison.
- Superlative meaning is a conventionalized set-comparison construction: a singular comparee is evaluated upward against a plural/set-valued COM standard.
- The construction does not automatically trigger APPL or object indexing.

### Passive

- Passive is marked by finite `-na-` in a new VOICE slot after AUX/DERIV and before APPL.
- The lexical patient/theme becomes ABS S and controls ordinary person agreement.
- The agent is optional; when overt, it is COM-marked and therefore demoted from core argument structure.
- The promoted passive patient is not represented in the ordinary object-index slot.
- Formal identity between passive `-na-` and patientive participle `-na` is retained as a naturalistic morphological relationship, but the two functions remain distinct synchronically.
- PASS + APPL is now a settled productive composition, supported by matched recipient, beneficiary/maleficiary, hierarchy, additional-relation, inanimate-index, tie-break, and AUX/DERIV probes.

These are reconciled developmental analyses, not yet promoted to `main`. The selected constructional choices are settled for the current developmental grammar, including PASS + APPL; the broader voice system remains a future question beyond this passive composition.

### Validation checkpoint — 2026-09-18

The reconciled syntax layer was checked against the current repository data:

- 268 example rows are present in `EXAMPLES.tsv`, with IDs remaining unique.
- The E-0242–E-0269 syntax examples have ten TSV fields, no surface-form hyphens, primary stress in IPA, and grammar/lexical references resolving to existing sections and entries.
- E-0251–E-0254 were reconciled so passive finite forms use the ordinary REALIS stem `ku` rather than the nonfinite stem `ka`.
- E-0255 tests comparison + IRREALIS; E-0256 tests comparison inside ordinary nominalized/dependent morphology; E-0257 tests passive + IRREALIS; E-0258 tests passive coordination without any CONJ inflection; E-0259 tests PASS + AUX/DERIV ordering.
- E-0260–E-0269 test PASS + APPL across LOC recipient, overt agent, COM benefactive/malefactive, APPL hierarchy, reversed order, additional relations, inanimate indexing, same-rank tie-breaking, and PASS + APPL + AUX/DERIV.
- `G-MORPH-06B`, `G-SYN-18`, `G-SYN-19`, and `G-SYN-20` are unique grammar-section identifiers.
- No lexical additions were required; all new probes reuse established roots and lexemes.
- Full runtime project validation remains separate from this static checkpoint because the repository's current workflow does not provide a general validation job on `developmental`.

## Open questions

The settled relational architecture and the completed syntax analyses should not be reopened without contradictory evidence. The selected speech, comparison, dependency, passive, and PASS + APPL analyses are reconciled. Remaining voice work concerns broader cross-domain stress tests rather than the basic PASS + APPL interaction.

Current open work is concentrated in:

1. Other cross-domain voice stress tests beyond the now-settled PASS + APPL composition
2. whether a small independent adposition class should be developed
3. lexical coverage for NAME and FILL/LOAD
4. runtime evaluation of generated-root output and parameter tuning based on observed distributions
5. eventual promotion of sufficiently tested developmental constructions into `main`

Unresolved lexical questions should not be converted into new universal case frames merely to make an English sentence expressible.

## Roadmap

**1 — Generator runtime validation.** Run small deterministic counts first, then the 1,600-root target; inspect shape distribution, collision behavior, semantic-family balance, and candidate quality before tuning.

**2 — Lexical valency / construction coverage.** Continue matched probes for under-specified lexical predicates and fill genuine semantic gaps before adding new roots.

**3 — Cross-domain syntax stress testing.** Finite speech complements, comparison, passive, and PASS + APPL are reconciled. Remaining work is broader voice/construction interaction testing before promotion.

**4 — Promotion review.** Re-run cross-domain contradiction checks, preserve historical/deprecated analyses, and promote only constructions with sufficient independent corpus support.

## Historical/provenance policy

- `GRAMMAR.md` controls current grammatical analysis.
- `EXAMPLES.tsv` provides evidence and regression coverage but never overrides grammar.
- `STATUS.md` records development state rather than serving as grammar.
- Deprecated examples remain only when they preserve useful testing or provenance.
- Superseded analyses should remain recoverable through notes and Git history rather than being silently rewritten as current rules.
