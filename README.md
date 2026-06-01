# Projection Relativity Sandbox

**Project:** Projection Relativity  
**Primary manuscript:** `paper/Oshetski_Projection_Relativity_Main.tex`   
**Manuscript Supplement:** `paper/Oshetski_Projection_Relativity_Supplement.tex`   
**Manuscript References:** `paper/Oshetski_Projection_Relativity_References.tex`   
**Author:** Michael Stanislaus Oshetski  
**ORCID:** [0009-0007-3623-7586](https://orcid.org/0009-0007-3623-7586)   
**Repository:** `oshetskiresearch/Projection-Relativity`  
**Status:** Active research sandbox / manuscript support repository  

---

**Overview**

Projection Relativity, abbreviated PR, is a geometry-first research program that treats observable physical sectors as projections of a single underlying spectral structure.
The framework is organized around a master projection field:
```math
\Psi(x,\xi)
```
Here, `x` denotes observable spacetime coordinates, while `xi` denotes internal projection coordinates.
In the minimal construction used by the main manuscript, the internal projection space has cylindrical structure:
```math
\mathcal{M}_{\mathrm{int}}
=
\mathbb{R}_{w}
\times
S^{1}_{\theta}
```
The non-compact coordinate `w` supplies a radial stiffness direction.  
The compact coordinate `theta` supplies a phase and winding direction.
The purpose of this repository is to support development of the Projection Relativity manuscript by keeping derivations, numerical tests, observational audits, plots, notes, failed paths, and reproducibility materials in one organized place.

---
**Core Concept**

Projection Relativity asks whether gravitational response, effective inertia, electromagnetic phase structure, and strong-field regularization can be described as different observable projections of one common internal geometric system.
Instead of treating each physical sector as an unrelated addition, PR organizes them as projection outputs from the same underlying field structure.
The basic conceptual chain is:
```text
master projection field
        ↓
internal spectral geometry
        ↓
sector projections
        ↓
observable stiffness, inertia, phase, and effective metric response
```
In symbolic form:
```math
\Psi(x,\xi)
\longrightarrow
\mathcal{M}_{\mathrm{int}}
\longrightarrow
\{P_X,\ P_{\mathrm{disp}},\ P_{\theta}\}
\longrightarrow
\{g_{\mu\nu}^{\mathrm{eff}},\ \mathcal{M}_{\mathrm{eff}},\ \alpha_{\mathrm{PR}}\}
```
The repository is therefore structured around separate but connected branches of the theory.

---
**Main Projection Sectors**

**1. Radial Stiffness / Gravitational Sector**

The radial coordinate `w` defines the stiffness direction of the internal projection space. This sector is used to study gravitational response, the radial spectral gap, low-energy General Relativity recovery, and strong-field regularization.
Representative objects include:
```math
O_X,
\qquad
\mu_{\min}^{2},
\qquad
g_{\mu\nu}^{\mathrm{eff}}
```
where `O_X` is the radial stiffness operator, `mu_min^2` is the first radial spectral gap, and `g_eff` is the effective projected metric.
This branch includes tests of the radial potential form:
```math
V_X(w)
=
1+w^2+\frac{3}{4}w^4
```
The radial branch is used to test whether a finite spectral stiffness floor can support gravitational recovery in the weak-field regime and finite-core regularization in the strong-field regime.

---
**2. Displacement / Effective Inertia Sector**

The displacement sector describes stable nonzero projection displacement and its contribution to effective inertial response.
This sector should be described in PR-native terms, not Standard Model terminology. The preferred language is:
```text
displacement sector
displacement potential
matter-displacement overlap
effective inertia matrix
stable nonzero displacement vacuum
```
Representative objects include:
```math
P_{\mathrm{disp}}[\Psi],
\qquad
\Phi_{\mathrm{disp}}(x),
\qquad
A(x),
\qquad
A_0,
\qquad
m_A,
\qquad
\mathcal{M}_{\mathrm{eff}}
```
Here `P_disp[Psi]` is the displacement projection, `Phi_disp(x)` is the projected displacement field, `A(x)` is the local displacement amplitude, `A_0` is the stable nonzero displacement vacuum, `m_A` is the displacement excitation scale, and `M_eff` is the effective inertia matrix.
A typical PR-native displacement chain is:
```math
\Psi
\longrightarrow
P_{\mathrm{disp}}[\Psi]
\longrightarrow
\Phi_{\mathrm{disp}}(x)
\longrightarrow
A(x)
\longrightarrow
A_0
\longrightarrow
m_A
\longrightarrow
\mathcal{M}_{\mathrm{eff}}
\longrightarrow
T_{\mu\nu}
\longrightarrow
g_{\mu\nu}^{\mathrm{eff}}
```
A representative displacement potential is:
```math
V_{\mathrm{disp}}(A)
=
V_0+\alpha_A A^2+\beta_A A^4
```
The stable nonzero displacement vacuum satisfies:
```math
A_0^2
=
-\frac{\alpha_A}{2\beta_A}
```
The displacement excitation scale is:
```math
m_A^2
=
\left.
\frac{d^2 V_{\mathrm{disp}}}{dA^2}
\right|_{A_0}
=
-4\alpha_A
=
8\beta_A A_0^2
```
---
**3. Compact Phase / Electromagnetic Sector**

The compact coordinate `theta` represents internal phase winding. This sector is used to study compact phase closure, electromagnetic-type structure, and fine-structure normalization from geometric constraints.
Representative objects include:
```math
O_{\theta},
\qquad
R_A,
\qquad
\theta,
\qquad
J_{\theta}^{\mu},
\qquad
\alpha_{\mathrm{PR}}
```
Here `O_theta` is the compact phase operator, `R_A` is the compact phase radius or normalization scale, `theta` is the compact internal phase coordinate, `J_theta^mu` is the conserved compact phase current, and `alpha_PR` is the PR fine-structure normalization.
The projection-field decomposition is commonly written as:
```math
\Psi
=
A e^{i\theta}
```
The associated compact phase current has the form:
```math
J_{\theta}^{\mu}
=
A^2 \partial^{\mu}\theta
```
The compact phase sector is treated as a geometric closure problem rather than as an inserted numerical normalization.

---
**4. Propagator and GR-Recovery Branch**

The propagator branch tests whether the projected theory preserves the correct low-energy gravitational behavior.
The target is that the projected theory recovers the massless low-energy gravitational pole and reduces to the General Relativity limit where required.
Representative objects include:
```math
G_{\mathrm{PR}}(k),
\qquad
F(k^2),
\qquad
G_{\mathrm{GR}}(k)
```
Here `G_PR(k)` is the projected gravitational propagator, `F(k^2)` is the projection correction or form factor, and `G_GR(k)` is the General Relativity low-energy propagator limit.
The required infrared recovery condition is schematically:
```math
G_{\mathrm{PR}}(k)
\longrightarrow
G_{\mathrm{GR}}(k)
\qquad
\mathrm{as}
\qquad
k^2 \rightarrow 0
```
This branch tracks:
```text
propagator structure
infrared limit
massless pole recovery
absence of unwanted extra poles
continuum stability
GR correspondence
```
---
**5. Finite-Core / Strong-Field Branch**

The finite-core branch tests whether the radial spectral gap produces a finite curvature ceiling and finite core radius in strong-field regimes.
This branch is used to study whether PR can regularize classical singular endpoints through geometric stiffness rather than through an externally imposed cutoff.
Representative objects include:
```math
r_c,
\qquad
K_{\max},
\qquad
\mu_{\min}^{2},
\qquad
\rho_{\mathrm{core}}
```
Here `r_c` is the finite core radius, `K_max` is the curvature ceiling, `mu_min^2` is the radial stiffness floor, and `rho_core` is the finite core density scale.
Representative topics include:
```text
finite core radius
curvature ceiling
radial stiffness floor
singularity avoidance
strong-field endpoint behavior
```
---
**6. Observational Audit Branches**

Observational audits are stored separately from core theory derivations. These audits are treated conservatively and are not described as externally confirmed unless all required controls and independent reproduction support that interpretation.
Current observational audit areas include:
```text
quasar residual tests
LoTSS / Faraday-rotation magnetic-area constraints
ringdown residual searches after Kerr subtraction
magnetar spin-residual diagnostics
foreground-control tests
matched-bin and random-label controls
```

The current PR magnetic-field branch is an area-law constraint, not a fixed universal magnetic-amplitude claim. The compact phase sector fixes a flux normalization, while the realized projected compact-phase area sets the magnetic field amplitude.

The gauge-invariant compact phase gradient is:
```math
X_{\mu}
=
\partial_{\mu}\theta
-
q\mathcal{A}_{\mu}
```
A residual compact phase-gradient curl defines the residual field strength:
```math
F_{\mu\nu}^{\mathrm{res}}
=
-\frac{1}{q}
\partial_{[\mu}X_{\nu]}^{\mathrm{res}}
```
Using the compact phase closure, the fixed PR compact flux normalization is:
```math
\Phi_{\theta}^{\mathrm{PR}}
=
\frac{\hbar}{e}
\frac{Z_A}{c_{\mathrm{bc}}}
=
9.009597185\times 10^{-15}\ \mathrm{Wb}
```
The magnetic area law is:
```math
B_{\mathrm{geo}}^{\mathrm{PR}}
=
\frac{\Phi_{\theta}^{\mathrm{PR}}}
{A_{\mathrm{proj}}^{(\theta)}}
```
or, in nanogauss with projected compact-phase area in square meters:
```math
B_{\mathrm{geo}}^{\mathrm{PR}}[\mathrm{nG}]
=
\frac{0.09009597185}
{A_{\mathrm{proj}}^{(\theta)}[\mathrm{m}^{2}]}
```
The Faraday-rotation mapping used for LoTSS-style constraints is:
```math
\mathrm{RM}_{\mathrm{pred}}
=
812\,n_e[\mathrm{cm}^{-3}]\,L[\mathrm{Mpc}]\,
B_{\mathrm{geo}}^{\mathrm{PR}}[\mathrm{nG}]\,
W_{\mathrm{EM}}
```
with:
```math
W_{\mathrm{EM}}
=
W_{\mathrm{orient}}W_{\mathrm{coh}}W_{\mathrm{fill}}W_z
```
Thus LoTSS/Faraday residuals are used to constrain the realized projected compact-phase area under plasma, coherence, filling, orientation, and redshift-window assumptions.

---
**Research Goals**

The current goals of the Projection Relativity sandbox are:
Develop a mathematically closed projection architecture from a minimal internal manifold.
Derive observable sectors from projection operations rather than from unrelated inserted assumptions.
Recover known low-energy gravitational behavior in the appropriate limit.
Test whether the radial spectral gap can regularize strong-field singular endpoints.
Derive compact phase normalization from geometric closure conditions.
Maintain reproducible numerical tests for every quantitative claim.
Track supported, preliminary, failed, and pending branches transparently.
Keep manuscript claims tied to explicit derivations, code, outputs, and interpretation notes.

---
**Repository Structure**

```text
Projection-Relativity/
│
├── manuscript/
│   ├── /Oshetski_Projection_Relativity_Main.tex
│   ├── /Oshetski_Projection_Relativity_Supplement.tex
│   ├── /Oshetski_Projection_Relativity_References.tex   
│   ├── /Oshetski_Projection_Relativity_Main.pdf
│   ├── /Oshetski_Projection_Relativity_Supplement.pdf
│   └── /Oshetski_Projection_Relativity_References.pdf  
│
├── test_harness/
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   ├── 
│   └── ...
│
├── data/
│   ├── README.md
│   ├── processed/
│   └── ...
│
├── plots/
│   ├── RESULTS_INDEX.md
│   ├── pr_lotss_magnetic_field/
│   └── ...
│
├── LICENSE
│
└── README.md
```
---
**Directory Guide**

Path	Purpose
`manuscript/`	Main manuscript and older drafts.
`test_harness/`	Reproducible scripts for theory tests, observational audits, and result generation.
`data/`	        Data policy, metadata, processed subsets, and reproducible download instructions. Raw large datasets are not stored here.
`plots/`	Generation code and plot outputs.

---
**Data Policy**

Raw external datasets are not stored in this repository.
The repository may include:
processed subsets,
reduced CSV extracts,
metadata,
reproducible download instructions,
audit summaries,
plots,
interpretation notes,
and lightweight derived results.
The repository should not include:
raw FITS files,
large raw catalogs,
private data,
secrets,
credentials,
API keys,
local environment files,
or machine-specific cache files.
Large or externally licensed datasets should be referenced through their source, DOI, archive link, or reproducible acquisition instructions.

---
**Reproducibility Policy**

Every major claim should be traceable to at least one of the following:
a manuscript derivation,
a script in `code/`,
a reduced result table in `results/`,
a test note in `tests/`,
a study note in `notes/`,
a finding summary in `finds/`,
or an explicit failed-path record in `docs/failed_paths/`.
Results should be labeled conservatively.
Label	Meaning
`supported`	Reproduced numerically or analytically in the sandbox.
`preliminary`	Directionally useful but not yet publication-grade.
`failed/de-emphasized`	Tested and found weak, contaminated, or non-supportive.
`pending`	Planned but not yet executed.

---
**Manuscript**

The main working manuscript is:
```text
manuscript/Oshetski_Projection_Relativity.tex
```
Working title:
```text
The Foundation of Projection Relativity:
A Spectral-Projection Architecture for Emergent Relativity
```
The manuscript develops the PR architecture from a master projection field and its internal spectral manifold. This repository supports the manuscript by preserving derivations, numerical tests, observational audits, plots, notes, and result summaries needed for transparent review.

---
**Development Workflow**

Workflow:
```bash
git checkout main
git pull

git checkout -b docs/or-code-branch-name

# edit files
# run checks
# update notes/results/tests as needed

git status
git add .
git commit -m "Describe the update"
git push -u origin docs/or-code-branch-name
```
Then open a pull request into `main`.

---
**Claim Discipline**

Projection Relativity is an active theoretical and computational research program. Repository language should clearly distinguish between:
derivation,
numerical support,
observational consistency,
preliminary evidence,
failed tests,
and open conjecture.
Do not describe preliminary observational audits as detections unless the required controls have been satisfied.
For example, the LoTSS residual-RM magnetic-field audit should be described as a projected compact-phase area constraint under plasma/window assumptions, not as a standalone cosmological magnetic-field detection or a universal fixed-field prediction.

---
**Citation / Attribution**

Author:
```text
Michael Stanislaus Oshetski
ORCID: 0009-0007-3623-7586
```
Project:
```text
Projection Relativity
```
Primary manuscript:
```text
The Foundation of Projection Relativity:
A Spectral-Projection Architecture for Emergent Relativity
```
Repository:
```text
oshetskiresearch/Projection-Relativity
```
A formal citation file may be added later as:
```text
CITATION.cff
```
---
**License**

License status is included in this repo.
```text
LICENSE
```
and update this README section accordingly.

---
**Maintainer Notes**

This repository is intended to remain transparent, auditable, and conservative in interpretation.
Preferred result workflow:
```text
derive
→ test
→ record
→ interpret
→ label status
```
Every result should be easy to trace from manuscript claim to code, output, and interpretation note.
