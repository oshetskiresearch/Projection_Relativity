# Projection Relativity I Data and Reproducibility Map

This directory is the authoritative inventory of the data-side artifacts
checked into the public repository for **Projection Relativity I (PR-I)**. It
distinguishes usable archives from unavailable support packages and from raw
datasets that must be obtained from their original providers.

No separately hosted Projection Relativity support bundle is required by this
release. The usable PR-I archives are versioned directly in this directory.
Large third-party catalogs and gravitational-wave strain remain external data;
they are not a missing PR-I bundle.

## Authoritative Section 11 Numbering

The current public manuscript fixes the following order:

| Manuscript location | Channel | Public data status |
|---|---|---|
| Section 11.1 | Quasar luminosity-linked velocity residual test | **Not available**; no public support archive is present. |
| Section 11.2 | Compact-phase magnetic area law and Faraday-rotation constraint | **Not available**; no public support archive is present. |
| Section 11.3 | Kerr recovery and gravitational-wave consistency | Two usable repository-contained archives. |
| Section 11.4 | Magnetar spin residuals from projection-energy inertia redistribution | No separate data archive; the displayed relations are covered by the manuscript, supplement, and symbolic harness. |
| Section 11.5 | Cosmological phase response and current stress tests | **Not available**; no public support archive is present. |

This numbering follows
[`Oshetski_Projection_Relativity_Main.tex`](../../manuscript/projection_relativity_I/Oshetski_Projection_Relativity_Main.tex).
Archive names and Section 11 archive-internal paths use the same numbering.

## Actual Public Tree

The checked-in PR-I data tree is:

