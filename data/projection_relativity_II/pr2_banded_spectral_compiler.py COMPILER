# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#  ______             __                   __                __        __        _______                                                               __
# /      \           |  \                 |  \              |  \      |  \      |       \                                                             |  \
#|  $$$$$$\  _______ | $$____    ______  _| $$_     _______ | $$   __  \$$      | $$$$$$$\  ______    _______   ______    ______    ______    _______ | $$____
#| $$  | $$ /       \| $$    \  /      \|   $$ \   /       \| $$  /  \|  \      | $$__| $$ /      \  /       \ /      \  |      \  /      \  /       \| $$    \
#| $$  | $$|  $$$$$$$| $$$$$$$\|  $$$$$$\\$$$$$$  |  $$$$$$$| $$_/  $$| $$      | $$    $$|  $$$$$$\|  $$$$$$$|  $$$$$$\  \$$$$$$\|  $$$$$$\|  $$$$$$$| $$$$$$$\
#| $$  | $$ \$$    \ | $$  | $$| $$    $$ | $$ __  \$$    \ | $$   $$ | $$      | $$$$$$$\| $$    $$ \$$    \ | $$    $$ /      $$| $$   \$$| $$      | $$  | $$
#| $$__/ $$ _\$$$$$$\| $$  | $$| $$$$$$$$ | $$|  \ _\$$$$$$\| $$$$$$\ | $$      | $$  | $$| $$$$$$$$ _\$$$$$$\| $$$$$$$$|  $$$$$$$| $$      | $$_____ | $$  | $$
# \$$    $$|       $$| $$  | $$ \$$     \  \$$  $$|       $$| $$  \$$\| $$      | $$  | $$ \$$     \|       $$ \$$     \ \$$    $$| $$       \$$     \| $$  | $$
#  \$$$$$$  \$$$$$$$  \$$   \$$  \$$$$$$$   \$$$$  \$$$$$$$  \$$   \$$ \$$       \$$   \$$  \$$$$$$$ \$$$$$$$   \$$$$$$$  \$$$$$$$ \$$        \$$$$$$$ \$$   \$$
#
# COLAB-USABLE VERSION
# PROJECTION RELATIVITY II: BANDED SPECTRAL COMPILER
# Michael Stanislaus Oshetski
# ORCID# 0009-0007-3623-7586
# June 2026
#
# "Dedicated to my brother and best friend,
# John Oshetski Jr. ("Motorhead")
# I'll see you in the decoherence!
#
# What this script does:
#   1. Initializes an N-basis harmonic oscillator Hilbert space to
#      represent the Projection Relativity radial operator.
#   2. Constructs the Hamiltonian as a sparse banded matrix to 
#      allow for high-precision (N=15,000) user setable spectral diagonalization.
#   3. Extracts the converged radial spectrum (lambda_0, lambda_1, lambda_3) 
#      to determine the fundamental geometric gaps.
#   4. Evaluates the finite-rank leakage (p1) via the compact 
#      boundary map to resolve the non-Abelian phase fiber coupling.
#   5. Outputs the boundary-resolved electromagnetic normalization 
#      (alpha^-1) as a zero-new-parameter geometric derivation.
#
#
# Generates: Results printed in the user terminal
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


import numpy as np
from scipy.linalg import eig_banded
from scipy.sparse import diags


