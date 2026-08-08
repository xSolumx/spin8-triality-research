# Spin(8) Triality and Noncommutative State-Space Research

This repository is a provenance-preserving research archive and executable
theorem harness. It contains five separable programs rather than one compound
claim:

1. [shared-family representation learning](programs/shared-family-learning/README.md);
2. [triality memory and intertwiner scans](programs/triality-memory/README.md);
3. [Spin(8) sensing and Cayley design](programs/spin8-sensing-and-design/README.md);
4. [Spin(8) signed Dirac--Gram inequalities](programs/spin8-dirac-gram/README.md);
5. [Spin(9) Dirac--Clifford sensing and exact design](programs/spin9-dirac-clifford-sensing/README.md).

The [program index](programs/README.md) is the recommended scientific entry
point. The [public release boundary](PUBLICATION_SCOPE.md) states what is and
is not committed. A result in one program is not evidence for another without
an explicit bridge. In particular, this repository does not claim a
production-ready language model.

The current claim statuses, replay tiers, and failure boundaries are defined in
the [gate and boundary audit](docs/GATE_AND_BOUNDARY_AUDIT_2026-08-06.md).

Reviewers of the strongest compact theorem can bypass the chronological
archive and begin with the
[balanced Cayley-spectrum referee package](referee/cayley-information-spectrum/README.md).

Positive results, negative results, and partially passed gates are retained
together. The central open mathematical target is the unrestricted signed
Dirac--Gram inequality. The repository proves several constrained and boundary
families, reduces the present two-edge obstruction to explicit polynomial
positivity gates, certifies those gates on the complete frozen `h=0` family,
reconstructs the unrestricted seven-variable margin exactly, and records
broader numerical counterexample searches without promoting them to proof.

## Current status

### Proved

- The maintained Spin(8) gamma system extends exactly to the nine symmetric
  Clifford involutions of the real 16-dimensional Spin(9) spin module. Three
  generic spinor probes have trivial common stabilizer, whereas a generic pair
  retains \(\operatorname{SU}(3)\). The associated sensing problem factors
  through a rank-three frame operator. Its linear information map has an exact
  nine-dimensional vector-grade kernel, and the convex approximate-design
  relaxation has complete optimizer family
  \(3I_{16}/16+\sum_i v_iP_i\), \(\lVert v\rVert\leq3/16\). No exact
  three-probe frame attains that relaxed optimum; its global optimum remains
  open. The algebraic symmetric candidate is nevertheless now proved to be a
  strict local optimum on the complete \(44\)-dimensional rank-three frame
  stratum modulo Spin(9): its quotient Hessian decomposes as
  \(V_1\oplus(V_5\otimes\mathbb R^2)\), and the exact coupled \(V_5\)
  multiplicity block is negative definite.
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
  \(8+8+8+4\), explaining the determinant structurally. On the orthonormal
  balanced information family, the Cayley-null design also uniquely minimizes
  \(\operatorname{tr}(I^{-1})\) and \(\operatorname{tr}(I^{-2})\), while
  \(\operatorname{tr}I=35\) and \(\operatorname{tr}(I^2)=67\) remain constant.
- The strengthened Dirac--Gram inequality

  \[
  \det I(X)\leq
  \det(XX^{\mathsf T})^3\det I(Q)
  \]

  is proved on the signed-star, Cayley-null edge, and variable-Cayley one-edge
  families. On the signed-star family the inequality is strict in the open
  parameter box, and its orientation-sensitive sector has the exact asymmetry
  factor \((1-u)(v-w)(1-z)^3\). Its normalized equality set is completely
  classified: \(z=1\) or \((u,v,w)=(0,0,0)\).
- The second residual edge is locally stable along the orthonormal equality
  line. At finite edge size, its eight signed margins reduce exactly to four
  degree-six conditions and four degree-twelve polynomial conditions. A
  complete 34-leaf triangular Bernstein atlas now proves all eight margins
  nonnegative on the frozen `h=0` two-edge family; interval-indeterminate
  controls are replayed with exact integer arithmetic.
