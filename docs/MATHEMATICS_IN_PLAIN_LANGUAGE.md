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

## Why five probes can determine the whole action

The older experiment checked a local question: if we nudge the unknown action
by a tiny amount, do five measurements detect every possible nudge? They did.
That still left a loophole: perhaps a completely different, far-away action
could give the same five answers.

Triality closes that loophole for one exact arrangement. Start with one vector
probe and four spinor probes. Whenever two known objects are combined by the
triality multiplication rule, the result must also be fixed by any action that
fixed the original probes. Repeating this rule is like solving a Sudoku: every
known entry forces more entries.

For the exact probes

```text
vector:          e0
positive spinor: e0, e1, e2, e4
```

the forced vectors eventually form a complete basis of all three
eight-dimensional triality spaces. Each exact basis determinant is `-1`, so
none of the directions is missing. An action fixing the five original probes
must therefore fix every basis vector, meaning it is globally the identity.

Remove `e4` and the closure stops at four dimensions in each space. Three
independent rotations remain completely invisible. Their exact commutators are
those of `su(2)`, so this is a continuous family of wrong answers, not rounding
error or failed training.

This proves a global five-versus-four separation for the displayed probes.

There are 70 ways to choose four coordinate spinors. The exact program checked
all of them. Fifty-six choices force all eight directions. Fourteen choices get
stuck in four dimensions. Those fourteen are the blocks of a famous binary
error-correcting code: the extended Hamming `[8,4,4]` code. Every set of three
coordinates belongs to exactly one exceptional block.

This does not mean the memory is performing error correction. It means the
geometry of the exceptional probe choices has the same exact combinatorial
pattern as that code.

The larger pattern is now known for every coordinate probe. Give the three
triality spaces three different two-bit labels and each of their eight
coordinates a three-bit label. Every coordinate probe then has a five-bit
barcode. Triality multiplication combines barcodes by XOR: a switch is on in
the answer exactly when it was on in one input but not both.

The exact program checked all 52,752 multiview coordinate choices of four or
five probes. Four barcodes can span at most four independent binary directions,
so none sees the whole five-dimensional barcode space. Five probes see it all
exactly when their five barcodes are independent. The remaining invisible
continuous symmetry has dimension 8, then 3, then 0 as binary rank rises from
3 to 4 to 5. Exact bracket and Killing-form checks identify these stages as
`SU(3)`, `SU(2)`, and no continuous stabilizer.

This completely classifies the coordinate case. Arbitrary non-coordinate
probes form a continuous problem. That orbit theorem is now also proved.

Every way of distributing four probes among the three views has at least three
independent relationship measurements that Spin(8) cannot change. Those
relationships force at least three invisible rotation directions. Exact
representatives show the bound is sharp, and the compact principal-orbit
theorem guarantees that unusual probe choices can only have more symmetry,
never less. Thus no four-probe arrangement works, coordinate or continuous.

For five probes, the exact coordinate atlas supplies a zero-ambiguity example
in every allocation that uses at least two views. Compact orbit theory then
says zero ambiguity holds on an open dense set: almost every such mixed design
works globally. Five probes in only one view still leave three rotations
unseen.

## How bilinear memory can remain parallel

Suppose two recurrent streams are updated independently. After both have been
computed, combine their current states with any bilinear rule and use that as
the input to a third recurrent stream. Each layer is still an ordinary affine
scan, so the construction needs two parallel scan stages and a fixed recurrent
state.

An exact proof adds the product of the two source states as temporary
coordinates. Those product coordinates make the whole update one linear
matrix multiplication. They are a proof device, not part of the streaming
cache.

The arrow direction matters. If the third stream feeds back into one source,
the polynomial degree grows forever. If it feeds both sources, the degree
doubles at every step. So triangular coupling is not an arbitrary engineering
choice; it is the boundary that preserves a finite exact scan.

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
| Five generic multiview probes identify 28 local action dimensions | Exact differential rank |
| Displayed five-probe tuple has no global ambiguity | Proved exactly |
| Displayed four-probe subset has an `su(2)` ambiguity | Proved exactly |
| All multiview coordinate four/five-probe closures follow `F_2^5` span | Exhaustively proved |
| Every continuous four-probe sensor is insufficient | Proved by invariants and principal orbits |
| Every mixed five-probe allocation is generically globally free | Proved |
| Generic triangular bilinear drive has a finite exact staged scan | Constructively proved |
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
