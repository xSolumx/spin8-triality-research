# Triality memory and intertwiner scans

## Scientific claim

Equivariant bilinear drives can be lifted into a triangular affine transition
algebra that remains closed under associative composition. `Spin(8)` triality
provides an exceptional eight-dimensional instance.

## Evidence map

| Result family | Canonical document | Status boundary |
|---|---|---|
| Triality algebra | [`SPIN8_TRIALITY_ALGEBRA_RESULTS.md`](../../docs/experiments/SPIN8_TRIALITY_ALGEBRA_RESULTS.md) | Exact algebraic diagnostics |
| Triangular triality lift | [`SPIN8_TRIANGULAR_TRIALITY_LIFT_RESULTS.md`](../../docs/experiments/SPIN8_TRIANGULAR_TRIALITY_LIFT_RESULTS.md) | Exact recurrence construction |
| General SchurScan theorem | [`INTERTWINER_SCHURSCAN_THEOREM.md`](../../docs/experiments/INTERTWINER_SCHURSCAN_THEOREM.md) | General mathematical lift and feedback boundary |
| Work-efficient scan benchmark | [`INTERTWINER_SCHURSCAN_BENCHMARK_RESULTS.md`](../../docs/experiments/INTERTWINER_SCHURSCAN_BENCHMARK_RESULTS.md) | Eager CPU/CUDA implementation result; no fused-kernel claim |
| Blind shared action | [`SPIN8_BLIND_SHARED_ACTION_RESULTS.md`](../../docs/experiments/SPIN8_BLIND_SHARED_ACTION_RESULTS.md) | Learned-action experiment |
| Continuous aliases | [`SPIN8_CONTINUOUS_ALIAS_RESULTS.md`](../../docs/experiments/SPIN8_CONTINUOUS_ALIAS_RESULTS.md) | Alias-learning experiment |
| Coded memory | [`SPIN8_CODED_MEMORY_RESULTS.md`](../../docs/experiments/SPIN8_CODED_MEMORY_RESULTS.md) | Multiplicity-channel memory |
| Tight-frame memory protocol | [`SPIN8_TIGHT_FRAME_MEMORY_PREREGISTRATION.md`](../../docs/experiments/SPIN8_TIGHT_FRAME_MEMORY_PREREGISTRATION.md) | Prospective protocol, not a result |

## Exact capacity boundary

For unit triality keys, single-pair binding is exactly invertible. With an
`H`-dimensional multiplicity code, `K <= H` orthogonal code columns give exact
linear slot isolation. Raw superposition in one eight-dimensional triality
space does not provide high-capacity associative memory.

## Nonclaims

- Scan closure does not imply a fused or production-competitive kernel. The
  maintained eager benchmark compares two local tensor programs only.
- Exact single-pair inversion does not imply high-capacity vector-symbolic
  retrieval.
- The program has not yet beaten direct slots or modern delta-rule/fast-weight
  baselines at matched state and compute.

## Standalone paper

Lead with the general Intertwiner SchurScan theorem, state the feedback
obstruction, and use triality as the exact exceptional example. Keep benchmark
claims in a separate empirical section or paper.
