# Symbolic and Numerical Modules

`code/` contains the public PR-IV certificates and reproduction generators.
`results/` contains checked outputs from the master runner. Regenerating the
directory is safe: each output has a stable name and is overwritten by its
own producing module.

The exact harness and source audit use only the Python standard library. The
PR-I spectral ledger and compact diagnostic propagation additionally require
NumPy and SciPy at the versions recorded in the package runtime manifest.

Run only through `code/run_all_pr4_audits.py` for the authoritative public
gate; it enforces component ordering and validates every result status.

