# Variable-Cayley Two-Edge Initial Gate Results

**Date:** 2026-08-06

**Preregistration:** `SPIN8_DIRAC_TWO_EDGE_PREREGISTRATION.md`

**Exact anchor artifact:**
`../../artifacts/spin8_dirac_two_edge_anchor_20260806.json`

**CUDA falsifier artifact:**
`../../artifacts/spin8_dirac_two_edge_attack_20260806.json`

## Result in one sentence

The clean second-residual bridge passed its first three frozen gates: exact
common-triality symmetry permits eight Walsh sectors, both disjoint rational
anchors activate all eight, and a 249,152-sample plus 32-restart CUDA attack
found no violation; this advances the family to exact degree analysis but does
not prove its inequality.

## Exact sign quotient

For parameter order `(a,d,e,g,i,c)`, exact common adjoint conjugacies induce

\[
(t_1,t_2,t_1t_2,t_4,t_2t_4,t_3t_4).
\]

The induced group has eight elements. Its annihilator in the 64-character
Walsh group has exactly eight elements:

```text
000000  001101  010110  011011
100011  101110  110101  111000
```

This derivation was completed before determinant anchors were evaluated. It
proves that every other character vanishes globally on this family.

## Exact anchor reconnaissance

Two disjoint rational-circle anchors were each crossed with all 64 sign
patterns. Results:

- exact direct determinants: `128`;
- nonzero sectors at anchor 0: `8`;
- nonzero sectors at anchor 1: `8`;
- supports equal between anchors: yes;
- both supports equal the complete symmetry annihilator: yes;
- exact target margins at both anchors: strictly positive.

The artifact stores all direct rational determinants and a digest over the
rows. A test recomputes the common symmetry, rebuilds the stored support, and
directly reevaluates one displayed `28 x 28` determinant.

This does not prove that all eight sector amplitudes are generically nonzero,
but matching full support at two unrelated interior points is strong
reconnaissance for the degree audit.

## Frozen CUDA falsifier

The prospective numerical gate used the local RTX 2070 SUPER in float64:

- uniform interior samples: `200,000`;
- boundary-biased samples: `49,152` (`4,096` per signed coordinate face);
- Adam restarts: `32`;
- steps per restart: `1,000`;
- optimizer parameter cap: `0.98`.

Results:

| Search | Maximum log advantage |
|---|---:|
| Uniform random | `-0.0125707` |
| Boundary-biased | `-0.0126687` |
| Optimized | `8.04e-14` |

The optimized point returned to the known equality manifold: `a,d,g,i` were
approximately zero and the two existing residual-scale values were near
`5e-8`. The tiny positive value is below the frozen `1e-8` violation threshold
by more than five orders of magnitude and is consistent with float64 roundoff.

## Scientific status

The family has passed Gates 1--3. It has **not** passed the degree,
reconstruction, exact holdout, or global positivity gates. In particular:

- numerical non-violation is not a theorem;
- two anchor supports do not establish radical amplitude factorizations;
- no interpolation degree has been frozen yet;
- the unrestricted family still has the `h` residual beyond this bridge.

The next action is the preregistered multi-slice exact degree and amplitude
audit. Full tensor interpolation is forbidden until conservative structural
bounds and disjoint slice checks agree.
