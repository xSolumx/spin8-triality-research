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
- Joint latent-address retraction removes collision slack that survives
  independently normalized routing.

### Active sensing and Cayley geometry

- Every unit query contributes an exact rank-seven projector, hence every
  five-query information operator has trace 35.
- The balanced sensor has exact invariants
  `det(I)=81/1024`, `trace(I)=35`, and `trace(I^-1)=43`.
- On the orthonormal balanced orbit,

  \[
  \det I_c=\frac{(1-c^2)^3(9-c^2)^2}{1024}.
  \]

  Cayley-null planes maximize information; calibrated Cayley planes are
  rank-25 endpoints.

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

See the [exact theorem writeup](docs/experiments/SPIN8_DIRAC_STAR_RESULTS.md),
[preregistration](docs/experiments/SPIN8_DIRAC_STAR_PREREGISTRATION.md), and
[raw certificate](artifacts/spin8_dirac_star_20260804.json).

## Repository map

| Path | Contents |
|---|---|
| [`src/`](src/README.md) | Executable research harnesses and algebra implementations |
| [`tests/`](tests/) | Foundational, recurrence, streaming, and ablation contracts |
| [`docs/RESEARCH_MAP.md`](docs/RESEARCH_MAP.md) | The research lineage and interpretation boundaries |
| [`docs/EXPERIMENT_INDEX.md`](docs/EXPERIMENT_INDEX.md) | Grouped index of every preregistration and result document |
| [`docs/experiments/`](docs/experiments/) | Preregistrations, results, corrections, and negative findings |
| [`artifacts/`](artifacts/README.md) | Raw JSON outputs retained for reproducibility |
| [`ARTIFACTS.sha256`](ARTIFACTS.sha256) | SHA-256 manifest for every published raw artifact |
| [`PROVENANCE.json`](PROVENANCE.json) | Source path, destination, size, and hash for the extraction |
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

The source extraction was validated with 111 tests passing and two expected
hardware-dependent skips. See [REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md)
before comparing a rerun with a frozen artifact.

## Scientific scope

The repository makes three distinctions explicit:

1. Exact algebraic certificates are not empirical training results.
2. Behavioral gates are not raw homomorphism gates.
3. A theorem on a constrained family is not the unrestricted theorem.

The next exact target is a conditional-decorrelation lemma controlling the
three residual Cholesky correlations in the Dirac–Schur operator. Language
model scale-up is intentionally downstream of that mechanism gate.

## Provenance and license

The extraction covers the research lineage from the frozen baseline commit
through source commit `a367a80`. All 463 scientific files in that range are
preserved. Checkpoints, transient logs, caches, virtual
environments, and the unrelated 44.8 MB historical language-model checkpoint
are deliberately excluded. Raw result JSON, preregistrations, and negative
results are retained.

Licensed under the GNU Affero General Public License v3.0. See [LICENSE](LICENSE).
