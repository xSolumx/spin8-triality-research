# Spin(9) Dirac--Clifford sensing and exact design

## Scientific object

This program studies the nine symmetric Clifford involutions on the real
16-dimensional spin representation of \(\operatorname{Spin}(9)\). It extends
the maintained Spin(8) gamma system, but it does not replace the triality
programs and currently makes no sequence-memory performance claim.

For

\[
D(a)=\sum_{i=0}^{8}a_iP_i,
\qquad
D(a)^2=\lVert a\rVert^2I_{16}.
\]

The second identity gives a norm-preserving real composition. Its use here is
in shared-action sensing and exact design.

## Claim ledger

| Claim | Evidence | Status boundary |
|---|---|---|
| Nine symmetric Clifford involutions and Spin(8) restriction | [`spin9_dirac_clifford.py`](../../src/spin9_dirac_clifford.py) | Exact coefficient and bracket checks |
| Generic one/two/three-spinor stabilizers | [`SPIN9_THREE_SPINOR_IDENTIFIABILITY.md`](../../docs/manuscripts/SPIN9_THREE_SPINOR_IDENTIFIABILITY.md) | Human stabilizer argument plus independent exact rank witnesses |
| Symmetric three-spinor conditioning curve | [`SPIN9_THREE_SPINOR_CONDITIONING.md`](../../docs/manuscripts/SPIN9_THREE_SPINOR_CONDITIONING.md) | Exact one-parameter theorem; not a global rank-three optimum |
| Frame-operator reduction and relaxed design optimum | [`SPIN9_FRAME_OPERATOR_REDUCTION.md`](../../docs/manuscripts/SPIN9_FRAME_OPERATOR_REDUCTION.md) | Exact theorem; the relaxation is unattainable by an exact three-probe frame |
| Numerical unrestricted search | [`SPIN9_THREE_SPINOR_GLOBAL_SCREEN.md`](../../docs/experiments/SPIN9_THREE_SPINOR_GLOBAL_SCREEN.md) | Ten-seed falsification campaign; no proof of global optimality |
| Cayley-null stabilizer and spectral branching | [`SPIN9_SYMMETRY_BRANCHING.md`](../../docs/manuscripts/SPIN9_SYMMETRY_BRANCHING.md) | Exact at the symmetric orbit |
| Fixed-plane orthonormality | [`SPIN9_FIXED_PLANE_ORTHONORMALITY.md`](../../docs/manuscripts/SPIN9_FIXED_PLANE_ORTHONORMALITY.md) | Exact for every plane on the symmetric curve; other support planes remain open |
| Grassmann normal slice | [`SPIN9_GRASSMANN_SLICE_THEOREM.md`](../../docs/manuscripts/SPIN9_GRASSMANN_SLICE_THEOREM.md) | Exact \(V_1\oplus(V_5\otimes\mathbb R^2)\) quotient decomposition at the candidate orbit |
| Strict local rank-three optimum | [`SPIN9_STRICT_LOCAL_D_OPTIMALITY.md`](../../docs/manuscripts/SPIN9_STRICT_LOCAL_D_OPTIMALITY.md) | Exact internally replayed local theorem modulo Spin(9); independent external review remains pending |

## Nonclaims and open gates

- The unrestricted global exact three-spinor optimum remains open.
- The numerical search cannot replace a global proof.
- No matched experiment shows a Spin(9) memory or sequence-model advantage.
- A single \(D(a)\) is an odd \(\operatorname{Pin}(9)\) element, not a
  Spin(9) rotor. Only an even product such as \(D(b)D(a)\) lies in the spin
  action.

## Reproduction

```powershell
$env:PYTHONPATH = "src"
python -m spin9_dirac_clifford --output artifacts/spin9_dirac_clifford_gate_20260807.json
python -m spin9_frame_operator --output artifacts/spin9_frame_operator_20260807.json
python -m spin9_local_hessian --output artifacts/spin9_local_hessian_exact.json
python -m pytest -q tests/test_spin9_dirac_clifford.py tests/test_spin9_frame_operator.py tests/test_spin9_local_hessian.py
```
