# PR-II Coverage Quality Report

This report separates full source accounting from direct Maple proof density.

## Current Harness Size

- PR-II Maple source lines: 1725
- PR-II Maple procedures: 46
- Last recorded PR-II Maple checks: 617
- Recorded non-LaTeX/core checks: 167
- Generated LaTeX-source assertions included in current Maple run: 450
- Current expected Maple checks: 617
- Includes generated Maple source audit with one assertion per display block.

## Display-Block Coverage

- Display blocks inventoried: 442
- Unmapped display blocks: 0
- Direct numeric/symbolic display matches: 53
- Section-chain PASS display blocks: 215
- Boundary/context/data/manuscript display blocks: 174

## Status Counts

| status | count |
| --- | --- |
| DATA | 62 |
| NOTE | 112 |
| PASS | 268 |

## Coverage Mode Counts

| mode | count |
| --- | --- |
| boundary | 62 |
| context | 12 |
| direct-numeric | 11 |
| direct-symbolic | 42 |
| note-boundary | 100 |
| section-chain | 215 |

## Interpretation

The release criterion is complete source accounting: every displayed block is mapped, classified, and asserted present in the audited source fixture.
Direct numeric/symbolic rows are independently recomputed; section-chain rows inherit the passing calculation chain identified by their manuscript section; `NOTE` and `DATA` rows are explicit non-theorem boundaries rather than test failures.

The machine-readable inventory preserves those distinctions so reviewers can trace each display without treating definitions, contextual restatements, or external diagnostics as independent derived claims.
