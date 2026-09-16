"""Reproducible localization metric.

Region is defined BEFORE the number is evaluated.

    eta_region = (integrated |response| in region) / (integrated |response| over domain)

On the gasket graph the public response without a field solver is the
nodal residual current r = L u. PROXY, not Maxwell stress divergence.
The historical 92% figure is a HYPOTHESIS and is not returned here.
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
