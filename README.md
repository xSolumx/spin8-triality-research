# Spin(8) Triality and Noncommutative State-Space Research

This repository is a provenance-preserving research archive and executable
theorem harness for noncommutative recurrence, shared-family learning, and
\(\operatorname{Spin}(8)\) triality sensing. It is not a claim of a
production-ready language model.

Positive results, negative results, and partially passed gates are retained
together. The central open mathematical target is the unrestricted signed
Dirac--Gram inequality. The repository proves several constrained and boundary
families, reduces the present two-edge obstruction to explicit polynomial
positivity gates, and records numerical counterexample searches without
promoting them to proof.

## Current status

### Proved

- One shared 28-dimensional bivector action generates the vector and both
  chiral eight-dimensional triality representations. The implementation checks
  the full \(\mathfrak{so}(8)\) brackets, center signatures, triality
  equivariance, scan parity, and norm preservation.
- Within the triality sensor model, every four-probe design has a
  positive-dimensional stabilizer. Every mixed five-probe allocation has an
  open dense free stratum, while a five-probe design confined to one
  representation retains a \(\operatorname{Spin}(3)\) stabilizer.
- The balanced five-query information operator has

  \[
  \det I=\frac{81}{1024},\qquad
  \operatorname{tr}I=35,\qquad
  \operatorname{tr}(I^{-1})=43.
  \]

  Its Cayley family splits into fixed invariant blocks of dimensions
  \(8+8+8+4\), explaining the determinant structurally.
- The strengthened Dirac--Gram inequality

  \[
  \det I(X)\leq
  \det(XX^{\mathsf T})^3\det I(Q)
  \]

  is proved on the signed-star, Cayley-null edge, and variable-Cayley one-edge
  families.
- The second residual edge is locally stable along the orthonormal equality
  line. At finite edge size, its eight signed margins reduce exactly to four
  degree-six conditions and four degree-twelve polynomial conditions.
- A triangular recurrence driven by an equivariant bilinear intertwiner has an
  exact finite lift, an associative staged scan, and fixed recurrent state.
  \(\operatorname{Spin}(8)\) triality is the exceptional instance studied here.

### Numerical and empirical evidence

- A float64 CUDA campaign tested 851,968 interior and boundary points of the
  finite two-edge polynomial gates without finding a violation.
- A separate ten-seed search tested 860,160 five-query designs and 1,680
  gradient starts without finding a global equal-five-query challenger.
- The historical SSM experiments verify streaming recurrence, scan/recurrent
  parity, and several mechanism-level learning gates. They do not establish a
  language-model advantage at competitive scale.

These results are counterexample searches or finite experiments. They are not
substitutes for the open global proofs or matched large-scale benchmarks.

### Still open

- global nonnegativity of the finite two-edge degree-six and degree-twelve
  polynomial families;
- the unrestricted seven-invariant signed Dirac--Gram inequality;
- global equal-five-query D-optimality over all allocations and frames;
- classification of exceptional nonprincipal five-probe strata;
- a triality-specific advantage over direct-slot, delta-rule, fast-weight, and
  structured orthogonal sequence baselines;
- competitive language-model scale-up and measured production throughput.

## Main result families

### 1. Algebra and recurrence

The algebra layer constructs all three eight-dimensional triality actions from
one shared \(\mathfrak{so}(8)\) generator and verifies their common invariant
tensor. The recurrent layer separates parallel training from streaming
inference without changing the transition law. Triangular bilinear coupling is
the exact boundary at which a finite staged scan remains possible; generic
feedback causes polynomial degree to grow without bound.

Read:
[foundations](docs/FOUNDATIONS.md),
[triality algebra](docs/experiments/SPIN8_TRIALITY_ALGEBRA_RESULTS.md), and
[Intertwiner SchurScans](docs/experiments/INTERTWINER_SCHURSCAN_THEOREM.md).

### 2. Identifiability and shared-family learning

Jointly constraining several observed actions to arise from one shared
representation removes relational null directions that independent fitting
cannot see. The five-probe theorems then identify the sharp generic sensing
boundary inside the triality action model: four probes are insufficient, while
five mixed probes are generically free.

Read:
[five-probe results](docs/experiments/SPIN8_FIVE_PROBE_RESULTS.md),
[continuous orbit theorem](docs/experiments/SPIN8_CONTINUOUS_PROBE_ORBIT_THEOREM.md),
and [blind shared-action results](docs/experiments/SPIN8_BLIND_ALIAS_ACTION_RESULTS.md).

### 3. Active sensing and Cayley information geometry

Each unit query contributes a rank-seven projector. The balanced sensor is a
strict local optimum modulo its 28-dimensional group orbit, and its information
operator has an exact block decomposition. Approximate design is a separate
problem: the equal five-point design is not globally optimal when fractional
measurement weights are permitted, whereas an eight-probe isotropic design is.

