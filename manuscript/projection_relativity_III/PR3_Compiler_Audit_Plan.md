# PR-III Compiler Audit Plan

PR-III should be developed as a compiler-backed closure program. This document defines the first planned validation modules and the no-fit audit structure.

---

## 1. Compiler philosophy

Every major PR-III equation should map to a reproducible symbolic or numerical test.

The compiler must verify:

1. The result follows from inherited projection geometry.
2. Gauge-null directions are not counted as physical modes.
3. Target observables are not injected as generation inputs.
4. Radiative corrections are stable under resolution changes.
5. Strong-sector closure does not require hand-tuned constants.
6. Anomaly traces cancel or are geometrically accounted for.

---

## 2. Proposed module layout

```text
code/
  pr3_v00_inheritance_ledger.py
  pr3_v01_scalar_hessian.py
  pr3_v02_gauge_null_removal.py
  pr3_v03_radiative_determinant.py
  pr3_v04_alpha_rad_closure.py
  pr3_v05_weak_angle_rad_shift.py
  pr3_v06_neutrino_rad_stability.py
  pr3_v07_su3_generator_audit.py
  pr3_v08_su3_boundary_closure.py
  pr3_v09_running_couplings.py
  pr3_v10_anomaly_audit.py
  pr3_v11_no_fit_audit.py
```

---

## 3. Module descriptions

### `pr3_v00_inheritance_ledger.py`

Purpose: load and freeze inherited PR-I / PR-II constants, operators, and symbolic objects.

Must verify:

- \(O_X\) is inherited, not re-fitted.
- \(O_\theta\) is inherited, not re-fitted.
- \(\mu_{\min}^2\) is inherited.
- PR-II tree-level electroweak/flavor objects are imported as frozen baseline values.

Output:

```text
inheritance_ledger.json
```

---

### `pr3_v01_scalar_hessian.py`

Purpose: construct the scalar / displacement / phase / gauge Hessian.

Core equation:

\[
\mathcal H_{AB}^{\rm PR}
=
\left.
\frac{\partial^2V_{\rm PR}}
{\partial\varphi^A\partial\varphi^B}
\right|_{\varphi=\varphi_0}.
\]

Must verify:

- Single-amplitude limit reproduces \(m_A^2=-4\alpha_A=8\beta_AA_0^2\).
- Hessian is symmetric or self-adjoint under the correct projection metric.
- Numerical eigenvalues are stable under precision changes.

Output:

```text
scalar_hessian_matrix.json
scalar_hessian_spectrum.csv
```

---

### `pr3_v02_gauge_null_removal.py`

Purpose: identify and quotient gauge-null modes before physical stability testing.

Must verify:

- Null modes correspond to gauge redundancies.
- Physical Hessian spectrum is nonnegative.
- No negative eigenvalue is hidden by the quotient.

Output:

```text
gauge_null_modes.json
physical_hessian_spectrum.csv
```

Failure condition:

\[
\exists\lambda_i<0
\quad
\text{in the physical Hessian spectrum with no geometric interpretation.}
\]

---

### `pr3_v03_radiative_determinant.py`

Purpose: compute the PR-native radiative effective action.

Core equation:

\[
\Delta\Gamma_{\rm PR}^{(1)}
=
\frac12
\operatorname{Tr}_{\rm PR}\log
(\mathcal H_{\rm PR}\mathcal H_{\rm ref}^{-1})
-
\operatorname{Tr}_{\rm ghost}\log
(\mathcal M_{\rm ghost}\mathcal M_{\rm ref}^{-1}).
\]

Must verify:

- Determinant or trace is regulated by the PR spectral ledger.
- Ghost contribution is included when gauge sectors are active.
- Result is stable under truncation / resolution changes.

Output:

```text
radiative_determinant_convergence.csv
radiative_effective_action.json
```

---

### `pr3_v04_alpha_rad_closure.py`

Purpose: compute the radiative correction to the inverse fine-structure constant.

Core equations:

\[
\Delta Z_A
=
\frac{\partial^2\Delta\Gamma_{\rm PR}^{(1)}}
{\partial F_{\mu\nu}\partial F^{\mu\nu}},
\]

\[
\alpha_{\rm PR,phys}^{-1}
=
\alpha_{\rm PR,tree}^{-1}
+4\pi\Delta Z_A^{\rm PR}.
\]

Must verify:

- CODATA \(\alpha\) is not imported.
- Correction is generated from \(O_X,O_\theta,P_A,P_{\rm EW},\mathcal H_{\rm PR}\).
- Tree value and radiative shift are separately reported.

Output:

```text
alpha_radiative_closure.json
alpha_no_fit_trace.log
```

---

### `pr3_v05_weak_angle_rad_shift.py`

