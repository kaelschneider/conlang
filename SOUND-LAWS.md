# Historical Sound Laws

Status: canonical. This file records the ordered relative chronology of the historical sound changes. The ordering is a project design decision grounded in the established forms and examples; it is not presented as recovered historical fact where the Git history did not previously specify an order.

`>` denotes a successive historical stage. Later rules apply to the outputs of earlier rules unless an environment explicitly limits the rule.

## Ordered chronology

### Stage I — Pre-/i/ palatalization

**1. `t, k > c / _i`**

Historical `t` and `k` become `c` before `/i/`. This change applies before the general intervocalic lenition, so a resulting `c` is not subsequently subject to `t > d` or `k > g`.

Examples:

- `ruki > ruci`
- `ruti > ruci`

**2. `c > tɕ / _i`**

The `c` created before `/i/` acquires a palatalized affricate realization.

**3. `tɕ > ɕ / _i`**

The palatalized affricate subsequently deaffricates before `/i/`.

The historical `*t` series may retain a transitional stop component in pronunciation, giving the established representation `/ru(t)ɕi/` for `ruti > ruci`. This is a phonetic realization, not a separate phoneme or a reversal of the historical merger.

### Stage II — Early sequence restructuring

These changes precede the general intervocalic lenition.

**4. `p, t, k + h > pp, tt, kk`**

A stop immediately followed by `h` coalesces as a geminate stop.

Examples:

- `r-u-k-h-a > rukha > rukka`
- `r-u-t-h-a > rutha > rutta`
- `r-u-p-h-a > rupha > ruppa`

Because the stop is absorbed into a geminate at this stage, it is no longer an intervocalic singleton target for the later lenition rules.

**5. `tc > c`**

Consonant sequence simplification reduces `tc` to `c`. This belongs to the same early cluster-coalescence period as `STOP+h` fusion, rather than to the later `*ndt > nt:` development.

**6. `wu > u`**

The prohibited sequence `wu` is repaired to `u`.

**7. `yi > ye`**

The prohibited sequence `yi` is repaired to `ye`. The grammatical identity of the final NONPAST marker is unchanged; `e` is the phonological repair, not a replacement tense exponent.

Thus `ku-t-y-i > kutyi > kutye` is a consequence of the general sequence repair.

### Stage III — Intervocalic lenition

A single historical weakening process affects intervocalic voiceless stops with consonant-specific outcomes.

**8. `p > h / V_V`**

This is historically continuous with the established word-initial `*p > h` development; the project treats the two environments as manifestations of the same general `p > h` weakening. Historical `*p` remains distinct from historical `*h` even where their modern reflexes overlap.

Examples:

- `rupi > ruhi`
- `rerupa > reruha`
- `ku-p-i > kupi > kuhi`

**9. `t > d / V_V`**

Examples:

- `reruta > reruda`
- `mente > mende`
- `menta > menda`

**10. `k > g / V_V`**

Example:

- `reruka > reruga`

**11. `g > ɣ / V_V`**

The voiced dorsal stop produced by the preceding rule continues weakening to a voiced velar/uvular fricative.

Example:

- `reruga > reruɣa`

**12. `h, ɣ > Ø / V_V`**

Intervocalic fricatives are subsequently lost.

Examples:

- `ruhi > rui`
- `reruha > rerua`
- `reruɣa > rerua`
- `kuhi > kui`

### Stage IV — Later lexicalized cluster reduction

**13. `*ndt > nt:`**

This is an independent later historical development attested in lexicalized material. It is not treated as part of the general intervocalic lenition process and is not established as a productive synchronic rule.

## Resulting major pathways

The ordered system yields the following principal consonant histories:

```text
*p > h > Ø        in leniting environments
 t > d            intervocalically
 k > g > ɣ > Ø    intervocalically
 t > c > tɕ > ɕ   before /i/
 STOP+h > geminate STOP
```

The asymmetry is intentional: the three stops participate in the same historical weakening process, but their trajectories diverge after the initial weakening.

## Regression set

The following forms should continue to derive without introducing ad hoc lexical exceptions:

```text
reruka > reruga > reruɣa > rerua
reruta > reruda
rerupa > reruha > rerua

ruki > ruci > /ruɕi/
ruti > ruci > /ru(t)ɕi/
rupi > ruhi > rui

r-u-k-h-a > rukha > rukka
r-u-t-h-a > rutha > rutta
r-u-p-h-a > rupha > ruppa

ku-p-i > kupi > kuhi > kui
mente > mende
menta > menda
```

## Scope and maintenance

These are historical sound laws, not unrestricted synchronic alternations. A modern form should not be altered merely because a historical rule could have applied to an earlier stage. Lexicalization, morphological boundaries, analogical replacement, and later restructuring may block or obscure historical developments.

Where a new form requires a contradiction of this chronology, the analysis should be recorded in `STATUS.md` rather than silently modifying an existing law.
