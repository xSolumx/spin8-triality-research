# Research map

This archive is organized as a sequence of increasingly strict mechanism
gates. Later results do not erase earlier failures; they answer narrower or
better-posed questions.

For the current adversarial claim audit, standalone paper opportunities,
correction ledger, and compressed next-research strategy, see
[Research audit and next strategy](RESEARCH_AUDIT_AND_NEXT_STRATEGY_2026-08-06.md).

## 1. Recurrent and streaming baseline

The first layer established full/chunk/token equivalence and fixed recurrent
state for GA and matched recurrence families.

Primary documents:

- [Recurrence ladder](experiments/RECURRENCE_LADDER_RESULTS.md)
- [Multi-group replication](experiments/RECURRENCE_LADDER_MULTIGROUP_1000.md)
- [Phase-two results](experiments/RESEARCH_PHASE_2_RESULTS.md)
- [Foundations](FOUNDATIONS.md)

## 2. Write-free finite-group mechanism gates

The research then removed writes, residual paths, contextual controllers, and
decay to ask whether SGD could discover fixed noncommutative token actions.

Primary documents:

- [Mechanism gate](experiments/MECHANISM_GATE_RESULTS.md)
- [Holonomy preregistration](experiments/HOLONOMY_PREREGISTRATION.md)
- [Householder transfer](experiments/HOUSEHOLDER_HOLONOMY_RESULTS.md)
- [PD-SSM baseline](experiments/PDSSM_BASELINE_RESULTS.md)

Interpretation boundary: held-out bigrams test shortcut freedom differently in
contextual models and fixed-token action models. They are not a single
before/after metric.

## 3. Representation discovery and shared-family retraction

The next line moved from independently normalized token actions to joint
retraction onto a shared representation manifold.

Primary documents:

- [Joint A5 rounding](experiments/JOINT_A5_ROUNDING_RESULTS.md)
- [Self-compiling retraction](experiments/SELF_COMPILING_RETRACTION_RESULTS.md)
- [Latent Cayley retraction](experiments/LATENT_CAYLEY_RETRACTION_RESULTS.md)
- [Partial Cayley completion](experiments/PARTIAL_CAYLEY_RETRACTION_RESULTS.md)
- [Inverse-cover theorem](experiments/INVERSE_COVER_IDENTIFIABILITY_THEOREM.md)

## 4. Endpoint-only learning and compiler supervision removal

Fixed-length endpoint training failed at chance; short-to-long curriculum
staging found the faithful basin. Follow-up controls separated curriculum
order, block structure, and gradient-mixing explanations.

Primary documents:

- [Fixed-length result](experiments/ENDPOINT_ONLY_FIXED_LENGTH_RESULTS.md)
- [Curriculum result](experiments/ENDPOINT_CURRICULUM_RESULTS.md)
- [Optimization controls](experiments/ENDPOINT_OPTIMIZATION_CAUSAL_RESULTS.md)
- [Block-order control](experiments/ENDPOINT_BLOCK_ORDER_RESULTS.md)
- [Zero-query manifold compiler](experiments/ENDPOINT_MANIFOLD_COMPILER_RESULTS.md)

## 5. Center fidelity, Q8, and blind state compilers

Rotor sandwich actions erase the central sign, while spinor left actions retain
it. Q8 exposed this kernel obstruction and motivated table-blind and state-only
compilers.

Primary documents:

- [Center-fidelity gate](experiments/SPINOR_CENTER_FIDELITY_GATE.md)
- [Q8 quality validation](experiments/Q8_SPINOR_QUALITY_GATE_VALIDATION_RESULTS.md)
- [Spin8 Q8 joint retraction](experiments/SPIN8_Q8_JOINT_RETRACTION_RESULTS.md)
- [Table-blind compiler](experiments/SPIN8_TABLE_BLIND_COMPILER_RESULTS.md)
- [State-only compiler](experiments/SPIN8_STATE_ONLY_COMPILER_RESULTS.md)
- [Exact congruence lattice](experiments/SPIN8_EXACT_CONGRUENCE_LATTICE_RESULTS.md)

