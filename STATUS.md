# Status

**Last updated:** 2026-09-18  
**Phase:** Relational grammar and the current construction-first corpus layer are validated; active work is generator runtime validation, lexical valency/construction coverage, and remaining independent syntax.  
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
- 240 example rows
- example status distribution: 9 stable, 3 analyzed, 3 unresolved, 110 experimental, 115 deprecated
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

Current generator/config version: **0.2.0**.

Current generation profile:

- default target: 1,600 candidates
- permitted range: 1,200–2,000
- root-shape weights sum to 1.0
- mixed mono-/disyllabic root shapes with CVCV as the principal high-capacity shape and CVCVC as fallback
- final `h/j` exclusion applies to configured syllable-final consonant positions
- orthographic `v/y` are normalized to phonological /w j/ for collision checks
- existing lexicon collisions and within-run collisions are rejected
- semantic graph: 133 nodes and 160 relations
- sound symbolism is a weak ranking prior; deterministic sound-to-meaning mapping is forbidden
- generated candidates remain experimental and are never written automatically to `LEXICON.tsv`

Static configuration and grammar-anchor checks are consistent with the current files. A runtime seeded generator smoke test has **not** been executed in this environment because the repository sandbox cannot resolve external GitHub access; candidate production therefore remains a separate runtime-validation step.

## Open questions

The settled relational architecture should not be reopened without contradictory evidence.

Current open work is concentrated in:

1. exact finite speech-complement / direct-speech syntax
2. comparison constructions
3. passive or related voice behavior
4. whether a small independent adposition class should be developed
5. lexical coverage for NAME and FILL/LOAD
6. runtime evaluation of generated-root output and parameter tuning based on observed distributions
7. eventual promotion of sufficiently tested developmental constructions into `main`

Unresolved lexical questions should not be converted into new universal case frames merely to make an English sentence expressible.

## Roadmap

**1 — Generator runtime validation.** Run small deterministic counts first, then the 1,600-root target; inspect shape distribution, collision behavior, semantic-family balance, and candidate quality before tuning.

**2 — Lexical valency / construction coverage.** Continue matched probes for under-specified lexical predicates and fill genuine semantic gaps before adding new roots.

**3 — Independent syntax.** Test finite speech complements, comparison, and passive constructions as separate construction families.

**4 — Promotion review.** Re-run cross-domain contradiction checks, preserve historical/deprecated analyses, and promote only constructions with sufficient independent corpus support.

## Historical/provenance policy

- `GRAMMAR.md` controls current grammatical analysis.
- `EXAMPLES.tsv` provides evidence and regression coverage but never overrides grammar.
- `STATUS.md` records development state rather than serving as grammar.
- Deprecated examples remain only when they preserve useful testing or provenance.
- Superseded analyses should remain recoverable through notes and Git history rather than being silently rewritten as current rules.
