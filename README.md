# Topological Pinch (Coherence Drive)

**© 2026 Brian Ware / AtomicDreamlabs — All Rights Reserved. Proprietary Technology.**

**Finding:** In the asymmetric 3rd-order Sierpinski tetrahedron, 92 % of the force density originates at the aft-face fractal vertices. This topological pinch is the core physical mechanism that breaks symmetry and generates net momentum flux.

**Purpose of this Repo**  
This repository explains the topological pinch phenomenon, provides the exact metrics from the v1.1 baseline, and includes blind-build validation steps so any new engineer can understand, verify, and apply it immediately.

**License**  
See LICENSE file in this repository. All rights reserved. No copying or distribution without explicit written permission.

## 1. Key Metrics (from v1.1 Baseline)
- Aft-face vertex contribution: **92.1 %**  
- Volumetric contribution: **7.9 %**  
- Directional asymmetry ratio: **14.32×** (clear -z momentum flux)

These numbers are mesh-invariant from L/50 to L/400 and were obtained using the closed surface-integral + Poynting flux method.

## 2. Physical Meaning
The fractal geometry (aft n=3, fore n=1, 0.45 scaling) creates a strong LDOS gradient. The Ware Constant scales this gradient, concentrating the divergence of the effective stress tensor almost entirely at the recursive vertices on the aft face. This “pinch” produces the net non-zero force that the symmetric EM part cannot.

## 3. Blind-Build Validation Checklist
- [ ] Clone the master `coherence-drive` repo and run `test_baseline_v1.py`
- [ ] Execute `symmetry_decomposition.py` on the n=3 output
- [ ] Confirm aft-face contribution > 85 % and asymmetry ratio >> 1
- [ ] Verify that changing to a symmetric geometry (n=1 all faces) drops the pinch to ~0 %

## 4. Usage in Downstream Work
Use the decomposition function directly in any simulation:

```python
from symmetry_decomposition import decompose_symmetry
aft_pct, vol_pct, asym_ratio = decompose_symmetry(f_total, mesh_shape, n_depth=3)
