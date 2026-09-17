# Conlang

A naturalistic a priori constructed language project. The repository is intentionally small and flat for human use and reliable AI-assisted retrieval/editing.

## Files

| File | Role |
|---|---|
| `README.md` | Repository rules, schemas, conventions, and editing protocol |
| `STATUS.md` | Current state, unresolved questions, decisions, and next actions |
| `GRAMMAR.md` | Canonical synchronic grammar |
| `LEXICON.tsv` | Canonical lexical and historical-root data |
| `EXAMPLES.tsv` | Canonical example/test corpus and analysis |

Do not create another file unless one of these becomes a real retrieval or editing bottleneck.

## Authority

1. `GRAMMAR.md` is authoritative for current grammatical rules.
2. `LEXICON.tsv` is authoritative for lexical entries and historical roots.
3. `EXAMPLES.tsv` records evidence/testing; examples do not override grammar.
4. `STATUS.md` records uncertainty and development state; it is not itself grammar.
5. Git history records change history.

When sources conflict, do not silently choose one. Preserve the conflict and record it in `STATUS.md` until explicitly resolved.

## Evidence levels

Keep these distinct:

- **OBSERVED** — directly attested in the existing corpus, historical material, or explicit project decisions.
- **ANALYZED** — an interpretation supported by observations but not yet established as a rule.
- **RULE** — explicitly established by the project and recorded in `GRAMMAR.md`.

Never silently promote an analysis to a rule.

Do not treat typological expectations, similarity to another language, frequency, or what “would make sense” as evidence that a form or rule is canonical.

When multiple analyses remain compatible with the evidence, preserve the ambiguity rather than selecting one.

## Scope lock

For every edit:

- Change only what is necessary to fulfill the user's request.
- Do not opportunistically normalize unrelated inconsistencies.
- Do not rewrite older material merely to fit a newer preferred analysis unless normalization is explicitly requested.
- Preserve historical evidence even when the current analysis changes.

## IDs

IDs are permanent and must never be reused.

- `G-*` = grammar rule
- `L-*` = lexicon entry
- `E-*` = example
- `Q-*` = open question in `STATUS.md`

Preserve existing IDs when editing.

## General data conventions

- TSV files are UTF-8, tab-separated, with one header row.
- Do not leave cells blank: use `?` for unknown/unresolved and `—` for not applicable.
- Use `;` to separate multiple IDs in reference fields.
- Do not use `;` inside an individual reference or free-text field.
- `Ø` means zero expression.
- Orthography, phonemic IPA, phonetic IPA, and historical reconstruction are distinct representations.
- IPA is explicit data; never silently infer or invent IPA.
- Phonemic IPA uses `/slashes/`; phonetic IPA uses `[brackets]`.
- Grammatical glosses use uppercase for grammatical categories; person-only verbal agreement uses `1`, `2`, `3`.

## Leipzig Glossing Rules

Interlinear glosses follow the Leipzig Glossing Rules as the default analytical convention.

- `-` = morpheme boundary
- `=` = clitic boundary
- `.` = multiple grammatical meanings expressed by one morph
- `:` = morphophonological/grammatical fusion in morphological glossing/segmentation

In an IPA field, a keyboard `:` is the plain-text substitute for IPA `ː`, marking length/gemination.

Segmentation and gloss must correspond as closely as possible one-to-one.

Example:

```text
ne-ku   k-u-k-i
1-ERG   HOLD-REAL-1-NONPAST
```

Do not add punctuation merely to make a gloss compact. Use a standard Leipzig abbreviation when one exists rather than inventing a new abbreviation. Project-specific abbreviations may be defined in `GRAMMAR.md` when the language requires them.

## LEXICON.tsv

Exact columns:

```text
id\tform\tipa\ttype\tpos\tgloss\tderived_from\tstatus\tnotes
```

`form` = canonical orthographic citation form.  
`ipa` = established phonemic IPA citation form.

### `type` controlled vocabulary

- `root` = historical/root-level base
- `lexeme` = independent modern lexical item
- `pronoun` = independent pronoun
- `proper` = proper name

### `pos` controlled vocabulary

`N`, `V`, `ADJ`, `ADV`, `PRON`, `NUM`, `PART`, `CONJ`, `ADP`, `INTJ`, `—`

### `status` controlled vocabulary

- `stable` = current canonical data
- `experimental` = used for testing but not canonical
- `deprecated` = retained historically but no longer current

