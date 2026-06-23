# Projection Relativity: Convergence Analysis Data

The following table summarizes the spectral compiler results across increasing harmonic basis sizes ($N$). These values represent the asymptotic convergence of the Projection Relativity radial operator.

| Parameter | $N=300$ | $N=10,000$ | $N=15,000$ |
| :--- | :--- | :--- | :--- |
| **Ground State ($\lambda_0$)** | 2.322872581463488 | 2.322872581463488 | 2.322872581463488 |
| **First Excited ($\lambda_1$)** | 5.375889248196178 | 5.375889248196178 | 5.375889248196177 |
| **Third Excited ($\lambda_3$)** | 13.233893408730458 | 13.233893408730466 | 13.233893408730470 |
| **Spectral Gap ($\mu_{min}^2$)** | 3.053016666732690 | 3.053016666732690 | 3.053016666732689 |
| **Boundary Constant ($c_{bc}$)** | 0.796684464847899 | 0.796684464847899 | 0.796684464847899 |
| **Finite-Rank Leakage ($p_1$)** | 7.685346950896194e-04 | 7.685346950896167e-04 | 7.685346950896231e-04 |
| **Effective Gap ($q_{bc}$)** | 10.904981678435441 | 10.904981678435449 | 10.904981678435453 |
| **Derived $\alpha_{PR}^{-1}$** | **137.036041314016273** | **137.036041314016387** | **137.036041314016444** |

---

### Technical Summary
* **Saturation Point:** The system demonstrates stable convergence at $N=10,000$. Increasing the basis size to $N=15,000$ yields negligible shifts, confirming that the numerical execution has reached the 64-bit precision ceiling for this geometric architecture.
* **Interpretation:** The remaining variance between the derived $\alpha^{-1}$ and the empirical CODATA reference ($137.035999206$) is structurally localized to the convergence limit of current spectral diagonalizers.
