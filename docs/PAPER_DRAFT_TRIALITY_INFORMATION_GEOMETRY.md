# Triality Information Geometry: Identifiability, Multiplicity Gauges, and Exact Dirac--Gram Bounds

**Working manuscript — 2026-08-06**

## Abstract

We study experimental design for a shared unknown `Spin(8)` action observed
through the vector and two chiral-spinor representations. Every unit probe
contributes a rank-seven orthogonal projector to a 28-dimensional Fisher
information operator. We prove four linked results. First, five generic probes
spanning two triality representations identify all 28 infinitesimal action
coordinates, whereas four generic probes retain an exact three-dimensional
stabilizer. Second, the balanced orthonormal five-probe information operator
has fixed invariant blocks of dimensions `8+8+8+4`, explaining its determinant
`81/1024` and its complete one-parameter Cayley spectrum. Third, repeated
probes in one representation possess an exact multiplicity-space orthogonal
gauge: their summed information depends only on their covariance. Finally, we
prove the strengthened Dirac--Gram determinant inequality on a complete
five-variable nonorthogonal family and derive the exact eight-sector polynomial
ansatz for the next six-variable bridge. The latter bridge has passed exact
symmetry, divisibility, multidegree, and adversarial falsification gates, but
its global positivity remains open. All promoted claims have replayable exact
arithmetic certificates.

## 1. Problem

Let `G_p^(r)`, `p=1,...,28`, denote the infinitesimal generators of one of the
three real eight-dimensional triality representations

\[
r\in\{V,S^+,S^-\}.
\]

For a probe `x` define

\[
J_r(x)_{kp}=(G_p^{(r)}x)_k,
\qquad
P_r(x)=J_r(x)^T J_r(x).
\]

Given probes `(r_j,x_j)`, their information operator is

\[
I=\sum_jP_{r_j}(x_j).
\]

The central questions are:

1. How many probes identify an unknown shared `Spin(8)` action?
2. Which five-probe design maximizes `det I`?
3. Which coordinate choices are genuine geometry and which are gauge?
4. Can these structures become learnable, scan-compatible memory mechanisms?

## 2. Exact projector geometry

For every unit probe,

\[
P_r(x)^2=P_r(x),\qquad \operatorname{rank}P_r(x)=7.
\]

The same-view and cross-view overlaps are

\[
\operatorname{tr}(P_r(x)P_r(y))
=1+6\langle x,y\rangle^2,
\]

and

\[
\operatorname{tr}(P_r(x)P_s(y))=\frac74,qquad r\ne s.
\]

Thus correlations within a representation change information quadratically,
whereas different triality views are exactly isoclinic at this contraction
level.

## 3. The sharp five-probe boundary

Five generic probes spanning two triality representations give information
rank 28. Four mixed probes give rank 25 and an exact three-dimensional
stabilizer. Five probes confined to one representation also give rank 25.

The local statement is therefore sharp:

\[
\text{four probes: 3D ambiguity},
\qquad
\text{five multiview probes: zero local slack}.
\]

An explicit integral five-probe tuple has trivial global stabilizer, while a
displayed four-probe subtuple has an exact `su(2)` stabilizer. Principal-orbit
arguments then promote generic mixed five-probe identifiability beyond the
coordinate examples.

This is an identifiability theorem, not a conditioning theorem. The balanced
sensor is separately distinguished by its information spectrum.

## 4. Exact Cayley spectrum

For an orthonormal balanced allocation `(1,2,2)` across `(V,S+,S-)`, the
information operator depends on the normalized Cayley coordinate `c`. A fixed
bivector-basis permutation gives invariant coordinate blocks

\[
I(c)=I_8^{(0)}(c)\oplus I_8^{(1)}(c)
\oplus I_8^{(2)}(c)\oplus I_4(c).
\]

Their determinants are

\[
\frac{1-c^2}{4},\qquad
\frac{(1-c^2)(9-c^2)}{16},\qquad
\frac{(1-c^2)(9-c^2)}{16},\qquad 1.
\]