The exact lattice audit corrected an earlier uniqueness interpretation:
transition closure alone cannot select a semantic quotient without observations
or an explicit prior.

## 6. Triality memory, action completion, and addressing

The constructive `Spin(8)` core introduced shared vector/chiral transport,
triality binding, triangular scans, and exact multiplicity-slot routing.

Primary documents:

- [Research program](SPIN8_TRIALITY_EXPERIMENT.md)
- [Triality algebra](experiments/SPIN8_TRIALITY_ALGEBRA_RESULTS.md)
- [Triangular lift](experiments/SPIN8_TRIANGULAR_TRIALITY_LIFT_RESULTS.md)
- [Identifiability](experiments/SPIN8_TRIALITY_IDENTIFIABILITY_RESULTS.md)
- [Blind shared action](experiments/SPIN8_BLIND_SHARED_ACTION_RESULTS.md)
- [Continuous aliases](experiments/SPIN8_CONTINUOUS_ALIAS_RESULTS.md)
- [Blind action and alias](experiments/SPIN8_BLIND_ALIAS_ACTION_RESULTS.md)

## 7. Five-probe identifiability and active sensing

Five multiview probes have full shared rank 28; four probes retain a
three-dimensional stabilizer. Active sensing then optimized the conditioning
of an already identifiable design.

Primary documents:

- [Five-probe theorem](experiments/SPIN8_FIVE_PROBE_RESULTS.md)
- [Exact global five-probe certificate](experiments/SPIN8_GLOBAL_FIVE_PROBE_THEOREM.md)
- [Binary coordinate triality geometry](experiments/SPIN8_BINARY_TRIALITY_GEOMETRY.md)
- [Continuous probe orbit theorem](experiments/SPIN8_CONTINUOUS_PROBE_ORBIT_THEOREM.md)
- [Active sensing](experiments/SPIN8_ACTIVE_SENSING_RESULTS.md)
- [Joint sensor retraction](experiments/SPIN8_JOINT_SENSOR_RETRACTION_RESULTS.md)

Interpretation boundary: identifiability is not conditioning. The five-probe
boundary and the balanced information spectrum are distinct results.
The exact global certificate proves one explicitly displayed free five-probe
tuple and one four-probe `su(2)` counterfamily.

The coordinate subproblem is now completely classified: the 24 coordinate
probes are nonzero-colour points in `F_2^5`, triality contraction is binary
addition, and five probes identify exactly when their labels form a basis.
The subsequent continuous orbit theorem uses exact invariant Jacobians,
stabilizer ranks, and the compact principal-orbit theorem. It proves that every
four-probe sensor is insufficient, while every mixed five-probe allocation has
an open dense globally free stratum. The remaining orbit problem is the full
classification of exceptional nonprincipal five-probe tuples, not the sharp
generic boundary.

The triangular recurrence has also been separated into a universal theorem and
its exceptional instance. See
[Intertwiner SchurScans](experiments/INTERTWINER_SCHURSCAN_THEOREM.md) for the
generic bilinear lift, SO(3) control, and feedback obstruction.

## 8. Cayley spectrum and Dirac–Gram proof program

The final layer replaced empirical sensor observations with exact projector
geometry and invariant polynomial certificates.

Primary documents:

- [Cayley spectrum theorem](experiments/SPIN8_CAYLEY_SPECTRUM_RESULTS.md)
- [Dirac–Gram gate](experiments/SPIN8_DIRAC_GRAM_RESULTS.md)
- [Signed star theorem](experiments/SPIN8_DIRAC_STAR_RESULTS.md)
- [Exact decorrelation counterexample](experiments/SPIN8_CONDITIONAL_DECORRELATION_COUNTEREXAMPLE.md)
- [Cayley-null edge theorem](experiments/SPIN8_DIRAC_EDGE_RESULTS.md)
- [Variable-Cayley one-edge reconstruction](experiments/SPIN8_DIRAC_ONE_EDGE_RESULTS.md)

The coordinatewise conditional-decorrelation lemma is exactly false. The
current frontier is the variable-Cayley one-edge family, where four orientation
sectors assemble into a tetrahedral matrix-positivity certificate, followed by
the remaining two residual Cholesky correlations.
