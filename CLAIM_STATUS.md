# Claim status — topological-pinch

**Classification:** RESEARCH / hypothesis  
**Status:** Unverified.  
**experimental_validation:** false  
**Historical 92% localization:** HYPOTHESIS — not reproduced

A graph-proxy metric exists (`localization.py`). On the public gasket
with Voronoi-of-corner regions and residual current Lu, the measured
eta is **not** 0.92. That number remains boxed as a hypothesis
until a mesh-refined Maxwell-stress integral, with the region declared
in advance, says otherwise.

**Sweep-172 observation (graph proxy only, not a field measurement):**
with the code default `u_corners = [1.0, -0.5, 0.0]`, levels 2, 3, and 4
returned the same partition

| region corner | eta | historical_92_reproduced |
|---------------|-----|--------------------------|
| 0 | 0.5 | false |
| 1 | 0.4 | false |
| 2 | 0.1 | false |

Local `pytest`: 5 passed, 0 failed (2026-10-01). This does not validate
aft-face localization, thrust, or any continuum stress integral.

**Sweep-159d note:** localized multiplicity of combinatorial eigenvalue
\(\lambda=6\) on the gasket
(\(\mathrm{mult}=\frac{3}{2}(3^{n-1}-1)\) for \(n\ge 2\), see
[sierpinski-geometry-045 SPECTRUM.md](https://github.com/beyond-repair/sierpinski-geometry-045/blob/main/SPECTRUM.md))
is a high-frequency graph fact. It is **not** a measurement of
\(\eta_{\rm region}=0.92\) and SHALL NOT be substituted for the pinch
hypothesis.

**2026-10-01 pinch-family addendum:** a Neumann neck collapses
\(\lambda_1\) as width drops. That is spectral, not a topological mouth,
and it does not select 0.08. The gap ratio crosses 0.08 only as a
geometry-dependent level set. Record:
`FALSIFICATION_2026-10-01_PINCH.md`. Status remains unverified.
experimental_validation remains false.