Hence

\[
\det I(c)=\frac{(1-c^2)^3(9-c^2)^2}{1024}.
\]

At `c=0`,

\[
\det I=\frac{81}{1024},\qquad
\operatorname{tr}I=35,qquad
\operatorname{tr}I^{-1}=43.
\]

At `|c|=1`, three information directions disappear. Cayley calibration and
information optimality are therefore different extremal problems: the
calibrated endpoint is maximally special geometrically but singular for this
estimation objective.

## 5. The strengthened Dirac--Gram inequality

Collect the four moving unit probes into `X`, put

\[
G=XX^T,qquad \Delta=\det G,qquad
c=\frac{\Phi(X)}{\sqrt\Delta},
\]

and let `Q=G^{-1/2}X`. The proposed inequality is

\[
\det I(X)\le \Delta^3\det I(Q).
\]

Equivalently,

\[
1024\Delta^2\det I(X)
\le(\Delta-\Phi^2)^3(9\Delta-\Phi^2)^2.
\]

The theorem is proved on three nested domains:

1. two exact one-correlation slices;
2. the complete signed-star family;
3. the complete variable-Cayley one-edge family with four active Gram
   correlations.

The largest proof uses common triality symmetry to reduce orientations to a
`4 x 4` group-circulant positivity problem, exact reconstruction on disjoint
rational grids, 256 direct exact holdouts, and two boundary-adapted Duffy
charts containing 1,901,250 exact Bernstein controls. The final difficult
boundary layers factor into separately certified nonnegative polynomials.

Coordinatewise removal of the remaining correlations is not monotone. An
exact rational counterexample rules out that attractive shortcut.

## 6. Multiplicity-space gauge theorem

If `m` probes use one representation and form the rows of `X`, then

\[
\sum_jP_r(x_j)_{pq}
=\operatorname{tr}(G_p^T G_q X^T X).
\]

Their information contribution depends only on the covariance `C=X^T X`.
For every `U` in `O(m)`, replacing `X` by `UX` changes nothing.

For two unit probes with correlation `rho`, the canonical gauge gives

\[
u=\frac{x+y}{\sqrt2},\qquad
v=\frac{x-y}{\sqrt2},
\]

with

\[
u\perp v,qquad \|u\|^2=1+\rho,qquad \|v\|^2=1-\rho.
\]

Correlation between repeated equal-strength probes is therefore exactly an
orthogonal-mode energy imbalance. This quotient is relevant both to sensor
design and to redundant channels in learned triality memories.

## 7. Exact amplitude theorem for the two-edge bridge

The next family has six circle pairs

\[
(a,A),(d,D),(e,E),(g,G),(i,I),(c,s).
\]

An exact twelve-coordinate sign audit combines common triality actions with
the independent sign gauge of each probe. Its induced group has order 512 and
its annihilator contains exactly eight characters. Every determinant sector
therefore has the global form

\[
S_m=s^6M_mH_m(a^2,d^2,e^2,g^2,i^2,c^2),
\]

where `M_m` is one fixed character monomial and `H_m` is an ordinary rational
polynomial.

The factor `s^6=(1-c^2)^3` is proved independently. At both Cayley boundary
branches the symbolic observation Jacobian has rank 25 and nullity 3. Every
maximal minor is order at least three in `s`; Cauchy--Binet makes the
information determinant order at least six. A two-branch quotient-ring
argument converts the analytic order into exact divisibility.

The same argument has now been checked on all ten branches of

\[
A,D,E,G,I=0.
\]

Every branch has rank 25/nullity 3. Thus

\[
A^6D^6E^6G^6I^6=\Delta^3
\]

divides the raw determinant globally, including the newly activated residual.
The normalized determinant is genuinely polynomial in the circle quotient.

The rank-seven Cauchy--Binet bound then yields conservative residual
multidegrees at most four per squared coordinate. The exact slice audit used
2,736 direct determinants: 144 polynomial slices and all 576 disjoint-node
checks passed. After forced factors are removed, all 126 nontrivial slices are
exact polynomial squares; their root degrees are at most three.

