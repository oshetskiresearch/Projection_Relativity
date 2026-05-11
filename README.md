# Projection Relativity

*A Spectral–Projection Framework for Emergent Gravity, Higgs Structure, and Electromagnetism*
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oshetskiresearch/Projection_Relativity/blob/main/Validation_Harness.ipynb)
---

## Overview

Projection Relativity (PR) is a spectral–projection framework that explores the emergence of gravity, Higgs structure, and electromagnetic behavior from a deeper projection-field architecture.

The framework is built around:
- A projection/master field
- An internal spectral operator
- Emergent spacetime geometry
- Finite-core gravitational structure
- Weak projection-sector corrections to classical Kerr/GR behavior

The project focuses on:
- Mathematical consistency
- Weak-field General Relativity recovery
- Kerr exterior closure
- Propagator stability
- Cosmological response structure
- Reproducible numerical validation

Projection Relativity does **not** discard General Relativity. Instead, the framework recovers GR/Kerr as the low-energy exterior limit:

$$
ds^2_{\mathrm{PR}} = ds^2_{\mathrm{Kerr}}, \qquad r > r_c
$$

The framework additionally predicts:
- Finite projection cores
- Weak projection-sector ringdown sidebands
- Spectral-geometry closure relationships

---

# Repository Structure

```text
ProjectionRelativity/
│
├── documents/
│   ├── Projection_Relativity_Main_Paper.tex
│   ├── Projection_Relativity_Main_Paper.pdf
│   ├── Projection_Relativity_Master_Equation_Sheet.tex
│   ├── projection_relativity_kerr_teukolsky_appendix.tex
│   ├── projection_relativity_kerr_teukolsky_appendix.pdf
│   └── dimensional_audit_report.txt
│
├── test_harness/
│   ├── projection_relativity_full_validation_harness.py
│   ├── projection_relativity_kerr_teukolsky_tester.py
│   └── validation_outputs.zip
│
├── data/
│   ├── projection_relativity_full_validation_results.csv
│   ├── projection_relativity_equation_status_table.csv
│   ├── projection_relativity_operator_rmax_scan.csv
│   ├── projection_relativity_kerr_exterior_summary.csv
│   ├── projection_relativity_full_teukolsky_qnm_results.csv
│   ├── projection_relativity_vacuum_selection_scan.csv
│   ├── projection_relativity_reference_comparison.csv
│   ├── projection_relativity_solar_system_summary.csv
│   ├── projection_relativity_solar_system_sweep.csv
│   ├── projection_relativity_sideband_mass_scaling.csv
│   ├── projection_relativity_qnm_backend_status.csv
│   ├── kerr_teukolsky_test_results.csv
│   ├── kerr_core_exterior_summary.csv
│   └── teukolsky_sideband_scan.csv
│
├── graphs/
│   ├── Internal Spectral Potential and Quantized Projection Modes.png
│   ├── pEmergent Metric Recovery and Finite-Core Regularization.png
│   ├── sideband_scaling.png
│   ├── cosmology_response.png
│   ├── vacuum_selection_scan.png
│   ├── kerr_exterior_validation.png
│   └── teukolsky_sideband_behavior.png
│
└── README.md
```

---

# Core Framework Components

## 1. Projection Field Structure

The framework begins with a projection/master field:

$$
\Psi(x,\xi)
$$

And an internal spectral operator:

$$
O_X = -\frac{d^2}{dw^2} + V_X(w)
$$

The operator structure generates:
- Spectral gaps
- Finite curvature scales
- Propagator corrections
- Projection-sector dynamics

---

## 2. Emergent Gravity

The effective metric emerges from projection correlations and recovers GR in the low-energy limit:

$$
G_{\mu\nu}^{\mathrm{PR}} = 0, \qquad r > r_c
$$

Weak-field tests recover:
- Newtonian gravity
- Light bending
- Shapiro delay
- Perihelion precession
- PPN consistency

---

## 3. Finite-Core Structure

The framework replaces singular cores with finite projection cores:

$$
r_c = \left( \frac{G_P M}{c^2 R_{\mathrm{max}}} \right)^{1/3}
$$

The projection core remains hidden inside:
- The horizon
- The photon ring
- The ISCO region

---

## 4. Kerr Exterior Closure

Outside the projection core:

$$
ds^2_{\mathrm{PR}} = ds^2_{\mathrm{Kerr}}
$$

The rotating exterior therefore preserves:
- Frame dragging
- Kerr horizons
- Ergospheres
- ISCO structure
- Standard exterior observables

---

## 5. Teukolsky Inheritance

Perturbations inherit the Kerr–Teukolsky structure:

$$
\mathcal{T}_{\mathrm{PR}} = \mathcal{T}_{\mathrm{Kerr}} + \Sigma_X
$$

The framework predicts only weak projection-sector residuals:

$$
A_X/A_0 \sim 10^{-3}
$$

---

# Validation Harnesses

## Full Validation Harness

Primary reproducibility suite: `projection_relativity_full_validation_harness.py`

Covers: Operator stability, propagator consistency, GR recovery, Kerr closure, cosmology, FSC closure, Higgs/EM safety, and solar-system recovery.

Current locked validation state:

$$
83\ \text{PASS}, \qquad 0\ \text{FAIL}, \qquad 0\ \text{OPEN}
$$

---

## Kerr / Teukolsky Closure Tester

Dedicated rotating black-hole validation suite: `projection_relativity_kerr_teukolsky_tester.py`

Current locked tester state:

$$
22\ \text{PASS}, \qquad 0\ \text{FAIL}
$$

---

# Dimensional Restoration Notes

The framework uses the coordinate convention $(t, r, \theta, \phi)$ rather than $(ct, r, \theta, \phi)$.

- The Kerr metric cross-term scales as $1/c$
- The determinant carries $c^2$
- Inverse metric temporal components retain consistent $c$-tracking

---

# Current Scope

Projection Relativity currently focuses on: **Gravity, Higgs structure, and Electromagnetism.**

The framework intentionally does **not** claim:
- Full Standard Model completion
- Fermion-family derivation
- Complete UV-finite quantum gravity proof

---

# License

This repository is released for technical review, reproducibility, and scientific discussion.

---

# Authors

**Michael Stanislaus Oshetski**  
ORCID: [0009-0007-3623-7586](https://orcid.org)

---

# Dedication

Dedicated to my brother and best friend,  
John Oshetski Jr. (“Motorhead”)

*“I’ll see you in the decoherence. Your information is never lost.”*
