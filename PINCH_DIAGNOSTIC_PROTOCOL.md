# Topological Pinch — Diagnostic Protocol

**Status:** Hypothesis + measurement protocol (claim level 0–1)  
**92% aft-face figure:** **unverified**  
**Linked framework:** [momentum-closure/MOMENTUM_PINCH_FRAMEWORK.md](https://github.com/beyond-repair/momentum-closure)

---

## 1. Hypothesis (precise)

On the 0.45 asymmetric Sierpinski-type geometry, the traction density
\(t_i = T_{\rm eff}^{ij} n_j\) is **not** uniformly distributed: a dominant fraction of
\(\int |t|\,dA\) (or of directed flux) concentrates on the **aft** face / fractal vertices.

This is offered as a possible *mechanism for incomplete cancellation* on a closed surface — not as a measured continuum force.

---

## 2. Relation to momentum closure

Momentum closure requires:

$$
\mathbf{F} = \oint T_{\rm eff}\cdot n\, dA.
$$

Pinch asks a finer question:

$$
\mathbf{F} = \mathbf{F}_{\rm aft} + \mathbf{F}_{\rm fore},
\qquad
L = \frac{|\mathbf{F}_{\rm aft}|}{|\mathbf{F}_{\rm aft}|+|\mathbf{F}_{\rm fore}|+\varepsilon}.
$$

- High \(L\) with **net** \(|\mathbf{F}|\) at noise floor → localization of *noise* or canceling pairs, **not** thrust.  
- High \(L\) with net \(|\mathbf{F}|\) **above** spherical control floor under refinement → only then a candidate continuum signal (still not `thrust_validated`).

---

## 3. Protocol (when attached to a frozen field problem)

1. **Freeze** constitutive map + BCs (acceptance criterion step 1).  
2. **Sphere control:** same T and partition logic; net F and preferred-axis L must be consistent with null.  
3. **Define partition** on the 0.45 mesh: aft face (opposite designated vertex) vs remaining faces; optional vertex-neighborhood sets.  
4. **Solve** fields; evaluate \(T_{\rm eff}\) on facets.  
5. **Report table** under joint refinement:  
   `|F_net|`, `|F_aft|`, `|F_fore|`, `L`, and sphere `|F_net|`.  
6. **Classify:**  
   - net ≤ floor → null (pinch fraction irrelevant to thrust);  
   - net > floor stably → candidate prediction path only.

**Forbidden:** quoting a single-run percentage (e.g. “92%”) without refinement and sphere control; fitting parameters to 30 μN/kW.

---

## 4. Stage-2 context

Scalar and Proca P-E2 studies archived as **null** for net continuum G.  
Those maps must not be reopened solely to “get a pinch percentage” without new constitutive/BVP content.

---

## 5. Claim flags

```
pinch_fraction_verified     = false
experimental_validation     = false
thrust_validated            = false
"92% figure"                = unverified
```
