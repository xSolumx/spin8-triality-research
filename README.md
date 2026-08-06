# Spin(8) Triality and Noncommutative State-Space Research

This repository is the cleaned, provenance-preserving research record for a
sequence of experiments on noncommutative recurrent state-space models,
finite-group action learning, shared-family retraction, and selective
`Spin(8)` triality dynamics.

It is a research archive and theorem harness—not a claim of a production-ready
language model. Positive, negative, and partially passed gates are retained
together so that the path to the final results remains auditable.

## Principal results

### Exact algebra and constant-state recurrence

- One shared 28-dimensional bivector generates the vector and both chiral
  eight-dimensional `Spin(8)` actions.
- The implementation checks the complete `so(8)` bracket table, center
  signatures, triality equivariance, scan/recurrent parity, and norm drift.
- The triangular triality recurrence retains fixed recurrent state and an
  associative training scan.

### Shared-family learning and identifiability

- Joint family retraction recovers held-out chiral actions where independently
  fitted actions retain exact unconstrained directions.
- Five generic probes spanning two triality views identify the 28-dimensional
  shared action; four probes retain an exact three-dimensional stabilizer.
- One displayed five-probe tuple now has an exact **global** certificate: its
  triality closure is a determinant-`-1` basis in all three representations.
  Its four-probe subset has an exact continuous `su(2)` stabilizer.
- The 24 coordinate probes form an exact `F_2^5` geometry. Exhausting all
  52,752 multiview four- and five-probe sensors proves that four never identify
  the full action and five do exactly when their labels are a binary basis.
  The stabilizer ladder is `SU(3) -> SU(2) -> trivial`; the earlier 14
  exceptional supports are the Hamming `[8,4,4]`/`S(3,4,8)` shadow of this law.
- The continuous orbit theorem is now sharp: every four-probe arrangement is
  insufficient, every mixed allocation has generic `su(2)` stabilizer Lie
  algebra, and every mixed five-probe allocation has an open dense globally
  free stratum. Five probes in a single view still leave `Spin(3)`.
- The triality-specific triangular scan has been generalized to any bilinear
  intertwiner, with an exact finite lift, an SO(3) cross-product control, and a
  formal feedback-degree obstruction.
- Joint latent-address retraction removes collision slack that survives
  independently normalized routing.

### Active sensing and Cayley geometry

- Every unit query contributes an exact rank-seven projector, hence every
  five-query information operator has trace 35.
- The balanced sensor has exact invariants
  `det(I)=81/1024`, `trace(I)=35`, and `trace(I^-1)=43`.
- Its full 35-dimensional Riemannian log-determinant Hessian has exactly the
  28 shared-`Spin(8)` orbit zero modes and seven strictly negative quotient
  modes. It is therefore a strict **local** equal-five-query optimum modulo
  symmetry; global equal-five-query optimality remains open.
- Approximate experimental design is a different domain. The equal five-point
  sensor fails the Kiefer--Wolfowitz sensitivity test there, while uniform
  mass on one eight-probe basis gives `M=I_28/4` and is globally approximate
  D-optimal.
- Native python-flint now independently replays the central matrix,
  characteristic-polynomial, boundary-rank, and degree-28 reweighting
  arithmetic. A ten-seed RTX 2070 SUPER falsifier searched 860,160 dense
  interiors and 1,680 gradient starts without finding a global-five-query
  challenger; that remains numerical evidence, not a theorem.
- The three minuscule `D4` weight octets form the classical 24-cell, but the
  24 sensor projectors form a different, continuously deformable three-colour
  tight fusion frame in `Gr(7,28)`. It is not spectrally optimal as an
  uncoloured Grassmannian packing and does not attain the chordal simplex
  bound; chordal optimality itself is not settled by that bound.
- On the orthonormal balanced orbit,

  \[
  \det I_c=\frac{(1-c^2)^3(9-c^2)^2}{1024}.
  \]

  Cayley-null planes maximize information; calibrated Cayley planes are
  rank-25 endpoints.