```text
data/projection_relativity_I/
|-- README.md
|-- pr_public_section_10_compact_phase_fsc.tar
|-- pr_public_section11_3_gw_kerr_consistency_support.tar.gz
`-- pr_public_section11_3_gw_residual_screen_support.tar.gz
```

There are no checked-in top-level `scripts/section11/`, `results/section11/`,
or `docs/section11/` directories. Those names occur only inside the usable
archives and appear in a separate extraction directory after unpacking.

The related public locations are:

| Material | Repository path |
|---|---|
| Main manuscript and supplement | [`manuscript/projection_relativity_I/`](../../manuscript/projection_relativity_I/) |
| Maple symbolic audit | [`test_harness/projection_relativity_I/symbolic/`](../../test_harness/projection_relativity_I/symbolic/) |
| Python numerical validation | [`test_harness/projection_relativity_I/numerical/`](../../test_harness/projection_relativity_I/numerical/) |
| Standalone PR-I plot archives and generators | [`plots/projection_relativity_I/`](../../plots/projection_relativity_I/) |

## Archive Inventory

### Section 10 compact-phase precision audit

[`pr_public_section_10_compact_phase_fsc.tar`](pr_public_section_10_compact_phase_fsc.tar)
contains a 20-digit precision audit script, JSON report, and CSV summary for the
compact-boundary/fine-structure calculation.

Status: **Available**.

### Section 11.1 quasar residual support

No Section 11.1 support archive is present in the public tree.

Status: **Not available**. No released table, plot, or reproduction script is
provided for this channel, and no external PR-I bundle should be inferred.

The quasar statistic defined in the manuscript is

```text
Delta v_est = c * (z_est - z_sys) / (1 + z_sys)
Delta v_high-low = median(Delta v_est)_high_L - median(Delta v_est)_low_L
```

Reproducing the observational analysis requires the applicable quasar catalog
from its original provider, with that provider's license and citation terms.

### Section 11.2 magnetic area-law support

No Section 11.2 support archive is present in the public tree.

Status: **Not available**. No released observational table, plot, or
reproduction script is provided for this channel.

The machine-checkable algebraic relations are covered by the PR-I symbolic
harness, including

```text
B_geo^PR = Phi_theta^PR / A_proj^(theta)
RM_pred = 812 * n_e * L * B_geo^PR * W_EM
```

An observational reproduction would additionally require the applicable
Faraday-rotation catalog and foreground/plasma assumptions from their original
sources.

### Section 11.3 Kerr-consistency support

[`pr_public_section11_3_gw_kerr_consistency_support.tar.gz`](pr_public_section11_3_gw_kerr_consistency_support.tar.gz)
contains:

```text
results/section11/11_3_gw_kerr_consistency/data/
plots/section11/11_3_gw_kerr_consistency/
scripts/section11/11_3_gw_kerr_consistency/
```

The payload includes ringdown sample and summary CSV files, PNG/PDF plots, and
the generating Python script. It supports Kerr consistency and a formally
gap-suppressed projection-sector residual; it is not a residual-detection
claim.

Status: **Available**.

### Section 11.3 residual/null-screen support

[`pr_public_section11_3_gw_residual_screen_support.tar.gz`](pr_public_section11_3_gw_residual_screen_support.tar.gz)
contains:

```text
results/section11/11_3_gw_residual_screen/
plots/section11/11_3_gw_residual_screen/
scripts/section11/11_3_gw_residual_screen/
docs/section11/11_3_gw_residual_screen/
```

The payload includes GW150914 screens, multi-event and focused-follow-up
tables, kernel/template interfaces, diagnostic plots, scripts, and supporting
method notes. These screens support the manuscript's conservative conclusion
that no statistically robust PR-specific residual was identified.

Status: **Available**.

Raw public strain is not redistributed in this archive. Where a script needs
strain data, obtain it from the original gravitational-wave data provider and
retain the provider's citation and license information.

### Section 11.4 magnetar relations

No separate Section 11.4 archive exists. The inertia-shift and spin-residual
relations are analytic claims covered by the manuscript, supplement, and Maple
audit rather than by a standalone observational dataset.

Status: **No separate data package**.

### Section 11.5 cosmology support

No Section 11.5 support archive is present in the public tree.

Status: **Not available**. No released likelihood, table, plot, or reproduction
script is provided for this channel. The manuscript presents it as a
conditional pressure test requiring a joint external-data analysis.

## Inspecting and Extracting the Usable Archives

Run these commands from the repository root. First inspect an archive without
extracting it:

```bash
tar -tf data/projection_relativity_I/pr_public_section11_3_gw_kerr_consistency_support.tar.gz
tar -tf data/projection_relativity_I/pr_public_section11_3_gw_residual_screen_support.tar.gz
```

Extract into a separate working directory so archive-internal `results/`,
`plots/`, `scripts/`, and `docs/` paths are not confused with checked-in public
repository paths:

```bash
mkdir pr1_section11_work
tar -xzf data/projection_relativity_I/pr_public_section11_3_gw_kerr_consistency_support.tar.gz -C pr1_section11_work
tar -xzf data/projection_relativity_I/pr_public_section11_3_gw_residual_screen_support.tar.gz -C pr1_section11_work
```

For the uncompressed Section 10 archive:

```bash
tar -xf data/projection_relativity_I/pr_public_section_10_compact_phase_fsc.tar -C pr1_section11_work
```

## Reproducibility Boundary

A fresh clone can directly:

1. compile the PR-I manuscript and supplement;
2. run the repository-local Maple symbolic audit;
3. run the PR-I numerical harness;
4. inspect and extract the two usable Section 11.3 support archives; and
5. inspect the Section 10 compact-phase precision audit.

A fresh clone cannot reproduce the unavailable quasar, magnetic, or
cosmological observational packages because no public support archives are
provided for those channels. Their **not available** status is documentation,
not a pointer to an external PR bundle. External raw datasets, where
applicable, remain governed by their original providers.

## Citation and Use

When using a repository-contained PR-I artifact, cite the PR-I manuscript and
this repository. When an analysis also uses an external catalog, survey, or
strain archive, cite the original data provider according to its policy.
