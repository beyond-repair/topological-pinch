# Governance — topological-pinch

**Classification:** RESEARCH  
**Claim level:** 0–1 (hypothesis only)  
**Governing source:** [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)

## Invariants

1. This repository does **not** contain a mesh, BEM solver, or measured flux integral.
2. The phrase “~92% aft-face localization” is **unverified**. It MUST NOT be treated as an experimental result.
3. Geometry lives in `sierpinski-geometry-045`. Solvers live in `stress-tensor-modification`. Program freeze lives in `coherence-drive`.
4. CI in this repo only checks that claim-cap documents exist. Green CI is **not** physics validation.
5. Promotion to ACTIVE requires tests of a solver/mesh plus SECURITY.md and operator approval in ADL-Governance.

## Sweep history (this repo)

- Sweep-096: documented RESEARCH + claim cap + docs-presence CI.
- Sweep-105 (2026-09-07): randomized re-select; re-audit; no physics promotion; docs tests extended.
