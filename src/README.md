# Source index

The source remains flat because the historical harnesses import one another by
module name. Editable installation adds this directory to the Python path.

## Maintained Spin(8) algebra and theorem core

- `spin8_triality.py`: vector and chiral representations, Lie algebra checks,
  triality tensor, affine scan primitives.
- `spin8_triality_lift.py`: triangular triality recurrence and binding.
- `spin8_triality_memory.py`: multiplicity-slot memory contracts.
- `spin8_five_probe_identifiability.py`: exact shared-rank and ambiguity gates.
- `spin8_active_sensing.py`: information operator and sensor metrics.
- `spin8_joint_sensor_retraction.py`: joint sensor-family continuation.
- `spin8_cayley_spectrum.py`: exact Cayley spectrum certificates.
- `spin8_dirac_gram.py`: projector geometry, Schur reduction, and falsifiers.
- `spin8_dirac_star.py`: independently replayed rational Bernstein theorem.
- `spin8_conditional_counterexample.py`: exact rational falsifier for naive
  Cholesky decorrelation.
- `spin8_dirac_edge.py`: exact Cayley-null four-correlation theorem with
  symbolic degree, symmetry, and Bernstein certificates.
- `spin8_dirac_one_edge.py`: variable-Cayley one-edge falsifier and exact
  four-sector Walsh audit.
- `spin8_dirac_one_edge_exact.py`: disjoint-grid reconstruction and
  tetrahedral principal-minor certificate utilities.
- `spin8_dirac_one_edge_positivity.py`: staged, crash-resilient integer
  Bernstein/Duffy replay for the still-open final determinant gate.

## Blind action and addressing line

- `spin8_blind_shared_action.py`
- `spin8_learned_address.py`
- `spin8_continuous_alias.py`
- `spin8_blind_alias_action.py`
- `spin8_masked_completion.py`
- `spin8_triality_identifiability.py`

## Group-action and compiler lineage

- `mechanistic_group_actions.py`, `representation_retraction.py`, and
  `latent_group_discovery.py` contain the A5 mechanism and shared-family
  compiler work.
- `q8_spinor_*` and `spin8_q8_*` contain the center-fidelity, regular-orbit,
  path-section, and observer-transport experiments.
- `spin8_table_blind_*`, `spin8_state_only_*`, and `spin8_finest_congruence_*`
  progressively remove tables, labels, and supplied state cardinality.
- `action_congruence_lattice.py` and the `*_lattice_audit.py` files certify the
  complete recovered congruence structure.

## Recurrence baselines

- `ga_ssm.py`, `GALib.py`, and `rotor_ssm_torch.py` are the maintained GA
  recurrence implementations.
- `recurrence_families_torch.py` and `compare_recurrences.py` implement the
  matched real, complex, quaternion, Householder, and rotor ladder.
- `schur_scan.py` implements the full isotypic multiplicity commutant and
  associative Schur-affine scan.
- `GA-SSM-1.py` through `GA-SSM-3.py` are retained research history, not the
  maintained interface.

For scientific interpretation, start with
[`docs/RESEARCH_MAP.md`](../docs/RESEARCH_MAP.md), not with an isolated script.