`derived_from` contains immediate parent `L-*` IDs separated by `;`, `—` for no parent, or `?` when unknown. Multiple parent IDs are allowed.

### Lexemes, derivation, and inflection

Do not create a lexicon entry for a predictable inflected form.

**Inflection** produces a grammatical form of an existing lexeme and normally does not receive its own `L-*` entry. Example:

```text
ka      lexeme / citation-nonfinite form
ku      k-u       HOLD-REAL
kuci    k-u-k-i   HOLD-REAL-1-NONPAST
```

Here `ka` is the lexeme; `ku` and `kuci` are grammatical forms, not separate lexemes.

**Lexical derivation** produces a new lexical item. When the resulting item functions as an independent lexeme, it receives its own `L-*` entry and its immediate lexical parent(s) are recorded in `derived_from`.

For example:

```text
ka + ra  →  kera
L-0016   +  L-0019 → L-0034
```

`kera` is a derived nonfinite stem/lexeme; its predictable REALIS form `keru` does not receive a separate lexicon entry.

`derived_from` records immediate lexical parents, not every ancestor. Separate parent IDs are separated by `;`.

Create a separate `L-*` entry only when evidence indicates lexicalization, productive or established lexical derivation, irregularity, historical independence, or another reason the form functions as an independent lexical item rather than a predictable grammatical form.

If the derivational relationship itself is uncertain, preserve the form and mark the analysis `?` rather than inventing one.

## Grammar and morphological analysis

When analyzing a form:

1. Identify the lexical base.
2. Apply established morphological rules.
3. Apply established phonological rules.
4. Distinguish productive morphology from historical developments.
5. Distinguish lexical stems from subsequent inflectional grades.
6. Mark any unresolved step with `?` rather than inventing an explanation.

Do not use historical reconstruction to justify a synchronic rule unless the project has explicitly established that rule as productive.

Keep phonological repair distinct from morphological substitution or deletion.

## EXAMPLES.tsv

Exact columns:

```text
id\ttext\tipa\ttranslation\tsegmentation\tgloss\tgrammar_refs\tentry_refs\tstatus\tnotes
```

`text` = orthographic example/utterance.  
`ipa` = phonemic IPA of the complete example when established.

`grammar_refs` contains `G-*` IDs.  
`entry_refs` contains `L-*` IDs.

Use `stable` only when the example is compatible with current canonical grammar.

Use `experimental` when it tests an unresolved analysis or contains unresolved lexical structure.

Examples are evidence and tests, not independent sources of grammar.

## IPA conventions

Use the established phoneme inventory in `GRAMMAR.md`.

Do not infer phonetic detail that the project has not established.

For every transcription, keep these conceptually separate:

```text
orthography: y
phonemic IPA: /j/
historical reconstruction: *j
```

Do not treat orthographic symbols, IPA symbols, and reconstructed forms as interchangeable.

Historical forms may receive their own transcription when relevant, but historical reconstruction must not be confused with modern synchronic IPA.

When typing IPA on a standard keyboard, `:` may substitute for `ː` for length/gemination.

## Editing protocol

Before editing:

1. Read `README.md` and `STATUS.md`.
2. Read the relevant grammar sections and lexical rows.
3. Identify whether each relevant fact is OBSERVED, ANALYZED, or RULE.

While editing:

4. Preserve all existing IDs.
5. Make the smallest necessary change.
6. Preserve `?` when something remains unresolved.
7. Do not silently promote experimental material to stable.
8. Preserve the distinction between synchronic grammar and historical explanation.
9. Preserve Leipzig segmentation/glossing.
10. Preserve explicit IPA rather than inventing new transcription.
11. Update affected examples and references when a canonical rule changes.
12. Do not normalize unrelated material.

Before finishing, verify:

- Did I change only the requested scope?
- Did I introduce any unsupported rule?
- Did I accidentally turn `?` into a fact?
- Do segmentation and gloss correspond?
- Does the IPA match the established phonology?
- Did I preserve all IDs?
- Did I update affected references?
- Did I accidentally create a lexical entry for a predictable inflected form?

## Interoperability

TSV is the canonical working format because it is compact, readable in GitHub, easy for LLMs to retrieve, and easy to diff.

The data model should remain simple enough to export later to standards such as CLDF or CoNLL-U without making those standards the repository's canonical representation.
