# Research programs and claim boundaries

The archive is organized by scientific question, not by the date on which a
file was produced. Five programs are maintained. A result transfers between
programs only through an explicit theorem, reduction, or matched experiment.

| Program | Central question | Evidence class at the frontier |
|---|---|---|
| [Shared-family learning](shared-family-learning/README.md) | When do joint relational constraints identify an action family that independent fits cannot? | Finite-group theorems and controlled optimization experiments |
| [Triality memory and SchurScans](triality-memory/README.md) | Which equivariant bilinear recurrences admit exact finite associative lifts? | Algebraic theorems, recurrence tests, and bounded systems benchmarks |
| [Spin(8) sensing and Cayley design](spin8-sensing-and-design/README.md) | How many mixed triality probes identify a shared action, and which balanced designs are best conditioned? | Exact generic, canonical-family, and local theorems |
| [Spin(8) Dirac--Gram inequalities](spin8-dirac-gram/README.md) | Can correlated probe frames beat their orthonormal completions after the cubic Gram penalty? | Computer-assisted family theorems, exact reductions, and open global gates |
| [Spin(9) Dirac--Clifford sensing](spin9-dirac-clifford-sensing/README.md) | What can three real spinors identify, and how is their exact design problem reduced? | Exact internally replayed theorems plus a numerical global screen |

## Authority of directories

- `programs/` states which claims belong together and where their authoritative
  evidence lives.
- `docs/manuscripts/` contains theorem narratives intended to be read as
  mathematics rather than chronology.
- `docs/experiments/` preserves preregistrations, empirical results, negative
  results, and later corrections.
- `src/` and `tests/` are the executable implementation and acceptance layer.
- `artifacts/` contains published machine-readable evidence covered by
  `ARTIFACTS.sha256`.
- `papers/` and `referee/` contain compact publication and independent-review
  packages. They do not inherit every claim in the historical archive.

## Non-transfer rules

- A finite-group compiler result is not a memory-capacity result.
- An exact sensing theorem is not a sequence-model benchmark.
- Associative scan closure is not a fused-kernel or throughput result.
- A constrained Dirac--Gram theorem is not the unrestricted theorem.
- A numerical global search is a falsification campaign, not a proof of global
  optimality.
- A Spin(9) composition identity does not establish a Spin(9) memory advantage.

The chronological lineage remains available in
[`docs/RESEARCH_MAP.md`](../docs/RESEARCH_MAP.md), but it is not the source of
current claim status. Publication scope is governed by
[`PUBLICATION_SCOPE.md`](../PUBLICATION_SCOPE.md).
