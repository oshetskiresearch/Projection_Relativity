# Projection Relativity II Electroweak / Flavor Validation Harness

Numerical validation harness for the Projection Relativity II electroweak and flavor-sector closure chain.

This repository contains a Colab-friendly Python script that generates PR-II candidate values, checks machine-testable structural identities, runs negative controls, and writes an audit package with JSON, CSV, and Markdown summaries.

Author: Michael Stanislaus Oshetski  
ORCID: 0009-0007-3623-7586  
Version date: June 2026

## What This Harness Checks

The script verifies the PR-II candidate chain wherever it is directly machine-checkable, including:

- PR-I compact-boundary ledger import and no-target-input discipline
- Compact electroweak lift using `R_w x S^1_Y x SU(2)_L`
- `SU(2)_L` generator algebra, commutators, Casimir checks, and negative controls
- Projection locking from `SU(2)_L x U(1)_Y` to `U(1)_em`
- Residual charge recovery using `Q = T3 + Y/2`
- Photon masslessness, W/Z mass matrix structure, weak mixing, and tree-level `rho_EW = 1`
- Weak-scale and Fermi-constant compact-boundary closure
- Charged-current and neutral-current coupling ledgers
- Fermion representation ledger and local/global anomaly cancellation
- Generation count candidate from the broken electroweak projection space
- Charged-lepton Koide sheet rule and precision mass candidates
- QCD coupling anchor, heavy-quark threshold candidates, and light-quark hierarchy diagnostics
- CKM and PMNS compact flavor-mixing candidates with unitarity and Jarlskog checks
- Neutrino normal-ordering candidate and Majorana-channel diagnostics
- Forbidden-input checks, negative controls, audit manifest, and scorecard

## Scope And Caveats

This is a numerical validation suite aligned with Projection Relativity II. It should be read as:

> Structurally derived, numerically validated where machine-checkable, and checked against negative controls and forbidden target-input leakage.

The harness does not claim that every electroweak precision, scalar-mass, radiative-running, QCD-scheme, or observational statement is fully certified by this script alone. Scalar mass closure, full loop-level electroweak precision, and strong-sector precision matching are assigned to a later PR-III precision layer.

Diagnostic reference values are loaded only after PR-II candidate values have already been generated. Target observables such as `G_F`, `v_EW`, `M_W`, `M_Z`, charged-lepton masses, quark masses, CKM values, PMNS values, `alpha_s(M_Z)`, `Lambda_QCD`, and neutrino mass splittings are not used as generation inputs.

## Requirements

- Python 3.9 or newer
- NumPy

Install the required dependency:

```bash
pip install numpy
```

No external data files are required.

## Usage

The script is intended to run both locally and in Google Colab. If you rename the Python file, adjust the commands below accordingly.

### Local Python

From the repository root:

```bash
python test_harness/projection_relativity_II/numerical/code/pr2_numerical_validation_harness.py
```

The script writes its audit package to:

```text
./pr2_harness_output/
./pr2_harness_output.zip
```

### Google Colab

Upload the script into a Colab session, then run:

```python
from google.colab import files
uploaded = files.upload()

%run pr2_numerical_validation_harness.py

files.download("/content/pr2_harness_output.zip")
```

In Colab, outputs are written to:

```text
/content/pr2_harness_output/
/content/pr2_harness_output.zip
```

## Output Files

The run creates a structured audit folder:

```text
pr2_harness_output/
  pr2_generated_outputs.json
  audit/
    PRII_RUN_SUMMARY.md
    PRII_RUN_SUMMARY.json
    PRII_TEST_RESULTS.csv
    PRII_AUDIT_MANIFEST.csv
  summary_tables/
    pr2_diagnostic_residuals.csv
    neutral_current_couplings.csv
    sector_overlap_spectra.csv
  step_outputs/
```

Important outputs:

- `pr2_generated_outputs.json` stores generated PR-II candidate values.
- `PRII_RUN_SUMMARY.md` gives the human-readable pass/fail summary.
- `PRII_RUN_SUMMARY.json` gives the machine-readable scorecard.
- `PRII_TEST_RESULTS.csv` lists every individual harness check.
- `PRII_AUDIT_MANIFEST.csv` maps theory sections to validation status and remaining obligations.
- `pr2_diagnostic_residuals.csv` compares generated candidates to diagnostic references after generation.

## Expected Current Status

The current harness version is expected to report:

```text
tests_total: 146
tests_passed: 146
tests_failed: 0
status: PASS
```

If any test fails, inspect:

```text
pr2_harness_output/audit/PRII_TEST_RESULTS.csv
pr2_harness_output/audit/PRII_RUN_SUMMARY.md
```

## Key Generated Quantities

The run summary includes generated values such as:

- `sin^2(theta_W)^PR`
- `Lambda_EW^PR`
- `v_EW^PR`
- `G_F^PR`
- `alpha_3^PR`
- charged-lepton mass candidates
- light-quark and heavy-threshold candidates
- CKM and PMNS mixing candidates
- neutrino mass-sector candidates
- `m_betabeta` candidate

These values are generated before diagnostic reference comparisons are loaded.

## Repository Layout

Public repository layout:

```text
test_harness/projection_relativity_II/numerical/
|-- README.md
|-- code/
|   `-- pr2_numerical_validation_harness.py
`-- results/
    `-- pr2_harness_output.zip
```

## Reproducibility Notes

The harness is intentionally self-contained:

- Generation constants are declared near the top of the script.
- Diagnostic references are separated from generation inputs.
- Forbidden target inputs are checked explicitly.
- Negative controls are included throughout the validation chain.
- Outputs are written in stable JSON, CSV, and Markdown formats.

For reproducible public releases, consider tagging the repository with the script date and preserving the generated audit package from the release run.

## Citation

If you use or discuss this harness, cite the author and repository:

```text
Michael Stanislaus Oshetski, Projection Relativity II Electroweak / Flavor Validation Harness, June 2026.
ORCID: 0009-0007-3623-7586
```

## License

This harness is distributed under the repository's root MIT `LICENSE`.