These results prove the amplitude form and degree ceiling. They do not yet
prove positivity of the eight orientation margins.

### 7.1 First exact sector

The smallest proof-safe sector, `110101`, was reconstructed independently on
two disjoint `4^6` rational grids. Their complete 243-term rational coefficient
maps agree, and 32 fresh points reproduce the original direct determinants
exactly. Its observed multidegree is `(2,2,2,2,1,1)`, below the structural
ceiling.

More unexpectedly, exact division gives

\[
H_{110101}=(1-a^2)Q_{110101},
\]

with a 162-term quotient of multidegree `(1,2,2,2,1,1)`. This converts a
slice-observed boundary multiplicity into a global identity for one complete
six-variable sector. It suggests that the remaining sectors should be reduced
by their boundary ideals before any full positivity certificate is attempted.
No sign claim is made for an individual sector, and the seven unreconstructed
sectors remain open.

The quotient also obeys a nested boundary law:

\[
Q=Q|_{i^2=c^2=0}+(1-d^2)(1-e^2)(1-g^2)R,
\]

where the base contains 42 terms and `R` is a 28-term multilinear polynomial.
Hence the two late chart coordinates enter only through the product of three
intermediate complement energies. This exact serial dependence is the main
structural lead for replacing the remaining flat tensor reconstructions by a
boundary-ideal recursion.

## 8. Connection to sequence models

Three reusable architectural principles emerge.

### Shared-family retraction

Relational constraints must be imposed on an entire token-action or address
family. Independent normalization leaves gauge slack and collisions. Joint
retraction recovered hidden Spin(8) actions and latent permutations in the
associated experiments.

### Multiplicity factoring

An eight-dimensional triality representation is a geometric carrier, not a
high-capacity superposition memory. Capacity belongs in a multiplicity factor
`R^H tensor R^8`. The new gauge theorem says this factor also contains an exact
orthogonal redundancy that should be quotiented or regularized.

### Triangular bilinear scans

Triality binding is bilinear. A feed-forward triangular coupling can be lifted
to a finite linear state and evaluated by staged associative scans, retaining
constant recurrent state. Feedback reversals cause unbounded polynomial degree
and are therefore outside the exact finite-scan class.

These principles are mathematical mechanisms. They are not yet evidence that
a Spin(8) language model beats strong delta-rule, fast-weight, or structured
state-space baselines.

## 9. Reproducibility standard

Promoted results use:

- exact rational or integer arithmetic for proof signs;
- separate numerical falsifiers that cannot promote a theorem;
- preregistered gates and explicit negative results;
- staged caches for large determinants and Bernstein charts;
- disjoint reconstruction grids and holdouts;
- SHA-256 manifests over published artifacts;
- full foundational regression tests.

The current two-edge frontier deliberately remains labelled open until full
coefficient reconstruction and positivity certification succeed.

## 10. Next theorem and next ML gate

The immediate mathematical task is staged reconstruction of the eight
polynomials `H_m` under the newly proved conservative multidegree bounds,
followed by group-circulant principal-minor or Schur positivity.

The immediate ML task, after the theorem campaign, is to impose the discovered
multiplicity gauge and shared-family retraction in the blind-action memory
harness and compare against direct slots, delta-rule memory, linear attention,
and Householder transport at matched recurrent-state and compute budgets.

## Claim boundary

Proved:

- sharp generic five-probe multiview identifiability;
- exact balanced Cayley spectrum and block mechanism;
- repeated-view covariance gauge;
- variable-Cayley one-edge Dirac--Gram theorem;
- two-edge global amplitude ansatz, `Delta^3` divisibility, and conservative
  degree ceiling.

Open:

- positivity of the complete two-edge bridge;
- the final residual and unrestricted Dirac--Gram inequality;
- nonbalanced allocation upper bounds and global five-query D-optimality;
- superiority of the resulting learned memory over matched modern baselines.