Read:
[Cayley spectrum](docs/experiments/SPIN8_CAYLEY_SPECTRUM_RESULTS.md),
[Cayley block theorem](docs/experiments/SPIN8_CAYLEY_BLOCK_THEOREM.md), and
[active sensing](docs/experiments/SPIN8_ACTIVE_SENSING_RESULTS.md).

### 4. Signed Dirac--Gram program

The exact proof program uses common triality symmetry, rational reconstruction,
rank-predicted boundary factors, and Bernstein/Duffy positivity certificates.
The one-edge family is complete. For the second edge, local stability and the
radical-to-polynomial reduction are proved; global polynomial positivity
remains the next exact gate.

Read:
[current synthesis](docs/ITERATION_NOTE_2026-08-06.md),
[one-edge theorem](docs/experiments/SPIN8_DIRAC_ONE_EDGE_RESULTS.md),
[two-edge local theorem](docs/experiments/SPIN8_TWO_EDGE_BOUNDARY_KERNEL_RESULTS.md),
and
[finite polynomial reduction](docs/experiments/SPIN8_TWO_EDGE_FINITE_REDUCTION_RESULTS.md).

### 5. Learning and compilation lineage

The earlier finite-group experiments separate continuous optimization from
exact algebraic compilation. They study when training finds approximate
noncommutative actions, when a compiler can recover a discrete action, and why
shared-family retraction succeeds where independent normalization leaves
unconstrained directions. These are mechanism studies, not evidence that
\(\operatorname{Spin}(8)\) has already improved general language modeling.

Read:
[research map](docs/RESEARCH_MAP.md),
[experiment index](docs/EXPERIMENT_INDEX.md), and
[research audit and next strategy](docs/RESEARCH_AUDIT_AND_NEXT_STRATEGY_2026-08-06.md).

## Reading paths

| Reader | Start here |
|---|---|
| Non-specialist | [The Mathematics in Plain Language](docs/MATHEMATICS_IN_PLAIN_LANGUAGE.md) |
| Mathematician | [Triality Information Geometry manuscript](docs/PAPER_DRAFT_TRIALITY_INFORMATION_GEOMETRY.md) |
| Sequence-model researcher | [Foundations](docs/FOUNDATIONS.md) and [Research Map](docs/RESEARCH_MAP.md) |
| Reproducer or reviewer | [Reproducibility](docs/REPRODUCIBILITY.md) and [Artifact Manifest](ARTIFACTS.sha256) |
| Future contributor | [Mathematical Writing Standard](docs/MATHEMATICAL_WRITING_STANDARD.md) |

## Repository map

| Path | Contents |
|---|---|
| [src](src/README.md) | Algebra, recurrence, exact-certificate, and falsifier harnesses |
| [tests](tests/) | Foundational, theorem, streaming, and documentation contracts |
| [Research Map](docs/RESEARCH_MAP.md) | Detailed research lineage and interpretation boundaries |
| [Experiment Index](docs/EXPERIMENT_INDEX.md) | Every preregistration, result, correction, and negative finding |
| [Research Audit and Next Strategy](docs/RESEARCH_AUDIT_AND_NEXT_STRATEGY_2026-08-06.md) | Paper-scale contributions, correction ledger, and next strategy |
| [Literature Audit](docs/LITERATURE_AUDIT_2026-08-06.md) | Primary-source literature audit and baseline requirements |
| [artifacts](artifacts/README.md) | Raw outputs retained for reproducibility |
| [Artifact Manifest](ARTIFACTS.sha256) | SHA-256 manifest for published artifacts |
| [Provenance](PROVENANCE.json) | Original extraction boundary and source hashes |

## Installation

Python 3.11 or newer is recommended.

    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    python -m pip install --upgrade pip
    python -m pip install -e ".[full]"

The exact symbolic gates use the base dependencies. The full extra adds the
JAX/Flax, dataset, and tokenizer dependencies required by the historical SSM
lineage.

## Validation

    python -m unittest discover -s tests -p "test_*.py"
    python tools/audit_math_docs.py

The maintained suite currently contains 175 passing tests. The latest bounded
run used six CPU cores, peaked at 3.962 GiB of process-tree resident memory, and
completed without crossing the 15 GiB watchdog. Read
[Reproducibility](docs/REPRODUCIBILITY.md) before comparing a rerun with a
frozen artifact.

## Scientific scope

The archive maintains four interpretation boundaries:

1. an exact algebraic certificate is not an empirical training result;
2. a finite numerical search is not a continuous proof;
3. a theorem on a constrained family is not the unrestricted theorem;
4. a mechanism-level SSM result is not a competitive language-model result.

The next mathematical task is endpoint factorization and staged positivity for
the finite two-edge polynomial gates. Language-model scale-up remains
downstream of the missing matched baselines and mechanism gates.

## Provenance and license

The original extraction covers 463 scientific files through source commit
a367a80. Checkpoints, transient logs, caches, virtual environments, and the
unrelated 44.8 MB historical language-model checkpoint are excluded. Later
research is explicitly post-extraction and is covered by ARTIFACTS.sha256 and
Git history.

Licensed under the GNU Affero General Public License v3.0. See [LICENSE](LICENSE).
