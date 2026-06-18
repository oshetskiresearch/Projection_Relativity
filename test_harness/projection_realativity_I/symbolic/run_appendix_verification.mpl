# Runner for the Projection Relativity paper and supplementary Maple harness.
# PR_RunAll also refreshes equation_map.md, harness_validation.md,
# equation_derivations.md, proof_report.md, spectrum_recompute.md,
# and equation_audit.md.
#
# From Maple, run:
#   read "run_appendix_verification.mpl";

read "ProjectionRelativityAppendixVerify.mpl":
PR_RunAll();
