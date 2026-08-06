# Exact Reconstruction of the Complete Two-Edge Sector Algebra

## Status

Completed on 2026-08-06 under the frozen shared-grid protocol.

This result proves the exact polynomial form of all eight orientation sectors
in the preregistered variable-Cayley, two-residual family. It also proves their
endpoint factors, a universal bridge to the already-proved one-edge theorem,
and an exact even/odd four-block reduction.

It does **not** yet prove that the eight final orientation margins are
nonnegative. The two-edge Dirac--Gram inequality therefore remains open.

## What was computed

Each rational point requires eight direct information determinants. Their
exact Walsh transform recovers all eight sectors simultaneously. The
proof-safe componentwise grid has `5^6=15,625` points.

Two disjoint grids were evaluated:

| Layer | Exact count |
|---|---:|
| Grid points | 31,250 |
| Direct 28-by-28 determinants | 250,000 |
| Independently reconstructed sector maps | 16 |
| Rational coefficients in each complete map | 6,664 |
| Fresh off-grid points | 32 |
| Fresh direct determinants | 256 |
| Fresh sector equalities | 256 |

The two complete coefficient maps are identical. Their common sector-row
digest is

```text
7d53d2d3a47a2583bb6fa124845fd6d284291e33f7b391d6223362a52c53b515
```

The verifier loads both maps, compares all coefficient rows, checks every
stored fresh equality in exact rational arithmetic, and regenerates the factor
atlas. It does not accept stored `passed` flags as proof.

## The eight exact polynomials

After the character-forced radical monomial and common Cayley factor are
removed, the residual sector polynomial is

\[
H_m(a^2,d^2,e^2,g^2,i^2,c^2).
\]

The exact reconstructed sizes are:

| Mask | Observed multidegree | Nonzero coefficients |
|---|---|---:|
| `000000` | `(3,3,3,3,3,2)` | 2,615 |
| `001101` | `(3,3,2,2,2,1)` | 666 |
| `010110` | `(3,2,2,2,2,2)` | 827 |
| `011011` | `(3,2,2,3,1,1)` | 509 |
| `100011` | `(2,3,3,3,1,1)` | 657 |
| `101110` | `(2,3,2,2,2,1)` | 524 |
| `110101` | `(2,2,2,2,1,1)` | 243 |
| `111000` | `(2,2,2,3,2,1)` | 623 |

Every observed degree lies below its predeclared structural ceiling. The old
independent `110101` reconstruction is reproduced byte-for-byte at the
coefficient-row level.

## Global endpoint-factor theorem

The endpoint factors previously seen only on one-dimensional slices now hold
as exact six-variable identities:

| Mask | Exact factors removed from `H_m` | Reduced terms |
|---|---|---:|
| `000000` | none | 2,615 |
| `001101` | `(1-a^2)(1-d^2)` | 352 |
| `010110` | none | 827 |
| `011011` | `(1-a^2)(1-d^2)(1-e^2)(1-g^2)` | 116 |
| `100011` | `(1-a^2)(1-d^2)(1-e^2)(1-g^2)` | 154 |
| `101110` | `(1-d^2)` | 392 |
| `110101` | `(1-a^2)` | 162 |
| `111000` | none | 623 |

Thus all eight prospectively recorded slice predictions were correct globally.
Exact division reduces the atlas from 6,664 to 5,241 coefficients.

## Universal flag law

Call the endpoint-reduced polynomial `Q_m`. Every sector, without exception,
satisfies

\[
Q_m=Q_m|_{i^2=c^2=0}
 +(1-d^2)(1-e^2)(1-g^2)R_m.
\]

More importantly, every sector satisfies the sharper one-edge bridge

\[
\boxed{
Q_m=Q_m|_{i^2=0}
 +i^2(1-d^2)(1-e^2)(1-g^2)T_m.
}
\]

The base `Q_m|_(i^2=0)` is exactly the variable-Cayley one-edge frame already
covered by the proved one-edge theorem. The new residual can influence the
even polynomial core only after passing through all three intermediate
complement energies `D^2 E^2 G^2`.

This is a flag law: the late coordinate is screened unless the earlier stages
of the Cholesky flag all retain transverse energy.

## Exact parity-block theorem

Four Walsh characters have no `i` sign and four contain it. Pair the eight
orientation rows by flipping only the sign of `i`. In each pair:

- all four even characters are unchanged;
- all four odd characters reverse sign;
- the even and odd sectors have the same exact `4 x 4` Hadamard table `W`.

Therefore the eight margins are exactly

\[
\lambda_{r,+}=W_r(E+O),\qquad
\lambda_{r,-}=W_r(E-O),
\]

where `E` and `O` are the four even- and odd-sector amplitude vectors. The
same statement can be phrased as positivity of two commuting `4 x 4`
group-circulants `K_+` and `K_-`.

Deleting the `i` bit from the even masks gives exactly the four Walsh
characters of the proved one-edge theorem:

```text
00000, 00111, 11011, 11100
```

At `i=0`, every odd amplitude vanishes and `K_+=K_-` becomes the one-edge
matrix. The two-edge problem is therefore an exact paired deformation of the
proved theorem, not an unrelated eight-sector positivity problem.

## What a high-school reader should picture

Imagine eight complicated answers written on eight cards. We discovered that
the cards come in four pairs. Within each pair, one part of the answer stays
the same and one part merely changes sign. Better still, the shared part is
the old problem we already solved.

The new coordinate cannot alter the shared polynomial freely. Its effect is
multiplied by four gates:

```text
i^2 (1-d^2) (1-e^2) (1-g^2).
```

If any one of those gates is zero, the new correction disappears exactly.
This is much stronger than observing a numerical pattern: every coefficient
was reconstructed twice with rational arithmetic, and the identities were
verified by exact polynomial division and recomposition.

## Scientific boundary

Proved here:

- all eight exact residual polynomials;
- their global endpoint factors;
- the universal flag-screening identity;
- the exact one-edge bridge;
- the even/odd Hadamard block reduction.

Still open:

- positive semidefiniteness of both `K_+` and `K_-` on the full six-cube;
- the final two-edge Dirac--Gram inequality;
- the third residual Cholesky edge and unrestricted Gram--Cayley theorem;
- global five-query D-optimality outside the proved families.

## Next best theorem gate

Do not attempt raw Bernstein positivity on individual sectors: exact boundary
faces already prove that some sector polynomials change sign.

The next gate is a matrix perturbation certificate. Write

\[
K_\pm=K_0\pm iL_{\mathrm{odd}}
       +i^2D^2E^2G^2L_{\mathrm{even}},
\]

with `K_0` the proved one-edge group-circulant and with the already-certified
character monomials retained inside `L_odd`. Then seek either:

1. an exact Schur-complement certificate relative to `K_0`;
2. radical-free principal-minor certificates for both signs simultaneously;
3. a sum-of-squares certificate after factoring the known one-edge boundary
   nullspaces.

The first required check is equality-kernel compatibility: the odd first-order
block must annihilate every boundary null vector of `K_0`, or else the proposed
global inequality is false near that boundary. This is a cheap exact
falsifier and should precede any large positivity run.
