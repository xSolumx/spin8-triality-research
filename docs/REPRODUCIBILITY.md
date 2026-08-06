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

The current suite passes 130 tests. The edge-theorem unit test is a lightweight
artifact verifier: it reconstructs the stored polynomials and Bernstein arrays,
directly compares both stored coefficient maps, requires complete equality
between stored and freshly recomputed symmetry/divisibility records, and
recomputes all 256 signed holdouts. It deliberately does not rerun the
interpolation grids.

The global five-probe unit test independently regenerates its integral
triality closure, exact generator annihilators, `su(2)` commutators, and
withheld-probe motions. It also checks that modifying a stored rank causes the
verifier to reject the report.

The coordinate-geometry test checks all 52,752 multiview coordinate sensors,
recomputes exact rational Lie ranks for all 141 distinct closures, and verifies
the `SU(3) -> SU(2) -> trivial` representative chain. The generic SchurScan
test independently compares its staged scan and finite homogeneous lift with
sequential recurrence and checks an SO(3) cross-product control.

The continuous-orbit test recomputes exact invariant tangent ranks, action
ranks, stabilizer brackets/Killing forms, and one globally free closure for
every mixed five-probe allocation. The compact principal-orbit theorem is the
mathematical inference layer connecting those exact certificates to the global
generic and universal claims.

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

## Exact Cayley-null edge-family replay

```bash
python -m spin8_dirac_edge \
  --output artifacts/spin8_dirac_edge_replay.json
```

This proof-bearing replay constructs the symbolic boundary-nullspace
certificate, derives the Walsh symmetry restriction, reconstructs two exact
coefficient maps on disjoint five-node grids, checks all 256 off-grid signed
determinants, and verifies the native Bernstein certificate. Acceptance
conditions are recorded in
[SPIN8_DIRAC_EDGE_PREREGISTRATION.md](experiments/SPIN8_DIRAC_EDGE_PREREGISTRATION.md).

The exact conditional-decorrelation counterexample has a faster replay:

```bash
python -m spin8_conditional_counterexample \
  --output artifacts/spin8_conditional_counterexample_replay.json
```

## Hardware-tuned variable-Cayley determinant replay

The final one-edge determinant certificate is intentionally staged so the
large SymPy polynomial and the million-control integer tensors never coexist.
On the reference workstation (8-core i7-9700K, 24 GB RAM, RTX 2070 SUPER), use
FLINT-backed exact arithmetic for the CPU stages. CUDA is used only for the
separate falsifier and never supplies proof signs.

```powershell
$env:SYMPY_GROUND_TYPES = "flint"
$env:PYTHONPATH = "src"
python -m spin8_dirac_one_edge_positivity determinant `
  --reconstruction artifacts/spin8_dirac_one_edge_exact_20260804.json `
  --output build/one_edge_positivity/determinant.json
python -m spin8_dirac_one_edge_positivity lower `
  --cache build/one_edge_positivity/determinant.json `
  --output build/one_edge_positivity/lower.json
python -m spin8_dirac_one_edge_positivity upper `
  --cache build/one_edge_positivity/determinant.json `
  --output build/one_edge_positivity/upper.json
python -m spin8_dirac_one_edge_positivity boundary `
  --reconstruction artifacts/spin8_dirac_one_edge_exact_20260804.json `
  --output build/one_edge_positivity/boundary.json
python -m spin8_dirac_one_edge_holdouts `
  --reconstruction artifacts/spin8_dirac_one_edge_exact_20260804.json `
  --workers 4 `
  --output build/one_edge_positivity/holdouts.json
python -m spin8_dirac_one_edge_positivity assemble `
  --reconstruction artifacts/spin8_dirac_one_edge_exact_20260804.json `
  --cache build/one_edge_positivity/determinant.json `
  --lower build/one_edge_positivity/lower.json `
  --upper build/one_edge_positivity/upper.json `
  --boundary build/one_edge_positivity/boundary.json `
  --lower-order artifacts/spin8_dirac_one_edge_positivity_20260804.json `
  --holdouts build/one_edge_positivity/holdouts.json `
  --output artifacts/spin8_dirac_one_edge_positivity_replay.json
```

Install `python-flint` to enable the optimized exact backend. The committed
2026-08-06 artifact records the completed exact theorem. The 10 MB published
determinant cache may replace the first stage when replaying later stages, but
its SHA-256 link to the reconstruction must still pass.

### Enforced workstation envelope

For any expensive stage on the reference i7-9700K, use the bounded runner:

```powershell
$env:PYTHONPATH = "src"
python -m spin8_resource_limits --workers 6 --memory-gib 15 -- `
  python -m <module> <arguments>
```

This pins the complete process tree to six logical cores, caps common native
thread pools, selects the FLINT SymPy ground domain, records peak process-tree
RSS, and terminates the stage at 15 GiB. The one-GiB margin keeps the symbolic
process below the requested 16-GiB ceiling despite watchdog sampling latency.

`spin8_flint_crosscheck.py` is the independent arithmetic check. Merely setting
`SYMPY_GROUND_TYPES=flint` improves speed but is not counted as independent
verification.

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
