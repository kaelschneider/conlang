# Grammar

This file is an index for the grammar after the repository was split into dedicated domain sources.

## Canonical grammar sources

| Domain | File | Scope |
|---|---|---|
| Phonology | `PHONOLOGY.md` | Synchronic phonology, syllable structure, vowels, consonants, prosody, and historical sound change |
| Morphology | `MORPHOLOGY.md` | Verbal and nominal morphology, inflection, derivation, case, and morphological constructions |
| Syntax | `SYNTAX.md` | Clause structure, word order, alignment, pronouns, questions, clause combining, and unresolved syntactic domains |

## Status and evidence

`LEXICON.tsv` is authoritative for lexical entries and root data. `EXAMPLES.tsv` is the provenance-bearing example corpus and regression resource. `STATUS.md` records unresolved questions, development state, and recovered decisions.

Historical sound changes are consolidated with phonology in `PHONOLOGY.md`; they are not treated as a separate synchronic grammar component.

Grammar section IDs retain their `G-PHON`, `G-MORPH`, and `G-SYN` namespaces so existing example references remain stable after the split. The domain files are now the authoritative locations for those sections.
