# Documentation Audit: 2026-08-06

## Scope

This pass covered every Markdown writeup in the maintained
`Spin8-Triality-Research` repository and the related `SSM-Models` archive. It
had two distinct layers:

1. an editorial rewrite of the current synthesis, plain-language explanation,
   research map, and inherited frontier note;
2. a mechanical audit of every Markdown file, including historical reports and
   preregistrations.

The second layer is deliberately described as an audit rather than a literary
rewrite of every historical paragraph. Preserving older preregistrations and
negative results verbatim is part of the scientific record; silently
modernizing their claims would damage provenance.

## Editorial changes

The current synthesis now explains the complete result ladder:

- exact `8+8+8+4` Cayley block factorization;
- exact variable-Cayley one-edge positivity theorem;
- exact local stability of the second residual edge;
- exact reduction of the finite second edge to degree-six and degree-twelve
  polynomial gates;
- the precise boundary between exact proof and numerical counterexample search.

The formerly compressed frontier note was rewritten into four falsifiable
programs. Claims that compact dynamics could store arbitrary infinite-group
state without qualification were removed; the defensible target is computation
of selected invariants or quotients.

## Mathematical-writing contract

The new [Mathematical Writing Standard](MATHEMATICAL_WRITING_STANDARD.md)
requires every central equation to state:

- the status of the claim;
- the domain and quantifiers;
- the meaning of its symbols;
- the exact consequence and remaining limitation.

It also separates reconstruction, identity verification, positivity, artifact
integrity, and floating-point falsification as distinct evidence layers.

## Automated checks

The repository now contains `tools/audit_math_docs.py` and a maintained unit
test. The audit rejects:

- deprecated promotional terminology in filenames or prose;
- the stale pre-rename note path;
- raw double-dollar display delimiters;
- known malformed generated-LaTeX fragments;
- unbalanced `\[` and `\]` display delimiters;
- broken relative Markdown links.

At the time of this report, the combined audit passed all 281 maintained
Markdown files in both research trees, and all 338 relative links resolved.
The complete maintained theorem and regression suite then passed all 175 tests
under six-core affinity, peaking at 3.962 GiB of process-tree resident memory.

## Interpretation boundary

This audit proves mechanical consistency of the documents it scans. It does
not prove that every historical argument is mathematically correct. Exact
claims remain governed by their theorem harnesses, artifacts, independent
arithmetic replays, and explicitly recorded open gates. Editorial elegance is
being used to expose those boundaries more clearly, never to make them appear
stronger.
