# How to read the experiment record

This directory is a chronological scientific record. It contains frozen
preregistrations, dated result reports, theorem certificates, negative results,
and later corrections. Those documents answer different questions and should
not be flattened into one undated narrative.

## Authority and chronology

Use this order when two statements appear to conflict:

1. the current repository [README](../../README.md) and
   [research map](../RESEARCH_MAP.md) for present status;
2. the [research audit and correction ledger](../RESEARCH_AUDIT_AND_NEXT_STRATEGY_2026-08-06.md)
   for known interpretive corrections;
3. the latest result or theorem document for the relevant family, together
   with its exact artifact and verifier;
4. the matching preregistration for what was committed before results were
   inspected;
5. earlier reports for the historical route by which the result was reached.

A dated sentence such as “the next gate is” means “the next gate at that
time.” A later addendum may supersede its roadmap without altering the original
record. A preregistered threshold remains part of history even if later work
adopts a separately named functional criterion.

## Evidence vocabulary

- **Theorem or exact identity:** derived symbolically or checked by exact
  arithmetic under an explicitly stated domain.
- **Computational certificate:** a finite exact object whose verifier checks the
  claimed identity or positivity condition. Artifact integrity, reconstruction,
  and mathematical sufficiency are separate obligations.
- **Numerical falsification:** a search that found no counterexample. It raises
  confidence but never proves global nonnegativity or optimality.
- **Empirical result:** a statement about the recorded seeds, budgets, hardware,
  and evaluation protocol. It is not automatically a reliability theorem.
- **Hypothesis or roadmap:** a proposed mechanism or next experiment, not an
  established result.

## Preservation rule

Historical observations, failed gates, and negative results are not silently
rewritten to match the current interpretation. When a later audit changes the
meaning of an earlier result, the correction belongs in a dated addendum or the
central correction ledger. Current manuscripts should state the corrected
interpretation directly and cite the historical path when it matters.

## Known examples of supersession

- Five probes established identifiability before the balanced sensor's
  conditioning and D-optimality questions were separated.
- Bigram generalization in fixed-token write-free actions tests whether
  optimization finds useful per-token operators; it is not the same falsifier
  as the earlier context-dependent model test.
- The behavioral functional gate is weaker than the original
  (10^{-3}) raw-homomorphism gate; the two counts must remain separate.
- The variable-Cayley one-edge theorem and the finite second-edge reduction
  supersede older documents that call the Cayley-null edge the current frontier.
- GPU sweeps over the finite two-edge gates are recorded as counterexample
  searches only; exact global positivity remains open.

This policy preserves history while preventing old, locally accurate language
from masquerading as the present theorem boundary.
