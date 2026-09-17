# Development Roadmap

**Logical phase structure for building out the language from established foundations.**

Each phase has hard dependencies on prior phases. Phases are listed in optimal order, but can partially overlap where noted.

---

## Phase 1: Phonology Completion (MOSTLY DONE)

**Goal:** Finalize synchronic phonology with tested allophony and prosody.

**Status:** Core inventory and syllable structure established. Edges remain.

**Tasks:**
- [ ] Confirm stress/syllable weight rules (or declare stress-neutral)
- [ ] Specify complete allophonic realizations (e.g., does /k/ [c] before /i/?)
- [ ] Test phonotactics against lexicon (are any roots unpronounceable?)
- [ ] Document any postlexical phonological rules (e.g., sandhi at morpheme boundaries)

**Deliverables:**
- `canon/phonology.md` — complete with allophony section
- `canon/allophony.md` (optional) — if rules are complex

**Blocking:** Nothing. Can work in parallel with morphology.

**Estimated effort:** 4–8 hours (mostly already done).

---

## Phase 2: Morphology Finalization (IN PROGRESS)

### Phase 2a: Verb Template Completion

**Goal:** Resolve remaining gaps in verb morphology.

**Status:** Template structure complete; two slot values unresolved.

**Tasks:**
- [ ] Semantically define `-we-` (AUX/DERIV slot) — consult open questions
- [ ] Semantically define `-w-` (discourse slot)
- [ ] Generate full conjugation paradigms for 3 test roots across all tense/aspect/mood combinations
- [ ] Identify any missing slots or redundancies

**Deliverables:**
- `morphology/verbs.md` — update with resolved -we- and -w- values
- `morphology/verb-paradigms.md` — 3 full paradigms (test roots)

**Blocking:** Nothing blocks this directly, but needed for Phase 3 testing.

**Estimated effort:** 6–10 hours.

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

**Estimated effort:** 10–16 hours total.

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

**Estimated effort:** 8–12 hours (needs example testing).

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

**Blocking:** Phase 4 (lexicon expansion) + Phase 5 (example generation).

**Estimated effort:** 20–34 hours total.

---

## Phase 4: Example Generation & Testing (Parallel with Phase 3b–3c)

**Goal:** Generate 20–50 example clauses to validate morphosyntax.

**Status:** No examples yet.

**Tasks:**
- [ ] **Transitive + intransitive** — Basic SVO / ergative patterns (10 examples)
- [ ] **Directional interactions** — Test i-/a-/Ø across different case slots (5 examples)
- [ ] **COM polysemy** — Test animate vs. inanimate COM with different verbs (5 examples)
- [ ] **TAM combinations** — Test tense/aspect/mood + agreement stacking (10 examples)
- [ ] **Clause combining** — Simple coordination, subordination, if present (10 examples)

**Deliverables:**
- `examples/test-clauses.md` — 20–50 interlinear examples (Leipzig glossing)
- Flag any morphological gaps or unexpected interactions

**Blocking:** Phase 5 (comprehensive lexicon).

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
- [ ] **Write 50–200 word passage** in simple narrative or descriptive style (e.g., "A person goes to the forest and finds something.")
- [ ] **Stress-test** — Use a variety of case forms, directionals, verb grades, and agreement patterns
- [ ] **Flag issues** — Any morphosyntactic combinations that feel unnatural or collide?
- [ ] **Revise canon** as needed based on testing

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
- [ ] **Sound-law documentation** (optional) — If pursuing diachronic depth, write up Neogrammarian correspondences
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
Phase 1 (Phonology)
    ↓
Phase 2a (Verbs) + Phase 2b (Nouns) ← must complete
    ↓
Phase 3a (Argument structure)
    ├→ Phase 3b (Verb-argument)
    ├→ Phase 3c (Clause combining)
    ├→ Phase 4 (Example testing) [can start in parallel with 3b]
    ├→ Phase 5 (Lexicon) [can start in parallel with 3c]
    └→ Phase 6 (Narrative) [depends on 4, 5]
        ↓
        Phase 7 (Polish)
```

---

## Summary: Total Effort & Timeline

| Phase | Effort | Status | Critical path? |
|-------|--------|--------|---|
| 1 | 4–8h | ~90% | No (blocking nothing) |
| 2 | 10–16h | ~70% | **Yes** (blocks 3) |
| 3 | 20–34h | ~40% | **Yes** (blocks 4–6) |
| 4 | 8–12h | 0% | **Yes** (validates 3) |
| 5 | 8–10h | 0% | No (parallelizable) |
| 6 | 6–10h | 0% | No (polish, not blocking) |
| 7 | 8–12h | 0% | No (final pass) |
| **TOTAL** | **64–102h** | ~38% | |

**Critical path:** Phase 2 → Phase 3 → Phase 4 → Phase 6 → Phase 7  
**Parallel tracks:** Phase 1 (any time), Phase 5 (with 3), Phase 6 (with 4–5)

**Realistic timeline (working ~2–4 hours/week):** 4–6 months to completion.

---

## Immediate Next Steps

1. **This week:** Phase 2a + 2b (resolve -we-, generate paradigms)
2. **Next week:** Phase 3a (genitive, word order, animacy rules via examples)
3. **Week 3:** Phase 4 (20 test clauses) + Phase 5 (derive 50 stems)
4. **Week 4+:** Phases 3b–3d + Phase 6

**Commits:**
- After Phase 2: promote verbs/nouns to canon
- After Phase 4: move validated syntactic rules from development → canon
- After Phase 6: finalize all canon files
- Phase 7: documentation pass

