# Variable-Cayley One-Edge Reconstruction Results

**Date:** 2026-08-04

**Protocol:** `SPIN8_DIRAC_ONE_EDGE_PREREGISTRATION.md`

**Protocol history:** `SPIN8_DIRAC_ONE_EDGE_PROTOCOL_HISTORY.md`

## What passed

- The exact common-triality sign group has Walsh annihilator
  `{1,egc,adgc,ade}`.
- A frozen 200,000-sample, 32-restart float64 CUDA attack found no violation.
  Optimization converged to the known orthonormal equality line; this is a
  falsifier pass, not a theorem.
- Two disjoint exact `4 x 4 x 4 x 4 x 6` grids recovered directly identical
  coefficient maps.
- The recovered multidegrees are exactly
  `F=(3,3,3,3,5)`, `H1=(2,2,2,2,1)`, `H2=(1,2,2,2,1)`, and
  `H3=(2,2,2,3,1)`.
- Term counts are respectively `1220`, `101`, `78`, and `192`.

The reconstruction artifact is
`../../artifacts/spin8_dirac_one_edge_exact_20260804.json`, SHA-256
`2f69dac6c572a7f001bfe29b16dedc04fe91e51dfa18ed8397c54ec3f2ad73e4`.

## Positivity gate: narrowed to one exact replay

Writing `x=T-F`, native exact Bernstein positivity passes for `x`,
`x^2-Q^2`, and `x^2-R^2`. It fails as a certificate for `x^2-P^2` with only
two negative controls, the worst `-16/27`. This does not falsify the
inequality.

Exact subdivision first certified the complete half-cube `z<=1/2` and three of
four `(r,w)` half-boxes for `z>=1/2`. The unresolved region was

\[
r,w\in[0,1/2],\qquad z\in[1/2,1],
\]

and every original negative control lay in the `u=v=0` layer. Recursive boxes
tracked toward `r=w=0` without terminating. This was a basis problem, not a
counterexample.

On that face, the polynomial is symmetric in `r,w` and depends on them only
through `s=r+w` and `p=rw`. Two exact cube charts cover the complete feasible
`(s,p)` region. Their Bernstein tensors have zero negative coefficients:

- `r+w<=1`: 51 boundary zeros, minimum positive `64/7`;
- `r+w>=1`: no zeros, minimum `2809/4`.

Together with the nonnegative off-face controls, this proves
`x^2-P^2>=0` on the full five-cube.

After removing the exact `(1-z)^9` factor, the cubic principal minor has only
three negative native controls, all on `u=v=0`. There it factors as

\[
C_3=X(X^2-P^2),
\]

so `X>=0` and the proved first minor prove the complete cubic minor.

The final determinant, after removing `(1-z)^12`, has 203,978 monomials and
only 21 negative native controls. The exact decomposition

\[
D_4=(X^2-P^2)^2+uvK
\]

does not close the proof: `K` has 116,846 negative native Bernstein controls.
That certificate basis is therefore rejected.

A better Duffy chart writes `u=t y` and `v=t(1-y)`. A float64 discovery screen
found negative controls only in radial layers zero and one; all layers 2--24
were positive. Those first two layers have exact identities

\[
B_0=G_0^2,
\qquad
B_1=G_0\left(G_0+\frac{G'_0}{12}\right).
\]

The first factor is the proved symmetric face. The second factor has an exact
Bernstein tensor with zero negatives, ten boundary zeros, and minimum positive
coefficient `256/9`. The complementary triangle
`1-u=t y, 1-v=t(1-y)` also had no negative controls in the discovery screen.

The proof is not yet promoted because repeated system crashes interrupted the
full exact integer replay of the two roughly 950,000-control chart tensors.
`spin8_dirac_one_edge_positivity.py` now splits this replay into restartable
determinant, lower-chart, upper-chart, boundary, and assembly stages.

## Scientific status

This is now an exact reconstruction, an exact proof of every lower-order
tetrahedral minor, and a sharply localized determinant candidate. It is
**not** yet the variable-Cayley one-edge theorem: the final chart layers were
screened numerically but have not completed their exact integer replay. The
Cayley-null edge theorem remains proved; the unrestricted Gram--Cayley
inequality and global five-query D-optimality remain open.