- The degree-28 Cayley information family splits exactly into constant
  `8 + 8 + 8 + 4` invariant blocks. Their balanced determinant contributions
  are `1/4`, `9/16`, `9/16`, and `1`; the twin `9/16` blocks are conjugate by
  an exact signed permutation. This explains `81/1024` structurally.

### Exact signed Dirac–Gram theorem

Relative to the fixed `Spin(7)` split, each moving query is the graph of an
isometric seven-frame and

\[
\det I=2^7 32^{-21}\det(8T-SS^T).
\]

The strengthened inequality

\[
\det I(X)\leq \det(XX^T)^3\det I(Q)
\]

is proved exactly on the complete signed four-parameter star family. The proof
uses two independent rational reconstructions, 32 exact signed holdouts, and
four-dimensional Bernstein positivity. The unrestricted theorem still has
three residual Cholesky correlations and remains open.

The Cayley-null edge theorem first added one residual Cholesky correlation. Exact
`Spin(7)` sign symmetry reduces its orientation algebra to the trivial and
`ade` Walsh characters; symbolic rank-three boundary defects prove `Delta^3`
divisibility; and two conservative five-node grids plus 256 all-sign holdouts
certify the complete four-correlation family. A separate exact rational
counterexample proves that residual correlations cannot simply be removed
monotonically.

The variable-Cayley one-edge extension is now also proved. It retains all four
active Gram correlations while allowing the normalized Cayley coordinate to
vary. Two exact Duffy charts certify the final 203,978-term determinant over
the complete five-cube; all 256 disjoint exact sign holdouts match. The
remaining two residual Cholesky edges and the unrestricted theorem remain
open.

The preregistered second-residual bridge has passed its exact symmetry,
anchor, numerical-falsifier, and multi-slice degree gates. A new
[multiplicity-gauge theorem](docs/SPIN8_MULTIPLICITY_GAUGE_THEOREM.md) shows
that repeated probes in one triality view depend only on their covariance:
their apparent correlation is exactly equivalent to an orthogonal-mode energy
imbalance. The companion
[eight-sector amplitude theorem](docs/SPIN8_TWO_EDGE_AMPLITUDE_THEOREM.md)
reduces all radicals to fixed monomials and one universal Cayley-boundary
factor. All eight sectors are now reconstructed exactly from two disjoint
shared grids: 250,000 direct determinants recover identical 6,664-coefficient
maps, and 256 fresh exact equalities hold. Every predicted endpoint factor is
global. The endpoint-reduced sectors obey an exact flag law connecting them to
the proved one-edge theorem, while their eight orientation margins split into
two commuting four-dimensional Hadamard blocks. Positivity of those two blocks,
and hence of the full two-edge family, remains open. On the principal
orthonormal equality line, however, the new residual is now proved to lower the
determinant strictly by a positive nine-coefficient Bernstein polynomial. See the
[complete reconstruction results](docs/experiments/SPIN8_DIRAC_TWO_EDGE_ALL_SECTOR_RESULTS.md).

See the [exact theorem writeup](docs/experiments/SPIN8_DIRAC_STAR_RESULTS.md),
[preregistration](docs/experiments/SPIN8_DIRAC_STAR_PREREGISTRATION.md), and
[raw certificate](artifacts/spin8_dirac_star_20260804.json).
The new boundary is documented in the
[edge theorem](docs/experiments/SPIN8_DIRAC_EDGE_RESULTS.md) and
[decorrelation counterexample](docs/experiments/SPIN8_CONDITIONAL_DECORRELATION_COUNTEREXAMPLE.md).
For a non-specialist explanation of the mathematical results and open gates,
read [The Mathematics in Plain Language](docs/MATHEMATICS_IN_PLAIN_LANGUAGE.md).

## Repository map

