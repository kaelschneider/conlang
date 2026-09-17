# Phonology

Status: canonical where stated; unresolved conditions remain in `STATUS.md`.

## G-PHON — Phonology

### G-PHON-01 — Syllable structure

Surface syllable structure is `(C)V(C)`. Productive onset clusters are not established. Complex sequences may arise historically or morphologically and subsequently reduce or fuse.

For historical conditioning, **OPEN** means a target consonant belongs to a syllable of shape `CV`; **CLOSED** means it belongs to a syllable of shape `CVC`. The distinction is structural and is not specific to any one coda consonant. Historical syllabification determines which syllable is relevant at the stage where a sound law applies.

Representative historical shapes for testing include `*pVpV`, `*pVpVn`, `*pVnpV`, and `*pVnpVn`; these are diagnostic configurations rather than separate lexical rules.

### G-PHON-02 — Vowels

The synchronic vowel inventory is `/a e i u/`. Long vowels are written `aa ee ii uu` and represented phonemically as `/aː eː iː uː/` when their quantity is established.

For historical vowel-environment notation:

- **F** = front vowel (`/e i/`)
- **B** = back vowel (`/a u/`)

Thus the four vowel-transition classes are:

| Class | Meaning |
|---|---|
| `F_F` | front → front |
| `F_B` | front → back |
| `B_F` | back → front |
| `B_B` | back → back |

The four classes are evaluated independently. No universal lenition hierarchy is assumed; the concrete outcomes are given by the historical matrix in G-PHON-04/G-PHON-05.

### G-PHON-03 — Consonants

The synchronic consonant inventory is `/p t k c m n s h w j r/`. In the established orthography, `c` represents `/ts/`, `v` represents `/w/`, and `y` represents `/j/`.

Conditioned phonetic realization is not exhaustively specified. Historical-source distinctions may survive as phonetic traces without creating additional synchronic phonemes.

### G-PHON-04 — Historical conditioning

The principal historical weakening system is conditioned by the interaction of:

1. the syllable containing the target consonant (**OPEN / CLOSED**), and
2. the neighboring-vowel transition class (**F_F / F_B / B_F / B_B**).

OPEN syllables permit a later stage of weakening than CLOSED syllables in the environments where the consonant has more than one weakening stage. The four vowel-transition classes are otherwise independent rather than ordered on a single scale.

The matrix below is the concrete current system. It applies to historical singleton `p, t, k` targets that reach the general weakening stage. A dash for `B_F` with `t/k` means that pre-/i/ palatalization has priority and the consonant does not enter the ordinary lenition path.

| Syllable | Target | `F_F` | `F_B` | `B_F` | `B_B` |
|---|---|---|---|---|---|
| OPEN | `p` | `h` | `h` | `Ø` | `Ø` |
| OPEN | `t` | `d` | `d` | PAL | `d` |
| OPEN | `k` | `g` | `k` | PAL | `Ø` |
| CLOSED | `p` | `p` | `p` | `h` | `h` |
| CLOSED | `t` | `t` | `t` | PAL | `d` |
| CLOSED | `k` | `k` | `k` | PAL | `g` |

`PAL` is the independently ordered `t, k > c > tɕ > ɕ / _i` pathway in G-PHON-05.

This matrix is a concrete design completion of cells that are not all directly instantiated by the small current corpus. Attested developments constrain the cells containing `reruka`, `reruta`, `rerupa`, `rupi`, `mente`, and `menta`; unsupported cells are completed by extending the same consonant-specific stage logic without introducing a new lenition series.

### G-PHON-05 — Historical sound laws and relative chronology

`>` denotes a successive historical stage. Later rules apply to the outputs of earlier rules unless an environment explicitly limits the rule.

#### Stage I — Pre-/i/ palatalization

**1. `t, k > c / _i`**

Historical `t` and `k` become `c` before `/i/`. This precedes the general weakening of those consonants, so a resulting `c` is not subsequently treated as historical `t` or `k` by the later lenition series.

**2. `c > tɕ / _i`**

The `c` created before `/i/` acquires a palatalized affricate realization.

**3. `tɕ > ɕ / _i`**

The palatalized affricate subsequently deaffricates before `/i/`.

Established developments include `ruki > ruci > /ruɕi/` and `ruti > ruci > /ru(t)ɕi/`. The latter may retain a transitional stop component as a phonetic trace of historical `*t`; this is not a separate phoneme or a reversal of the historical merger.

#### Stage II — Early sequence restructuring

These changes precede the general weakening process.

**4. `p, t, k + h > pp, tt, kk`**

A stop immediately followed by `h` coalesces as a geminate stop.

Examples:

- `r-u-k-h-a > rukha > rukka`
- `r-u-t-h-a > rutha > rutta`
- `r-u-p-h-a > rupha > ruppa`

Because the stop has been restructured as a geminate, it is no longer an intervocalic singleton target for the later weakening series.

**5. `tc > c`**

Consonant-sequence simplification reduces `tc` to `c`. This belongs to the early cluster-coalescence period rather than the later lexicalized `*ndt > nt:` development.

**6. `wu > u`**

The prohibited sequence `wu` is repaired to `u`.

**7. `yi > ye`**

