# Projection Relativity II Core Equation Derivations

This report records Maple-side derivation routes for central equations in the PR-II harness.

## B007 - Weak mixing from boundary deficit

- paper_location: sec:pr2_weak_mixing_boundary_closure
- maple_proc: `RunPR2Tests`
- start: `sin2 = 1/4 - (1-c_bc)/q_bc`
- maple_step: Substitute PR-I q_bc and c_bc, then evalf.
- result: `0.231355763298189`

## B017 - Weak scale from compact hierarchy action

- paper_location: sec:pr2_generated_weak_scale_fermi_constant
- maple_proc: `RunPR2Tests`
- start: `v_EW = Mbar_Pl exp(-S_total) sqrt(q_bc c_bc sin2)`
- maple_step: Build S_base, add second-order non-Abelian correction, exponentiate.
- result: `246.21959589022453 GeV`

## A009 - Cubic hypercharge anomaly cancellation

- paper_location: sec:pr2_cubic_hypercharge_anomaly
- maple_proc: `RunPR2Tests`
- start: `6(1/3)^3 + 3(-4/3)^3 + 3(2/3)^3 + 2(-1)^3 + 2^3`
- maple_step: Simplify exact rational expression.
- result: `0`

## L010 - Koide identity from three-sheet trigonometry

- paper_location: sec:pr2_koide_identity_three_sheet_geometry
- maple_proc: `RunPR2Tests`
- start: `sum m_a/(sum sqrt(m_a))^2 with k_a(theta)`
- maple_step: Use sum cos(theta+2pi a/3)=0 and sum cos^2(...)=3/2.
- result: `2/3`

## Q011-Q020 - Three-loop QCD threshold ledger

- paper_location: sec:pr2_qcd_threshold_ledger
- maple_proc: `RunPR2Tests`
- start: `alpha_s^(nf)(mu,Lambda_nf)`
- maple_step: Invert three-loop running and impose alpha_s continuity at t, b, c thresholds.
- result: `Lambda_6, Lambda_5, Lambda_4, Lambda_3 and running diagnostics`

## M008/M018 - Flavor-matrix unitarity

- paper_location: sec:pr2_ckm_pmns_flavor_projection
- maple_proc: `RunPR2Tests`
- start: `V = standard unitary parameterization(s12,s23,s13,delta)`
- maple_step: Compute HermitianTranspose(V).V - I and take max residual.
- result: `CKM and PMNS residuals <= 1e-14`

## N015 - Neutrinoless double-beta effective mass

- paper_location: sec:pr2_majorana_phase_boundary
- maple_proc: `RunPR2Tests`
- start: `abs(m2 c13^2 s12^2 + m3 s13^2 exp(i phi_M))`
- maple_step: Use phi_M = pi C_conf and generated normal-ordering masses.
- result: `1.507694477e-3 eV`

