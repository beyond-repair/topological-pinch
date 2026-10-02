"""Reproducible localization metric.

Region is defined BEFORE the number is evaluated.

    eta_region = (integrated |response| in region) / (integrated |response| over domain)

On the gasket graph the public response without a field solver is the
nodal residual current r = L u. PROXY, not Maxwell stress divergence.
The historical 92% figure is a HYPOTHESIS and is not returned here.

On this Dirichlet problem the residual is supported only on the three
corner nodes (the interior is graph-harmonic), so eta is the share of
|r| at that corner. Interior Voronoi labels do not move eta.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


def _key(p, nd=10):
    return (round(float(p[0]), nd), round(float(p[1]), nd))


def build_gasket(level: int):
    c0 = np.array([0.0, 0.0])
    c1 = np.array([1.0, 0.0])
    c2 = np.array([0.5, math.sqrt(3.0) / 2.0])
    pos_map, positions, edges = {}, [], set()

    def vid(p):
        k = _key(p)
        if k not in pos_map:
            pos_map[k] = len(positions)
            positions.append(p.copy())
        return pos_map[k]

    def rec(a, b, c, d):
        if d == 0:
            ia, ib, ic = vid(a), vid(b), vid(c)
            for i, j in ((ia, ib), (ib, ic), (ic, ia)):
                if i != j:
                    edges.add((min(i, j), max(i, j)))
            return
        rec(a, 0.5 * (a + b), 0.5 * (c + a), d - 1)
        rec(0.5 * (a + b), b, 0.5 * (b + c), d - 1)
        rec(0.5 * (c + a), 0.5 * (b + c), c, d - 1)

    rec(c0, c1, c2, level)
    P = np.vstack(positions)
    C = np.array([pos_map[_key(c0)], pos_map[_key(c1)], pos_map[_key(c2)]], dtype=int)
    return P, sorted(edges), C


def laplacian(n, edges):
    L = np.zeros((n, n))
    for i, j in edges:
        L[i, i] += 1; L[j, j] += 1; L[i, j] -= 1; L[j, i] -= 1
    return L


def dirichlet_residual(level: int, u_corners: np.ndarray):
    P, E, C = build_gasket(level)
    L = laplacian(len(P), E)
    n = len(P)
    mask = np.ones(n, dtype=bool)
    mask[C] = False
    interior = np.where(mask)[0]
    u = np.zeros(n)
    u[C] = u_corners
    u[interior] = np.linalg.solve(L[np.ix_(interior, interior)], -L[np.ix_(interior, C)] @ u[C])
    return P, C, L @ u


@dataclass
class LocalizationResult:
    level: int
    region_definition: str
    eta: float
    n_region: int
    n_domain: int
    historical_92_reproduced: bool


def corner_voronoi_eta(level: int, region_corner: int = 0, u_corners=None) -> LocalizationResult:
    if u_corners is None:
        u_corners = np.array([1.0, -0.5, 0.0])
    P, C, residual = dirichlet_residual(level, u_corners)
    d = np.stack([np.linalg.norm(P - P[C[k]], axis=1) for k in range(3)], axis=1)
    label = np.argmin(d, axis=1)
    region = label == region_corner
    resp = np.abs(residual)
    denom = float(resp.sum())
    eta = float(resp[region].sum() / denom) if denom else float("nan")
    return LocalizationResult(
        level=level,
        region_definition=f"voronoi(corner={region_corner}) on gasket level {level}",
        eta=eta,
        n_region=int(region.sum()),
        n_domain=int(len(P)),
        historical_92_reproduced=abs(eta - 0.92) < 0.02,
    )


# Default boundary used by the public proxy. Not fitted to 0.92 or 0.08.
DEFAULT_U_CORNERS = (1.0, -0.5, 0.0)
HISTORICAL_ETA = 0.92
REPORT_LEVELS = (0, 1, 2, 3, 4, 5)
# Absolute residual on non-corners must sit under this. Direct solves
# on these levels are far smaller; this is a support test, not a fit.
RESIDUAL_SUPPORT_ATOL = 1e-8


def vertex_count(level: int) -> int:
    """Sierpinski gasket iteration, level 0 = one triangle."""
    return (3 ** (level + 1) + 3) // 2


def edge_count(level: int) -> int:
    return 3 ** (level + 1)


def partition(level: int, u_corners=None) -> list[LocalizationResult]:
    if u_corners is None:
        u_corners = np.array(DEFAULT_U_CORNERS, dtype=float)
    return [corner_voronoi_eta(level, region_corner=k, u_corners=u_corners) for k in range(3)]


def corner_residual(level: int, u_corners=None) -> np.ndarray:
    if u_corners is None:
        u_corners = np.array(DEFAULT_U_CORNERS, dtype=float)
    _P, corners, residual = dirichlet_residual(level, np.asarray(u_corners, dtype=float))
    return np.asarray(residual[corners], dtype=float)


def residual_supported_only_on_corners(level: int, u_corners=None, atol: float = RESIDUAL_SUPPORT_ATOL) -> bool:
    if u_corners is None:
        u_corners = np.array(DEFAULT_U_CORNERS, dtype=float)
    _P, corners, residual = dirichlet_residual(level, np.asarray(u_corners, dtype=float))
    support = set(np.where(np.abs(residual) > atol)[0].tolist())
    return support == set(int(c) for c in corners)


def report_rows(levels=REPORT_LEVELS, u_corners=None) -> list[dict]:
    if u_corners is None:
        u_corners = np.array(DEFAULT_U_CORNERS, dtype=float)
    rows = []
    previous = None
    for level in levels:
        positions, edges, _corners = build_gasket(level)
        parts = partition(level, u_corners)
        residual = corner_residual(level, u_corners)
        sum_abs = float(np.abs(residual).sum())
        if previous is None or abs(previous) < 1e-15:
            scale = None
        else:
            scale = sum_abs / previous
        rows.append(
            {
                "level": int(level),
                "nodes": int(len(positions)),
                "nodes_formula": vertex_count(level),
                "edges": int(len(edges)),
                "edges_formula": edge_count(level),
                "eta": [float(part.eta) for part in parts],
                "historical_92": [bool(part.historical_92_reproduced) for part in parts],
                "support_corners_only": residual_supported_only_on_corners(level, u_corners),
                "residual": [float(value) for value in residual],
                "sum_abs_r": sum_abs,
                "scale_from_prev": scale,
            }
        )
        previous = sum_abs
    return rows


def locks_hold(rows: list[dict] | None = None, tol: float = 1e-12) -> bool:
    """Graph-proxy locks. Passing is not a measurement of eta=0.92."""
    rows = report_rows() if rows is None else rows
    expected = (0.5, 0.4, 0.1)
    for row in rows:
        if row["nodes"] != row["nodes_formula"] or row["edges"] != row["edges_formula"]:
            return False
        if not row["support_corners_only"]:
            return False
        if any(row["historical_92"]):
            return False
        for got, exp in zip(row["eta"], expected):
            if abs(got - exp) > tol:
                return False
        scale = row["scale_from_prev"]
        if scale is not None and abs(scale - 0.6) > 1e-9:
            return False
        if abs(sum(row["eta"]) - 1.0) > 1e-9:
            return False
    return bool(rows)


def main() -> None:
    u = np.array(DEFAULT_U_CORNERS, dtype=float)
    print("topological-pinch — Claim-0 graph-proxy report")
    print("Not a Maxwell-stress integral. Not thrust. The 0.92 figure is not an input and is not refit.")
    print(f"default u_corners = [{u[0]:.1f}, {u[1]:.1f}, {u[2]:.1f}]")
    print("eta = |r| share of the declared Voronoi corner. r = L u on the gasket graph.")
    print("Interior nodes are graph-harmonic, so they do not move eta.")
    print()
    print("level  nodes  edges  eta0      eta1      eta2      corners_only  r0          r1          r2          scale")
    rows = report_rows(u_corners=u)
    for row in rows:
        scale = row["scale_from_prev"]
        scale_s = "n/a" if scale is None else f"{scale:.6f}"
        r0, r1, r2 = row["residual"]
        e0, e1, e2 = row["eta"]
        print(
            f"{row['level']:5d}  {row['nodes']:5d}  {row['edges']:5d}  "
            f"{e0:.6f}  {e1:.6f}  {e2:.6f}  "
            f"{str(row['support_corners_only']).lower():12s}  "
            f"{r0: .6f}  {r1: .6f}  {r2: .6f}  {scale_s}"
        )
    print()
    print("lock: levels 0-5 default boundary partition is 0.500000 / 0.400000 / 0.100000")
    print("lock: historical_92_reproduced is false on every corner (window |eta-0.92|<0.02)")
    print("miss: corner 0 eta=0.500000 is short of 0.92 by 0.420000")
    print("miss: corner 1 eta=0.400000 is short of 0.92 by 0.520000")
    print("miss: corner 2 eta=0.100000 is short of 0.92 by 0.820000")
    print("observation: successive sum(|corner residual|) scales by 0.600000 = 3/5 on this boundary")
    print("that scale is the gasket flux factor for fixed corner potentials, not 0.08 and not 0.92")
    print("level 0 corner residual = [2.500000, -2.000000, -0.500000]; later levels multiply by (3/5)^n")
    print()
    print("experimental_validation = false")
    print("thrust_validated = false")
    print("energy_extraction_validated = false")
    if not locks_hold(rows):
        raise SystemExit("in-tree graph-proxy lock failed")


if __name__ == "__main__":
    main()
