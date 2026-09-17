# Phonology

Status: canonical where stated; unresolved conditions remain in `STATUS.md`.

## G-PHON — Phonology

### G-PHON-01 — Syllable structure

Surface syllable structure is `(C)V(C)`. Productive onset clusters are not established. Complex sequences may arise historically or morphologically and subsequently reduce or fuse.

For historical conditioning, **OPEN** means a syllable of shape `CV`; **CLOSED** means a syllable of shape `CVC`. The distinction is structural and is not specific to any one coda consonant. Historical syllabification determines which syllable is relevant in a given sound-law environment.

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

The four classes participate in historical conditioning. `F_F` and `B_B` are the stronger lenition class in the current working model; `F_B` and `B_F` are intermediate. This does not by itself determine the outcome of every consonant in every syllable configuration.

### G-PHON-03 — Consonants

The synchronic consonant inventory is `/p t k c m n s h w j r/`. In the established orthography, `c` represents `/ts/`, `v` represents `/w/`, and `y` represents `/j/`.

Conditioned phonetic realization is not exhaustively specified. Historical-source distinctions may survive as phonetic traces without creating additional synchronic phonemes.

### G-PHON-04 — Historical conditioning framework

The principal historical weakening system is conditioned by the interaction of:

1. syllable structure (**OPEN / CLOSED**), and
2. the neighboring-vowel transition class (**F_F / F_B / B_F / B_B**).

These factors jointly shape the outcome. Closure is not a universal on/off switch for lenition; its effect is environment-specific.

The four vowel-transition classes provide a relative lenition hierarchy, while individual consonants follow consonant-specific trajectories after a common initial weakening process.

The exact outcome of every OPEN/CLOSED × F_F/F_B/B_F/B_B cell remains under corpus testing and should not be filled in by analogy alone.

### G-PHON-05 — Historical sound laws and relative chronology

`>` denotes a successive historical stage. Later rules apply to the outputs of earlier rules unless an environment explicitly limits the rule. The relative chronology below is a project design decision grounded in established forms and the current regression set; it is not claimed to be recovered historical fact where earlier project history did not specify the ordering.

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

The three voiceless stops participate in one historically related weakening process, but their first-stage outcomes are consonant-specific:

**8. `p > h`**

**9. `t > d`**

**10. `k > g`**

These first-stage outcomes are then subject to further consonant-specific weakening where the OPEN/CLOSED and vowel-transition environment permits it:

**11. `g > ɣ`**

**12. `h, ɣ > Ø`**

The historical path therefore includes:

```text
*p > h > Ø
*t > d
*k > g > ɣ > Ø
```

but the actual endpoint is conditioned by the relevant syllable structure and vowel transition. The old blanket rule `C > ... / V_V` is superseded by this conditioned framework.

Word-initial `*p > h` is historically continuous with the broader `p` weakening but has a distinct environment from the intervocalic development. Historical `*p` remains distinct from historical `*h` despite overlap in their modern reflexes.

Established regression paths remain compatible with the framework when their environments permit the indicated endpoint, for example:

```text
reruka > reruga > reruɣa > rerua
reruta > reruda
rerupa > reruha > rerua
rupi > ruhi > rui
ku-p-i > kupi > kuhi > kui
mente > mende
menta > menda
```

#### Stage IV — Later lexicalized cluster reduction

**13. `*ndt > nt:`**

This is an independent later development attested in lexicalized material. It is not part of the general weakening series and is not established as a productive synchronic rule.

### G-PHON-06 — Historical/synchronic scope

Historical sound laws explain how modern forms arose; they are not automatically productive synchronic alternations.

Lexicalization, morphological reanalysis, analogical restoration, later grammaticalization, and other restructuring may preserve or obscure historical outputs. A modern form should not be changed merely because an older rule could have applied to an earlier stage.

In particular, established modern forms are not to be rewritten until the conditioned sound-law matrix has been tested against the complete corpus.

### G-PHON-07 — Orthography and IPA

The established orthography uses `v = /w/`, `y = /j/`, and `c = /ts/`. IPA records pronunciation rather than orthographic spelling. Thus orthographic `v` is transcribed `/w/`, orthographic `y` is transcribed `/j/`, and orthographic `c` is `/ts/` unless a documented phonetic realization is being represented.

Long vowels are written doubled and transcribed with IPA length `ː` when established.

When IPA is typed on a standard keyboard, `:` may be used as the plain-text substitute for IPA `ː` for length/gemination. In morphological glossing/segmentation, `:` retains its project/Leipzig use for morphophonological or grammatical fusion.

### G-PHON-08 — Prosody

Stress is predictable rather than contrastive and weight-sensitive: stress falls on the rightmost heavy syllable; if there is no heavy syllable, stress falls on the penultimate syllable. The exact definition of heavy remains unresolved, including the interaction of vowel length and coda weight. IPA stress marks should not be added to lexical entries until the relevant stress assignment is established.

## Historical regression notes

The current conditioned system was prompted by corpus regression against the existing `LEXICON.tsv` and `EXAMPLES.tsv`. The regression showed that a blanket `V_V` rule would overgenerate changes in established forms and that the historical environment must instead track syllable openness/closure and the F/B transition class.

The following issues remain diagnostic rather than silently repaired:

- possible historical erosion of forms such as `apa`, `ita`, `teta`, and `keka` under a blanket rule;
- apparent interactions with grammatical forms such as `neku`, `seku`, and `kerande-te`;
- the separate later reduction `ada > da`, which still requires placement in the chronology;
- exact modern IPA consequences of the pre-/i/ `c > tɕ > ɕ` pathway in established forms.

These are to be resolved from the conditioned historical environment rather than by weakening or exception-listing the core sound changes.