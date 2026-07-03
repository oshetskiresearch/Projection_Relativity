# PR-III Equation Dependency Graph

This document records the dependency structure for PR-III. The purpose is to keep the manuscript and compiler aligned: every output must trace back to inherited projection geometry or to a newly derived PR-III object.

---

## 1. Master dependency chain

\[
\boxed{
\Psi(x,\xi)
\rightarrow
\{P_{\rm disp},P_A,P_{\rm EW},P_3,P_{\rm rad}\}
\rightarrow
\{\mathcal H_{\rm PR},\Delta\Gamma_{\rm PR},Z_1,Z_2,Z_3\}
\rightarrow
\{\alpha,\sin^2\theta_W,G_F,\alpha_s,\text{mass stability}\}.
}
\]

PR-III is therefore a precision layer on top of PR-II:

\[
\boxed{
\mathcal O_{\rm PR}^{\rm phys}
=
\mathcal O_{\rm PR}^{(0)}
+
\Delta\mathcal O_{\rm PR}^{\rm rad}
+O(\Delta^2).
}
\]

---

## 2. Scalar Hessian branch

Inherited displacement potential:

\[
V_{\rm disp}(A)=V_0+\alpha_AA^2+\beta_AA^4,
\qquad
\beta_A>0.
\]

Vacuum:

\[
A_0^2=-\frac{\alpha_A}{2\beta_A}.
\]

Single-amplitude curvature:

\[
m_A^2=
\left.\frac{d^2V_{\rm disp}}{dA^2}\right|_{A_0}
=-4\alpha_A
=8\beta_AA_0^2.
\]

Full PR-III Hessian:

\[
\boxed{
\mathcal H_{AB}^{\rm PR}
=
\left.
\frac{\partial^2V_{\rm PR}}
{\partial\varphi^A\partial\varphi^B}
\right|_{\varphi=\varphi_0}.
}
\]

Candidate coordinate set:

\[
\varphi^A
=\{A,\theta,Y,W^a,\chi^A_{\rm color},\ldots\}.
\]

Physical stability condition after gauge-null removal:

\[
\boxed{
\operatorname{spec}(\mathcal H_{\rm PR}^{\rm phys})\ge0.
}
\]

---

## 3. Radiative effective-action branch

Define the PR-native one-loop layer:

\[
\boxed{
\Delta\Gamma_{\rm PR}^{(1)}
=
\frac12
\operatorname{Tr}_{\rm PR}
\log
\left(
\mathcal H_{\rm PR}\mathcal H_{\rm ref}^{-1}
\right)
-
\operatorname{Tr}_{\rm ghost}
\log
\left(
\mathcal M_{\rm ghost}\mathcal M_{\rm ref}^{-1}
\right).
}
\]

Radiative normalization shifts:

\[
\boxed{
\Delta Z_A
=
\frac{\partial^2\Delta\Gamma_{\rm PR}^{(1)}}
{\partial F_{\mu\nu}\partial F^{\mu\nu}}.
}
\]

\[
\boxed{
\Delta Z_W
=
\frac{\partial^2\Delta\Gamma_{\rm PR}^{(1)}}
{\partial W^a_{\mu\nu}\partial W^{a\mu\nu}}.
}
\]

\[
\boxed{
\Delta Z_G
=
\frac{\partial^2\Delta\Gamma_{\rm PR}^{(1)}}
{\partial G^A_{\mu\nu}\partial G^{A\mu\nu}}.
}
\]

Fine-structure branch:

\[
\boxed{
\alpha_{\rm PR,phys}^{-1}
=
\alpha_{\rm PR,tree}^{-1}
+
\Delta\alpha_{\rm PR,rad}^{-1},
\qquad
\Delta\alpha_{\rm PR,rad}^{-1}=4\pi\Delta Z_A^{\rm PR}.
}
\]

---

## 4. Electroweak radiative branch

\[
\boxed{
\sin^2\theta_W^{\rm phys}
=
\sin^2\theta_W^{(0)}
+
\Delta\sin^2\theta_W^{\rm rad}.
}
\]

\[
\boxed{
G_F^{\rm phys}=G_F^{(0)}+\Delta G_F^{\rm rad}.
}
\]

