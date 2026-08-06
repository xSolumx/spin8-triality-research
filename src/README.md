# Source index

The source remains flat because the historical harnesses import one another by
module name. Editable installation adds this directory to the Python path.

## Maintained Spin(8) algebra and theorem core

- `spin8_triality.py`: vector and chiral representations, Lie algebra checks,
  triality tensor, affine scan primitives.
- `spin8_triality_lift.py`: triangular triality recurrence and binding.
- `spin8_triality_memory.py`: multiplicity-slot memory contracts.
- `spin8_five_probe_identifiability.py`: exact shared-rank and ambiguity gates.
- `spin8_global_probe_certificate.py`: exact integral triality closure proving
  one global five-probe free tuple and a four-probe `su(2)` counterfamily.
- `spin8_coordinate_geometry.py`: exhaustive `F_2^5` classification of all
  coordinate four/five-probe sensors and their exact stabilizer ladder.
- `spin8_continuous_probe_orbits.py`: invariant/principal-orbit certificate
  proving universal four-probe insufficiency and generic mixed five-probe
  global identifiability.
- `intertwiner_schurscan.py`: generic triangular bilinear scan, finite
  homogeneous lift, SO(3) control, and cyclic-feedback degree obstruction.
- `spin8_active_sensing.py`: information operator and sensor metrics.
- `spin8_joint_sensor_retraction.py`: joint sensor-family continuation.
- `spin8_cayley_spectrum.py`: exact Cayley spectrum certificates.
- `spin8_cayley_blocks.py`: exact `8 + 8 + 8 + 4` invariant-block mechanism
  behind the balanced Cayley characteristic law and determinant `81/1024`.
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
- `spin8_dirac_one_edge_holdouts.py`: all 256 exact disjoint determinant
  holdouts and a lightweight stored-artifact verifier.
- `spin8_dirac_one_edge_positivity.py`: staged, crash-resilient integer
  Bernstein/Duffy proof of the final determinant gate.
- `spin8_dirac_two_edge.py`: exact common-symmetry and two-anchor sector audit
  for the preregistered `h=0`, residual-`i` bridge.
- `spin8_dirac_two_edge_attack.py`: uniform, boundary-biased, and optimized
  CUDA falsifier for that bridge; never used for proof signs.

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
