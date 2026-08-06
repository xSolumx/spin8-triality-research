# Breakthrough Note: Structure and Positivity in Spin(8) Triality Sensing

**Date:** 2026-08-06

## The two results

### 1. The recurring Cayley spectrum has an exact block mechanism

For the balanced five-probe `Spin(8)` triality sensor, the 28-dimensional
information operator is exactly block diagonal after one fixed bivector-basis
permutation:

\[
I(c)=I_8^{(0)}(c)\oplus I_8^{(1)}(c)
\oplus I_8^{(2)}(c)\oplus I_4(c).
\]

The two middle blocks are conjugate by a displayed, constant signed
permutation. Their determinants, together with those of the other blocks, are

\[
\frac{1-c^2}{4},\qquad
\frac{(1-c^2)(9-c^2)}{16},\qquad
\frac{(1-c^2)(9-c^2)}{16},\qquad 1.
\]

This explains at once:

- why the characteristic polynomial has repeated factors;
- why the determinant has powers `(1-c^2)^3(9-c^2)^2`;
- why the Cayley-null value is exactly `81/1024`;
- why three information directions disappear at calibrated endpoints.

The important correction is that these are certified invariant *coordinate*
blocks. A representation-theoretic irreducibility classification under the
residual stabilizer is a promising next theorem, not something inferred from
the factorization.

### 2. The variable-Cayley one-edge inequality is proved

The strengthened Dirac--Gram inequality is now exact on the family with four
active Gram correlations and variable normalized Cayley coordinate. Common
triality symmetry reduces all orientations to a four-by-four tetrahedral
matrix. Exact positivity of its principal minors is proved over the entire
five-dimensional parameter cube.

The load-bearing final determinant has 203,978 monomials. Its certificate uses
two Duffy charts:

\[
u=t y,\quad v=t(1-y),
\qquad\text{and}\qquad
1-u=t y,\quad1-v=t(1-y).
\]

The upper chart has no negative Bernstein controls. In the lower chart, every
negative control is confined to radial layers zero and one. Those layers are
proved separately through

\[
B_0=G_0^2,
\qquad
B_1=G_0\left(G_0+\frac{G'_0}{12}\right),
\]

and exact positivity certificates for both factors. Thus all orientation
eigenvalues are nonnegative throughout the frozen family.

## Evidence standard

This promotion rests on exact arithmetic, not floating-point survival:

- two disjoint tensor grids reconstructed identical rational polynomials;
- 256 disjoint direct rational determinants match the reconstruction exactly;
- 1,901,250 chart controls were evaluated with integer arithmetic;
- the exceptional boundary layers have exact algebraic identities;
- the final artifact cryptographically links the reconstruction, determinant
  cache, holdouts, lower-order minors, and assembled acceptance predicate;
- a replay verifier recomputes the stored holdout predictions and all
  lightweight acceptance checks.

The audit also found and corrected an earlier unsupported sentence claiming
the 256 holdouts had already run. The source artifact had honestly retained
`holdouts_pending: true`; the missing experiment was run before theorem
promotion.

## Why this may be paper-worthy

The combination is stronger than either result alone. The first result reveals
the spectral anatomy of the optimal orthonormal sensor. The second proves a
nonorthogonal deformation theorem using symmetry reduction plus
boundary-adapted exact positivity. Together they form a coherent mathematical
story about how exceptional triality geometry controls experimental-design
information.

A defensible paper claim is:

> We derive an exact invariant-block factorization for the balanced Spin(8)
> triality information family and prove the strengthened Dirac--Gram bound on
> a complete variable-Cayley four-correlation family by an independently
> replayable rational Bernstein/Duffy certificate.

This is narrower—and stronger—than claiming global five-query optimality.

## The honest frontier

The work does **not** yet prove the unrestricted seven-invariant Dirac--Gram
inequality. Two residual Cholesky edges remain. It also does not prove the
nonbalanced allocation upper bounds or global D-optimality among all
five-query designs.

The next best bridge is to activate exactly one additional residual edge. Its
symmetry characters and degree bounds should be derived before interpolation.
The existing block basis should be tested first; if it reduces the new
determinant, use it. If not, preregister a boundary-adapted certificate and an
exact counterexample protocol before spending on another large expansion.

## Primary evidence

- [Cayley block theorem](experiments/SPIN8_CAYLEY_BLOCK_THEOREM.md)
- [Variable-Cayley one-edge theorem](experiments/SPIN8_DIRAC_ONE_EDGE_RESULTS.md)
- [Cayley block artifact](../artifacts/spin8_cayley_blocks_20260806.json)
- [Final Duffy certificate](../artifacts/spin8_dirac_one_edge_duffy_20260806.json)
- [Exact holdouts](../artifacts/spin8_dirac_one_edge_holdouts_20260806.json)
- [Reproducibility protocol](REPRODUCIBILITY.md)
