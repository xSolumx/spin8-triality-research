# The Mathematics in Plain Language

This page explains the newest Dirac--Gram results without assuming university
mathematics. It also separates what is proved from what is still being tested.

## The basic question

Imagine trying to work out an unknown 28-number rotation by shining five
carefully chosen flashlights at it. Each flashlight gives some information. We
want five directions that reveal as much as possible without repeating one
another.

The balanced Spin(8) arrangement has the information score

\[
\det(I)=81/1024.
\]

The determinant is a volume score. If it is large, the measurements distinguish
many nearby possibilities. If it is zero, at least one direction is completely
invisible.

## Why perpendicular probes look special

Four unit vectors have a Gram matrix. Its entries are their pairwise dot
products. Perpendicular vectors have dot product zero, so a perfectly
orthogonal frame has Gram determinant one. Correlated or nearly repeated
vectors have a smaller Gram determinant.

The Dirac--Gram conjecture says that correlation cannot secretly improve the
information score after the natural volume penalty is included:

\[
\det I(X)\leq \det(XX^T)^3\det I(Q).
\]

Here `X` is a possibly correlated frame and `Q` is its orthonormal version. The
cube appears because three independent directions of information disappear
when a probe becomes redundant.

## What has been proved

The inequality is proved exactly for two increasingly large families:

1. the signed star family, with three active correlations;
2. the Cayley-null edge family, with four active correlations.

"Exactly" means the proof uses rational numbers and polynomial identities, not
rounded decimals. Two separate rational grids reconstructed the same
polynomials. Exact off-grid tests agreed with direct determinants. Bernstein
coefficients then proved that the relevant polynomials never become negative
inside the whole parameter box.

## A proof idea that failed

It was tempting to simplify a general correlated frame by turning off three
extra correlations one at a time. An exact rational counterexample shows that
this can make the normalized information score *smaller* by a factor of about
3.2168.

This does not disprove the main inequality. It disproves only that shortcut.
The lesson is simple: correlations interact, so removing them one by one can
move information around before it removes it.

## The current one-edge frontier

The next family allows the Cayley angle to vary as well. Exact symmetry reduces
sixteen possible sign choices to four polynomial sectors. Those four numbers
are the eigenvalues of a symmetric 4 by 4 matrix. Proving the matrix is
positive is equivalent to proving every sign choice at once.

The lower-order matrix tests are now proved. The difficult final test is the
determinant of that 4 by 4 matrix.

In ordinary cube coordinates its polynomial has 257,049 Bernstein controls and
only 21 are negative. A negative control is not a negative function value; it
means that particular coordinate net is too loose to prove positivity.

The useful change of coordinates is

\[
u=t y,\qquad v=t(1-y).
\]

Think of `t` as distance from a corner and `y` as the direction used to leave
the corner. This is called a Duffy chart. It separates "how far" from "which
way", exactly where ordinary boxes kept zooming forever.

The screen found that every difficult control lives in the first two distance
layers. Those layers factor into already nonnegative pieces. The other 23
layers and the complementary triangle screened positive. This is strong
evidence and a clear proof plan, but the million-control exact integer replay
has been interrupted by system crashes. Therefore the variable-Cayley theorem
is still labelled open.

## Why the crashes do not count as evidence

A computer stopping does not make a theorem true or false. The new replay tool
splits the calculation into five stages and links them with SHA-256 hashes. A
completed stage can be checked and reused after a restart. The GPU is used only
to search quickly for counterexamples. Final signs must come from exact CPU
integer arithmetic.

## Honest scoreboard

| Claim | Status |
|---|---|
| Balanced sensor invariants `81/1024`, `35`, and `43` | Exact |
| Five generic multiview probes identify 28 action dimensions | Exact |
| Signed star Dirac--Gram inequality | Proved |
| Cayley-null four-correlation edge inequality | Proved |
| Removing residual correlations is always helpful | Disproved |
| Variable-Cayley one-edge inequality | Final exact replay open |
| Unrestricted seven-parameter inequality | Open |
| Global best possible five-query design | Open |

The central discovery is not merely a number. It is a method: use common
triality symmetry to shrink the sign problem, exact rank loss to predict the
right determinant factors, and boundary-adapted coordinates when ordinary
boxes hide a nonnegative boundary.