def compile_projection_relativity_banded(N=1):
    print("=" * 68)
    print("PROJECTION RELATIVITY: BANDED SPECTRAL COMPILER")
    print("=" * 68)
    print(f"[SYS] Harmonic basis size: N={N}")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Compact boundary cofactor
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    T_A = 1.0 / 4.0
    T_X = 3.0 / 4.0

    R_bc = (
        1.0
        + T_A**3
        + T_A**4
        + T_X * (T_A**5 - T_A**8)
    ) / (
        1.0
        - T_A**3
        - T_A**4
    )

    c_bc = T_X * (
        1.0
        + T_A**2
        - T_A**6 * R_bc
    )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Exact harmonic-basis matrix elements
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    n = np.arange(N, dtype=np.float64)

    # <n|w^4|n>
    w4_diag = 0.75 * (2.0 * n**2 + 2.0 * n + 1.0)

    # <n|w^4|n+2>
    n2 = np.arange(N - 2, dtype=np.float64)
    w4_off2 = (
        n2 + 1.5
    ) * np.sqrt(
        (n2 + 1.0) * (n2 + 2.0)
    )

    # <n|w^4|n+4>
    n4 = np.arange(N - 4, dtype=np.float64)
    w4_off4 = 0.25 * np.sqrt(
        (n4 + 1.0)
        * (n4 + 2.0)
        * (n4 + 3.0)
        * (n4 + 4.0)
    )

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # O_X = H_HO + 1 + 3/4 w^4
    # Upper-banded storage with bandwidth 4
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    H_diag = (
        2.0 * n
        + 2.0
        + 0.75 * w4_diag
    )

    H_off2 = 0.75 * w4_off2
    H_off4 = 0.75 * w4_off4

    H_band = np.zeros((5, N), dtype=np.float64)

    # Main diagonal
    H_band[4, :] = H_diag

    # +2 diagonal
    H_band[2, 2:] = H_off2

    # +4 diagonal
    H_band[0, 4:] = H_off4

    # Compute only the first four eigenpairs.
    evals, evecs = eig_banded(
        H_band,
        lower=False,
        eigvals_only=False,
        select="i",
        select_range=(0, 3),
        check_finite=False,
    )

    l0 = evals[0]
    l1 = evals[1]
    l3 = evals[3]

    q1 = l1 - l0
    q3 = l3 - l0

    print("-" * 68)
    print("CONVERGED RADIAL SPECTRUM")
    print(f"lambda_0 = {l0:.15f}")
    print(f"lambda_1 = {l1:.15f}")
    print(f"lambda_3 = {l3:.15f}")
    print(f"mu_min^2 = {q1:.15f}")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # W = c_bc I + w^2 + 3/4 w^4
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    w2_diag = n + 0.5

    w2_off2 = 0.5 * np.sqrt(
        (n2 + 1.0) * (n2 + 2.0)
    )

    W_diag = (
        c_bc
        + w2_diag
        + 0.75 * w4_diag
    )

    W_off2 = (
        w2_off2
        + 0.75 * w4_off2
    )

    W_off4 = 0.75 * w4_off4

    W_op = diags(
        diagonals=[
            W_off4,
            W_off2,
            W_diag,
            W_off2,
            W_off4,
        ],
        offsets=[-4, -2, 0, 2, 4],
        shape=(N, N),
        format="csr",
    )

    phi1 = evecs[:, 1]
    phi3 = evecs[:, 3]

    W11 = float(phi1 @ (W_op @ phi1))
    W33 = float(phi3 @ (W_op @ phi3))
    W13 = float(phi1 @ (W_op @ phi3))

    k1_sq = 1.0
    k3_sq = (q3 / q1) ** 2

    P_matrix = np.array(
        [
            [
                k1_sq * W11 * k1_sq,
                k1_sq * W13 * k3_sq,
            ],
            [
                k3_sq * W13 * k1_sq,
                k3_sq * W33 * k3_sq,
            ],
        ],
        dtype=np.float64,
    )

    P_evals, P_evecs = np.linalg.eigh(P_matrix)

    dominant_index = np.argmax(P_evals)
    dominant_vector = P_evecs[:, dominant_index]

    p1 = dominant_vector[0] ** 2

    q_bc = (
        p1 * q1
        + (1.0 - p1) * q3
    )

    alpha_inv = 4.0 * np.pi * q_bc

    print("-" * 68)
    print("COMPACT BOUNDARY MAP")
    print(f"c_bc       = {c_bc:.15f}")
    print(f"p1         = {p1:.15e}")
    print(f"q_bc       = {q_bc:.15f}")

    print("=" * 68)
    print("ELECTROMAGNETIC NORMALIZATION")
    print(f"alpha^-1   = {alpha_inv:.15f}")
    print("=" * 68)

    return {
        "N": N,
        "lambda_0": l0,
        "lambda_1": l1,
        "lambda_3": l3,
        "mu_min_sq": q1,
        "c_bc": c_bc,
        "p1": p1,
        "q_bc": q_bc,
        "alpha_inv": alpha_inv,
    }
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#  Set N below
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
if __name__ == "__main__":
    result = compile_projection_relativity_banded(N=15000)