Purpose: compute or bound electroweak radiative shifts.

Targets:

\[
\Delta\sin^2\theta_W,
\quad
\Delta G_F,
\quad
\Delta m_W,
\quad
\Delta m_Z,
\quad
\Delta\rho_{\rm PR}^{\rm rad}.
\]

Must verify:

- No PDG electroweak values are generation inputs.
- \(\rho_{\rm EW}^{(0)}=1\) is preserved at tree level.
- Radiative corrections are controlled.

Output:

```text
electroweak_radiative_shifts.json
rho_parameter_audit.json
```

---

### `pr3_v06_neutrino_rad_stability.py`

Purpose: test whether the PR-II neutrino branch is radiatively stable.

Target:

\[
m_{\beta\beta}^{\rm PR}=1.508\ \mathrm{meV}.
\]

Must verify:

- PR-II value is imported as a tree/boundary output.
- \(\Delta m_{\beta\beta}^{\rm rad}\) is derived, bounded, or explicitly deferred.
- No experimental \(m_{\beta\beta}\) constraints are used as inputs.

Output:

```text
neutrino_radiative_stability.json
```

---

### `pr3_v07_su3_generator_audit.py`

Purpose: verify strong-fiber algebra.

Must verify:

\[
[T_A,T_B]=if^{ABC}T_C,
\]

\[
\operatorname{Tr}(T_AT_B)=\frac12\delta_{AB}.
\]

Output:

```text
su3_generator_audit.json
su3_structure_constants.csv
```

---

### `pr3_v08_su3_boundary_closure.py`

Purpose: derive or constrain the strong-fiber boundary normalization.

Targets:

\[
Z_3^{\rm PR},
\qquad
g_3^{\rm PR},
\qquad
\alpha_s^{\rm PR}(\mu).
\]

Must verify:

- \(\alpha_s(m_Z)\) is not an input.
- Boundary closure is geometric, not numerical fitting.
- Failed closures are logged.

Output:

```text
su3_boundary_closure.json
su3_failed_closure_ledger.md
```

---

### `pr3_v09_running_couplings.py`

Purpose: compute or audit running-coupling behavior.

Core equation:

\[
\mu\frac{dg_i}{d\mu}=\beta_i^{\rm PR}(g_1,g_2,g_3;\mathcal M_{\rm int}).
\]

Required qualitative gates:

\[
\beta_1>0,
\qquad
\beta_3<0.
\]

Output:

```text
running_coupling_audit.json
beta_function_signs.csv
```

---

### `pr3_v10_anomaly_audit.py`

Purpose: verify gauge and mixed gravitational anomaly cancellation.

Required checks:

- \([SU(3)]^3\)
- \([SU(2)]^2U(1)\)
- \([SU(3)]^2U(1)\)
- \([U(1)]^3\)
- \([\mathrm{grav}]^2U(1)\)

Output:

```text
anomaly_audit.json
anomaly_trace_table.csv
```

Failure condition:

Any uncancelled anomaly without a derived geometric cancellation.

---

### `pr3_v11_no_fit_audit.py`

Purpose: scan all PR-III modules for forbidden empirical inputs.

Must verify forbidden data are not used as generation inputs:

- CODATA \(\alpha\)
- PDG electroweak masses and couplings
- PDG \(\alpha_s\)
- CKM/PMNS observed entries
- Quark and lepton masses as target inputs
- Neutrino mass observables as target inputs

Output:

```text
no_fit_audit_report.md
no_fit_dependency_graph.json
```

---

## 4. Standard output table

Every module should produce a row in the master audit table:

| Quantity | Generated by | Forbidden input check | Status |
|---|---|---|---|
| \(\Delta\alpha^{-1}_{\rm rad}\) | PR radiative determinant | no CODATA \(\alpha\) | pass/fail |
| \(\Delta\sin^2\theta_W\) | \(Z_1,Z_2\) shifts | no PDG weak angle | pass/fail |
| \(Z_3\) | color boundary ledger | no \(\alpha_s\) input | pass/fail |
| \(\beta_3\) sign | representation / fiber trace | no QCD fit | pass/fail |
| anomalies | representation ledger | no manual cancellation | pass/fail |
| Hessian spectrum | \(V_{\rm PR}\) | no manual mass insertion | pass/fail |

---

## 5. First sprint

The first implementation sprint should produce only these modules:

```text
pr3_v00_inheritance_ledger.py
pr3_v01_scalar_hessian.py
pr3_v02_gauge_null_removal.py
pr3_v03_radiative_determinant.py
pr3_v04_alpha_rad_closure.py
```

No \(SU(3)\) public claim should be made until the scalar Hessian and radiative fine-structure gap are under control.
