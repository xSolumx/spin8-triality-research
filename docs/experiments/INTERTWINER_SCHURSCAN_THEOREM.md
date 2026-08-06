# Intertwiner SchurScans: the general triangular theorem

**Date:** 2026-08-06  
**Status:** constructive algebraic theorem with executable parity checks  
**Reference implementation:** `src/intertwiner_schurscan.py`  
**Artifact:** `artifacts/intertwiner_schurscan_20260806.json`  
**Preregistration:** none; this generalization was extracted from the earlier
triality-specific staged scan

## The theorem

Let `U`, `V`, and `W` be finite-dimensional real vector spaces and let

\[
\beta:U\times V\longrightarrow W
\]

be any bilinear map. Consider the triangular recurrence

\[
\begin{aligned}
u_t &= A_tu_{t-1}+a_t,\\
v_t &= B_tv_{t-1}+b_t,\\
w_t &= C_tw_{t-1}+c_t+\beta(u_t,v_t).
\end{aligned}
\]

Then:

1. the complete sequence is computable by two stages of associative affine
   scans;
2. recurrent inference stores exactly
   `dim(U) + dim(V) + dim(W)` scalars;
3. the recurrence admits an exact one-stage homogeneous linear lift on

   \[
   \mathbb R\oplus U\oplus V\oplus(U\otimes V)\oplus W;
   \]

4. if a group acts on `U`, `V`, and `W` and `beta` is an intertwiner, the
   bilinear drive is equivariant without changing the scan proof.

The practical two-stage schedule is

```text
U affine scan ----\
                   beta at each position ---> W affine scan
V affine scan ----/
```

Both stages have logarithmic parallel depth. The number of stages is a fixed
constant independent of sequence length.

## Exact homogeneous lift

Write `q = u tensor v`. One step gives

\[
\begin{aligned}
q'={}&(A\otimes B)q
 +(Au)\otimes b
 +a\otimes(Bv)
 +a\otimes b,\\
w'={}&Cw+c+\widetilde\beta q',
\end{aligned}
\]

where `beta-tilde: U tensor V -> W` is the linearization of the bilinear map.
Every right-hand term is linear in

\[
[1,u,v,q,w].
\]

Therefore each token is one finite matrix on the lifted state. Matrix
composition is associative, so an ordinary prefix scan gives an independent
machine-check of the staged construction.

The lift is a proof device. It is not required in the streaming cache and need
not be materialized in the efficient training implementation.

## The feedback obstruction

The direction of the dependency arrows is load-bearing. If `w` feeds back
linearly into one source, generic polynomial degree grows as

\[
2,3,4,5,\ldots.
\]

If it feeds both sources, the bilinear term generically doubles the degree:

\[
2,4,8,16,\ldots,2^t.
\]

Consequently no fixed finite collection of monomials can give an exact linear
lift for generic cyclic feedback at arbitrary length. Special algebras may
close by additional identities, but associativity cannot be claimed merely
from bilinearity.

This gives a clean architectural boundary:

> Acyclic multilinear coupling permits a finite staged scan. Generic cyclic
> multilinear feedback does not.

## Nonexceptional control

To separate the universal scan theorem from Spin(8), the executable harness
uses the ordinary SO(3) cross product

\[
\beta(u,v)=u\times v.
\]

It is an equivariant bilinear intertwiner

\[
(Ru)\times(Rv)=R(u\times v),\qquad R\in SO(3).
\]

At float64 precision over random length-31 recurrences, the maintained artifact
reports:

- staged scan versus recurrence: `2.84e-14` maximum absolute error;
- homogeneous lift versus recurrence: `4.97e-14`;
- SO(3) equivariance: `1.78e-15`;
- streaming state: 9 scalars;
- proof lift: 19 scalars.

Thus scan compatibility is not a triality-only effect.

## What Spin(8) adds

The universal theorem supplies scheduling and closure. Spin(8) triality adds
properties the SO(3) control does not:

- three inequivalent eight-dimensional representations tied by one invariant;
- an exact normed-division-algebra bind/unbind operation for unit arguments;
- the five-probe cross-view identifiability structure;
- the binary coordinate geometry and exceptional stabilizer ladder documented
  separately.

Those are the properties that a triality model must exploit to beat matched
generic bilinear or direct-memory baselines. Merely passing scan parity is not
a Spin(8) advantage.

## Why this could be a paper

The contribution is not “we can scan matrix products.” It is a general design
rule for adding structured multiplicative interactions to recurrent models
without silently destroying parallelism:

1. factor the state into representation streams;
2. orient bilinear or multilinear intertwiners along a directed acyclic graph;
3. scan each layer of the graph;
4. keep nonlinear cleanup outside the recurrence;
5. reject cyclic couplings unless a finite closure algebra is proved.

The construction naturally extends to a representation quiver and to higher
multilinear maps. A depth-`d` dependency graph yields `d` staged scans, still
with `O(log N)` sequence depth for fixed `d`.

Publication novelty remains subject to a dedicated literature comparison.
In particular, Fujii and Yamakita's 2026
[Bilinear Input Modulation for Mamba](https://arxiv.org/abs/2604.17221)
explicitly distinguishes sequential bilinear computation from scan-compatible
bilinear variants. It is a mandatory nearby comparison. The candidate distinct
point here is the acyclic multistream intertwiner construction, exact finite
homogeneous lift, and representation-equivariant formulation—not the broad
idea that bilinear modulation can appear in an SSM.

## Claim boundary

Established here:

- exact staged/recurrent equivalence for the displayed triangular recurrence;
- an explicit finite homogeneous lift;
- an independent SO(3) intertwiner instance;
- formal degree growth showing why generic feedback is outside this theorem.

Not yet established:

- throughput superiority over fused production SSM kernels;
- better retrieval or language modelling than delta-rule/attention baselines;
- a no-go theorem covering every possible nonlinear coordinate transform;
- novelty relative to every prior cascaded-scan, semidirect-product, or
  equivariant recurrent construction.

## Replay

```powershell
$env:PYTHONPATH='src'
python -m intertwiner_schurscan `
  --output artifacts/intertwiner_schurscan_20260806.json
python -m unittest discover -s tests -p "test_intertwiner_schurscan.py" -v
```
