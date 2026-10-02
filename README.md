<div align="center">

# Topological Pinch

### Hypothesis: asymmetry **localizes** stress divergence — not a measured 92%

[![RESEARCH](https://img.shields.io/badge/classification-RESEARCH-f59e0b?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/claim_0%E2%80%931_hypothesis-7c3aed?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)

</div>

---

## Why this exists

Symmetric boundaries cancel. The Coherence Drive story needs a **reason** a surface integral might not vanish — e.g. stronger localization on one face of an asymmetric fractal geometry.

That idea is called **topological pinch**. It is a **hypothesis**, not a certified mesh result.

## Status of this tree

**RUNNABLE SKETCH — NOT A COMPLETE PRODUCT** (Claim-0). Classification remains RESEARCH.

The runnable check is a gasket-graph residual proxy (`localization.py`, printed by `report.py`). It is not a mesh, not a Maxwell-stress integral, and not thrust. The historical ~92% figure is **not** an input and is **not** reproduced. No constant is refit.

```text
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```

Default boundary `u_corners = [1.0, -0.5, 0.0]`, levels 0–5, from the code (not a fit):

| corner | eta | vs 0.92 | historical_92_reproduced |
|--------|-----|---------|--------------------------|
| 0 | 0.500000 | short by 0.420000 | false |
| 1 | 0.400000 | short by 0.520000 | false |
| 2 | 0.100000 | short by 0.820000 | false |

The code treats `|eta - 0.92| < 0.02` as a reproduction. None of these values fall in that window.

`r = L u` is supported only on the three Dirichlet corners, because the interior is graph-harmonic. Interior Voronoi labels do not move eta. Level-0 corner residual is `[2.5, -2.0, -0.5]`. On this boundary, level `n` multiplies that vector by `(3/5)^n` (successive sums of absolute residual scale by 0.600000). That factor is an observation of this solve. It is not 0.08 and not 0.92.

## Install, run, and test

No configuration file. The default Dirichlet corners live in `localization.py`. Nothing is downloaded at runtime.

```bash
git clone https://github.com/beyond-repair/topological-pinch.git
cd topological-pinch
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
topological-pinch
python report.py
python -m localization
pytest -q
```

`topological-pinch`, `python report.py`, and `python -m localization` print the same report. NumPy is required. `pytest` is in `requirements.txt`.

| Command | What a passing run shows | What it does not say |
|---------|--------------------------|----------------------|
| `topological-pinch` | Partition 0.500000 / 0.400000 / 0.100000 at levels 0–5; corner-only residual; scale 0.600000; explicit misses vs 0.92 | Aft-face stress localization, a measured 92%, net thrust, or a neck derivation of 0.08 |
| `pytest -q` | The same locks, including the known misses, plus docs-presence | Experimental validation |

CI, when present, runs pytest. A green run is not a mesh study.

## Why you need it

| You want… | This repo |
|-----------|-----------|
| The *narrative* of aft-face localization | Yes — as hypothesis |
| A number like “92.1% proven” | **No** — not confirmed here |
| A universal 0.08 from a narrowing neck | **No** — see 2026-10-01 falsification |
| Geometry + BEM directionality | Sibling repos below |

## How it works (intended story)

1. Build **0.45** asymmetric Sierpinski-type geometry.
2. Solve fields / stresses on that mesh.
3. Ask whether divergence or flux **concentrates** on the aft face.
4. Only then quote a percentage — with mesh study attached.

That mesh study is not in this repository. What is here is the graph proxy above. Sweep-172 (2026-10-01) recorded levels 2–4 as 0.5 / 0.4 / 0.1; those rows are inside the level 0–5 table.

2026-10-01 operator test: Neumann spectral collapse under a narrowing neck is real and does not select 0.08. A gap-ratio crossing of 0.08 is a level set, not a fixed point. Record: [FALSIFICATION_2026-10-01_PINCH.md](FALSIFICATION_2026-10-01_PINCH.md).

## Related

- Geometry: [sierpinski-geometry-045](https://github.com/beyond-repair/sierpinski-geometry-045)
- Solvers: [stress-tensor-modification](https://github.com/beyond-repair/stress-tensor-modification)
- Theory freeze: [coherence-drive](https://github.com/beyond-repair/coherence-drive)
- Derivation ledger: [-ware-constant-derivation](https://github.com/beyond-repair/-ware-constant-derivation)
- Governance: [GOVERNANCE.md](GOVERNANCE.md) / [CLAIM_STATUS.md](CLAIM_STATUS.md)