\[
\boxed{
m_W^{\rm phys}=m_W^{(0)}+\Delta m_W^{\rm rad},
\qquad
m_Z^{\rm phys}=m_Z^{(0)}+\Delta m_Z^{\rm rad}.
}
\]

Custodial / rho audit:

\[
\boxed{
\rho_{\rm EW}^{\rm phys}
=
\frac{m_W^2}{m_Z^2\cos^2\theta_W}
=1+\Delta\rho_{\rm PR}^{\rm rad}.
}
\]

---

## 5. Neutrino radiative-stability branch

PR-II boundary output:

\[
\boxed{
m_{\beta\beta}^{\rm PR}=1.508\ \mathrm{meV}.
}
\]

PR-III stability check:

\[
\boxed{
m_{\beta\beta}^{\rm phys}
=m_{\beta\beta}^{(0)}
+
\Delta m_{\beta\beta}^{\rm rad}.
}
\]

Required qualitative result:

\[
\boxed{
|\Delta m_{\beta\beta}^{\rm rad}|
\ll
m_{\beta\beta}^{(0)}
\quad
\text{or a derived controlled correction.}
}
\]

---

## 6. Strong phase-fiber branch

Candidate internal extension:

\[
\boxed{
\mathcal M_{\rm int}^{\rm PR3}
=
\mathbb R_w
\times
\mathcal F_{\rm EW}
\times
\mathcal F_c,
\qquad
\mathcal F_c\sim SU(3)_c.
}
\]

Color connection:

\[
\boxed{
\mathcal G_\mu=G_\mu^AT_A,
\qquad
A=1,\ldots,8.
}
\]

Color curvature:

\[
\boxed{
\mathcal G_{\mu\nu}
=
\partial_\mu\mathcal G_\nu
-
\partial_\nu\mathcal G_\mu
+g_3[\mathcal G_\mu,\mathcal G_\nu].
}
\]

Component form:

\[
\boxed{
G_{\mu\nu}^A
=
\partial_\mu G_\nu^A
-
\partial_\nu G_\mu^A
+g_3f^{ABC}G_\mu^BG_\nu^C.
}
\]

Generator normalization audit:

\[
\boxed{
\operatorname{Tr}(T_AT_B)=\frac12\delta_{AB}.
}
\]

Strong closure targets:

\[
\boxed{
Z_3^{\rm PR},
\qquad
g_3^{\rm PR},
\qquad
\alpha_s^{\rm PR}(\mu).
}
\]

---

## 7. Running coupling branch

\[
\boxed{
\mu\frac{dg_i}{d\mu}
=
\beta_i^{\rm PR}(g_1,g_2,g_3;\mathcal M_{\rm int}),
\qquad
i=1,2,3.
}
\]

Required qualitative gates:

\[
\boxed{\beta_1>0,}
\]

\[
\boxed{\beta_2\ \text{consistent with electroweak matter content},}
\]

\[
\boxed{\beta_3<0.}
\]

The condition \(\beta_3<0\) is the asymptotic-freedom gate. Without it, PR-III may have an \(SU(3)\) algebra but not a QCD-like strong sector.

---

## 8. Anomaly-audit branch

Required checks:

\[
[SU(3)]^3,
\qquad
[SU(2)]^2U(1),
\qquad
[SU(3)]^2U(1),
\qquad
[U(1)]^3,
\qquad
[\mathrm{grav}]^2U(1).
\]

Practical ledger form:

\[
\boxed{
\sum_{\rm left}Y=0,
\qquad
\sum_{\rm left}Y^3=0.
}
\]

\[
\boxed{
\sum_{\rm doublets}Y=0,
\qquad
\sum_{\rm color\ triplets}Y=0.
}
\]

If these do not vanish, PR-III must either derive a geometric cancellation or stop.

---

## 9. Manuscript dependency summary

The manuscript should proceed in this order:

```text
Inherited ledger
-> scalar Hessian
-> gauge-null quotient
-> radiative determinant
-> alpha precision closure
-> electroweak precision stability
-> neutrino stability
-> SU(3) fiber
-> running couplings
-> anomaly audit
-> no-fit audit
```

This order keeps PR-III from opening the strong sector before the exposed PR-II radiative seam is closed.
