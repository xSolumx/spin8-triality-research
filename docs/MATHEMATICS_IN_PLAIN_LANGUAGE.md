# The Mathematics in Plain Language

This chapter explains the current Dirac--Gram and triality results without
assuming advanced university mathematics. It distinguishes carefully among
four kinds of conclusion:

- theorems proved for an entire continuous family;
- finite classifications verified exhaustively;
- numerical searches that found no counterexample;
- conjectures that remain open.

## The basic question

A transformation in \(\operatorname{Spin}(8)\) has 28 local degrees of freedom.
Imagine trying to identify such an unknown transformation using only five
carefully chosen probes. Each probe reveals part of the action. The design
problem is to choose probes whose information overlaps as little as possible,
so that together they distinguish all nearby transformations.

The balanced \(\operatorname{Spin}(8)\) arrangement has the information score

\[
\det I=\frac{81}{1024}.
\]

The determinant is a local volume measure. A large value means that nearby
transformations produce clearly distinguishable measurements. A zero value
means that at least one infinitesimal direction of motion is completely
invisible.

The value \(81/1024\) now has a direct structural explanation. At the balanced
point, the 28-dimensional information operator separates into four independent
blocks. Their determinant contributions are

\[
\frac14,\qquad\frac9{16},\qquad\frac9{16},\qquad1.
\]

Therefore

\[
\det I
=\frac14\cdot\frac9{16}\cdot\frac9{16}\cdot1
=\frac{81}{1024}.
\]

The two factors \(9/16\) arise from blocks related by a fixed signed-permutation
symmetry, so their equality is forced rather than accidental. At either
calibrated endpoint of the Cayley parameter, one eigenvalue in each of three
blocks vanishes. This is why the observation map loses exactly three ranks.

## Why perpendicular probes are the natural benchmark

Let the four probe vectors be the rows of \(X\). Their Gram matrix is

\[
G=XX^{\mathsf T}.
\]

The entries of \(G\) are the pairwise inner products of the probes. If the rows
are orthonormal, then \(G=I_4\) and \(\det G=1\). As the probes become
correlated, the volume of the parallelepiped they span decreases, so \(\det G\)
decreases. If one probe becomes redundant, \(\det G=0\).

The Dirac--Gram conjecture says that correlation cannot secretly improve the
information score after the natural volume penalty is included:

\[
\det I(X)\leq \det(XX^{\mathsf T})^3\det I(Q).
\]

Here \(Q\) is the orthonormal frame obtained from \(X\) by removing this purely
geometric distortion. The exponent 3 is not an adjustable penalty: it is the
order forced by the rank-loss geometry when one probe becomes redundant and
three independent observation directions disappear.

## The repeated-sensor gauge

The next bridge correlates two probes in the same triality representation. At
first this appears to introduce a new geometric degree of freedom, but part of
it is only a choice of coordinates.

Place the two probe vectors in a two-row matrix \(X\). Their combined
information depends only on the covariance \(X^{\mathsf T}X\). Replacing \(X\)
by \(UX\), where \(U\in O(2)\) mixes the two rows, leaves that covariance—and
therefore the information operator—unchanged.

If the two unit probes have inner product \(r\), their normalized sum and
difference directions are orthogonal, with squared weights \(1+r\) and
\(1-r\). Thus two correlated, equally weighted probes are exactly equivalent
to two orthogonal modes with unequal weights.

This does not prove the next inequality. It identifies the right variables:
the proof should use a rank-two covariance and its energy split, rather than
carry a redundant choice of sensor labels through a much larger polynomial.

## What has been proved

The inequality is proved for three increasingly large continuous families:

1. the signed star family, with three active correlations;
2. the Cayley-null edge family, with four active correlations;
3. the variable-Cayley one-edge family, which keeps those four correlations
   while allowing the Cayley angle to vary.

The proof layers are described later. In brief, rational reconstruction and
off-grid determinant identities establish the target polynomials, while
Bernstein certificates establish their signs throughout the relevant
continuous parameter boxes. These are theorem certificates, not conclusions
drawn from a dense floating-point sample.

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
eight-dimensional triality spaces. Each basis determinant is \(-1\), so none
of the directions is missing. Any compatible \(\operatorname{Spin}(8)\) action
that fixes the five probes must also fix everything generated from them by
triality multiplication. Because that closure contains a basis in all three
representations, the action is the identity in each representation and has no
residual group ambiguity.

