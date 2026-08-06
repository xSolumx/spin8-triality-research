# Exact Cayley Block Theorem

**Date:** 2026-08-06

**Status:** exact post-extraction theorem certificate

**Harness:** `src/spin8_cayley_blocks.py`

**Raw certificate:** `artifacts/spin8_cayley_blocks_20260806.json`

## Result in one sentence

The recurring degree-28 Cayley information polynomial is not an opaque
computer-algebra factorization: in the maintained bivector basis the complete
one-parameter information family has four constant invariant coordinate
blocks of dimensions `8 + 8 + 8 + 4`, two of the eight-dimensional blocks are
exact signed-permutation twins, and their four determinants multiply to

\[
\frac{(1-c^2)^3(9-c^2)^2}{1024}.
\]

## The exact split

For the balanced representative

\[
(v;p_1,p_2;n_1,n_2)
=(e_0;e_0,e_1;e_2,c e_3+s e_4),
\qquad c^2+s^2=1,
\]

construct the exact `28 x 28` information matrix `I(c,s)`. Its off-diagonal
support graph has four connected components, independent of `c` and `s`, with
dimensions

\[
8,\quad 8,\quad 8,\quad 4.
\]

After the corresponding fixed coordinate permutation,

\[
I(c,s)=I_8^{(0)}\oplus I_8^{(1)}\oplus I_8^{(2)}\oplus I_4.
\]

This is a direct matrix identity. It does not depend on evaluating at generic
numeric values or guessing eigenvalue multiplicities.

## Local characteristic laws

Writing the characteristic variable as `lambda`, exact reduction in
`Q[c,s]/(s^2+c^2-1)` gives

\[
\begin{aligned}
\chi_0={}&-\frac14(\lambda-1)^2\\
&\cdot(2c\lambda-c-2\lambda^3+8\lambda^2-6\lambda+1)\\
&\cdot(2c\lambda-c+2\lambda^3-8\lambda^2+6\lambda-1),
\end{aligned}
\]

\[
\begin{aligned}
\chi_1=\chi_2=\frac1{16}
&(c-2\lambda^2+4\lambda-1)
(c-2\lambda^2+6\lambda-3)\\
&\cdot(c+2\lambda^2-6\lambda+3)
(c+2\lambda^2-4\lambda+1),
\end{aligned}
\]

and

\[
\chi_3=(\lambda-1)^2(\lambda^2-3\lambda+1).
\]

The two middle blocks are more than isospectral. The artifact stores an exact
orthogonal signed-permutation matrix `U` satisfying

\[
U I_8^{(1)}(c,s)=I_8^{(2)}(c,s)U
\]

identically on the circle quotient. The first block also contains a displayed
constant eigenvector with eigenvalue one, proving a genuine `1 + 7` invariant
refinement.

## Why `81/1024` keeps appearing

At `lambda=0`, the four block determinants are

\[
\frac{1-c^2}{4},\qquad
\frac{(1-c^2)(9-c^2)}{16},\qquad
\frac{(1-c^2)(9-c^2)}{16},\qquad
1.
\]

Therefore

\[
\det I(c)
=\frac{1-c^2}{4}
\left(\frac{(1-c^2)(9-c^2)}{16}\right)^2
=\frac{(1-c^2)^3(9-c^2)^2}{1024}.
\]

At the Cayley-null point `c=0`, this is

\[
\det I(0)=\frac14\left(\frac9{16}\right)^2
=\frac{81}{1024}.
\]

At the calibrated endpoints `c=+/-1`, exactly three determinant factors
vanish. This makes the previously observed rank loss of three directions
structurally visible block by block.

## What is genuinely new here

The earlier Cayley-spectrum theorem already proved the full polynomial. This
result supplies the missing mechanism behind it:

1. the factorization is localized to four constant invariant subspaces;
2. the repeated factors come from two exactly conjugate blocks;
3. the powers `3` and `2` in the determinant law are forced by the block
   determinants;
4. the special value `81/1024` is the product `1/4 x 9/16 x 9/16 x 1`.

This is a cleaner mathematical explanation, not a stronger global optimum
claim.

## Scope boundary

The block theorem is exact for the orthonormal balanced Cayley family. It does
not by itself prove a nonorthogonal inequality. A separate Duffy/Bernstein
certificate now proves the variable-Cayley one-edge extension, but the two
remaining residual Cholesky edges, unrestricted Dirac--Gram inequality, and
global five-query D-optimality remain open.

The blocks are called *invariant coordinate blocks* because that is exactly
what the certificate proves. No claim is made here that all four are
irreducible representation-theoretic summands for a larger symmetry group.
