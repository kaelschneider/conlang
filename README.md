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
- Grammatical glosses use uppercase (`ERG`, `GEN`, `NONPAST`, `1SG`).

## LEXICON.tsv

Exact columns:

```text
id	form	type	pos	gloss	derived_from	status	notes
```

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

## EXAMPLES.tsv

Exact columns:

```text
id	text	translation	segmentation	gloss	grammar_refs	entry_refs	status	notes
```

`grammar_refs` contains `G-*` IDs. `entry_refs` contains `L-*` IDs. Multiple references are separated by `;`.

Use `stable` only when the example is compatible with the current canonical grammar. Use `experimental` when it tests an unresolved analysis or contains unresolved lexical structure.

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
10. Prefer targeted edits over broad rewrites.

## Interoperability

The data model is deliberately TSV-first but follows simple relational conventions used by linguistic data standards. It can later be exported to richer standards such as CLDF or CoNLL-U without making those formats the canonical working representation.
