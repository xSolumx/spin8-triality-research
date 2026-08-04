# Reproducibility

## Environment

Use Python 3.11 or newer. For the complete historical suite:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e ".[full]"
```

CUDA is optional. Hardware-specific tests skip when their backend is absent.
Exact SymPy certificates and CPU recurrence checks do not require CUDA.

## Test suite

```bash
python -m unittest discover -s tests -p "test_*.py"
```

The extraction gate passed 111 tests with two expected skips. The theorem
artifact also has a lightweight integrity replay in the foundational tests.

## Exact Dirac-star replay

```bash
python -m spin8_dirac_star \
  --output artifacts/spin8_dirac_star_replay.json
```

The replay is intentionally expensive. It reconstructs two exact rational
coefficient maps, compares them, evaluates exact Bernstein coefficients, and
checks 32 signed off-grid determinants.

Acceptance conditions are frozen in
[SPIN8_DIRAC_STAR_PREREGISTRATION.md](experiments/SPIN8_DIRAC_STAR_PREREGISTRATION.md).

## Artifact integrity

`ARTIFACTS.sha256` contains one SHA-256 entry per published JSON artifact.
On Linux/macOS:

```bash
sha256sum --check ARTIFACTS.sha256
```

On PowerShell, compare `Get-FileHash -Algorithm SHA256` with the manifest.

`PROVENANCE.json` records the original path, extracted destination, byte size,
and SHA-256 hash for every source-derived file.

## Determinism caveat

Exact rational certificates are deterministic. Some CUDA training experiments
are not bitwise deterministic across devices or PyTorch/CUDA releases. The
documents therefore report dense distributions, per-seed results, gate
hierarchies, and raw artifacts rather than silently treating a seed label as a
bitwise-reproducible checkpoint.

## Deliberate exclusions

The public repository does not include:

- virtual environments and caches;
- transient stdout/stderr logs;
- model and compiler checkpoints (`.pt`, `.msgpack`);
- the unrelated historical 44.8 MB language-model checkpoint;
- unrelated applications from the parent monorepo.

These exclusions remove generated payloads, not scientific claims. Frozen JSON
outputs, preregistrations, corrections, negative results, and theorem
certificates are retained.