Remove `e4` and the closure stops at four dimensions in each space. Three
independent rotations remain completely invisible. Their exact commutators are
those of `su(2)`, so this is a continuous family of wrong answers, not rounding
error or failed training.

This proves a global five-versus-four separation for the displayed probes.

There are 70 ways to choose four coordinate spinors. Finite enumeration checks
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

The finite coordinate atlas contains 52,752 multiview choices of four or five
probes, all of which were enumerated. Four barcodes can span at most four
independent binary directions,
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

For five probes, the coordinate atlas supplies a trivial-stabilizer example in
every allocation that uses at least two views. Compact orbit theory then says
that a trivial stabilizer occurs on an open dense set: almost every such mixed
design works globally. Five probes in only one view still leave three rotations
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

## The completed one-edge gate

The next family allows the Cayley angle to vary as well. Exact symmetry reduces
sixteen possible sign choices to four polynomial sectors. Those four numbers
are the eigenvalues of a symmetric 4 by 4 matrix. Proving the matrix is
positive is equivalent to proving every sign choice at once.

The lower-order matrix tests are proved. The difficult final test was the
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

The exact replay confirmed that every difficult control lives in the first two
distance layers. Those layers factor into already nonnegative pieces. All
layers from 2 through 24 are exactly nonnegative, and the complementary
triangle has no negative controls at all. The variable-Cayley theorem is
therefore proved on this whole family.

## From the gauge to the second residual edge

The first boundary factor of that proof is now exact. When the Cayley angle
reaches either endpoint, the observation system loses exactly three ranks.
That forces its information determinant to vanish with six powers of the
distance from the endpoint. In formulas, every orientation sector contains
`(1-c^2)^3`. The same factor occurs in the proposed upper bound, so it can be
cancelled before tackling the remaining polynomial.

There is also an exact reason that the remaining square roots fit together.
When every signed coordinate and every circle complement is audited together,
the 4,096 possible sign patterns collapse to a 512-element gauge group with
only eight allowed polynomial characters. Each visible orientation sector has
one unique hidden complement parity. Thus every apparent radical is a fixed
front factor; what remains is an ordinary polynomial in six squared numbers.

The first of those eight polynomials has now been recovered completely. Two
different exact 4-by-4-by-4-by-4-by-4-by-4 grids gave the identical rational
formula, and 32 new points matched calculations made directly from the
original matrices. The safe degree bound allowed 4,096 coefficient positions;
only 243 were used.

Then the formula revealed two extra pieces of structure. First, all 243 terms
share the factor `1-a^2`, reducing the real core to 162 terms. Second, every
term in which either of the last two coordinates appears also contains

```text
(1-d^2)(1-e^2)(1-g^2).
```

After removing that product, only a 28-term formula remains, and it is linear
in every squared coordinate. The subsequent complete reconstruction found the
same screening rule in **all eight** sectors. In everyday language:
information added late in this triangular coordinate chain can affect the
even polynomial core only if every intermediate direction is still available.
This is an exact dependency law, not a numerical correlation.

There is an even simpler picture. The eight sign cases form four pairs. In
each pair, flipping the new coordinate leaves four ingredients alone and
reverses the other four. The unchanged half is exactly the earlier one-edge
problem that has already been proved. So the new theorem problem is two
four-by-four blocks built as controlled deformations of a solved case—not
eight unrelated monsters.

The first danger point has also been settled. Starting from four perfectly
orthogonal probes, turning on the new correlation always makes the determinant
smaller, never larger. After exact simplification the difference is a positive
two-variable polynomial whose nine Bernstein coefficients are all positive;
the smallest is still `103`. Other exceptional boundary arrangements remain
to be checked.

On two outer faces, the remaining 162-term formula collapses to products of
only a few simple factors. One face is always nonpositive and another is always
nonnegative. That catches a tempting but wrong proof plan: the eight internal
sign components do not each need to be positive. They are like ingredients
with positive and negative flavors; only the eight final orientation totals
must be nonnegative.

## The second edge: what is now exact

The first one-edge theorem has a line of equality: a family of perfectly
balanced arrangements where the upper bound is attained. Before attempting a
global proof with a second correlation, we asked the most dangerous local
question. Could an arbitrarily small second edge tip one of the zero margins
below zero?

The exact answer is no along the entire orthonormal equality line. Almost
everywhere, the margin curves upward quadratically. At one Cayley endpoint a
single direction is quadratically flat, but the exact fourth-order term is

\[
64s^2(2-s^2),
\qquad 0<s\leq1,
\]