- On the unrestricted seven-circle chart, triality symmetry reduces all
  physical margins to sixteen exact seven-variable polynomial sectors. Two
  disjoint rational grids reconstruct identical coefficient maps from
  2,500,000 exact determinants, and 32 fresh rational points verify all 512
  sector identities. The full tangent cone along the orthonormal equality line
  is nonnegative; at its calibrated endpoint, every tangent-null cone lifts by
  the strictly positive quartic \(128(p^2+q^2)^2\). This is an exact structural
  and local theorem, not yet a global positivity proof. A separate exact
  boundary-supported Bernstein decomposition proves globally that the trivial
  Fourier amplitude dominates the Euclidean norm of all fifteen nontrivial
  modes. The proof isolates the only four native-basis obstructions onto two
  identical three-variable faces, certifies those faces in triangular charts,
  and leaves a 588,245-control nonnegative remainder. This controls the RMS
  orientation deviation on the complete seven-cube, but does not yet force
  every individual orientation margin to be nonnegative. A Walsh-convolution
  bound additionally proves the first four elementary-symmetric orientation
  invariants nonnegative, leaving the invariant hierarchy
  \(e_5,\ldots,e_{16}\) open. A complementary exact theorem closes the
  complete four-variable face \(u_a=u_h=0,\ c^2=1\): its three surviving
  nontrivial Walsh modes form a Klein-four block, and every principal minor
  of the associated group-circulant matrix is nonnegative. This is a boundary
  theorem, not the unrestricted seven-variable result.
- On the adjacent five-variable face \(u_a=0,\ c^2=1\), eight surviving
  sectors form \((\mathbb Z/2\mathbb Z)^3\). An exact subgroup-chain Schur
  reduction splits the problem into two commuting Klein-four blocks. The
  complete first block is now proved positive semidefinite, and the scalar
  minor of the second block follows exactly from the global Fourier-energy
  theorem. The second block's quadratic, cubic, and determinant gates remain
  open, so the full adjacent face is not yet a theorem.
- A triangular recurrence driven by an equivariant bilinear intertwiner has an
  exact finite lift, an associative staged scan, and fixed recurrent state.
  \(\operatorname{Spin}(8)\) triality is the exceptional instance studied here.

### Numerical and empirical evidence

- Before the exact atlas was constructed, a float64 CUDA campaign tested
  851,968 interior and boundary points of the finite two-edge polynomial gates
  without finding a violation. That historical screen is now supporting
  falsification evidence, not the theorem certificate.
- A separate ten-seed search tested 860,160 five-query designs and 1,680
  gradient starts without finding a global equal-five-query challenger.
- The historical SSM experiments verify streaming recurrence, scan/recurrent
  parity, and several mechanism-level learning gates. They do not establish a
  language-model advantage at competitive scale.

These results are counterexample searches or finite experiments. They are not
substitutes for the open global proofs or matched large-scale benchmarks.

### Still open

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
The [work-efficient scan benchmark](docs/experiments/INTERTWINER_SCHURSCAN_BENCHMARK_RESULTS.md)
separates algebraic work, dependency depth, memory, and eager CPU/CUDA timing.

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
The one-edge and frozen `h=0` two-edge families are complete. The latter uses a
34-leaf rational-circle triangular atlas, outward Bernstein enclosures, and
exact integer replay for every cancellation control. The final Cholesky
residual has now been reconstructed exactly in sixteen sectors; the remaining
gap is a domain-wide sign certificate, not an unknown polynomial identity.

