# Development Roadmap

**Logical phase structure for building out the language from established foundations.**

Each phase has hard dependencies on prior phases. Phases are listed in optimal order, but can partially overlap where noted.

---

## Phase 1: Phonology Completion (COMPLETE)

**Goal:** Establish the phonological framework while deliberately allowing detailed phonetic rules to emerge through testing.

**Decisions:**
- `-we-` is dropped from the AUX/DERIV inventory.
- `-w-` is dropped from the discourse slot.
- Allophony is environment-driven, with historical sound changes used as evidence where relevant; detailed rules are canonized only after repeated examples support them.
- Stress is weight-sensitive and may be morphologically conditioned; exact rules remain emergent and test-driven.

**Status:** Complete at the framework/decision level. Detailed allophony, stress, and phonotactic edge cases will be resolved opportunistically during example generation rather than in advance.

**Tasks:**
- [x] Resolve `-we-` → dropped
- [x] Resolve `-w-` → dropped
- [x] Establish allophony policy
- [x] Establish stress/syllable-weight policy
- [ ] Test phonotactics against lexicon (are any roots unpronounceable?)
- [ ] Document postlexical phonological rules if repeated testing establishes them

**Deliverables:**
- `canon/phonology.md` — update with current allophony/prosody policy
- `canon/allophony.md` (optional) — only if rules become complex enough to warrant a separate file

**Blocking:** Nothing. Detailed phonology can develop alongside morphology and syntax.

---

## Phase 2: Morphology Finalization (IN PROGRESS)

### Phase 2a: Verb Template Completion

**Goal:** Validate the existing verb template through paradigms and examples rather than add unresolved morphology speculatively.

**Status:** Template structure established; `-we-` and `-w-` have been removed.

**Tasks:**
- [ ] Generate full conjugation paradigms for 3 test roots across tense/aspect/agreement combinations
- [ ] Identify any missing slots or redundancies through example generation

**Deliverables:**
- `morphology/verbs.md` — reflect the resolved inventory
- `morphology/verb-paradigms.md` — 3 full paradigms (test roots)

**Blocking:** Phase 3 testing.

**Estimated effort:** 4–8 hours.

---

### Phase 2b: Noun System Validation

**Goal:** Confirm that all 18 case forms are phonologically distinct and semantically coherent.

**Status:** Case system designed; not yet tested with real roots.

**Tasks:**
- [ ] Test all 18 forms on 3–5 nouns, checking for phonological collapse/ambiguity
- [ ] Verify COM polysemy examples work (animate vs. inanimate arguments)
- [ ] Generate noun paradigm examples for each case series
- [ ] Confirm that directional prefixes never trigger allophony that obscures case suffixes

**Deliverables:**
- `morphology/noun-paradigms.md` — 5 full noun paradigms (one per case series)
- `morphology/cases.md` — add "Phonological note" section if needed

**Blocking:** Phase 3 (syntax) depends on this.

**Estimated effort:** 3–6 hours.

---

### Phase 2 Subtotal

**Blocking:** Phase 3 (syntax decisions).

**Estimated effort:** 7–14 hours total.

---

## Phase 3: Syntax Framework (IN PROGRESS)

**Goal:** Resolve core syntactic decisions; establish phrase structure and clause templates.

**Status:** Basic structure hypothesized; needs formalization + testing.

### Phase 3a: Core Argument Structure

**Tasks:**
- [ ] **Animacy/person Split-S conditions** — When does patient take ABS vs. ergative patterning? Generate decision table.
- [ ] **Genitive position** — Pre- or post-nominal? Decide + test with examples.
- [ ] **Word order** — SVO hypothesis? Test with V-final vs. V-medial examples. Confirm modifier order (Adj-N or N-Adj).
- [ ] **Adpositions** — Needed? If yes, pre- or post-? If no, how do spatial relations beyond cases get expressed?

**Deliverables:**
- `syntax/word-order.md` — finalized with tested examples
- `syntax/noun-phrase.md` — genitive, modifier, determiner position

