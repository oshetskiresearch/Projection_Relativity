# Projection Relativity III Test Harnesses

This directory separates the public validation work for Projection Relativity
III into two packages:

- [`symbolic/`](symbolic/) contains the Maple symbolic tester, the full
  equation audit, and the audit of numerical values printed in the paper.
- [`numerical/`](numerical/) is the location for the separate numerical
  validation and reproducibility tester.

The two packages test different layers of the work and are documented
separately. The checked symbolic and manuscript-audit run is summarized in
[`RUN_SUMMARY.md`](RUN_SUMMARY.md).
