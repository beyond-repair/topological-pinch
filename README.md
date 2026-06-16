# Topological Pinch (Coherence Drive)

**© 2026 Brian Ware / AtomicDreamlabs — All Rights Reserved. Proprietary Technology.**

**Finding:** In the asymmetric 3rd-order Sierpinski tetrahedron (α=0.45 scaling), 92.1 % of force density originates at aft-face fractal vertices. This topological pinch breaks symmetry and generates net momentum flux via Ware-scaled LDOS gradient.

**Purpose**  
Exact metrics, physical derivation, and blind-build validation for immediate simulation/hardware integration.

**License**  
See LICENSE file. All rights reserved.

## 1. Key Metrics (v1.1 Baseline)
- Aft-face vertex contribution: **92.1 %**  
- Volumetric contribution: **7.9 %**  
- Directional asymmetry ratio: **14.32×** (clear -z momentum flux)

Mesh-invariant (L/50 to L/400); derived from closed surface-integral + Poynting subtraction in physics_evaluator.py (stress-tensor-modification repo).

## 2. Physical Meaning
Fractal geometry induces strong ∇LDOS. M2 renormalization W(n) scales this gradient, concentrating divergence of the effective stress tensor T_eff^{ij} (master Ware term in T_μν^eff = T_μν + W T_μν^info) at recursive aft vertices. Produces the topological pinch enabling target thrust F/P ≈ 3×10^{-8} N/W. Fully consistent with master Proca sector (ghost-free for W(n) < 0.125, subluminal v_g, r_0 ∝ M_b^{0.40} coherence) and |A|^4 saturation.

## 3. Blind-Build Validation Checklist
- [ ] Clone master ware-constant-phenomenology, ware-constant-derivation, stress-tensor-modification, and m2-renormalization-law.  
- [ ] Run test_baseline_v1.py at n=3.  
- [ ] Execute symmetry_decomposition.py on output.  
- [ ] Confirm aft-face >85%, asymmetry >>1, and M2 non-linear ratios (0.795/1.000/1.259 at fixed α=0.45).  
- [ ] Symmetric geometry (uniform n=1) yields pinch ≈0%.  
- [ ] Cross-check with r_0 scaling and |A|^4 boundary saturation.

## 4. Usage in Downstream Work
```python
from symmetry_decomposition import decompose_symmetry
aft_pct, vol_pct, asym_ratio = decompose_symmetry(f_total, mesh_shape, n_depth=3)