| Path | Contents |
|---|---|
| [`src/`](src/README.md) | Executable research harnesses and algebra implementations |
| [`tests/`](tests/) | Foundational, recurrence, streaming, and ablation contracts |
| [`docs/RESEARCH_MAP.md`](docs/RESEARCH_MAP.md) | The research lineage and interpretation boundaries |
| [`docs/RESEARCH_AUDIT_AND_NEXT_STRATEGY_2026-08-06.md`](docs/RESEARCH_AUDIT_AND_NEXT_STRATEGY_2026-08-06.md) | Adversarial corrections, standalone paper opportunities, and the next strategy |
| [`docs/LITERATURE_AUDIT_2026-08-06.md`](docs/LITERATURE_AUDIT_2026-08-06.md) | Primary-source audit, continuous-deformation corrections, and updated baseline requirements |
| [`docs/experiments/SPIN8_RESOURCE_FLINT_GPU_AUDIT.md`](docs/experiments/SPIN8_RESOURCE_FLINT_GPU_AUDIT.md) | Six-core/15-GiB execution contract, independent FLINT replay, CUDA falsifiers, and noise profile |
| [`docs/BREAKTHROUGH_NOTE_2026-08-06.md`](docs/BREAKTHROUGH_NOTE_2026-08-06.md) | Publication-scoped write-up of the exact Cayley blocks and variable-Cayley theorem |
| [`docs/PAPER_DRAFT_TRIALITY_INFORMATION_GEOMETRY.md`](docs/PAPER_DRAFT_TRIALITY_INFORMATION_GEOMETRY.md) | Integrated manuscript covering identifiability, Cayley blocks, gauges, and Dirac--Gram results |
| [`docs/EXPERIMENT_INDEX.md`](docs/EXPERIMENT_INDEX.md) | Grouped index of every preregistration and result document |
| [`docs/experiments/`](docs/experiments/) | Preregistrations, results, corrections, and negative findings |
| [`artifacts/`](artifacts/README.md) | Raw JSON outputs retained for reproducibility |
| [`ARTIFACTS.sha256`](ARTIFACTS.sha256) | SHA-256 manifest for every published raw artifact |
| [`PROVENANCE.json`](PROVENANCE.json) | Source path, destination, size, and hash for the original extraction boundary |
| [`docs/EXTRACTION_SCOPE.md`](docs/EXTRACTION_SCOPE.md) | Audited inclusion and exclusion boundary |

## Installation

Python 3.11 or newer is recommended.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e ".[full]"
```

The exact symbolic Spin(8) gates require only the base dependencies. The
`full` extra adds JAX/Flax, dataset, and tokenizer dependencies used by the
earlier SSM lineage.

## Validation

```bash
python -m unittest discover -s tests -p "test_*.py"
python -m spin8_dirac_star \
  --output artifacts/spin8_dirac_star_replay.json
```

The current repository is validated by 164 passing tests. See
[REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md)
before comparing a rerun with a frozen artifact.

## Scientific scope

The repository makes three distinctions explicit:

1. Exact algebraic certificates are not empirical training results.
2. Behavioral gates are not raw homomorphism gates.
3. A theorem on a constrained family is not the unrestricted theorem.

The variable-Cayley one-edge determinant gate is complete. The smallest
second-residual family has survived exact symmetry and degree analysis plus a
large numerical falsifier. Its next exact target is a covariance-quotiented
sector factorization, followed by staged positivity. Language-model scale-up
remains downstream of these mechanism gates.

## Provenance and license

The original extraction covers the research lineage from the frozen baseline commit
through source commit `a367a80`. All 463 scientific files in that range are
preserved. Checkpoints, transient logs, caches, virtual
environments, and the unrelated 44.8 MB historical language-model checkpoint
are deliberately excluded. Raw result JSON, preregistrations, and negative
results are retained. Research added after extraction is outside
`PROVENANCE.json` by design and is labelled post-extraction; its artifacts are
covered by `ARTIFACTS.sha256` and Git history.

Licensed under the GNU Affero General Public License v3.0. See [LICENSE](LICENSE).