The prohibited sequence `yi` is repaired to `ye`. The grammatical identity of the final NONPAST marker is unchanged; `e` is the phonological repair rather than a replacement tense exponent.

Thus `ku-t-y-i > kutyi > kutye` retains `-i` as NONPAST historically.

#### Stage III — Conditioned consonant weakening

The three voiceless stops participate in one historically related weakening process, but their first-stage outcomes are consonant-specific. The stage reached is determined by the matrix in G-PHON-04.

**8. `p > h`**

**9. `t > d`**

**10. `k > g`**

The later stages are consonant-specific:

**11. `h > Ø`** in the matrix cells where `p` reaches complete loss.

**12. `g > ɣ`** in the cells where `k` reaches the fricative stage.

**13. `ɣ > Ø`** in the cells where `k` reaches complete loss.

The historical paths therefore remain:

```text
*p > h > Ø
*t > d
*k > g > ɣ > Ø
```

but each consonant reaches only the endpoint permitted by its OPEN/CLOSED × vowel-transition cell.

Established regression paths are now fully represented by the matrix:

```text
reruka > reruga > reruɣa > rerua
reruta > reruda
rerupa > reruha > rerua
rupi > ruhi > rui
ku-p-i > kupi > kuhi > kui
mente > mende
menta > menda
```

`neku`, `seku`, and `keka` also remain unchanged in the general matrix because their `k` occurs in the weak `F_B` environment. Other stable forms whose apparent modern intervocalic stop does not fit the historical exposure of the weakening layer (`apa`, `ita`, and `teta`) are retained as later lexical/structural formations rather than being created as exceptions to the sound law.

Word-initial `*p > h` is historically continuous with the broader `p` weakening but has a distinct environment from intervocalic weakening. Historical `*p` remains distinct from historical `*h`.

#### Stage IV — Generalized sonorant-cluster reduction

Complex sonorant clusters undergo late simplification with compensatory lengthening of the surviving consonant. The currently established cluster-specific outcomes are:

**14. `nm > m:`**

**15. `nr > n:`**

Thus:

```text
menme > mem:e
menra > men:a
```

These are members of a generalized historical cluster-reduction process, not lexical exceptions.

#### Stage V — Later initial-vowel reduction

**16. `a > Ø / #_dV`**

An initial unstressed `a` is lost before `d`.

Thus the established lexical chain is:

```text
*ata > ada > da
```

The later vowel-loss rule is independent of the main stop-weakening matrix and follows `t > d`.

#### Stage VI — Later lexicalized cluster reduction

**17. `*ndt > nt:`**

This is an independent later development attested in lexicalized material. It is not part of either the general weakening series or the generalized sonorant-cluster reduction, and is not established as a productive synchronic rule.

### G-PHON-06 — Historical/synchronic scope

Historical sound laws explain how modern forms arose; they are not automatically productive synchronic alternations.

Lexicalization, morphological reanalysis, analogical restoration, later grammaticalization, and other restructuring may preserve or obscure historical outputs. A modern form should not be changed merely because an older rule could have applied to an earlier stage.

The current modern lexical and example forms are retained while their historical derivations are tested against the concrete matrix.

### G-PHON-07 — Orthography and IPA

The established orthography uses `v = /w/`, `y = /j/`, and `c = /ts/`. IPA records pronunciation rather than orthographic spelling. Thus orthographic `v` is transcribed `/w/`, orthographic `y` is transcribed `/j/`, and orthographic `c` is `/ts/` unless a documented phonetic realization is being represented.

Long vowels are written doubled and transcribed with IPA length `ː` when established.

When IPA is typed on a standard keyboard, `:` may be used as the plain-text substitute for IPA `ː` for length/gemination. In morphological glossing/segmentation, `:` retains its project/Leipzig use for morphophonological or grammatical fusion.

### G-PHON-08 — Prosody

Stress is predictable rather than contrastive and is mora-weighted:

- `CV` = light (1 mora)
- `CVV` = heavy (2 morae)
- `CVC` = heavy (2 morae)
- `CVVC` = superheavy but treated as heavy for stress assignment

Stress falls on the rightmost heavy syllable. If a word contains no heavy syllable, stress falls on the penultimate syllable.

### Historical regression notes

The conditioned system replaces the previous blanket `V_V` analysis. The regression evidence now supports the concrete OPEN/CLOSED × F/F transition matrix rather than an unconditional intervocalic rule.

The principal established diagnostic cells are:

- `reruka` — OPEN `B_B`, `k > g > ɣ > Ø`
- `reruta` — OPEN `B_B`, `t > d`
- `rerupa` — OPEN `B_B`, `p > h > Ø`
- `rupi` / `ku-p-i` — OPEN `B_F`, `p > h > Ø`
- `mente` — OPEN `F_F`, `t > d`
- `menta` — OPEN `F_B`, `t > d`
- `neku`, `seku`, `keka` — weak `F_B` `k` environment, no general weakening
- `menme`, `menra` — generalized late sonorant-cluster reduction
- `ada` — later initial-vowel reduction after `t > d`

The stable forms `apa`, `ita`, and `teta` are assigned to a later lexical/structural stratum rather than being used to create exceptions to the productive historical matrix. This preserves the concrete sound laws while allowing historically opaque formations to remain stable.
