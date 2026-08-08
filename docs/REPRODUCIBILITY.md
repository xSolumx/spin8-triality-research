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
python tools/verify_artifact_manifest.py
```

As of 2026-08-06, the current suite passes 188 tests. The recorded full run was
restricted to six logical processors, completed in 375.8 seconds including the
resource supervisor, and peaked at 4.074 GiB of process-tree resident memory.
The edge-theorem unit test is a lightweight
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
sequential recurrence, checks noncommutative irregular-length order and
gradients, exercises a length-2,048 contract, and checks an SO(3) cross-product
control.

## Intertwiner SchurScan benchmark

The benchmark records eager tensor-program behavior; it does not claim a fused
production kernel. CPU execution is capped at six threads.

```powershell
$env:PYTHONPATH = "src"
python -m pytest -q `
  tests/test_intertwiner_schurscan.py `
  tests/test_benchmark_intertwiner_schurscan.py

python -m benchmark_intertwiner_schurscan `
  --device cuda --dtype float32 --batch 8 `
  --lengths 16 32 64 128 256 512 1024 2048 4096 `
  --warmup 5 --repeats 15 --backward-max-length 256 `
  --lift-max-length 32 --threads 6 `
  --output artifacts/intertwiner_schurscan_cuda_replay.json
```

Canonical 2026-08-07 hardware results and checksums are listed in
[`INTERTWINER_SCHURSCAN_BENCHMARK_RESULTS.md`](experiments/INTERTWINER_SCHURSCAN_BENCHMARK_RESULTS.md).

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

## Publication theorem extensions

The Cayley design-criterion laws, the forced-factor reduction of the signed
star certificate, and an independent FLINT arithmetic replay are reproduced
with:

```powershell
$env:PYTHONPATH = "src"
python -m spin8_cayley_blocks
python -m spin8_cayley_flag `
  --output artifacts/spin8_cayley_flag_replay.json
python -m spin8_cayley_criteria `
  --output artifacts/spin8_cayley_criteria_replay.json
python -m spin8_dirac_star_structure `
  --output artifacts/spin8_dirac_star_structure_replay.json
python -m spin8_dirac_star_foundations `
  --output artifacts/spin8_dirac_star_foundations_replay.json
python -m spin8_publication_flint_crosscheck `
  --threads 6 `
  --output artifacts/spin8_publication_flint_crosscheck_replay.json
python -m unittest discover -s tests `
  -p "test_spin8_publication_theorems.py" -v
```

The FLINT pass repeats the rational polynomial divisions, derivative
identities, endpoint eigenvalue slopes, and all 1,907 reduced Bernstein
coefficients. It deliberately accepts the maintained rational coefficient
maps as input; the full star replay above remains the independent check that
regenerates those maps from exact determinant samples.

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

The complete equality-set audit reuses those proof objects and reconstructs
the exact zero-control supports under the same six-core limit:

```powershell
$env:PYTHONPATH = "src"
python -m spin8_dirac_one_edge_equality `
  --reconstruction artifacts/spin8_dirac_one_edge_exact_20260804.json `
  --cache artifacts/spin8_dirac_one_edge_determinant_cache_20260806.json `
  --assembled artifacts/spin8_dirac_one_edge_duffy_20260806.json `
  --workers 6 `
  --output artifacts/spin8_dirac_one_edge_equality_replay.json
```

The exact two-edge endpoint-jet flag law is lightweight to replay from the
published sector maps:

```powershell
$env:PYTHONPATH = "src"
python -m spin8_dirac_two_edge_endpoints `
  --coefficients artifacts/spin8_dirac_two_edge_all_sectors_coefficients_20260806.json `
  --output artifacts/spin8_dirac_two_edge_endpoints_replay.json
```

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
