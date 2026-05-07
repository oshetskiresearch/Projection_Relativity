
------------------------------
## Dynamic_Gravity: Dynamic Gravity Validation Suite
This repository contains the computational validation suite for Dynamic Gravity (DG). The framework treats observable physical sectors such as gravity, gauge fields, and the Higgs sector—as projections of a single internal spectral system.

Theoretical Overview
The core of this research is the Master Chain:
$$\Psi \rightarrow \hat{O}_\Psi \rightarrow \{u_n, \mu_n\} \rightarrow P_i[\Psi] \rightarrow \mathcal{O}_i$$ 
This repository provides tools to verify the algebraic and numerical consistency of this flow, focusing on:

* Internal Hilbert Space: Spectral operator ($\hat{O}_\Psi$) and eigenvalue equations.
* Emergent Geometry: Determinant-normalized metrics ($g_{eff}$) derived from correlation kernels.
* Gauge-Higgs Closure: Numerical predictions for fine structure ($\alpha^{-1}$) and boson masses ($m_W, m_Z$).

Project Structure
* documentation/: Core Master Equation Sheets and Dynamic Gravity theory PDFs.
* src/: Core mathematical logic for symbolic and numerical computations.
* testers/: Python-based validation scripts for symbolic and numerical checks.
* results/: Output data, scoreboard CSVs, and benchmark logs.

Validation Tester Suite
This project is under active development. The current suite includes:
| Tester | Purpose | Status |
|---|---|---|
| Action Variation | Euler–Lagrange checks for $\mathcal{L}_\Psi$ and gauge variations. | Active |
| Tensor Consistency | Kerr determinant, inverse, and Schwarzschild Ricci-flatness. | Active |
| Curvature Geometry | Einstein tensor and Kerr algebraic geometry verification. | Active |
| Fine Structure | Numerical closure for $\alpha^{-1}$ and compact winding scales. | Active |
| Finite-Core Regularity | Testing curvature saturation and density cutoffs. | Upcoming |

Results & Benchmarks
The results/ directory stores the latest computational runs. Key targets for current first-order closures include:

* Fine Structure: $\alpha^{-1}_{DG} \simeq 137.1877$
* Weak Angle: $\sin^2 \theta_{W}^{DG} \simeq 0.232518$
* Mass Closure: $m_W \simeq 80.116$ GeV / $m_Z \simeq 91.451$ GeV

Getting Started
   1. Prerequisites:
  
   pip install numpy sympy
  
   2. Run a Test:
  
   python testers/action_variation_tester_v3.1.py
  
   3. Verify Data: Compare generated .csv files in the results/ folder against the documentation.

------------------------------
Michael Stanislaus Oshetski
ORCID: 0009-0007-3623-7586
------------------------------