Read:
[current synthesis](docs/DIRAC_GRAM_TWO_EDGE_STATUS_2026-08-06.md),
[one-edge theorem](docs/experiments/SPIN8_DIRAC_ONE_EDGE_RESULTS.md),
[two-edge local theorem](docs/experiments/SPIN8_TWO_EDGE_BOUNDARY_KERNEL_RESULTS.md),
and
[finite polynomial reduction](docs/experiments/SPIN8_TWO_EDGE_FINITE_REDUCTION_RESULTS.md),
and
[two-edge atlas theorem](docs/experiments/SPIN8_DIRAC_TWO_EDGE_ATLAS_RESULTS.md),
and
[unrestricted reconstruction and tangent theorem](docs/experiments/SPIN8_DIRAC_UNRESTRICTED_RECONSTRUCTION_RESULTS.md),
and
[complete global adjacent-octet quadratic gate](docs/experiments/SPIN8_DIRAC_OCTET_QUADRATIC_RESULTS.md).

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
| Publication reader | [Cayley Spectrum paper](docs/manuscripts/CAYLEY_INFORMATION_SPECTRUM.md) and [Signed-Star paper](docs/manuscripts/SIGNED_STAR_DIRAC_GRAM.md) |
| Sequence-model researcher | [Foundations](docs/FOUNDATIONS.md) and [Research Map](docs/RESEARCH_MAP.md) |
| Reproducer or reviewer | [Reproducibility](docs/REPRODUCIBILITY.md) and [Artifact Manifest](ARTIFACTS.sha256) |
| Future contributor | [Mathematical Writing Standard](docs/MATHEMATICAL_WRITING_STANDARD.md) |
| Manuscript reviewer | [Full Manuscript Audit](docs/MANUSCRIPT_AUDIT_2026-08-06.md) |

For a complete, status-labelled tour of the documentation, begin with the
[Documentation Guide](docs/README.md).

## Repository map

| Path | Contents |
|---|---|
| [src](src/README.md) | Algebra, recurrence, exact-certificate, and falsifier harnesses |
| [tests](tests/) | Foundational, theorem, streaming, and documentation contracts |
| [Documentation Guide](docs/README.md) | Reader paths, claim-status legend, and logically grouped manuscripts |
| [Manuscripts](docs/manuscripts/README.md) | Self-contained theorem papers separated from the chronological archive |
| [Research Map](docs/RESEARCH_MAP.md) | Detailed research lineage and interpretation boundaries |
| [Experiment Index](docs/EXPERIMENT_INDEX.md) | Every preregistration, result, correction, and negative finding |
| [Research Audit and Next Strategy](docs/RESEARCH_AUDIT_AND_NEXT_STRATEGY_2026-08-06.md) | Paper-scale contributions, correction ledger, and next strategy |
| [Literature Audit](docs/LITERATURE_AUDIT_2026-08-06.md) | Primary-source literature audit and baseline requirements |
| [Provenance and History](docs/PROVENANCE_AND_HISTORY.md) | Extraction snapshot, post-extraction amendments, and historical-reading policy |
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
    python tools/verify_artifact_manifest.py

The maintained suite currently contains 188 passing tests. The latest bounded
run used six CPU cores, took 375.8 seconds including supervision, peaked at
4.074 GiB of process-tree resident memory, and completed without crossing the
15 GiB watchdog. Read
[Reproducibility](docs/REPRODUCIBILITY.md) before comparing a rerun with a
frozen artifact.

## Scientific scope

The archive maintains four interpretation boundaries:

1. an exact algebraic certificate is not an empirical training result;
2. a finite numerical search is not a continuous proof;
3. a theorem on a constrained family is not the unrestricted theorem;
4. a mechanism-level SSM result is not a competitive language-model result.

The next mathematical task is a covariance-orbit reduction for the final
Cholesky residual in the unrestricted Dirac--Gram inequality. Language-model
scale-up remains downstream of the missing matched baselines and mechanism
gates.

## Provenance and license

The original extraction covers 463 scientific files through source commit
a367a80. Checkpoints, transient logs, caches, virtual environments, and the
unrelated 44.8 MB historical language-model checkpoint are excluded. Later
research is explicitly post-extraction and is covered by ARTIFACTS.sha256 and
Git history.

Licensed under the GNU Affero General Public License v3.0. See [LICENSE](LICENSE).
