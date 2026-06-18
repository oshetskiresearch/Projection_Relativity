# Projection Relativity
**Public manuscripts, validation harnesses, data packages, and generated figures**

**PR-I release:** [Zenodo DOI](https://doi.org/10.5281/zenodo.20545407)  
**Repository:** `oshetskiresearch/Projection_Relativity`  
**Author:** Michael Stanislaus Oshetski  
**Email:** oshetski.research@proton.me  
**ORCID:** [0009-0007-3623-7586](https://orcid.org/0009-0007-3623-7586)  
**Status:** Public multi-manuscript research and reproducibility repository

---

## Overview

This repository contains the public source, validation code, supporting data, and generated plots for the Projection Relativity manuscript series.

The repository is organized by paper using the directory names:

```text
projection_relativity_I
projection_relativity_II
```

Each major repository area separates PR-I and PR-II so that manuscript files, test harnesses, data products, and plots remain traceable to the paper they support.

---

## Manuscript Packages

| Package | Scope | Primary location |
|---|---|---|
| **Projection Relativity I** | Spectral-projection gravity, displacement-generated inertia, compact electromagnetic phase, finite-core regularization, and first observational diagnostics | [`manuscript/projection_relativity_I/`](manuscript/projection_relativity_I/) |
| **Projection Relativity II** | Compact non-Abelian electroweak projection, tree-level scalar-coupling ledger, fermion/flavor structure, QCD diagnostics, CKM/PMNS candidates, and neutrino-sector candidates | [`manuscript/projection_relativity_II/`](manuscript/projection_relativity_II/) |

PR-I is the released foundational manuscript associated with the Zenodo DOI above. PR-II extends the public project into the electroweak and flavor sectors and is accompanied by its own validation directories.

---

## Repository Structure

The current `main` branch is organized as follows:

```text
Projection_Relativity/
│
├── manuscript/
│   ├── projection_relativity_I/
│   │   ├── README.md
│   │   ├── Oshetski_Projection_Relativity_Main.tex
│   │   ├── Oshetski_Projection_Relativity_Supplement.tex
│   │   └── Oshetski_Projection_Relativity_References.bib
│   │
│   └── projection_relativity_II/
│       ├── README.md
│       └── PR-II manuscript source and bibliography files
│
├── test_harness/
│   ├── projection_relativity_I/
│   │   ├── symbolic/
│   │   └── numerical/
│   │
│   └── projection_relativity_II/
│       ├── symbolic/
│       └── numerical/
│
├── data/
│   ├── projection_relativity_I/
│   └── projection_relativity_II/
│
├── plots/
│   ├── projection_relativity_I/
│   └── projection_relativity_II/
│
├── LICENSE
└── README.md
```

The tree above intentionally lists only the current paper-scoped root directories. If additional roots such as `results/`, `docs/`, or `scripts/` are added later, they should use the same paper-directory convention:

```text
<root>/projection_relativity_I/
<root>/projection_relativity_II/
```

---

## Directory Guide

| Path | Purpose |
|---|---|
| [`manuscript/projection_relativity_I/`](manuscript/projection_relativity_I/) | PR-I main manuscript, supplement, bibliography, and manuscript README. |
| [`manuscript/projection_relativity_II/`](manuscript/projection_relativity_II/) | PR-II manuscript source, bibliography, and manuscript README. |
| [`test_harness/projection_relativity_I/symbolic/`](test_harness/projection_relativity_I/symbolic/) | PR-I Maple symbolic audit, equation maps, proof reports, and negative controls. |
| [`test_harness/projection_relativity_I/numerical/`](test_harness/projection_relativity_I/numerical/) | PR-I Python/Colab numerical validation files and outputs. |
| [`test_harness/projection_relativity_II/symbolic/`](test_harness/projection_relativity_II/symbolic/) | PR-II symbolic-audit location. |
| [`test_harness/projection_relativity_II/numerical/`](test_harness/projection_relativity_II/numerical/) | PR-II Python/Colab electroweak-flavor validation harness and generated audit outputs. |
| [`data/projection_relativity_I/`](data/projection_relativity_I/) | PR-I data policy, derived observational products, manifests, and external-source instructions. |
| [`data/projection_relativity_II/`](data/projection_relativity_II/) | PR-II boundary-ledger data, diagnostic reference data, and generated support tables. |
| [`plots/projection_relativity_I/`](plots/projection_relativity_I/) | PR-I generated figures and observational plots. |
| [`plots/projection_relativity_II/`](plots/projection_relativity_II/) | PR-II electroweak, flavor, mass-ledger, and audit figures. |

---

## Quick Start

### Read or compile Projection Relativity I

Start in:

```text
manuscript/projection_relativity_I/
```

Primary source files include:

```text
Oshetski_Projection_Relativity_Main.tex
Oshetski_Projection_Relativity_Supplement.tex
Oshetski_Projection_Relativity_References.bib
```

A standard local build sequence is:

```bash
cd manuscript/projection_relativity_I
pdflatex Oshetski_Projection_Relativity_Main.tex
bibtex Oshetski_Projection_Relativity_Main
pdflatex Oshetski_Projection_Relativity_Main.tex
pdflatex Oshetski_Projection_Relativity_Main.tex
```

Compile the supplement separately from the same directory when needed.

### Read or compile Projection Relativity II

Start in:

```text
manuscript/projection_relativity_II/
```

Follow the local `README.md` for the current PR-II source and bibliography filenames and build instructions.

### Run the PR-I Maple symbolic audit

The PR-I symbolic checker is located at:

```text
test_harness/projection_relativity_I/symbolic/
```

From a local Maple session:

```maple
restart:
currentdir("C:/path/to/Projection_Relativity/test_harness/projection_relativity_I/symbolic"):
read "ProjectionRelativityAppendixVerify.mpl":
PR_RunAll();
```

The checker verifies repository-local manuscript files. It does not download manuscript files during the run.

Recommended release language:

```text
symbolically audited and numerically validated where machine-checkable
```

### Run the PR-I numerical validation package

Use the scripts and instructions under:

```text
test_harness/projection_relativity_I/numerical/
```

### Run the PR-II validation package

Use the Colab/Python harnesses under:

```text
test_harness/projection_relativity_II/numerical/
```

The PR-II harness is designed to verify machine-checkable parts of the electroweak/flavor chain, including structural identities, closure candidates, precision candidates, diagnostic ledgers, negative controls, and forbidden target-input checks.

The PR-II input discipline separates:

```text
allowed geometric generation inputs
```

from:

```text
diagnostic reference values loaded only after generation
```

This separation is central to the PR-II zero-new-parameter candidate claim.

---

## Package Scope

### Projection Relativity I

PR-I includes:

- radial spectral-gap and branch checks;
- low-energy gravitational and Kerr-exterior recovery tests;
- displacement/inertia and compact electromagnetic closure;
- finite-core and strong-field checks;
- Maple symbolic verification;
- numerical validation scripts;
- observational support packages for quasar residuals, gravitational-wave Kerr consistency, compact magnetic area-law constraints, and the Hubble/DESI pressure test.

### Projection Relativity II

PR-II includes:

- the compact electroweak lift and projection-locking ledger;
- weak mixing, weak-scale, and Fermi closure candidates;
- the tree-level compact order-mode and scalar-coupling ledger;
- charged- and neutral-current checks;
- anomaly cancellation and generation-sheet tests;
- charged-lepton, quark/QCD, CKM, PMNS, and neutrino-sector candidates;
- numerical audit outputs, negative controls, and forbidden-input checks.

PR-II is presented as a tree-level electroweak/flavor compact-boundary closure candidate. Scalar-mass closure, full electroweak radiative precision, and final strong-sector precision matching are outside its present scope.

---

## Data Policy

Raw external datasets are generally not stored in this repository when they are large, externally licensed, or more appropriately fetched from their original public archives.

The repository may include:

- reduced CSV or Parquet products;
- compact boundary-ledger tables;
- diagnostic reference tables;
- metadata and checksums;
- reproducible download instructions;
- audit summaries;
- generated plots;
- lightweight derived results.

The repository does not include:

- private data;
- secrets, credentials, or API keys;
- machine-specific cache files;
- large raw public datasets unless redistribution is appropriate.

External datasets retain their original licenses and citation requirements.

---

## Reproducibility Policy

Every major quantitative claim should be traceable to one or more of the following:

- a manuscript derivation;
- a supplementary derivation;
- a symbolic audit row;
- a Python or Colab script;
- a generated result table;
- a generated plot;
- a manifest entry;
- an external data-source description.

The validation packages do not certify claims outside their machine-checkable scope. Physical assumptions, external data dependencies, numerical backends, renormalization conventions, and interpretation boundaries should remain explicitly labeled.

### Result-status labels

| Label | Meaning |
|---|---|
| `STRUCTURAL` | Algebraic, representation-theoretic, or tree-level identity checked by the harness. |
| `CLOSURE_CANDIDATE` | A generated compact-boundary relation that does not use its target observable as an input. |
| `PRECISION_CANDIDATE` | A closure candidate with high-accuracy post-generation diagnostic agreement. |
| `DIAGNOSTIC_LEDGER` | A running, matching, comparison, or scheme-dependent analysis rather than a final theorem. |
| `SUPPORTED` | Reproduced analytically, symbolically, numerically, or through a documented data workflow. |
| `PRELIMINARY` | Directionally useful but not used as primary evidence. |
| `DE_EMPHASIZED` | Tested and found weak, contaminated, superseded, or non-supportive. |
| `PENDING` | Expected but not yet included or regenerated. |
| `RAW_EXTERNAL` | Public raw data that must be obtained from its original source. |
| `DERIVED_TABLE` | A table derived from external data, symbolic output, or numerical output. |

---

## Claim Discipline

Projection Relativity is an active theoretical and computational research program. Repository language should distinguish clearly among:

- derivation;
- structural identity;
- symbolic audit;
- numerical validation;
- closure candidate;
- precision candidate;
- diagnostic comparison;
- observational consistency;
- superseded or de-emphasized tests;
- open conjecture and deferred precision work.

The preferred release language remains:

```text
symbolically audited and numerically validated where machine-checkable
```

---

## Citation and Attribution

**Author:** Michael Stanislaus Oshetski  
**ORCID:** [0009-0007-3623-7586](https://orcid.org/0009-0007-3623-7586)  
**Project:** Projection Relativity  
**PR-I manuscript:** *The Foundation of Projection Relativity: A Spectral-Projection Architecture for Emergent Relativity*  
**PR-II manuscript:** *The Foundation of Projection Relativity II: Geometric Constraints on the Non-Abelian Phase Fiber*  
**PR-I DOI:** [10.5281/zenodo.20545407](https://doi.org/10.5281/zenodo.20545407)  
**Repository:** `oshetskiresearch/Projection_Relativity`

When using an externally sourced dataset or derived table, also cite the original survey, catalog, collaboration, or archive according to its citation policy.

---

## License

The repository code and support files are released under the MIT License. See [`LICENSE`](LICENSE) for the full text.

Unless otherwise stated, manuscript content and external datasets retain their respective licenses and citation requirements.

---

## Contact

For questions about either manuscript, the symbolic or numerical validation packages, the data directories, or the public reproducibility structure:

**Michael Stanislaus Oshetski**  
**Email:** oshetski.research@proton.me  
**ORCID:** [0009-0007-3623-7586](https://orcid.org/0009-0007-3623-7586)