**Estimated effort:** 8–12 hours.

---

### Phase 3b: Verb-Argument Interface

**Tasks:**
- [ ] **Negative morphology** — Position in verb template? Scope (negates predicate, object, or both)?
- [ ] **Valence** — How are causatives, passives, applicatives expressed? (Currently via cases + directionals; confirm.)
- [ ] **Agreement conditioning** — Does agreement mark only agent? Agent + object? Hierarchical?
- [ ] **Object marking interactions** — How do reflexive/reciprocal markers interact with case system?

**Deliverables:**
- `syntax/negation.md` — established rules + examples
- `syntax/valence.md` — causative, passive, applicative derivation

**Estimated effort:** 6–10 hours.

---

### Phase 3c: Clause Combining

**Tasks:**
- [ ] **Converbs** — Which stem grades / case forms signal subordination? How does switch-reference work?
- [ ] **Relative clauses** — Prenominal, postnominal, or internally headed?
- [ ] **Coordination** — Asyndetic, particles, or verbal agreement?
- [ ] **Conditional / causal** — Morphological markers or purely syntactic?

**Deliverables:**
- `syntax/clause-combining.md` — templates + examples
- `syntax/converbs.md` (optional) — if system is complex

**Estimated effort:** 4–8 hours.

---

### Phase 3d: Information Structure (Low Priority)

**Tasks:**
- [ ] **Topic/focus** — Expressed via word order, particles, or intonation?
- [ ] **Definiteness** — Marked grammatically or pragmatic?
- [ ] **Obviation** — Used (especially in relative clauses)?

**Deliverables:**
- `syntax/information-structure.md` (optional)

**Estimated effort:** 2–4 hours (can defer).

---

### Phase 3 Subtotal

**Blocking:** Phase 4 (example generation) and later lexicon expansion.

**Estimated effort:** 20–34 hours total.

---

## Phase 4: Example Generation & Testing (Parallel with Phase 3b–3c)

**Goal:** Generate 20–50 example clauses to validate morphosyntax.

**Status:** No examples yet.

**Tasks:**
- [ ] **Transitive + intransitive** — Basic word-order and argument-structure patterns (10 examples)
- [ ] **Directional interactions** — Test i-/a-/Ø across different case slots (5 examples)
- [ ] **COM polysemy** — Test animate vs. inanimate COM with different verbs (5 examples)
- [ ] **TAM combinations** — Test tense/aspect/agreement stacking (10 examples)
- [ ] **Clause combining** — Simple coordination, subordination, if present (10 examples)
- [ ] **Phonological testing** — Record recurring allophonic, stress, and weight patterns and promote only repeated rules to canon

**Deliverables:**
- `examples/test-clauses.md` — 20–50 interlinear examples (Leipzig glossing)
- Flag any morphological or phonological gaps and unexpected interactions

**Blocking:** Lexicon expansion and running text.

**Estimated effort:** 8–12 hours.

---

## Phase 5: Lexicon Expansion (Parallel with Phase 3–4)

**Goal:** Grow from 10 to 50–100+ usable stems.

**Status:** 10 monoconsonantal roots established.

**Tasks:**
- [ ] **Derivational morphology** — Document how each root combines with stem grades (-a-, -e-, -u-, -i-) and common affixes
- [ ] **Semantic derivation** — Generate 3–5 related stems per root (agent nouns, instrumental nouns, stative verbs, etc.)
- [ ] **Test productivity** — Do derivations follow predictable patterns, or are many suppletive?
- [ ] **Sound-law interaction** — Do derived stems undergo the same sound changes as roots?

**Sub-targets:**
- [ ] 10 roots × 5 derivatives = ~50 stems (Phase 5a, ~4 hours)
- [ ] Add 10–20 borrowed or onomatopoetic roots (Phase 5b, ~2 hours)
- [ ] Total ~70–100 stems (Phase 5c, ~2 hours)

**Deliverables:**
- `lexicon/roots.md` — expanded with derivations
- `lexicon/derivations.md` (optional) — systematic documentation of patterns

