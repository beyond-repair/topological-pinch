# Governance — topological-pinch

**Classification:** RESEARCH  
**Claim level:** 0–1 (hypothesis only)  
**Governing source:** [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)

## Invariants

1. This repository does **not** contain a mesh, BEM solver, or measured flux integral.
2. The phrase “~92% aft-face localization” is **unverified**. It MUST NOT be treated as an experimental result.
3. Geometry lives in `sierpinski-geometry-045`. Solvers live in `stress-tensor-modification`. Program freeze lives in `coherence-drive`.
4. CI runs `pytest` over docs-presence checks and the graph-proxy in `localization.py`. A green run is **not** physics validation and SHALL NOT be cited as a mesh study.
5. Promotion to ACTIVE requires tests of a solver/mesh plus SECURITY.md and operator approval in ADL-Governance.
6. The default-boundary Voronoi residual partition (levels 0–5: 0.500000 / 0.400000 / 0.100000) is a graph proxy observation. Residual support is the three Dirichlet corners only. It is not a Maxwell-stress integral and is not the historical 92% figure. `topological-pinch` prints that miss. A green run is not thrust.

## Sweep history (this repo)

- Sweep-096: documented RESEARCH + claim cap + docs-presence CI.
- Sweep-105 (2026-09-07): randomized re-select; re-audit; no physics promotion; docs tests extended.
- Sweep-139: declared-region localization proxy. Historical 92% remains a hypothesis.
- Sweep-159d: disallowed identifying gasket λ=6 multiplicity with the 92% pinch hypothesis.
- Spectral pointer commit: 92% pinch is not a consequence of the locked spectral kernel.
- Sweep-172 (2026-10-01): randomized re-select. Local pytest 5 passed. CI last observed success on head `5a7f2d0` (run 36817680614) before this commit. Classification unchanged. No release. No archive flag.
