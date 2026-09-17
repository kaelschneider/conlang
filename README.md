# Conlang

A naturalistic a priori constructed language project. The repository is intentionally small and flat for human use and reliable AI-assisted retrieval/editing.

## Files

| File | Role |
|---|---|
| `README.md` | Repository rules, schemas, and editing protocol |
| `STATUS.md` | Current state, unresolved questions, decisions, and next actions |
| `GRAMMAR.md` | Canonical synchronic grammar |
| `LEXICON.tsv` | Canonical lexical and historical-root data |
| `EXAMPLES.tsv` | Canonical/example sentence data and analysis |

Do not create another file unless one of these becomes a real retrieval or editing bottleneck.

## Authority

1. `GRAMMAR.md` is authoritative for current grammatical rules.
2. `LEXICON.tsv` is authoritative for lexical entries and historical roots.
3. `EXAMPLES.tsv` records evidence/testing; examples do not override grammar.
4. `STATUS.md` records uncertainty and development state; it is not itself grammar.
5. Git history records change history.

If sources conflict, do not silently choose one. Record the conflict in `STATUS.md` and resolve it explicitly.

## IDs

IDs are permanent and must never be reused.

- `G-*` = grammar rule
- `L-*` = lexicon entry
- `E-*` = example
- `Q-*` = open question in `STATUS.md`

## General data conventions

- TSV files are UTF-8, tab-separated, with one header row.
- Do not leave cells blank: use `?` for unknown/unresolved and `—` for not applicable.
- Use `;` to separate multiple IDs in a reference field.
- Do not use `;` inside an individual reference or free-text field.
- `Ø` means zero expression.
- IPA is enclosed in `/slashes/` for phonemic forms and `[brackets]` for phonetic forms.
- IPA is explicit data: do not infer or silently generate it from the orthography.
- Grammatical glosses use uppercase (`ERG`, `GEN`, `NONPST`, `1SG`).

## Leipzig Glossing Rules

Interlinear glosses follow the Leipzig Glossing Rules as the default analytical convention. The project uses hyphens for morpheme boundaries, `=` for clitics, and `.` inside a gloss for fused/portmanteau grammatical meanings where a single morph expresses multiple categories. A colon `:` may be used for phonological/grammatical fusion where appropriate.

Project-specific gloss abbreviations are controlled by `GRAMMAR.md`. Use established Leipzig abbreviations where they fit; do not invent a new abbreviation when a standard one is adequate. Glosses should be aligned one-to-one with segmented morphemes whenever possible.

Examples:

```text
ne-ku   k-u-i
1SG-ERG hold-REAL-NPST
```

A fused form should instead be represented according to its actual morphology, e.g. `X.Y` in the gloss if one morph expresses two grammatical values. Do not use punctuation merely to make a gloss look compact.

## LEXICON.tsv

Exact columns:

```text
id\tform\tipA\ttype\tpos\tgloss\tderived_from\tstatus\tnotes
```

`form` is the canonical orthographic citation form. `ipa` is its phonemic IPA citation form when established.

### `type` controlled vocabulary

`root` = historical/root-level base  
`lexeme` = independent modern lexical item  
`pronoun` = independent pronoun  
`proper` = proper name

### `pos` controlled vocabulary

`N` noun; `V` verb; `ADJ` adjective; `ADV` adverb; `PRON` pronoun; `NUM` numeral; `PART` particle; `CONJ` conjunction; `ADP` adposition; `INTJ` interjection; `—` not applicable.

### `status` controlled vocabulary

`stable` = current canonical data  
`experimental` = used for testing but not canonical  
`deprecated` = retained historically but no longer current

`derived_from` contains `L-*` IDs separated by `;`; use `—` for no parent and `?` when the relationship is unknown.

### Lexeme vs. inflected form

Do not create a lexicon entry for a predictable inflected form. The lexeme/citation form is stored once; productive forms are analyzed in `EXAMPLES.tsv` and `GRAMMAR.md`.

For example, the HOLD lexeme is `ka`. Its relationship to forms found in clauses is grammatical:

```text
ka    citation/nonfinite lexeme
ku    k-u     HOLD-REAL
kui   k-u-i   HOLD-REAL-NPST
```

Thus `ku` and `kui` are not separate `L-*` entries unless later evidence shows that they are independent lexicalized forms.

## EXAMPLES.tsv

Exact columns:

```text
id\ttext\tipa\ttranslation\tsegmentation\tgloss\tgrammar_refs\tentry_refs\tstatus\tnotes
```

`text` is the orthographic sentence. `ipa` is the phonemic pronunciation of the complete sentence when established. `grammar_refs` contains `G-*` IDs. `entry_refs` contains `L-*` IDs. Multiple references are separated by `;`.

`segmentation` should show morpheme boundaries using `-` and clitic boundaries using `=`. `gloss` should follow Leipzig conventions and correspond to the segmentation.

Use `stable` only when the example is compatible with the current canonical grammar. Use `experimental` when it tests an unresolved analysis or contains unresolved lexical structure.

## IPA conventions

IPA is phonemic unless a field explicitly requires phonetic transcription. Use the phoneme inventory established in `GRAMMAR.md`; do not introduce IPA symbols that are not supported by the current phonological analysis. Historical forms may be transcribed separately when relevant, but historical reconstruction must not be confused with the synchronic IPA of the modern language.

## Editing protocol

1. Read `README.md` and `STATUS.md` before editing.
2. Read the relevant grammar sections and lexical rows before changing examples.
3. Preserve all existing IDs.
4. Change the smallest possible unit.
5. Never infer a missing fact when the repository marks it `?`.
6. When a rule changes, inspect and update affected examples and references in the same change.
7. Never silently promote experimental material to stable.
8. Keep synchronic grammar separate from historical explanation.
9. Keep phonological repair distinct from morphological substitution.
10. Preserve Leipzig-style segmentation/glossing when editing examples.
11. Prefer targeted edits over broad rewrites.

## Interoperability

The data model is deliberately TSV-first but follows simple relational conventions used by linguistic data standards. It can later be exported to richer standards such as CLDF or CoNLL-U without making those formats the canonical working representation.
