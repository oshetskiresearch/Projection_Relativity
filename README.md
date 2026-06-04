# The Foundation of Projection Relativity   
**A Spectral-Projection Architecture for Emergent Relativity**  **[DOI](https://zenodo.org/records/20528719)**   

**Project:** Projection Relativity  
**Primary manuscript source:** `manuscript/Oshetski_Projection_Relativity_Main.tex`  
**Supplement source:** `manuscript/Oshetski_Projection_Relativity_Supplement.tex`  
**Bibliography:** `manuscript/Oshetski_Projection_Relativity_References.bib`  
**Primary manuscript PDF:** `manuscript/Oshetski_Projection_Relativity_Main.pdf`  
**Supplement PDF:** `manuscript/Oshetski_Projection_Relativity_Supplement.pdf`  
**Author:** Michael Stanislaus Oshetski  
**Email:** oshetski.research@proton.me  
**ORCID:** [0009-0007-3623-7586](https://orcid.org/0009-0007-3623-7586)  
**Repository:** `oshetskiresearch/Projection_Relativity`  
**Status:** Public manuscript and reproducibility package  

---

## Overview

Projection Relativity, abbreviated **PR**, is a geometry-first research framework in which observable physical sectors are treated as projections of a single underlying spectral structure. The framework is organized around a master projection field,

```math
\Psi(x,\xi),
```

where `x` denotes observable spacetime coordinates and `\xi` denotes internal projection coordinates. In the minimal construction used by the manuscript, the internal projection space has radial--compact cylindrical structure,

```math
\mathcal{M}_{\mathrm{int}}
=
\mathbb{R}_{w}
\times
S^{1}_{\theta}.
```

The non-compact coordinate `w` supplies the radial stiffness direction. The compact coordinate `\theta` supplies the phase and winding direction. This repository provides the manuscript, supplement, symbolic audit outputs, numerical validation scripts, derived data products, and plots needed to inspect and reproduce the claims made in the paper.

---

## Core Idea

Projection Relativity asks whether gravitational response, effective inertia, electromagnetic phase structure, and strong-field regularization can be described as different observable projections of one common internal geometric system. Instead of treating each physical sector as an unrelated addition, PR organizes them as outputs of projection maps acting on the same master field.

The conceptual chain is:

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
\{P_g,\ P_{\mathrm{disp}},\ P_A,\ P_X,\ P_\theta\}
\longrightarrow
\{g_{\mu\nu}^{\mathrm{eff}},\ \mathcal{M}_{\mathrm{eff}},\ A_\mu,\ \Sigma_X,\ H_{\mathrm{PR}}\}.
```

---

## Main Projection Sectors

### 1. Radial Stiffness / Gravitational Sector

The radial coordinate `w` defines the stiffness direction of the internal projection space. This sector is used to study gravitational response, the radial spectral gap, low-energy General Relativity recovery, Kerr exterior recovery, and finite-core regularization.

Representative objects include:

```math
O_X,
\qquad
\mu_{\min}^{2},
\qquad
g_{\mu\nu}^{\mathrm{eff}}.
```

Here `O_X` is the radial stiffness operator, `\mu_min^2` is the first radial spectral gap, and `g_eff` is the effective projected metric. The projection-trace radial branch is

```math
V_X(w)
=
1+w^2+\frac{3}{4}w^4.
```

This branch tests whether a finite spectral stiffness floor can support gravitational recovery in the weak-field regime and finite-core regularization in the strong-field regime.

---

### 2. Displacement / Effective Inertia Sector

The displacement sector describes stable nonzero projection displacement and its contribution to effective inertial response. The manuscript uses PR-native terminology: displacement sector, displacement potential, matter--displacement overlap, effective inertia matrix, and stable nonzero displacement vacuum.

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
\mathcal{M}_{\mathrm{eff}}.
```

A typical displacement chain is:

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
g_{\mu\nu}^{\mathrm{eff}}.
```

A representative displacement potential is:

```math
V_{\mathrm{disp}}(A)
=
V_0+\alpha_A A^2+\beta_A A^4.
```

The stable nonzero displacement vacuum satisfies:

```math
A_0^2
=
-\frac{\alpha_A}{2\beta_A},
```

and the displacement excitation scale is:

```math
m_A^2
=
\left.
\frac{d^2 V_{\mathrm{disp}}}{dA^2}
\right|_{A_0}
=
-4\alpha_A
=
8\beta_A A_0^2.
```

---

### 3. Compact Phase / Electromagnetic Sector

The compact coordinate `\theta` represents internal phase winding. This sector is used to study compact phase closure, electromagnetic-type structure, and boundary-resolved compact electromagnetic normalization from geometric constraints.

Representative objects include:

```math
O_{\theta},
\qquad
R_A,
\qquad
\theta,
\qquad
X_\mu,
\qquad
F_{\mu\nu},
\qquad
\alpha_{\mathrm{PR}}.
```

The projection-field decomposition is commonly written as:

```math
\Psi
=
A e^{i\theta}.
```

The gauge-invariant compact phase gradient is:

```math
X_{\mu}
=
\partial_{\mu}\theta
-
q\mathcal{A}_{\mu}.
```

The compact phase sector is treated as a geometric closure problem rather than as an inserted numerical normalization.

---

### 4. Propagator and Low-Energy Recovery

The propagator branch tests whether the projected theory preserves the correct low-energy gravitational behavior. The target is massless-pole recovery, Newton normalization, absence of unwanted low-energy poles, and correspondence with the GR limit where required.

Representative objects include:

```math
D_{\mu\nu\rho\sigma}^{(P)}(k),
\qquad
F_E(k^2),
\qquad
D_{\mu\nu\rho\sigma}^{(N)}(k).
```

The required low-energy condition is:

```math
F_E(z)=O(z^2),
\qquad
\frac{F_E(z)}{z}\rightarrow0
\quad
(z\rightarrow0).
```

This branch tracks propagator structure, infrared recovery, massless-pole preservation, pole-residue normalization, continuum stability, and GR correspondence.

---

### 5. Finite-Core / Strong-Field Branch

The finite-core branch tests whether the radial spectral gap produces a finite curvature ceiling and finite core radius in strong-field regimes. This branch studies whether PR can regularize classical singular endpoints through geometric stiffness rather than through an externally imposed cutoff.

Representative objects include:

```math
r_c,
\qquad
R_{\max},
\qquad
\mu_{\min}^{2},
\qquad
\rho_{\max}.
```

The core regularization chain is:

```math
\mu_{\min}^2>0
\quad\Longrightarrow\quad
R_{\max}<\infty
\quad\Longrightarrow\quad
r_c(M)
=
\left(
\frac{G_NM}{c^2R_{\max}}
\right)^{1/3}
>0.
```

Representative topics include finite core radius, curvature ceiling, radial stiffness floor, singularity avoidance, compact-object stability, and strong-field endpoint behavior.

---

## Observational and Reproducibility Channels

Observational analyses are stored separately from core theory derivations and are interpreted conservatively. The active public-release channels are:

```text
11.1 Quasar luminosity-linked velocity residuals
11.2 Gravitational-wave Kerr consistency / residual-null screens
11.3 Compact-phase magnetic area law / LoTSS
11.4 High-field phase/displacement response
11.5 Hubble/DESI phase-response pressure test
```

### Quasar residuals

The quasar channel is the primary positive observational diagnostic in the current manuscript. It tests the sign of luminosity-linked velocity residuals under matched-bin and low-ionization systemic anchoring controls.

The velocity residual is:

```math
\Delta v_{\mathrm{est}}
=
c\,\frac{z_{\mathrm{est}}-z_{\mathrm{sys}}}{1+z_{\mathrm{sys}}}.
```

The primary sign statistic is:

```math
\Delta v_{\mathrm{high-low}}
=
\mathrm{median}(\Delta v_{\mathrm{est}})_{\mathrm{high}\ L}
-
\mathrm{median}(\Delta v_{\mathrm{est}})_{\mathrm{low}\ L}.
```

The PR sign prediction is:

```math
\Delta v_{\mathrm{high-low}}<0.
```

### Gravitational waves

The gravitational-wave channel is treated as a Kerr-recovery consistency channel. The manuscript does not claim a statistically robust public-data detection of a PR-specific gravitational-wave residual.

The active response decomposition is:

```math
A_{\mathrm{obs}}(\omega)
=
A_{\mathrm{Kerr}}(\omega)
+
A_X(\omega),
```

with `A_X` gap-suppressed relative to the Kerr response.

### Magnetic area law / LoTSS

The current magnetic-field branch is an area-law constraint, not a fixed universal magnetic-amplitude claim. The compact phase sector fixes a flux normalization, while the realized projected compact-phase area sets the magnetic field amplitude.

The compact phase flux normalization is:

```math
\Phi_{\theta}^{\mathrm{PR}}
=
\frac{\hbar}{e}
\frac{Z_A}{c_{\mathrm{bc}}}
=
9.009597185\times 10^{-15}\ \mathrm{Wb}.
```

The magnetic area law is:

```math
B_{\mathrm{geo}}^{\mathrm{PR}}
=
\frac{\Phi_{\theta}^{\mathrm{PR}}}
{A_{\mathrm{proj}}^{(\theta)}}.
```

or, in nanogauss with projected compact-phase area in square meters:

```math
B_{\mathrm{geo}}^{\mathrm{PR}}[\mathrm{nG}]
=
\frac{0.09009597185}
{A_{\mathrm{proj}}^{(\theta)}[\mathrm{m}^{2}]}.
```

The Faraday-rotation mapping used for LoTSS-style constraints is:

```math
\mathrm{RM}_{\mathrm{pred}}
=
812\,n_e[\mathrm{cm}^{-3}]\,L[\mathrm{Mpc}]\,
B_{\mathrm{geo}}^{\mathrm{PR}}[\mathrm{nG}]\,
W_{\mathrm{EM}},
```

with:

```math
W_{\mathrm{EM}}
=
W_{\mathrm{orient}}W_{\mathrm{coh}}W_{\mathrm{fill}}W_z.
```

LoTSS/Faraday residuals are used to constrain the realized projected compact-phase area under plasma, coherence, filling, orientation, and redshift-window assumptions.

---

## Repository Structure

```text
Projection_Relativity/
│
├── manuscript/
│   ├── Oshetski_Projection_Relativity_Main.tex
│   ├── Oshetski_Projection_Relativity_Supplement.tex
│   ├── Oshetski_Projection_Relativity_References.bib
│   ├── Oshetski_Projection_Relativity_Main.pdf
│   └── Oshetski_Projection_Relativity_Supplement.pdf
│
├── test_harness/
│   ├── symbolic/
│   │   ├── ProjectionRelativityAppendixVerify.mpl
│   │   ├── run_appendix_verification.mpl
│   │   ├── README.md
│   │   ├── equation_audit.md
│   │   ├── equation_map.md
│   │   ├── equation_derivations.md
│   │   ├── proof_report.md
│   │   ├── harness_validation.md
│   │   └── spectrum_recompute.md
│   │
│   └── numerical/
│       ├── code/
│       ├── notebooks/
│       └── RESULTS.md
│
├── data/
│   ├── README.md
│   └── section11/
│
├── plots/
│   └── section11/
│
├── CITATION.cff
├── LICENSE
└── README.md
```

---

## Directory Guide

| Path | Purpose |
|---|---|
| `manuscript/` | Main manuscript, supplement, bibliography, and compiled PDFs. |
| `test_harness/symbolic/` | Maple symbolic audit harness and generated audit reports. |
| `test_harness/numerical/` | Python/Colab numerical validation harnesses and summary outputs. |
| `scripts/section11/` | Reproduction and plotting scripts for Section 11 diagnostics. |
| `data/` | Data policy, metadata, processed subsets, and external-source instructions. |
| `results/` | Derived CSV/Parquet tables and numerical outputs. |
| `plots/` | Generated figures used by the manuscript or supplement. |
| `docs/` | Public reproducibility notes, manifests, and interpretation guides. |

---

## Quick Start

### Read the manuscript

Start with:

```text
manuscript/Oshetski_Projection_Relativity_Main.pdf
manuscript/Oshetski_Projection_Relativity_Supplement.pdf
```

The LaTeX sources are provided in the same directory.

### Run the Maple symbolic audit

From a local Maple session:

```maple
restart:
currentdir("C:/path/to/Projection_Relativity/test_harness/symbolic"):
read "ProjectionRelativityAppendixVerify.mpl":
PR_RunAll();
```

The checker verifies the local manuscript files under `manuscript/`. It does not download files from GitHub during the run. The generated reports are written into `test_harness/symbolic/`.

Recommended release language:

```text
symbolically audited and numerically validated where machine-checkable
```

The audit does not certify claims outside its machine-checkable scope. Assumptions, external datasets, numerical backends, and physical interpretation boundaries are labeled in the audit reports.

### Inspect Section 11 data products

Section 11 derived outputs are organized under:

```text
results/section11/
plots/section11/
scripts/section11/
data/section11/
docs/section11/
```

The manifest, when present, is:

```text
docs/section11/SECTION11_MANIFEST.csv
```

---

## Data Policy

Raw external datasets are generally not stored in this repository. Large catalogs, raw gravitational-wave strain files, and externally licensed data should be fetched from their original public sources using the supplied instructions or scripts.

The repository may include:
- processed subsets,
- reduced CSV/Parquet extracts,
- metadata,
- reproducible download instructions,
- audit summaries,
- plots,
- interpretation notes,
- lightweight derived results.

The repository does not include:
- large raw public catalogs unless license and size permit,
- private data,
- secrets,
- credentials,
- API keys,
- local environment files,
- machine-specific cache files.

---

## Reproducibility Policy

Every major quantitative claim is traceable to at least one of the following:

- a manuscript derivation,
- a supplement derivation chain,
- a Maple audit row,
- a Python or Colab script,
- a reduced result table,
- a generated plot,
- a manifest entry,
- an external raw-data source description.

Use conservative status labels for result files:

| Label | Meaning |
|---|---|
| `SUPPORTED` | Reproduced analytically, symbolically, numerically, or by a documented derived-data workflow. |
| `PRELIMINARY` | Directionally useful but not used as primary manuscript evidence. |
| `DE_EMPHASIZED` | Tested and found weak, contaminated, superseded, or non-supportive. |
| `PENDING` | Expected but not yet included or regenerated. |
| `RAW_EXTERNAL` | Raw data is public but must be downloaded from an external source. |
| `DERIVED_TABLE` | Table derived from raw data, simulation output, or symbolic/numerical workflow. |

---

## Research Goals

The current goals of the Projection Relativity repository are to:

- develop a mathematically closed projection architecture from a minimal internal manifold;
- derive observable sectors from projection operations rather than unrelated inserted assumptions;
- recover known low-energy gravitational behavior in the appropriate limit;
- test whether the radial spectral gap can regularize strong-field singular endpoints;
- derive compact phase normalization from geometric closure conditions;
- maintain reproducible symbolic and numerical checks for quantitative claims;
- keep manuscript claims tied to explicit derivations, code, outputs, and interpretation notes.

---

## Claim Discipline

Projection Relativity is an active theoretical and computational research program. Repository language is clearly distinguish between:

- derivation,
- symbolic audit,
- numerical support,
- observational consistency,
- primary evidence,
- secondary diagnostics,
- de-emphasized or superseded tests,
- open conjecture.
---

## Citation / Attribution

**Author:** Michael Stanislaus Oshetski  
**ORCID:** [0009-0007-3623-7586](https://orcid.org/0009-0007-3623-7586)  
**Project:** Projection Relativity  
**Primary manuscript:** *The Foundation of Projection Relativity: A Spectral-Projection Architecture for Emergent Relativity*  
**Repository:** `oshetskiresearch/Projection_Relativity`  

A formal `CITATION.cff` is located in the root directory

---

## License

The code and repository support files are released under the MIT License. See [`LICENSE`](LICENSE) for the full text.
Unless otherwise stated, external datasets retain their original licenses and citation requirements.

---

## Contact
For questions about the manuscript, derivation ledger, or reproducibility package, use the contact information listed above or in the main manuscript.
