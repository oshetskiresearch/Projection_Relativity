Projection Relativity Numerical Validation Harness
Scope: numerically validated where machine-checkable; complements the Maple symbolic checker.

Summary
Overall status: PASS
Run mode: stress
PASS: 113
WARNING: 0
FAIL: 0
QNM backend: analytic Kerr 220 fit fallback
Scorecard
Core theory numerics: PASS
Weak-gravity GR recovery: PASS
Strong-gravity GR exterior: PASS
Physical semantics: PASS
Phenomenology diagnostics: PASS
Paper/supplement source text: PASS
Stress and failure injection: PASS
Key Values
lambda0 finite-difference: 2.322863529581
lambda1 finite-difference: 5.375830272675
mu_min^2 finite-difference: 3.052966743094
final radial convergence error: 1.630251489360e-12
radial stability gap CV: 6.420005096628e-02
vacuum scan baseline rank: 1
c_bc: 0.796684464847899
Phi_theta^PR Wb: 9.009597185360e-15
B area-law coefficient nG m^2: 9.009597185360e-02
r_core/r_g benchmark: 3.288224774381e-04
Mercury perihelion GR check: 42.981975 arcsec/century
solar-grazing light bending GR check: 1.751243 arcsec
PPN gamma: 1.000000000000
PPN beta: 1.000000000000
de Sitter precession check: 6.620972 arcsec/year
binary-pulsar orbital-decay relative error: 2.136188770893e-05
max Kerr ergosurface g_tt residual: 2.220446049250e-16
far-field frame dragging residual: 1.937950723987e-05
Schwarzschild ISCO radius: 6.000000000000 M
max gap-residual amplitude ratio: 2.110739164295e-03
Friedmann H0 recovery residual: 0.000000000000e+00
Boundary Language
This Python suite is numerical. It does not replace the Maple symbolic checker and does not claim every physical or observational statement is certified beyond the machine-checkable scope