which is strictly positive. In geometric language, the apparent flat floor is
not another hidden equality corridor; a finer measurement shows that it rises.

A plausible quadratic shortcut nevertheless fails away from that equality
line. An exact rational example makes its proposed auxiliary expression
negative. This does not disprove the target inequality. It tells us that the
full finite-edge dependence, rather than only its first two derivatives, is
essential.

That full dependence has now been simplified exactly. If \(i\) is the new edge,
set

\[
x=i^2,\qquad y=\sqrt{1-x},\qquad 0\leq y\leq1.
\]

Each pair of signed answers becomes

\[
m_\pm=L(y)\pm\sqrt{1-y^2}\,R(y).
\]

The two answers are both nonnegative exactly when their midpoint is
nonnegative and their half-separation is no larger than that midpoint:

\[
m_+\geq0\ \text{and}\ m_-\geq0
\quad\Longleftrightarrow\quad
L(y)\geq\sqrt{1-y^2}\,\lvert R(y)\rvert.
\]

Because both sides of the right-hand inequality are then nonnegative, squaring
is reversible. Hence the condition is equivalent to

\[
L(y)\geq0,
\qquad
L(y)^2-(1-y^2)R(y)^2\geq0.
\]

The first expression has degree six in \(y\); the second has degree twelve.
Thus a nested-radical, eight-sign problem has become eight ordinary polynomial
sign problems. This conversion is an exact algebraic identity. A GPU search
over 851,968 interior and boundary samples found no negative value, but the
global signs of those polynomials remain open until an exact positivity
certificate is built.

## Why the crashes did not count as evidence

A computer stopping does not make a theorem true or false. The new replay tool
splits the calculation into five stages and links them with SHA-256 hashes. A
completed stage can be checked and reused after a restart. The GPU is used only
to search quickly for counterexamples. The final signs came from exact CPU
integer arithmetic.

## Honest scoreboard

| Claim | Status |
|---|---|
| Balanced sensor invariants \(81/1024\), \(35\), and \(43\) | Computed by symbolic identity |
| Five generic multiview probes identify 28 local action dimensions | Proved locally by full differential rank |
| Displayed five-probe tuple has trivial stabilizer | Proved |
| Displayed four-probe subset has an \(\mathfrak{su}(2)\) stabilizer | Proved |
| All multiview coordinate four/five-probe closures follow \(\mathbb F_2^5\) span | Exhaustively verified over the finite coordinate atlas |
| Every continuous four-probe sensor is insufficient | Proved by invariants and principal orbits |
| Every mixed five-probe allocation is generically globally free | Proved |
| Generic triangular bilinear drive has a finite exact staged scan | Constructively proved |
| Signed star Dirac--Gram inequality | Proved |
| Cayley-null four-correlation edge inequality | Proved |
| Removing residual correlations is always helpful | Disproved |
| Variable-Cayley one-edge inequality | Proved |
| Repeated-view covariance gauge | Proved by symbolic identity |
| Common two-edge Cayley boundary factor \((1-c^2)^3\) | Proved by symbolic factorization |
| All eight two-edge sector polynomials and endpoint factors | Reconstructed and verified in exact arithmetic |
| Universal two-edge flag law and paired four-block reduction | Proved by symbolic identity |
| Two-edge stability transverse to the orthonormal equality line | Proved |
| Finite two-edge radical-to-polynomial reduction | Proved |
| Degree-six and degree-twelve finite two-edge gates are globally nonnegative | Open; no violation in 851,968 sampled points |
| Balanced five-query sensor is a strict local optimum after removing rotations | Proved |
| All 35 one-camera coordinate-circle deformations | Proved |
| Equal balanced sensor is best with fractional measurement weights | Disproved by exact counterexample |
| Eight-probe isotropic approximate design is globally best | Proved |
| 24 coloured sensors are spectrally optimal as an ordinary subspace packing | Disproved by exact comparison |
| 24 coloured sensors attain the chordal simplex bound | Disproved by exact comparison |
| 24 coloured sensors are chordally optimal | Open; missing the bound is not a proof |
| Variable-Cayley two-edge inequality | Open; block positivity remains |
| Unrestricted seven-parameter inequality | Open |
| Global best possible five-query design | Open |

The central methodological result is a proof strategy rather than a single
determinant value: exploit triality symmetry before expanding signs, use exact
rank loss to predict determinant factors, and replace ordinary box coordinates
with boundary-adapted charts when positivity is concentrated near a singular
face.
