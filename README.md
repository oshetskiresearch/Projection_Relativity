# The Foundation of Projection Relativity   
**Public manuscripts, validation harnesses, data packages, and generated figures**

**PR-I release:** [Zenodo DOI](https://doi.org/10.5281/zenodo.20545407)<br>
**PR-II release:** [Zenodo DOI](https://doi.org/10.5281/zenodo.20817164)<br>
**PR-III release:** [Zenodo DOI](https://doi.org/10.5281/zenodo.20817164)<br>

**Repository:** `oshetskiresearch/Projection_Relativity`<br>
**Author:** Michael Stanislaus Oshetski<br>
**Email:** oshetski.research@proton.me<br>
**ORCID:** [0009-0007-3623-7586](https://orcid.org/0009-0007-3623-7586)<br>
**Status:** Public multi-manuscript research and reproducibility repository

---

## Overview

This repository contains the public source, validation code, supporting data,
and generated plots for the Projection Relativity manuscript series.

The repository is organized by paper using the directory names:

```text
projection_relativity_I
projection_relativity_II
projection_relativity_III
```

Each major repository area separates PR-I, PR-II, and PR-III so that manuscript
files, test harnesses, data products, and plots remain traceable to the paper
they support.

---

## Manuscript Packages

| Package | Scope | Primary location |
|---|---|---|
| **Projection Relativity I** | Spectral-projection gravity, displacement-generated inertia, compact electromagnetic phase, finite-core regularization, and first observational diagnostics | [`manuscript/projection_relativity_I/`](manuscript/projection_relativity_I/) |
| **Projection Relativity II** | Compact non-Abelian electroweak projection, tree-level scalar-coupling ledger, fermion/flavor structure, QCD diagnostics, CKM/PMNS candidates, and neutrino-sector candidates | [`manuscript/projection_relativity_II/`](manuscript/projection_relativity_II/) |
| **Projection Relativity III** | Zero-parameter radiative and cross-sector closure of the inherited projection ledger across electromagnetic, electroweak, neutrino, strong, anomaly, and running-continuity sectors | [`manuscript/projection_relativity_III/`](manuscript/projection_relativity_III/) |

PR-I is the released foundational manuscript. PR-II extends the public project
into the electroweak and flavor sectors. PR-III develops the radiative and
cross-sector closure ledger inherited from PR-I and PR-II and is accompanied by
symbolic, manuscript-conformance, and numerical reproducibility packages.

---

## Repository Structure

The current `main` branch is organized as follows:

```text
Projection_Relativity/
|-- manuscript/
|   |-- projection_relativity_I/
|   |-- projection_relativity_II/
|   `-- projection_relativity_III/
|       |-- README.md
|       |-- Oshetski_Projection_Relativity_III_Main.tex
|       |-- Oshetski_Projection_Relativity_III_Main.pdf
|       `-- Oshetski_Projection_Relativity_III_References.bib
|
|-- test_harness/
|   |-- projection_relativity_I/
|   |   |-- symbolic/
|   |   `-- numerical/
|   |-- projection_relativity_II/
|   |   |-- symbolic/
|   |   `-- numerical/
|   `-- projection_relativity_III/
|       |-- symbolic/
|       `-- numerical/
|
|-- data/
|   |-- projection_relativity_I/
|   |-- projection_relativity_II/
|   `-- projection_relativity_III/
|       |-- code/
|       |-- data/
|       `-- PR3_PUBLIC_DATA_MANIFEST.json
|
|-- plots/
|   |-- projection_relativity_I/
|   |-- projection_relativity_II/
|   `-- projection_relativity_III/
|
|-- LICENSE
`-- README.md
```

If additional roots such as `results/`, `docs/`, or `scripts/` are added later,
they should use the same paper-directory convention:

```text
<root>/projection_relativity_I/
<root>/projection_relativity_II/
<root>/projection_relativity_III/
```

---

## Directory Guide

| Path | Purpose |
|---|---|
| [`manuscript/projection_relativity_I/`](manuscript/projection_relativity_I/) | PR-I main manuscript, supplement, bibliography, and manuscript README. |
| [`manuscript/projection_relativity_II/`](manuscript/projection_relativity_II/) | PR-II manuscript source, bibliography, and manuscript README. |
| [`manuscript/projection_relativity_III/`](manuscript/projection_relativity_III/) | PR-III manuscript source, compiled PDF, bibliography, and manuscript README. |
| [`test_harness/projection_relativity_I/symbolic/`](test_harness/projection_relativity_I/symbolic/) | PR-I Maple symbolic audit, equation maps, proof reports, and negative controls. |
| [`test_harness/projection_relativity_I/numerical/`](test_harness/projection_relativity_I/numerical/) | PR-I Python/Colab numerical validation files and outputs. |
| [`test_harness/projection_relativity_II/symbolic/`](test_harness/projection_relativity_II/symbolic/) | PR-II symbolic-audit location. |
| [`test_harness/projection_relativity_II/numerical/`](test_harness/projection_relativity_II/numerical/) | PR-II Python/Colab electroweak-flavor validation harness and generated audit outputs. |
| [`test_harness/projection_relativity_III/symbolic/`](test_harness/projection_relativity_III/symbolic/) | PR-III Maple checks, negative controls, complete display-equation accounting, and manuscript numerical-value audit. |
| [`test_harness/projection_relativity_III/numerical/`](test_harness/projection_relativity_III/numerical/) | PR-III Python schema/numerical and canonical release-byte reproducibility tester. |
| [`data/projection_relativity_I/`](data/projection_relativity_I/) | PR-I data policy, derived observational products, manifests, and external-source instructions. |
| [`data/projection_relativity_II/`](data/projection_relativity_II/) | PR-II boundary-ledger data, diagnostic reference data, and generated support tables. |
| [`data/projection_relativity_III/`](data/projection_relativity_III/) | Canonical PR-III construction generators, JSON ledgers, input/reference data, and SHA-256 pair manifest. |
| [`plots/projection_relativity_I/`](plots/projection_relativity_I/) | PR-I generated figures and observational plots. |
| [`plots/projection_relativity_II/`](plots/projection_relativity_II/) | PR-II electroweak, flavor, mass-ledger, and audit figures. |
| [`plots/projection_relativity_III/`](plots/projection_relativity_III/) | PR-III generated-figure and plot-documentation location. |

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

Follow the local `README.md` for the current PR-II source and bibliography
filenames and build instructions.

### Read or compile Projection Relativity III

The public source and compiled PDF are located in:

```text
manuscript/projection_relativity_III/
```

A standard local build sequence is:

```bash
cd manuscript/projection_relativity_III
pdflatex Oshetski_Projection_Relativity_III_Main.tex
bibtex Oshetski_Projection_Relativity_III_Main
pdflatex Oshetski_Projection_Relativity_III_Main.tex
pdflatex Oshetski_Projection_Relativity_III_Main.tex
```

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

The checker verifies repository-local manuscript files. It does not download
manuscript files during the run.

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

The PR-II harness verifies machine-checkable parts of the electroweak/flavor
chain, including structural identities, closure candidates, precision
candidates, diagnostic ledgers, negative controls, and forbidden target-input
checks.

The PR-II input discipline separates allowed geometric generation inputs from
diagnostic reference values loaded only after generation. This separation is
central to the PR-II zero-new-parameter candidate claim.

### Run the PR-III symbolic and manuscript audit

From the PR-III harness directory, run the Maple layer with:

```powershell
cd test_harness/projection_relativity_III
cmaple run_pr3_maple_test.mpl
```

The full equation and manuscript-value audit commands are documented in
[`test_harness/projection_relativity_III/symbolic/README.md`](test_harness/projection_relativity_III/symbolic/README.md).
The checked public run is summarized in
[`test_harness/projection_relativity_III/RUN_SUMMARY.md`](test_harness/projection_relativity_III/RUN_SUMMARY.md).

### Run the PR-III numerical reproducibility test

From the numerical harness directory:

```powershell
cd test_harness/projection_relativity_III/numerical
python run_pr3_numerical_validation.py
```

The checked run verifies 41 declared generator/data pairs at the
schema/numerical tier and at the canonical release-byte tier. The canonical
construction generators and JSON ledger are published under
[`data/projection_relativity_III/`](data/projection_relativity_III/).

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
- observational support packages for quasar residuals, gravitational-wave
  Kerr consistency, compact magnetic area-law constraints, and the Hubble/DESI
  pressure test.

### Projection Relativity II

PR-II includes:

- the compact electroweak lift and projection-locking ledger;
- weak mixing, weak-scale, and Fermi closure candidates;
- the tree-level compact order-mode and scalar-coupling ledger;
- charged- and neutral-current checks;
- anomaly cancellation and generation-sheet tests;
- charged-lepton, quark/QCD, CKM, PMNS, and neutrino-sector candidates;
- numerical audit outputs, negative controls, and forbidden-input checks.

PR-II is presented as a tree-level electroweak/flavor compact-boundary closure
candidate. Scalar-mass closure, full electroweak radiative precision, and final
strong-sector precision matching are outside its present scope.

### Projection Relativity III

PR-III includes:

- inherited PR-I and PR-II source, boundary, and no-fit provenance ledgers;
- electromagnetic radiative extraction and residual-closure checks;
- electroweak transport, weak-mass, weak-angle, and precision diagnostics;
- neutrino radiative stability, ordering, and effective-mass diagnostics;
- strong-sector color, active-flavor threshold, and one-loop running checks;
- anomaly cancellation, Witten-parity, and running-continuity audits;
- a global cross-sector consistency and no-fit provenance ledger;
- Maple checks, negative controls, full display-equation accounting, and an
  audit of numerical values printed in the manuscript;
- Python manifest, schema/numerical, and canonical release-byte
  reproducibility tests for all 41 declared generator/data pairs.

PR-III presents a finite-tier radiative and cross-sector closure ledger. It does
not claim a complete all-orders Standard Model or QCD theorem, a full
nonperturbative confinement and hadronization construction, or raw generator
stdout byte identity.

---

## Data Policy

Raw external datasets are generally not stored in this repository when they
are large, externally licensed, or more appropriately fetched from their
original public archives.

The repository may include:

- reduced CSV or Parquet products;
- compact boundary-ledger tables;
- diagnostic reference tables;
- metadata and checksums;
- reproducible download instructions;
- audit summaries;
- generated plots;
- lightweight derived results.

For PR-III, the canonical construction code and JSON ledgers are maintained in
[`data/projection_relativity_III/`](data/projection_relativity_III/). The
symbolic and numerical audit code is maintained separately under
[`test_harness/projection_relativity_III/`](test_harness/projection_relativity_III/).

The repository does not include:

- private data;
- secrets, credentials, or API keys;
- machine-specific cache files;
- large raw public datasets unless redistribution is appropriate.

External datasets retain their original licenses and citation requirements.

---

## Reproducibility Policy

Every major quantitative claim should be traceable to one or more of the
following:

- a manuscript derivation;
- a supplementary derivation;
- a symbolic audit row;
- a Python or Colab script;
- a generated result table;
- a generated plot;
- a manifest entry;
- an external data-source description.

The validation packages do not certify claims outside their machine-checkable
scope. Physical assumptions, external data dependencies, numerical backends,
renormalization conventions, and interpretation boundaries should remain
explicitly labeled.

For PR-III, schema/numerical reproducibility and canonical release-byte
reproducibility are separate checked tiers. Raw generator stdout bytes and raw
checked-in JSON key order are not release identities and are not claimed.

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

Projection Relativity is an active theoretical and computational research
program. Repository language should distinguish clearly among:

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

**Author:** Michael Stanislaus Oshetski<br>
**ORCID:** [0009-0007-3623-7586](https://orcid.org/0009-0007-3623-7586)<br>
**Project:** Projection Relativity<br>
**PR-I manuscript:** *The Foundation of Projection Relativity: A Spectral-Projection Architecture for Emergent Relativity*<br>
**PR-II manuscript:** *The Foundation of Projection Relativity II: Geometric Constraints on the Non-Abelian Phase Fiber*<br>
**PR-III manuscript:** *The Foundation of Projection Relativity III: Zero-Parameter Radiative and Cross-Sector Closure of the Projection Ledger*<br>
**PR-I DOI:** [10.5281/zenodo.20545407](https://doi.org/10.5281/zenodo.20545407)<br>
**PR-II DOI:** [10.5281/zenodo.20817164](https://doi.org/10.5281/zenodo.20817164)<br>
**PR-III DOI:** [10.5281/zenodo.20817164](https://doi.org/10.5281/zenodo.20817164)<br>
**Repository:** `oshetskiresearch/Projection_Relativity`

When using an externally sourced dataset or derived table, also cite the
original survey, catalog, collaboration, or archive according to its citation
policy.

---

## License

The repository code and support files are released under the MIT License. See
[`LICENSE`](LICENSE) for the full text.

Unless otherwise stated, manuscript content and external datasets retain their
respective licenses and citation requirements.

---

## Contact

For questions about any manuscript, the symbolic or numerical validation
packages, the data directories, or the public reproducibility structure:

**Michael Stanislaus Oshetski**<br>
**Email:** oshetski.research@proton.me<br>
**ORCID:** [0009-0007-3623-7586](https://orcid.org/0009-0007-3623-7586)
