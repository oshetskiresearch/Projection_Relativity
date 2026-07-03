# PR-III Scope Ledger

## Purpose

PR-III is the radiative and strong-sector continuation of PR-I and PR-II. Its purpose is to test whether the electroweak and flavor boundary ledger developed in PR-II survives the next precision layer.

\[
\boxed{\text{PR-III} = \text{radiative closure} + \text{scalar Hessian} + SU(3)_c\ \text{phase-fiber topology}}
\]

PR-III should be written as a closure and falsification program, not as a discovery-sprawl manuscript.

---

## 1. Inherited objects

These objects are inherited and should not be redefined unless a revision explicitly changes the prior ledger.

| Object | Inherited from | PR-III role |
|---|---|---|
| \(\Psi(x,\xi)\) | PR-I | Master projection field |
| \(\mathcal M_{\rm int}=\mathbb R_w\times S^1_\theta\) | PR-I | Radial stiffness and compact phase seed |
| \(O_X\) | PR-I | Radial spectral regulator |
| \(O_\theta\) | PR-I | Compact phase operator |
| \(\mu_{\min}^2\) | PR-I | Gap, finite-core scale, and low-energy residual suppressor |
| \(P_g\) | PR-I | Gravitational projection sector |
| \(P_{\rm disp}\) | PR-I / PR-II | Scalar displacement and Hessian source |
| \(P_A\) | PR-I / PR-II | Electromagnetic compact phase projection |
| \(P_X\) | PR-I | Projection-response / residual sector |
| \(P_\theta\) | PR-I | Cosmological compact phase-stress sector |
| \(SU(2)_L\times U(1)_Y\) boundary ledger | PR-II | Electroweak tree / boundary input |
| Projection flavor sheets | PR-II | Charged-lepton, quark, CKM, PMNS, and neutrino ledgers |
| \(m_{\beta\beta}^{\rm PR}\) | PR-II | Neutrino radiative-stability target |

---

## 2. New PR-III objects

PR-III must define these objects from the inherited ledger.

| New object | Required role |
|---|---|
| \(\mathcal H_{\rm PR}\) | Full projected scalar / gauge Hessian |
| Gauge-null quotient | Removal of unphysical flat directions |
| \(\Delta\Gamma_{\rm PR}^{(1)}\) | PR-native radiative effective action |
| \(\Delta Z_A\) | Electromagnetic radiative normalization shift |
| \(\Delta Z_W\) | Weak-sector radiative normalization shift |
| \(\Delta Z_G\) | Strong-sector radiative normalization shift |
| \(\mathcal F_c\) | Candidate compact color phase fiber |
| \(P_3\) | Strong-sector projection operator |
| \(Z_3^{\rm PR}\) | Strong-fiber kinetic normalization |
| \(g_3^{\rm PR}\) | Strong coupling boundary output |
| \(\alpha_s^{\rm PR}(\mu)\) | Scale-dependent strong coupling |
| \(\beta_i^{\rm PR}\) | Running-coupling functions for \(i=1,2,3\) |
| Anomaly traces | Gauge and mixed gravitational consistency checks |
| No-fit audit table | Proof that target observables are not generation inputs |

---

## 3. Forbidden empirical generation inputs

The following may not be used as generation inputs. They may only be used after PR-III outputs are frozen.

- CODATA \(\alpha\)
- PDG \(m_W\), \(m_Z\), \(G_F\), \(\sin^2\theta_W\)
- PDG or lattice \(\alpha_s(m_Z)\)
- PDG quark masses
- Measured CKM matrix entries
- Measured PMNS matrix entries
- Measured neutrino mass targets
- Measured \(m_{\beta\beta}\) constraints as fitted targets

---

## 4. Required outputs

PR-III should attempt to generate or constrain:

\[
\alpha_{\rm PR,phys}^{-1}
=
\alpha_{\rm PR,tree}^{-1}
+
\Delta\alpha_{\rm PR,rad}^{-1},
\]

\[
\sin^2\theta_W^{\rm phys}
=
\sin^2\theta_W^{(0)}
+
\Delta\sin^2\theta_W^{\rm rad},
\]

\[
G_F^{\rm phys}
=
G_F^{(0)}+
\Delta G_F^{\rm rad},
\]

\[
m_W^{\rm phys}=m_W^{(0)}+\Delta m_W^{\rm rad},
\qquad
m_Z^{\rm phys}=m_Z^{(0)}+\Delta m_Z^{\rm rad},
\]

\[
\rho_{\rm EW}^{\rm phys}
=
\frac{m_W^2}{m_Z^2\cos^2\theta_W}
=1+\Delta\rho_{\rm PR}^{\rm rad},
\]

\[
m_{\beta\beta}^{\rm phys}
=
m_{\beta\beta}^{(0)}
+
\Delta m_{\beta\beta}^{\rm rad},
\]

\[
\alpha_s^{\rm PR}(\mu),
\qquad
\beta_3^{\rm PR}<0.
\]

---

## 5. Hard failure conditions

PR-III fails or must be narrowed if any of the following occur:

1. \(\mathcal H_{\rm PR}\) has unexplained negative physical eigenvalues.
2. Gauge-null modes cannot be cleanly separated from physical scalar/gauge modes.
3. \(\Delta\alpha_{\rm PR,rad}^{-1}\) requires CODATA \(\alpha\) as an input.
4. Electroweak radiative shifts require PDG weak observables as inputs.
5. The \(SU(3)\) algebra closes only by hand.
6. The strong-sector trace rule requires fitted \(\alpha_s\).
7. \(\beta_3^{\rm PR}\ge0\) for the QCD-like branch.
8. Gauge or mixed gravitational anomalies do not cancel and no geometric cancellation exists.
9. The PR-II neutrino branch is radiatively unstable.
10. The no-fit audit detects hidden target injection.

---

## 6. Immediate execution order

1. Freeze the inherited PR-I / PR-II ledger.
2. Define the scalar Hessian.
3. Remove gauge-null directions.
4. Define the PR-native radiative determinant.
5. Compute \(\Delta\alpha_{\rm PR,rad}^{-1}\).
6. Check electroweak radiative stability.
7. Check neutrino branch radiative stability.
8. Open \(SU(3)_c\) phase-fiber topology.
9. Derive or constrain \(Z_3^{\rm PR}\), \(g_3^{\rm PR}\), and \(\alpha_s^{\rm PR}(\mu)\).
10. Run anomaly and no-fit audits.

---

## 7. Working public posture

PR-III should state:

> PR-I established the radial--compact projection foundation. PR-II organized the electroweak and flavor ledger as compact boundary structure. PR-III tests whether that ledger survives scalar stability, radiative precision, and strong phase-fiber closure.

It should not state:

> PR-III completes all particle physics.

until the radiative, anomaly, and strong-sector closure gates pass.
