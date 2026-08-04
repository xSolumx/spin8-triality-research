# Raw artifacts

This directory contains the JSON outputs that support the research documents.
They are retained as immutable evidence, including failed gates and controls.

- `ARTIFACTS.sha256` at repository root hashes every JSON file here.
- `PROVENANCE.json` records each artifact's source path and extraction hash.
- Checkpoints and transient logs are deliberately excluded; see
  [`docs/REPRODUCIBILITY.md`](../docs/REPRODUCIBILITY.md).

Artifact presence does not upgrade the corresponding claim. Read the matching
preregistration and results document under `docs/experiments/` for the gate,
known confounds, corrections, and interpretation boundary.
