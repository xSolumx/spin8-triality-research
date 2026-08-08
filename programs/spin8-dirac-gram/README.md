# Spin(8) signed Dirac--Gram inequalities

## Scientific object

For a correlated four-probe frame (X), with symmetric whitening
(Q=(XX^{\mathsf T})^{-1/2}X), the strengthened inequality asks whether

\[
\det I(X)\leq \det(XX^{\mathsf T})^3\det I(Q).
\]

The exponent three records the exact boundary divisibility proved in the
maintained families. This is a computer-assisted real-algebraic program,
distinct from probe identifiability and from sequence modelling.

## Claim ledger

| Claim | Canonical source | Status |
|---|---|---|
| Signed-star inequality and strict interior | [`SIGNED_STAR_DIRAC_GRAM.md`](../../docs/manuscripts/SIGNED_STAR_DIRAC_GRAM.md) | Exact computer-assisted theorem on the full signed-star ansatz |
| Variable-Cayley one-edge family | [`SPIN8_DIRAC_ONE_EDGE_RESULTS.md`](../../docs/experiments/SPIN8_DIRAC_ONE_EDGE_RESULTS.md) | Exact computer-assisted theorem on the stated one-edge domain |
| Frozen two-edge atlas | [`SPIN8_DIRAC_TWO_EDGE_ATLAS_RESULTS.md`](../../docs/experiments/SPIN8_DIRAC_TWO_EDGE_ATLAS_RESULTS.md) | Exact finite Bernstein atlas on the frozen `h=0` family |
| Unrestricted sector reconstruction | [`SPIN8_DIRAC_UNRESTRICTED_RECONSTRUCTION_RESULTS.md`](../../docs/experiments/SPIN8_DIRAC_UNRESTRICTED_RECONSTRUCTION_RESULTS.md) | Exact polynomial reconstruction and held-out identity checks; not positivity |
| Fourier-energy inequality | [`UNRESTRICTED_FOURIER_ENERGY.md`](../../docs/manuscripts/UNRESTRICTED_FOURIER_ENERGY.md) | Exact aggregate second-moment bound; not orientation-wise positivity |
| Endpoint Klein-four face | [`UNRESTRICTED_ENDPOINT_KLEIN_FACE.md`](../../docs/manuscripts/UNRESTRICTED_ENDPOINT_KLEIN_FACE.md) | Exact complete boundary-face theorem |
| Adjacent endpoint octet | [`UNRESTRICTED_ENDPOINT_OCTET_REDUCTION.md`](../../docs/manuscripts/UNRESTRICTED_ENDPOINT_OCTET_REDUCTION.md) | Exact reduction and partial theorem; higher Schur minors remain open |

## Open claims

- positivity of every one of the sixteen unrestricted orientation margins on
  the complete feasible seven-variable domain;
- the remaining elementary-symmetric orientation gates (e_5,\ldots,e_{16});
- the unresolved Schur minors on the adjacent endpoint face;
- any deduction of global five-query optimality from these partial results.

## Certificate boundary

Exact interpolation, exact identity reconstruction, and exact positivity are
different obligations. A reconstructed polynomial is not a positivity proof;
a nonnegative aggregate Fourier energy does not imply that every orientation
sector is nonnegative; and a failed Bernstein basis is a failed certificate,
not a counterexample to the inequality.
