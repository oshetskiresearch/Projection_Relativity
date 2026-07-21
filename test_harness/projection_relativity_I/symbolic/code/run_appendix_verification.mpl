# Runner for the Projection Relativity paper and supplementary Maple harness.
# PR_RunAll also refreshes equation_map.md, harness_validation.md,
# equation_derivations.md, proof_report.md, spectrum_recompute.md,
# and equation_audit.md.
#
# From the repository root in Maple, run:
#   read "test_harness/projection_relativity_I/symbolic/code/run_appendix_verification.mpl";

read "test_harness/projection_relativity_I/symbolic/code/ProjectionRelativityAppendixVerify.mpl":
PR_RunAll();