**Blocking:** Phase 6 (running text).

**Estimated effort:** 8–10 hours total.

---

## Phase 6: Narrative Examples & Polish (Parallel with Phase 5)

**Goal:** Generate 1–2 coherent paragraphs in the language to stress-test everything.

**Status:** No running text yet.

**Tasks:**
- [ ] **Write 50–200 word passage** in simple narrative or descriptive style
- [ ] **Stress-test** — Use a variety of case forms, directionals, verb grades, and agreement patterns
- [ ] **Flag issues** — Any morphosyntactic combinations that feel unnatural or collide?
- [ ] **Revise canon** as needed based on testing
- [ ] **Revisit phonology** where running text exposes recurring allophonic/stress patterns

**Deliverables:**
- `examples/narrative-sample.md` — running text + English translation + grammatical notes
- Any revisions back to canon files

**Blocking:** Phase 7 (finalization).

**Estimated effort:** 6–10 hours.

---

## Phase 7: Documentation & Polish (Final)

**Goal:** Finalize all documentation; produce clean summary documents.

**Status:** In-progress; scattered across canon and development.

**Tasks:**
- [ ] **Typological summary** — 1-page overview of language type, unique features, design goals
- [ ] **Grammar sketch** — 5–10 page overview of phonology/morphology/syntax for quick reference
- [ ] **Lexicon export** — Consolidated root + derived stem list with glosses
- [ ] **Sound-law documentation** (optional) — If pursuing diachronic depth, write up sound correspondences
- [ ] **Clean up open-questions.md** — Promote resolved items to canon, archive obsolete questions

**Deliverables:**
- `README.md` → updated with links to final documents
- `canon/typology.md` — brief description
- `reference/grammar-sketch.md` — accessible overview
- `lexicon/complete-inventory.md` — all roots + stems, organized by semantic domain

**Estimated effort:** 8–12 hours.

---

## Dependency Graph

```
Phase 1 (Phonology) — COMPLETE
    ↓
Phase 2a (Verbs) + Phase 2b (Nouns)
    ↓
Phase 3a (Argument structure)
    ├→ Phase 3b (Verb-argument)
    ├→ Phase 3c (Clause combining)
    ├→ Phase 4 (Example testing) [can start in parallel with 3b]
    ├→ Phase 5 (Lexicon) [can start in parallel with 3]
    └→ Phase 6 (Narrative) [depends on 4, 5]
        ↓
        Phase 7 (Polish)
```

---

## Summary: Total Effort & Timeline

| Phase | Effort | Status | Critical path? |
|-------|--------|--------|---|
| 1 | — | **Complete** | No |
| 2 | 7–14h | ~70% | **Yes** (blocks 3) |
| 3 | 20–34h | ~40% | **Yes** (blocks 4–6) |
| 4 | 8–12h | 0% | **Yes** (validates 3) |
| 5 | 8–10h | 0% | No (parallelizable) |
| 6 | 6–10h | 0% | No (polish, not blocking) |
| 7 | 8–12h | 0% | No (final pass) |
| **TOTAL REMAINING** | **57–92h** | | |

**Critical path:** Phase 2 → Phase 3 → Phase 4 → Phase 6 → Phase 7  
**Parallel tracks:** Phase 5 can proceed with Phases 3–4; detailed Phase 1 phonology can be refined opportunistically throughout testing.

---

## Immediate Next Steps

1. **Next:** Generate 5–10 example sentences using established roots and morphology.
2. Use those examples to test **alignment, genitive position, word order, and negation**.
3. Generate complete verb and noun paradigms while testing phonological interactions.
4. Expand the lexicon to 30–50 stems once productive patterns are clear.
5. Write a first 1–2 paragraph text to stress-test the resulting grammar.
6. Promote only repeatedly supported phonological and syntactic patterns to canonical status.

**Commits:**
- After Phase 2: promote validated verbs/nouns to canon
- After Phase 4: move validated syntactic rules from development → canon
- After Phase 6: finalize all canon files
- Phase 7: documentation pass

