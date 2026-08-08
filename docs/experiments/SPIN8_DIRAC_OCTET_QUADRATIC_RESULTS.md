# A Global Quadratic Schur-Minor Certificate on the Adjacent Endpoint Octet

**Exact computer-assisted theorem result — 2026-08-08**

**Status:** first of three quadratic principal-minor families proved globally

**Preregistration:**
[`SPIN8_DIRAC_OCTET_QUADRATIC_PREREGISTRATION.md`](SPIN8_DIRAC_OCTET_QUADRATIC_PREREGISTRATION.md)

**Assembly verifier:**
[`spin8_dirac_endpoint_octet_quadratic_certificate.py`](../../src/spin8_dirac_endpoint_octet_quadratic_certificate.py)

**Assembled artifact:**
[`spin8_dirac_endpoint_octet_quadratic_0_global_20260808.json`](../../artifacts/spin8_dirac_endpoint_octet_quadratic_0_global_20260808.json)

**Artifact SHA-256:**
`b596f3a845a2f67a7e545c767da51524104980007ff5ac855f7ee7b23c0eddd0`

## Result

On the adjacent Cayley-endpoint face, the exact octet reduction writes the
remaining Schur block as

\[
Z=X^2-(1-y^2)R^2,
\qquad
(u_d,u_e,u_g,u_i,y)\in[0,1]^5.
\]

Let \(Z_0\) be its identity coefficient and let \(Z_\mu\) be the coefficient
associated with the first nontrivial Klein-four mode

\[
\mu=0011001.
\]

The corresponding two-by-two principal-minor condition is

\[
q_\mu=Z_0^2-s_\mu Z_\mu^2,
\]

where \(s_\mu\) is the exact forced-square monomial carried by that mode. The
assembled certificate establishes

\[
\boxed{
q_{0011001}(u_d,u_e,u_g,u_i,y)\ge 0
\quad\text{throughout }[0,1]^5.
}
\]

This is a domain-wide exact sign theorem. It is not a numerical minimum, a
sampled statement, or an inference from a failed counterexample search.

## Why the native certificate failed

The polynomial has 233,064 power terms. Its native tensor-product Bernstein
form contains 224 negative controls. Those controls do **not** imply that the
polynomial is negative: Bernstein coefficients are sufficient, not necessary,
for positivity.

A bounded float64 CUDA falsifier searched 4,096 random points and optimized
eight starts for every physical orientation. It found no negative value. Its
smallest normalized margin, approximately \(0.02032\), approached the known
equality corner rather than an interior counterexample. This screen motivated
the local analysis but contributes no step to the proof.

## Exact domain decomposition

The proof begins with a dyadic partition of the five-cube. At the first level,
30 of 32 boxes are natively Bernstein-nonnegative. The two exceptions are
labelled `00001` and `00010`, using the coordinate order

\[
(u_d,u_e,u_g,u_i,y).
\]

All 32 children of `00010` certify. Of the 32 children of `00001`, 31
certify. The sole residual box is `00001/00001`, namely

\[
0\le u_d,u_e,u_g,u_i\le\frac14,
\qquad
\frac34\le y\le1.
\]

Equivalently, all five nonnegative deviations

\[
u_d,\quad u_e,\quad u_g,\quad u_i,\quad 1-y
\]

lie in \([0,\tfrac14]\).

## The five-chart equality blow-up

At a nonzero point of the residual box, choose a largest deviation \(m\). Set

\[
r=4m,
\qquad
x_j=\frac{d_j}{m}\quad(j\ne\text{pivot}).
\]

Then \(r,x_j\in[0,1]\). The five possible choices of largest deviation give
five charts whose union covers the complete residual box. In every chart, the
minor is exactly divisible by \(r^4\). Thus the unresolved equality is a
quartic germ, as predicted independently before the blow-up calculation.

The quotient is certified differently in the five charts:

| Pivot deviation | Exact certificate |
|---|---|
| \(u_d\) | signed-square tangent product, two exact boundary factorizations, nested Bernstein selectors, and a four-box corner atlas |
| \(u_e\) | signed-square tangent product and an exact degree-one selector comparison |
| \(u_g\) | signed-square tangent product and an exact degree-two selector comparison |
| \(u_i\) | native tensor-product Bernstein positivity |
| \(1-y\) | native tensor-product Bernstein positivity |

The two middle charts use the identity

\[
H_M=H_m+F\sum_{j=m}^{M-1}(1-r)^j,
\]

where \(M=68\), \(m=1\) or \(2\), \(F\ge0\) is the exceptional-divisor
polynomial, and \(H_m\) is natively Bernstein-nonnegative. The correction is
therefore nonnegative exactly; changing selector exponent does not change the
polynomial being proved.

The hardest radial axis in the \(u_d\)-chart contains the exact factor

\[
(2t-1)^2\bigl(-56t^3+220t^2+70t+13\bigr).
\]

The cubic has degree-three Bernstein coefficients

\[
13,\qquad \frac{109}{3},\qquad 133,\qquad 247,
\]

so it is strictly positive on \([0,1]\). The square records the only remaining
axis equality. Four exact half-boxes certify the transverse two-variable
remainder around that equality.

## What the lightweight verifier checks

The assembly verifier recomputes:

1. the SHA-256 hash of every source artifact;
2. completeness of all three binary atlases and their exact unresolved paths;
3. the stored exact Bernstein sign counts of every accepted atlas cell;
4. radius-order four and all five pivot acceptance predicates;
5. the load-bearing stored factor, selector, and comparison identities.

It deliberately states what it trusts: the exact coefficient arrays and
power-to-Bernstein transforms produced by the source harnesses. A full replay
uses
[`spin8_dirac_endpoint_octet_quadratic.py`](../../src/spin8_dirac_endpoint_octet_quadratic.py)
and
[`spin8_dirac_endpoint_octet_blowup.py`](../../src/spin8_dirac_endpoint_octet_blowup.py).

## Plain-language interpretation

The unresolved polynomial was not negative. Its first coordinate system was
poorly adapted to a point where several directions vanish together. Ordinary
dyadic boxes isolated that point; a blow-up then recorded the *relative rates*
at which the five deviations approach zero. In those relative coordinates,
the apparent sign ambiguity separates into squares, positive one-variable
factors, and finitely many nonnegative Bernstein tensors.

This is a useful methodological result as well as a theorem slice: when an
exact positivity certificate fails only near a high-order equality, refine the
ordinary domain until the obstruction is isolated, then replace infinite
subdivision by a finite max-coordinate blow-up.

## Nonclaims and next gate

This result proves exactly one of the three quadratic conditions required for
\(Z\succeq0\). It does not prove:

- the other two quadratic principal minors;
- the cubic principal minor or (det Z);
- positivity of the complete adjacent endpoint octet;
- the unrestricted seven-circle Dirac--Gram inequality;
- global five-query D-optimality.

The next exact gate is to apply the same adversarial sequence—native audit,
finite dyadic localization, and only then a boundary-adapted blow-up—to the
other two quadratic modes. Their superficially similar native failures are not
assumed to share this certificate.
