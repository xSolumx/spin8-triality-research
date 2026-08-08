"""Machine-readable evidence contracts for the maintained research gates.

This module does not prove any mathematical claim.  Its purpose is narrower:
it prevents one evidence layer from being reported as another.  In particular,
an artifact hash is not an algebraic replay, a numerical search is not a
positivity certificate, and a passing implementation test is not an empirical
architecture comparison.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STATUSES = {
    "operational",
    "validated_implementation",
    "empirical",
    "proved_exact",
    "proved_hybrid",
    "exact_negative",
    "exact_reduction",
    "numerical_only",
    "open",
}

EVIDENCE_LAYERS = {
    "artifact_hash",
    "static_contract",
    "resource_contract",
    "exact_arithmetic",
    "symbolic_identity",
    "exact_reconstruction",
    "positivity_certificate",
    "exact_counterexample",
    "external_theorem",
    "floating_point_falsifier",
    "raw_artifact",
    "checkpoint_replay",
    "implementation_parity",
    "negative_control",
    "multi_seed",
}


@dataclass(frozen=True)
class GateContract:
    """The acceptance boundary for one current claim family."""

    gate_id: str
    claim: str
    status: str
    evidence_layers: tuple[str, ...]
    test_suites: tuple[str, ...]
    artifacts: tuple[str, ...]
    boundary_obligations: tuple[str, ...]
    limitations: tuple[str, ...]
    replay_tier: str
    external_inputs: tuple[str, ...] = ()


GATES: tuple[GateContract, ...] = (
    GateContract(
        gate_id="repository_integrity",
        claim="Published bytes, relative links, notation delimiters, and bounded-run settings agree with the maintained archive contract.",
        status="operational",
        evidence_layers=("artifact_hash", "static_contract", "resource_contract"),
        test_suites=(
            "tests/test_artifact_manifest.py",
            "tests/test_documentation_contract.py",
            "tests/test_gate_contracts.py",
            "tests/test_spin8_resource_limits.py",
        ),
        artifacts=(),
        boundary_obligations=(
            "A hash match checks bytes, not mathematical truth.",
            "The documentation audit is syntactic and link-level, not a semantic proof.",
            "Resource tests verify configured ceilings, not worst-case complexity.",
        ),
        limitations=("This gate cannot promote any scientific claim.",),
        replay_tier="unit",
    ),
    GateContract(
        gate_id="ga_ssm_streaming_contract",
        claim="The maintained rotor SSM implementations expose constant recurrent state and agree across full, chunked, and token-streaming execution.",
        status="validated_implementation",
        evidence_layers=("implementation_parity", "negative_control"),
        test_suites=("tests/test_ga_ssm.py", "tests/test_rotor_ssm_torch.py"),
        artifacts=(),
        boundary_obligations=(
            "Identity initialization must retain a nonzero tangent gradient.",
            "Long scans must agree within declared floating-point tolerance.",
            "CUDA coverage is conditional on CUDA availability and is reported separately.",
        ),
        limitations=(
            "Correct recurrence and gradients do not establish a sequence-model advantage.",
        ),
        replay_tier="unit",
    ),
    GateContract(
        gate_id="finite_group_recurrence_evidence",
        claim="The finite-group harness implements the stated fixed-action, compiler, holonomy, and streaming controls and preserves the archived cohort results.",
        status="empirical",
        evidence_layers=(
            "implementation_parity",
            "negative_control",
            "raw_artifact",
            "multi_seed",
        ),
        test_suites=("tests/test_recurrence_harness.py",),
        artifacts=(
            "artifacts/mechanistic_a5_ga_holonomy_multiscale_dense_seed0_1500.json",
            "artifacts/q8_spinor_quality_gate_validation_dense_seeds10_19.json",
        ),
        boundary_obligations=(
            "Functional accuracy, positive margin, and raw homomorphism gates remain distinct.",
            "Held-out words do not by themselves test changed-generator transfer.",
            "Pure fixed-token operators structurally compose unseen bigrams.",
        ),
        limitations=(
            "Most training checkpoints are not published, so the archive verifies harness semantics and raw reports but cannot retrain every historical cohort.",
        ),
        replay_tier="artifact_only_empirical",
    ),
    GateContract(
        gate_id="triangular_schurscan",
        claim="A triangular bilinear recurrence with an equivariant intertwiner admits two associative affine scans and a finite homogeneous lift.",
        status="proved_exact",
        evidence_layers=(
            "exact_arithmetic",
            "symbolic_identity",
            "implementation_parity",
        ),
        test_suites=("tests/test_intertwiner_schurscan.py",),
        artifacts=("artifacts/intertwiner_schurscan_20260806.json",),
        boundary_obligations=(
            "The staged parallel scan must equal the sequential recurrence.",
            "The SO(3) control must reduce to the cross product.",
            "State-dependent feedback is excluded by the degree obstruction.",
        ),
        limitations=("This theorem is not specific evidence of a Spin(8) advantage.",),
        replay_tier="unit",
    ),
    GateContract(
        gate_id="triality_algebra_and_memory",
        claim="The maintained Spin(8) triality tensor is equivariant, unit-key binding is exactly invertible, and the staged memory recurrences obey their algebraic contracts.",
        status="proved_exact",
        evidence_layers=(
            "exact_arithmetic",
            "symbolic_identity",
            "implementation_parity",
        ),
        test_suites=("tests/test_foundational_contracts.py",),
        artifacts=("artifacts/intertwiner_schurscan_20260806.json",),
        boundary_obligations=(
            "Single-pair inversion is separated from multi-pair superposition capacity.",
            "Multiplicity-slot capacity is rank-limited by the number of channels.",
            "Any nonlinear cleanup remains outside the associative recurrence.",
        ),
        limitations=(
            "Exact binding is not a high-capacity VSA result and does not establish a retrieval advantage.",
        ),
        replay_tier="bounded_full",
    ),
    GateContract(
        gate_id="shared_family_retraction",
        claim="Jointly constrained action and address families complete held-out relational structure that independently normalized controls leave underidentified.",
        status="empirical",
        evidence_layers=(
            "raw_artifact",
            "multi_seed",
            "negative_control",
            "implementation_parity",
        ),
        test_suites=("tests/test_foundational_contracts.py",),
        artifacts=(
            "artifacts/spin8_blind_shared_action_seeds0_9.json",
            "artifacts/spin8_joint_sensor_retraction_seeds20_29.json",
            "artifacts/spin8_learned_address_seeds0_9.json",
            "artifacts/spin8_continuous_alias_seeds0_9.json",
        ),
        boundary_obligations=(
            "Independent controls must fit the supplied observations before failure is informative.",
            "Direct transport and binding paths must be tested separately to exclude bypasses.",
            "Logical-ID and continuous-alias regimes must not be conflated.",
        ),
        limitations=(
            "The direct-memory control also succeeds in the latent-address task; that result supports shared-family retraction, not a triality-specific advantage.",
        ),
        replay_tier="artifact_only_empirical",
    ),
    GateContract(
        gate_id="four_vs_five_probe_identifiability",
        claim="Four shared triality probes retain a positive-dimensional principal stabilizer, whereas every mixed five-probe allocation has a nonempty open free stratum.",
        status="proved_hybrid",
        evidence_layers=("exact_arithmetic", "symbolic_identity", "external_theorem"),
        test_suites=(
            "tests/test_global_five_probe_certificate.py",
            "tests/test_spin8_continuous_probe_orbits.py",
            "tests/test_spin8_coordinate_geometry.py",
        ),
        artifacts=(
            "artifacts/spin8_global_five_probe_certificate_20260806.json",
            "artifacts/spin8_continuous_probe_orbits_20260806.json",
            "artifacts/spin8_coordinate_geometry_20260806.json",
        ),
        boundary_obligations=(
            "Single-view and mixed-view allocations have different four-probe stabilizers.",
            "Generic freeness is not the claim that every five-probe configuration is free.",
            "Independent per-view actions are outside the shared-action theorem.",
        ),
        limitations=(
            "The theorem is an identifiability result, not a conditioning bound.",
        ),
        replay_tier="bounded_full",
        external_inputs=(
            "The principal-orbit theorem for smooth compact-group actions: every isotropy contains a conjugate of the principal isotropy, and the principal stratum is open and dense.",
        ),
    ),
    GateContract(
        gate_id="balanced_cayley_information_family",
        claim="The orthonormal balanced information family has the exact 8+8+8+4 block spectrum and determinant (1-z)^3(9-z)^2/1024, with z=c^2.",
        status="proved_hybrid",
        evidence_layers=(
            "exact_arithmetic",
            "symbolic_identity",
            "external_theorem",
        ),
        test_suites=(
            "tests/test_foundational_contracts.py",
            "tests/test_cayley_referee_package.py",
            "tests/test_spin8_publication_theorems.py",
        ),
        artifacts=(
            "artifacts/spin8_cayley_blocks_20260806.json",
            "artifacts/spin8_cayley_criteria_20260806.json",
            "artifacts/spin8_cayley_flag_20260806.json",
        ),
        boundary_obligations=(
            "The endpoints z=1 have exact rank 25 and three equal first-order losses.",
            "The Cayley-null point z=0 is regular in the oriented cover but a boundary after c and -c are identified.",
            "The exact flag calculation excludes an internal continuous split invariant.",
        ),
        limitations=(
            "Local Lie-rank calculations do not prove the global orbit classification.",
            "The family theorem does not establish global five-query optimality.",
        ),
        replay_tier="external_plus_exact",
        external_inputs=(
            "Classical cohomogeneity-one classification of the Spin(7) action on the oriented Grassmannian of four-planes.",
        ),
    ),
    GateContract(
        gate_id="balanced_local_exact_design",
        claim="The balanced equal-five configuration is a strict local exact-design optimum modulo symmetry.",
        status="proved_exact",
        evidence_layers=("exact_arithmetic", "symbolic_identity"),
        test_suites=("tests/test_spin8_five_query_local_geometry.py",),
        artifacts=("artifacts/spin8_five_query_local_geometry_20260806.json",),
        boundary_obligations=(
            "The quotient Hessian removes symmetry zero modes.",
            "A finite circle atlas checks non-coordinate tangent directions.",
        ),
        limitations=(
            "Local optimality is not global optimality across all allocations.",
        ),
        replay_tier="unit",
    ),
    GateContract(
        gate_id="approximate_design_domain",
        claim="The eight-support isotropic design is D-optimal in the approximate-design domain, and exact five-query weights cannot realize that shortcut.",
        status="proved_hybrid",
        evidence_layers=(
            "exact_arithmetic",
            "symbolic_identity",
            "negative_control",
            "external_theorem",
        ),
        test_suites=("tests/test_spin8_approximate_design_audit.py",),
        artifacts=("artifacts/spin8_approximate_design_audit_20260806.json",),
        boundary_obligations=(
            "Exact-design and approximate-design feasible sets are kept separate.",
            "The Kiefer-Wolfowitz sensitivity equality is checked exactly.",
        ),
        limitations=(
            "This does not settle the equal-weight five-query exact-design problem.",
        ),
        replay_tier="unit",
        external_inputs=(
            "The Kiefer--Wolfowitz general equivalence theorem for D-optimal approximate designs.",
        ),
    ),
    GateContract(
        gate_id="d4_24cell_bridge",
        claim="The maintained D4/24-cell bridge identities hold exactly, together with the recorded non-equivalence certificate.",
        status="proved_exact",
        evidence_layers=("exact_arithmetic", "symbolic_identity"),
        test_suites=("tests/test_spin8_d4_24cell_bridge.py",),
        artifacts=("artifacts/spin8_d4_24cell_bridge_20260806.json",),
        boundary_obligations=(
            "The bridge identity and the non-equivalence statement are tested independently.",
        ),
        limitations=(
            "The bridge does not transfer optimality between inequivalent design domains.",
        ),
        replay_tier="unit",
    ),
    GateContract(
        gate_id="signed_star_dirac_gram",
        claim="The strengthened Dirac--Gram inequality and its complete equality classification hold on the full four-parameter signed-star ansatz.",
        status="proved_exact",
        evidence_layers=(
            "exact_arithmetic",
            "exact_reconstruction",
            "symbolic_identity",
            "positivity_certificate",
        ),
        test_suites=(
            "tests/test_foundational_contracts.py",
            "tests/test_spin8_publication_theorems.py",
        ),
        artifacts=(
            "artifacts/spin8_dirac_star_20260804.json",
            "artifacts/spin8_dirac_star_foundations_20260806.json",
            "artifacts/spin8_dirac_star_structure_20260806.json",
        ),
        boundary_obligations=(
            "Circle-quotient divisibility is proved before interpolation.",
            "Both orientation signs and disjoint exact grids are checked.",
            "Equality is classified as z=1 or the orthonormal star centre.",
        ),
        limitations=("Three residual Cholesky correlations lie outside this ansatz.",),
        replay_tier="expensive_exact",
    ),
    GateContract(
        gate_id="conditional_decorrelation_map",
        claim="Monotone removal of the selected residual correlations at fixed star coordinates and normalized Cayley invariant is false.",
        status="exact_negative",
        evidence_layers=("exact_arithmetic", "exact_counterexample"),
        test_suites=("tests/test_foundational_contracts.py",),
        artifacts=("artifacts/spin8_conditional_counterexample_20260804.json",),
        boundary_obligations=(
            "The rational witness includes an exact positive-definite Gram certificate.",
            "Only the specified deformation is falsified, not every invariant-preserving path.",
        ),
        limitations=(
            "The unrestricted Dirac--Gram inequality is not falsified by this witness.",
        ),
        replay_tier="unit",
    ),
    GateContract(
        gate_id="variable_cayley_one_edge",
        claim="The strengthened Dirac--Gram inequality and equality set hold on the variable-Cayley one-residual-edge family.",
        status="proved_exact",
        evidence_layers=(
            "exact_arithmetic",
            "exact_reconstruction",
            "symbolic_identity",
            "positivity_certificate",
        ),
        test_suites=(
            "tests/test_foundational_contracts.py",
            "tests/test_spin8_publication_theorems.py",
        ),
        artifacts=(
            "artifacts/spin8_dirac_one_edge_determinant_cache_20260806.json",
            "artifacts/spin8_dirac_one_edge_duffy_20260806.json",
            "artifacts/spin8_dirac_one_edge_equality_20260806.json",
        ),
        boundary_obligations=(
            "Both Duffy charts and their common boundary are certified.",
            "Exact holdouts are distinct from reconstruction nodes.",
            "Equality is z=1 or the orthonormal one-edge centre.",
        ),
        limitations=(
            "The second and third residual Cholesky edges remain outside this family.",
        ),
        replay_tier="expensive_exact",
    ),
    GateContract(
        gate_id="multiplicity_gauge",
        claim="The multiplicity-space gauge reduction and its rank statement hold exactly on the declared representation.",
        status="proved_exact",
        evidence_layers=("exact_arithmetic", "symbolic_identity"),
        test_suites=("tests/test_spin8_multiplicity_gauge.py",),
        artifacts=("artifacts/spin8_multiplicity_gauge_20260806.json",),
        boundary_obligations=("Gauge and physical directions are counted separately.",),
        limitations=(
            "A gauge count is not an optimization or generalization theorem.",
        ),
        replay_tier="unit",
    ),
    GateContract(
        gate_id="two_edge_exact_reconstruction",
        claim="All eight symmetry-allowed two-edge sector polynomials have been reconstructed exactly and checked on disjoint exact holdouts.",
        status="exact_reduction",
        evidence_layers=(
            "exact_arithmetic",
            "exact_reconstruction",
            "symbolic_identity",
        ),
        test_suites=(
            "tests/test_spin8_dirac_two_edge.py",
            "tests/test_spin8_dirac_two_edge_amplitude.py",
            "tests/test_spin8_dirac_two_edge_reconstruct.py",
            "tests/test_spin8_dirac_two_edge_shared_reconstruct.py",
        ),
        artifacts=(
            "artifacts/spin8_dirac_two_edge_all_sectors_coefficients_20260806.json",
            "artifacts/spin8_dirac_two_edge_all_sectors_holdouts_20260806.json",
            "artifacts/spin8_dirac_two_edge_amplitude_20260806.json",
        ),
        boundary_obligations=(
            "Walsh support follows from exact common-triality symmetries.",
            "Every determinant boundary branch has the declared rank loss.",
            "Reconstruction identity is separated from sign certification.",
        ),
        limitations=(
            "Exact polynomial recovery does not prove the recovered margins nonnegative.",
        ),
        replay_tier="expensive_exact",
    ),
    GateContract(
        gate_id="two_edge_local_kernel",
        claim="The second residual edge is locally nonnegative at the orthonormal equality line, while the proposed global quadratic-Schur proof strategy has an exact counterexample.",
        status="exact_negative",
        evidence_layers=(
            "exact_arithmetic",
            "symbolic_identity",
            "exact_counterexample",
        ),
        test_suites=(
            "tests/test_spin8_dirac_two_edge_kernel.py",
            "tests/test_spin8_dirac_two_edge_kernel_flint.py",
        ),
        artifacts=(
            "artifacts/spin8_dirac_two_edge_orthonormal_transverse_20260806.json",
            "artifacts/spin8_two_edge_kernel_flint_20260806.json",
        ),
        boundary_obligations=(
            "Odd transverse derivatives vanish on the equality line.",
            "The exact counterexample rejects only the quadratic-Schur certificate strategy.",
            "FLINT independently replays the SymPy jet arithmetic.",
        ),
        limitations=("Local nonnegativity does not imply global two-edge positivity.",),
        replay_tier="bounded_full",
    ),
    GateContract(
        gate_id="two_edge_finite_polynomial_gate",
        claim="The two-edge problem reduces reversibly to four degree-six and four degree-twelve radical-free polynomial inequalities, with a proved endpoint-jet structure.",
        status="exact_reduction",
        evidence_layers=(
            "exact_arithmetic",
            "symbolic_identity",
            "floating_point_falsifier",
        ),
        test_suites=(
            "tests/test_spin8_dirac_two_edge_finite.py",
            "tests/test_spin8_publication_theorems.py",
        ),
        artifacts=(
            "artifacts/spin8_dirac_two_edge_endpoints_20260806.json",
            "artifacts/spin8_two_edge_finite_falsifier_20260806.json",
            "artifacts/spin8_dirac_two_edge_atlas_20260807.json",
        ),
        boundary_obligations=(
            "Both signs introduced by radical elimination remain explicit.",
            "The i2=1 endpoint core and first transverse jet are checked exactly in all eight sectors.",
            "Interior GPU search is a falsifier only.",
        ),
        limitations=(
            "This reduction is now joined to a separate global atlas certificate; it still does not cover the final h residual.",
        ),
        replay_tier="bounded_full",
    ),
    GateContract(
        gate_id="two_edge_global_positivity",
        claim="All eight finite two-edge polynomial margins are nonnegative on their complete feasible domain.",
        status="proved_exact",
        evidence_layers=(
            "exact_arithmetic",
            "exact_reconstruction",
            "positivity_certificate",
        ),
        test_suites=(
            "tests/test_spin8_dirac_two_edge_finite.py",
            "tests/test_spin8_publication_theorems.py",
        ),
        artifacts=(
            "artifacts/spin8_dirac_two_edge_all_sectors_coefficients_20260806.json",
            "artifacts/spin8_dirac_two_edge_atlas_20260807.json",
        ),
        boundary_obligations=(
            "Both children of every triangular split must be retained in the cover.",
            "Every interval-indeterminate control must receive exact integer replay.",
            "The certificate covers non-vertex interiors and all chart boundaries.",
        ),
        limitations=(
            "The theorem is confined to the frozen h=0 two-edge family and does not classify its complete equality set.",
        ),
        replay_tier="expensive_exact",
    ),
    GateContract(
        gate_id="global_five_query_exact_design",
        claim="The balanced equal-five allocation is globally D-optimal among all exact five-query allocations and nonorthogonal probes.",
        status="open",
        evidence_layers=("floating_point_falsifier", "raw_artifact", "multi_seed"),
        test_suites=("tests/test_spin8_gpu_design_audit.py",),
        artifacts=("artifacts/spin8_gpu_design_cohort_20260806.json",),
        boundary_obligations=(
            "Every allocation, nonorthogonal interior deformation, and rank-deficient boundary must be addressed.",
            "Kiefer-Wolfowitz approximate-design optimality cannot substitute for this exact-design gate.",
        ),
        limitations=(
            "Open: the current GPU campaign is a counterexample search only.",
        ),
        replay_tier="open",
    ),
    GateContract(
        gate_id="final_residual_exact_bridge",
        claim="The unrestricted chart has a 16-sector sign reduction of degree at most four in h^2, and the complete h-extension of the former equality slice satisfies the strengthened Dirac--Gram inequality.",
        status="proved_exact",
        evidence_layers=(
            "exact_arithmetic",
            "symbolic_identity",
            "positivity_certificate",
        ),
        test_suites=("tests/test_spin8_publication_theorems.py",),
        artifacts=("artifacts/spin8_dirac_final_residual_20260807.json",),
        boundary_obligations=(
            "The exact equality-slice determinant must be reduced in the two circle relations.",
            "Every floating-positive near-singular candidate must be rationalized and replayed exactly.",
            "The sign reduction must retain all 16 quotient characters and both h and H boundary factors.",
        ),
        limitations=(
            "The exact positivity theorem is confined to a=d=e=g=i=0; the 16-sector reduction does not certify global sign in the other six variables.",
        ),
        replay_tier="bounded_full",
    ),
    GateContract(
        gate_id="unrestricted_dirac_gram",
        claim="The strengthened Dirac--Gram inequality holds on the unrestricted feasible Gram--Cayley domain.",
        status="open",
        evidence_layers=(
            "exact_arithmetic",
            "symbolic_identity",
            "exact_reconstruction",
            "floating_point_falsifier",
        ),
        test_suites=(
            "tests/test_spin8_dirac_two_edge_finite.py",
            "tests/test_spin8_publication_theorems.py",
        ),
        artifacts=(
            "artifacts/spin8_dirac_two_edge_atlas_20260807.json",
            "artifacts/spin8_dirac_final_residual_20260807.json",
            "artifacts/spin8_dirac_unrestricted_structure_20260807.json",
            "artifacts/spin8_dirac_unrestricted_comparison_20260807.json",
            "artifacts/spin8_dirac_unrestricted_tangent_20260807.json",
            "artifacts/spin8_dirac_unrestricted_core_20260807.json",
            "artifacts/spin8_dirac_unrestricted_energy_20260807.json",
            "artifacts/spin8_dirac_endpoint_klein_face_20260807.json",
            "artifacts/spin8_two_edge_finite_falsifier_20260806.json",
        ),
        boundary_obligations=(
            "All 16 final-residual sectors, non-vertex interiors, and singular boundaries must receive a domain-wide sign certificate.",
        ),
        limitations=(
            "Open: the exact equality slice and final-axis degree reduction do not imply global positivity in the other six variables.",
        ),
        replay_tier="open",
    ),
    GateContract(
        gate_id="unrestricted_polynomial_identity",
        claim="The unrestricted Dirac--Gram margin has an exact sixteen-sector seven-variable polynomial representation, exact local endpoint control, and an exact global full-sector Fourier-energy bound.",
        status="exact_reduction",
        evidence_layers=(
            "exact_arithmetic",
            "symbolic_identity",
            "exact_reconstruction",
        ),
        test_suites=("tests/test_spin8_publication_theorems.py",),
        artifacts=(
            "artifacts/spin8_dirac_unrestricted_structure_20260807.json",
            "artifacts/spin8_dirac_unrestricted_coefficients_20260807/alpha_summary.json",
            "artifacts/spin8_dirac_unrestricted_coefficients_20260807/beta_summary.json",
            "artifacts/spin8_dirac_unrestricted_comparison_20260807.json",
            "artifacts/spin8_dirac_unrestricted_tangent_20260807.json",
            "artifacts/spin8_dirac_unrestricted_core_20260807.json",
            "artifacts/spin8_dirac_unrestricted_energy_20260807.json",
            "artifacts/spin8_dirac_endpoint_klein_face_20260807.json",
        ),
        boundary_obligations=(
            "The two complete coefficient maps must agree exactly on disjoint rational grids.",
            "Fresh rational holdouts must recompute all sixteen sectors from direct determinants.",
            "The calibrated endpoint requires a weighted fourth-order blow-up because the tangent cone is degenerate there.",
            "The coupled-core Bernstein theorem is restricted to c^2<=2/3 and does not absorb the other thirteen sectors.",
            "The full-sector Fourier-energy theorem controls the RMS Walsh deviation on the complete seven-cube; an L2 bound does not establish every physical margin.",
            "The first four elementary-symmetric orientation invariants are globally nonnegative; e5 through e16 remain open.",
            "The complete ua=uh=0, c^2=1 endpoint face is positive by an exact Klein-four group-circulant principal-minor certificate; other endpoint faces remain open.",
        ),
        limitations=(
            "Exact reconstruction and local positivity do not prove global nonnegativity on the seven-cube.",
        ),
        replay_tier="expensive_exact",
    ),
    GateContract(
        gate_id="triality_specific_ml_advantage",
        claim="Triality transport improves state efficiency, extrapolation, sample efficiency, or measured throughput over matched modern memory baselines.",
        status="open",
        evidence_layers=("raw_artifact", "negative_control"),
        test_suites=(
            "tests/test_recurrence_harness.py",
            "tests/test_foundational_contracts.py",
        ),
        artifacts=("artifacts/spin8_learned_address_seeds0_9.json",),
        boundary_obligations=(
            "Direct slot memory, delta-rule memory, Householder transport, diagonal complex SSMs, and measured-throughput controls must be budget matched.",
            "A shared-family retraction win is not automatically a triality win.",
        ),
        limitations=("Open: no decisive matched modern-baseline campaign exists.",),
        replay_tier="open",
    ),
    GateContract(
        gate_id="independent_exact_backend_crosscheck",
        claim="Selected publication-critical rational identities agree between SymPy and python-flint implementations.",
        status="operational",
        evidence_layers=("exact_arithmetic", "negative_control"),
        test_suites=(
            "tests/test_spin8_flint_crosscheck.py",
            "tests/test_spin8_publication_theorems.py",
        ),
        artifacts=(
            "artifacts/spin8_flint_crosscheck_20260806.json",
            "artifacts/spin8_publication_flint_crosscheck_20260806.json",
        ),
        boundary_obligations=(
            "Crosschecks must reconstruct independently rather than deserialize one backend's coefficients into the other.",
        ),
        limitations=(
            "Backend agreement supports arithmetic reliability; it is not a proof of an unstated inference.",
        ),
        replay_tier="unit",
    ),
    GateContract(
        gate_id="schurscan_backend_benchmark",
        claim="The maintained eager SchurScan benchmark records work, parity, and bounded CPU/CUDA forward and training timings for the stated hardware and tensor programs.",
        status="empirical",
        evidence_layers=("raw_artifact", "implementation_parity", "negative_control"),
        test_suites=("tests/test_benchmark_intertwiner_schurscan.py",),
        artifacts=(
            "artifacts/intertwiner_schurscan_cpu_i7_9700k_20260807.json",
            "artifacts/intertwiner_schurscan_cuda_rtx2070s_20260807.json",
            "artifacts/intertwiner_schurscan_cpu_training_i7_9700k_20260807.json",
            "artifacts/intertwiner_schurscan_cuda_training_rtx2070s_20260807.json",
        ),
        boundary_obligations=(
            "Tree and Hillis--Steele implementations must agree with the sequential recurrence before timing is interpreted.",
            "Work counts, dependency depth, and observed latency remain separate quantities.",
            "Forward and full-gradient timing are reported separately on the named hardware.",
        ),
        limitations=(
            "These eager PyTorch measurements do not establish fused-kernel, production-throughput, or hardware-general superiority.",
        ),
        replay_tier="artifact_only_empirical",
    ),
    GateContract(
        gate_id="spin9_clifford_sensing_core",
        claim="The maintained real Spin(9) Clifford system, frozen spinor-rank witnesses, symmetric conditioning curve, and isotropy branching identities satisfy their exact algebraic contracts.",
        status="proved_exact",
        evidence_layers=("exact_arithmetic", "symbolic_identity"),
        test_suites=(
            "tests/test_spin9_dirac_clifford.py",
            "tests/test_spin9_three_spinor_conditioning.py",
            "tests/test_spin9_three_spinor_symmetry.py",
        ),
        artifacts=(
            "artifacts/spin9_dirac_clifford_gate_20260807.json",
            "artifacts/spin9_three_spinor_conditioning_20260807.json",
            "artifacts/spin9_three_spinor_symmetry_20260807.json",
        ),
        boundary_obligations=(
            "The nine Clifford involutions and the Spin(8) restriction are checked coefficientwise.",
            "Frozen rank witnesses and generic stabilizer statements are not conflated.",
            "The spectral factorization is scoped to the symmetric one-parameter family.",
        ),
        limitations=(
            "These exact identities do not prove the unrestricted global three-spinor design optimum or any sequence-model advantage.",
        ),
        replay_tier="bounded_full",
    ),
    GateContract(
        gate_id="spin9_frame_and_local_design",
        claim="The Spin(9) information map admits the stated frame-operator reduction, and the symmetric candidate has an exact negative-definite quotient Hessian on the complete local rank-three stratum modulo Spin(9).",
        status="proved_exact",
        evidence_layers=("exact_arithmetic", "symbolic_identity"),
        test_suites=(
            "tests/test_spin9_frame_operator.py",
            "tests/test_spin9_grassmann_slice.py",
            "tests/test_spin9_local_hessian.py",
        ),
        artifacts=(
            "artifacts/spin9_frame_operator_20260807.json",
            "artifacts/spin9_grassmann_slice_20260807.json",
            "artifacts/spin9_local_hessian_exact.json",
        ),
        boundary_obligations=(
            "Frame rank and information-matrix rank are kept distinct.",
            "The quotient slice includes both V5 multiplicity copies and their coupling.",
            "The exact local Hessian is normalized by the intrinsic Grassmann tangent metric.",
        ),
        limitations=(
            "Strict local D-optimality does not imply a global optimum over all rank-three frames.",
        ),
        replay_tier="bounded_full",
    ),
    GateContract(
        gate_id="spin9_global_three_spinor_design",
        claim="A bounded multistart numerical search found no three-spinor frame with larger determinant than the symmetric candidate.",
        status="numerical_only",
        evidence_layers=("floating_point_falsifier", "raw_artifact", "multi_seed"),
        test_suites=("tests/test_spin9_three_spinor_global_screen.py",),
        artifacts=("artifacts/spin9_three_spinor_global_screen_20260807.json",),
        boundary_obligations=(
            "Every reported start count, seed, tolerance, and optimization domain is preserved in the artifact.",
            "Boundary-biased and non-symmetric starts remain distinguishable in analysis.",
        ),
        limitations=(
            "The screen is counterexample-search evidence only; unrestricted global D-optimality remains open.",
        ),
        replay_tier="artifact_only_numerical",
    ),
)


def validate_gate_contracts(root: Path = ROOT) -> list[str]:
    """Return all schema and evidence-category violations."""

    errors: list[str] = []
    ids = [gate.gate_id for gate in GATES]
    if len(ids) != len(set(ids)):
        errors.append("gate identifiers are not unique")

    discovered_tests = {
        path.relative_to(root).as_posix() for path in (root / "tests").glob("test_*.py")
    }
    covered_tests: set[str] = set()

    for gate in GATES:
        prefix = gate.gate_id
        for field_name in (
            "evidence_layers",
            "test_suites",
            "artifacts",
            "boundary_obligations",
            "limitations",
            "external_inputs",
        ):
            if not isinstance(getattr(gate, field_name), tuple):
                errors.append(f"{prefix}: {field_name} must be a tuple")
        if gate.status not in STATUSES:
            errors.append(f"{prefix}: unknown status {gate.status!r}")
        unknown_layers = set(gate.evidence_layers) - EVIDENCE_LAYERS
        if unknown_layers:
            errors.append(f"{prefix}: unknown evidence layers {sorted(unknown_layers)}")
        if not gate.boundary_obligations:
            errors.append(f"{prefix}: has no explicit boundary obligations")
        if not gate.limitations:
            errors.append(f"{prefix}: has no explicit limitations")

        for relative in (*gate.test_suites, *gate.artifacts):
            if not (root / relative).is_file():
                errors.append(f"{prefix}: missing evidence path {relative}")
        covered_tests.update(gate.test_suites)

        if gate.status == "proved_exact":
            if "exact_arithmetic" not in gate.evidence_layers:
                errors.append(f"{prefix}: exact theorem lacks exact arithmetic")
            forbidden = {"external_theorem", "floating_point_falsifier"}
            if forbidden & set(gate.evidence_layers):
                errors.append(f"{prefix}: exact theorem depends on a non-exact layer")
        if gate.status == "proved_hybrid":
            if (
                "external_theorem" not in gate.evidence_layers
                or not gate.external_inputs
            ):
                errors.append(
                    f"{prefix}: hybrid theorem does not name its external input"
                )
        elif gate.external_inputs:
            errors.append(
                f"{prefix}: external inputs are only valid for hybrid theorems"
            )
        if (
            gate.status == "exact_negative"
            and "exact_counterexample" not in gate.evidence_layers
        ):
            errors.append(
                f"{prefix}: exact negative result lacks an exact counterexample"
            )
        if gate.status == "empirical" and (
            "raw_artifact" not in gate.evidence_layers or not gate.artifacts
        ):
            errors.append(f"{prefix}: empirical result lacks raw artifacts")
        if gate.status == "open":
            if not any("Open:" in limitation for limitation in gate.limitations):
                errors.append(f"{prefix}: open gate is not explicitly labelled open")
            forbidden = {"positivity_certificate", "checkpoint_replay"}
            if forbidden & set(gate.evidence_layers):
                errors.append(f"{prefix}: open gate advertises completion evidence")
        if gate.status == "exact_reduction" and any(
            layer in gate.evidence_layers
            for layer in ("positivity_certificate", "exact_counterexample")
        ):
            errors.append(f"{prefix}: reduction is conflated with resolution")

    missing_tests = sorted(discovered_tests - covered_tests)
    stale_tests = sorted(covered_tests - discovered_tests)
    if missing_tests:
        errors.append(f"unclassified test suites: {missing_tests}")
    if stale_tests:
        errors.append(f"registry lists nonexistent test suites: {stale_tests}")
    return errors


def main() -> int:
    errors = validate_gate_contracts()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {len(GATES)} gate contracts cover every maintained test suite")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
