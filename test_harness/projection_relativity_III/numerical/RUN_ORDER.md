# PR-III Audit Run Order

Run or inspect the PR-III ledger in this order.

The `code/...` and `data/...` construction paths below are relative to
`data/projection_relativity_III` at the repository root. Audit commands are run
from `test_harness/projection_relativity_III/numerical`.

## Alpha and electromagnetic closure

```text
code/pr3_v04h_residual_closure_bound.py
```

Required data:

```text
data/alpha_residual_closure_current_precision.json
```

## Electroweak precision closure

```text
code/pr3_v05a_ew_scale_transport_protocol.py
code/pr3_v05b_ew_running_inventory_kernel.py
code/pr3_v05c_ew_running_candidate.py
code/pr3_v05d_weak_mass_ledger_audit.py
code/pr3_v05e_ew_diagnostic_comparison.py
code/pr3_v05f_weak_angle_oblique_refinement.py
code/pr3_v05g_vector_self_energy_candidate.py
code/pr3_v05h_c2_diagnostic_comparison.py
code/pr3_v05i_final_ew_precision_audit.py
code/pr3_v05j_neutral_D3_refinement.py
```

Final data:

```text
data/electroweak_neutral_D3_candidate_C3.json
```

## Neutrino branch stability

```text
code/pr3_v06a_neutrino_branch_lock.py
code/pr3_v06b_neutrino_radiative_kernel.py
code/pr3_v06c_mbb_stability.py
code/pr3_v06d_ordering_pmns_stability.py
code/pr3_v06e_neutrino_diagnostic_comparison.py
code/pr3_v06f_final_neutrino_closure.py
```

Final data:

```text
data/neutrino_final_closure_audit.json
```

## Strong sector

```text
code/pr3_v07a_strong_phase_fiber_lock.py
code/pr3_v07b_strong_spectral_running_kernel.py
code/pr3_v07c_one_loop_color_audit.py
code/pr3_v07d_threshold_active_flavor_audit.py
code/pr3_v07e_strong_diagnostic_comparison.py
code/pr3_v07f_final_strong_closure.py
```

Final data:

```text
data/strong_final_closure_audit.json
```

## Global consistency ledger

```text
code/pr3_v08a_global_ledger_lock.py
code/pr3_v08b_anomaly_registry_audit.py
code/pr3_v08c_running_continuity_audit.py
code/pr3_v08d_no_fit_provenance_manifest.py
code/pr3_v08e_cross_sector_diagnostic_table.py
code/pr3_v08f_final_priii_consistency_statement.py
```

Final data:

```text
data/global_final_priii_consistency_statement.json
```

## Reproducibility runner

### Tier A: default hardened audit

```bash
python code/run_all_pr3_audits.py
```

This validates:

```text
1. locked JSON status fields and required artifact presence
2. curated targeted regeneration schema/gate consistency for schemas/pr3_regeneration_targets.json
```

Expected result:

```text
PR-III reproducibility audit: PASS
```

### Manifest-only compatibility mode

```bash
python code/run_all_pr3_audits.py --manifest-only
```

This validates only file presence and expected locked status fields.

### Tier B: full 41-pair schema/numeric artifact audit

```bash
python code/pr3_artifact_drift_audit.py
python code/pr3_artifact_drift_audit.py --json > results/tier_b_artifact_drift_audit.json
```

This uses:

```text
schemas/pr3_full_regeneration_pairs.json
```

Expected result:

```text
pairs_checked: 41
pairs_passed: 41
pairs_failed: 0
failure_classes:
  pass: 41
```

Supporting summaries:

```bash
python code/pr3_schema_drift_summary.py results/tier_b_artifact_drift_audit.json
python code/pr3_numeric_drift_summary.py results/tier_b_artifact_drift_audit.json
```

Expected summary state:

```text
mechanical_top_level_wrapper_drift: 0
nested_structural_schema_drift: 0
representation_mismatch: 0
numeric_drift_beyond_policy: 0
numeric_failure_event_count: 0
```

### Tier C: canonical release byte-exact audit

```bash
python code/pr3_release_byte_exact_audit.py
python code/pr3_release_byte_exact_audit.py --json > results/tier_c_release_byte_exact_audit.json
```

This uses:

```text
schemas/pr3_release_byte_exact_policy.json
schemas/pr3_full_regeneration_pairs.json
```

Expected result:

```text
PR-III canonical release byte-exact audit: PASS
pairs_checked: 41
pairs_passed: 41
pairs_failed: 0
canonical release byte matches: 41/41
```

To write the regenerated canonical release tree:

```bash
python code/pr3_release_byte_exact_audit.py --write-release-tree results/pr3_canonical_release
```

The release tree should contain the 41 regenerated canonical release JSON artifacts.

### Tier D: raw generator/file-order diagnostics, not the release claim

The older full-target drift-report command remains useful as a raw-generator/canonical-diff diagnostic:

```bash
python code/run_all_pr3_audits.py --full-targets --drift-report
```

This command is expected to show canonical diffs and formatting/root-wrapper drift unless it is explicitly wired to the Pass 016 release-byte policy. It is not the Tier C release-byte authority.

The older strict byte-exact command remains a stress test of raw canonical generator output:

```bash
python code/run_all_pr3_audits.py --full-targets --byte-exact
```

This is not the PR-III release-byte claim.

## Drift and release policy

Artifact reproducibility is separated into tiers:

```text
Tier A: manifest/default repo audit
Tier B: full 41-pair schema/numeric artifact reproducibility
Tier C: canonical release byte-exact regeneration
Tier D: raw checked-in file-order or raw generator stdout byte identity
```

Current PR-III claim:

```text
Tier A: PASS
Tier B: PASS
Tier C: PASS
Tier D: NOT CLAIMED
```

The Tier C release-byte policy is:

```text
release_tier: canonical_release_bytes
canonical_json.indent: 2
canonical_json.sort_keys: true
canonical_json.ensure_ascii: false
canonical_json.terminal_newline: true
```

The Tier C policy allows root metadata wrapper normalization and numeric display locking only after schema/numeric reproducibility has passed. It does not relax numeric tolerances and does not modify physics values.
