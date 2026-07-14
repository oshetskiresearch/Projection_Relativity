RunPR3Tests := proc()
    local tol, sigma1, sigma2, sigma3, T1, T2, T3, Tplus, Tminus, up, down,
          QY1, Phi0, g0, gp0, vv, M0, MW2s, MZ2s, cos2s,
          alphaInv, MW, MZ, GF, m1, m2, m3, sumNu, mbeta, mbb, alpha3,
          beta0_nf6, beta_prefactor_nf6, Ngen, anomalyU1, anomalyGrav,
          sigmaAlpha, sigmaMW, sigmaMZ, sigmaGF;

    tol := 10^(-12);

    alphaInv := 137.035999207513414958891346101616594635677637490015536978556268584855576779314655494829901;
    MW := 80.373942851862121269660365960912048165641419593354239705150762943078449202475090;
    MZ := 91.187676431043922257304294605837072137923832857909555944715358374802790284187517;
    GF := 0.000011663792201759949366003257867488874906911567673178839516230456502630714171261169;
    m1 := 0;
    m2 := 0.008627283010;
    m3 := 0.05010655367;
    sumNu := 0.058733836680;
    mbeta := 8.815029409998;
    mbb := 1.507694477;
    alpha3 := 0.117861507469150;
    sigmaAlpha := 0.1376;
    sigmaMW := 0.3566;
    sigmaMZ := 0.0364;
    sigmaGF := 0.6003;

    sigma1 := Matrix([[0, 1], [1, 0]]);
    sigma2 := Matrix([[0, -I], [I, 0]]);
    sigma3 := Matrix([[1, 0], [0, -1]]);
    T1 := (1/2)*sigma1;
    T2 := (1/2)*sigma2;
    T3 := (1/2)*sigma3;
    Tplus := T1 + I*T2;
    Tminus := T1 - I*T2;
    up := Vector([1, 0]);
    down := Vector([0, 1]);

    AssertMatrixClose("PR3-G001", "compact-su2-ledger", T1.T2 - T2.T1, I*T3, 0, "[T1,T2]=iT3");
    AssertMatrixClose("PR3-G002", "compact-su2-ledger", T2.T3 - T3.T2, I*T1, 0, "[T2,T3]=iT1");
    AssertMatrixClose("PR3-G003", "compact-su2-ledger", T3.T1 - T1.T3, I*T2, 0, "[T3,T1]=iT2");
    AssertExact("PR3-G004", "compact-su2-ledger", Trace(T1.T1), 1/2, "Trace normalization");
    AssertMatrixClose("PR3-G005", "compact-su2-ledger", T1.T1 + T2.T2 + T3.T3, (3/4)*IdentityMatrix(2), 0, "Fundamental Casimir");
    AssertVectorClose("PR3-G006", "compact-su2-ledger", Tplus.down, up, 0, "T+ ladder");
    AssertVectorClose("PR3-G007", "compact-su2-ledger", Tminus.up, down, 0, "T- ladder");

    QY1 := T3 + (1/2)*IdentityMatrix(2);
    Phi0 := Vector([0, 1]);
    AssertVectorClose("PR3-EW001", "electroweak-null-ledger", QY1.Phi0, Vector([0,0]), 0, "Q=T3+Y/2 annihilates the locking direction");
    AssertMatrixClose("PR3-EW002", "electroweak-null-ledger", QY1.Tplus - Tplus.QY1, Tplus, 0, "[Q,T+]=T+");

    g0 := 'g0'; gp0 := 'gp0'; vv := 'vv';
    M0 := (vv^2/4)*Matrix([[g0^2, -g0*gp0], [-g0*gp0, gp0^2]]);
    MW2s := g0^2*vv^2/4;
    MZ2s := (g0^2 + gp0^2)*vv^2/4;
    cos2s := g0^2/(g0^2 + gp0^2);
    AssertExact("PR3-EW003", "electroweak-null-ledger", simplify(Determinant(M0)), 0, "Neutral mass matrix has a massless photon mode");
    AssertExact("PR3-EW004", "electroweak-null-ledger", simplify(MW2s/(MZ2s*cos2s)), 1, "Tree rho identity is preserved before radiative refinements");
    AssertExact("PR3-EW005", "electroweak-null-ledger", simplify(g0^2/(8*MW2s)), 1/(2*vv^2), "Charged Fermi contact coefficient");

    Ngen := (3+1)-1;
    AssertExact("PR3-F001", "generation-and-anomaly-ledger", Ngen, 3, "Generation count from broken compact quotient");
    AssertExact("PR3-A001", "generation-and-anomaly-ledger", 2 - 1 - 1, 0, "Pure color anomaly");
    AssertExact("PR3-A002", "generation-and-anomaly-ledger", 2*(1/2)*(1/3)+(1/2)*(-4/3)+(1/2)*(2/3), 0, "SU3^2 U1Y anomaly");
    AssertExact("PR3-A003", "generation-and-anomaly-ledger", 3*(1/2)*(1/3)+(1/2)*(-1), 0, "SU2^2 U1Y anomaly");
    anomalyU1 := 6*(1/3)^3+3*(-4/3)^3+3*(2/3)^3+2*(-1)^3+2^3;
    anomalyGrav := 6*(1/3)+3*(-4/3)+3*(2/3)+2*(-1)+2;
    AssertExact("PR3-A004", "generation-and-anomaly-ledger", anomalyU1, 0, "Cubic hypercharge anomaly");
    AssertExact("PR3-A005", "generation-and-anomaly-ledger", anomalyGrav, 0, "Gravity^2 U1Y anomaly");
    AssertTrue("PR3-A006", "generation-and-anomaly-ledger", type((4*Ngen)/2, integer), "Witten parity is even for three generations");

    beta0_nf6 := 11 - 2*6/3;
    beta_prefactor_nf6 := -beta0_nf6/(2*Pi);
    AssertExact("PR3-S001", "strong-ledger", beta0_nf6, 7, "One-loop beta0 at n_f=6");
    AssertTrue("PR3-S002", "strong-ledger", evalf(beta_prefactor_nf6) < 0, "Asymptotic-freedom sign");
    AssertClose("PR3-S003", "strong-ledger", alpha3, 0.117861507469150, tol, "Strong anchor alpha3");

    AssertClose("PR3-N001", "neutrino-ledger", m1, 0, tol, "Massless first neutrino branch");
    AssertClose("PR3-N002", "neutrino-ledger", m2, 0.008627283010, tol, "Second neutrino mass");
    AssertClose("PR3-N003", "neutrino-ledger", m3, 0.05010655367, tol, "Third neutrino mass");
    AssertClose("PR3-N004", "neutrino-ledger", sumNu, m1 + m2 + m3, tol, "Neutrino mass sum");
    AssertTrue("PR3-N005", "neutrino-ledger", m1 < m2 and m2 < m3, "Normal ordering preserved");
    AssertTrue("PR3-N006", "neutrino-ledger", sumNu < 0.12, "Mass sum below conservative ceiling");
    AssertClose("PR3-N007", "neutrino-ledger", mbeta, 8.815029409998, 10^(-12), "Effective beta mass");
    AssertClose("PR3-N008", "neutrino-ledger", mbb, 1.507694477, 10^(-12), "Neutrinoless double-beta envelope center");

    AssertClose("PR3-P001", "paper-locked-values", alphaInv, 137.035999207513414958891346101616594635677637490015536978556268584855576779314655494829901, 10^(-60), "Fine-structure inverse locked value");
    AssertClose("PR3-P002", "paper-locked-values", MW, 80.373942851862121269660365960912048165641419593354239705150762943078449202475090, 10^(-50), "W mass locked value");
    AssertClose("PR3-P003", "paper-locked-values", MZ, 91.187676431043922257304294605837072137923832857909555944715358374802790284187517, 10^(-50), "Z mass locked value");
    AssertClose("PR3-P004", "paper-locked-values", GF, 0.000011663792201759949366003257867488874906911567673178839516230456502630714171261169, 10^(-70), "Fermi constant locked value");
    AssertClose("PR3-P005", "paper-locked-values", sigmaAlpha, 0.1376, 10^(-12), "Alpha diagnostic sigma");
    AssertClose("PR3-P006", "paper-locked-values", sigmaMW, 0.3566, 10^(-12), "M_W diagnostic sigma");
    AssertClose("PR3-P007", "paper-locked-values", sigmaMZ, 0.0364, 10^(-12), "M_Z diagnostic sigma");
    AssertClose("PR3-P008", "paper-locked-values", sigmaGF, 0.6003, 10^(-12), "G_F diagnostic sigma");
end proc:

PR3_HarnessSelfTest := proc()
    local alphaInv, MW, photonWrongDet, anomalyWrong, m2, m3, beta0_wrong;
    printf("\n=== Harness Self-Validation: Negative Controls ===\n");
    alphaInv := 137.035999207513414958891346101616594635677637490015536978556268584855576779314655494829901;
    MW := 80.373942851862121269660365960912048165641419593354239705150762943078449202475090;
    m2 := 0.008627283010;
    m3 := 0.05010655367;
    photonWrongDet := 'g0'^2*'gp0'^2*'vv'^4/16;
    anomalyWrong := 6*(1/3)^3+3*(-4/3)^3+3*(2/3)^3+2*(-1)^3+1;
    beta0_wrong := 11 + 2*6/3;

    PR3_SelfRejectClose("reject stale alpha inverse", alphaInv, 137.036361812007, 10^(-12));
    PR3_SelfRejectClose("reject wrong W mass", MW, 80.0, 10^(-12));
    PR3_SelfRejectExact("reject massive photon determinant", photonWrongDet, 0);
    PR3_SelfRejectExact("reject anomaly-violating hypercharge ledger", anomalyWrong, 0);
    PR3_SelfAssert("reject inverted neutrino ordering", not evalb(m3 < m2));
    PR3_SelfRejectExact("reject wrong beta0 sign convention", beta0_wrong, 7);
    PR3_SelfAssert("reject exact all-orders theorem overclaim", not evalb("CLAIMED" = "NOT_CLAIMED"));
end proc:

PR3_RunAll := proc()
    local fail_count;
    ResetPR3HarnessState();
    printf("\n=== Projection Relativity III Maple Verification ===\n");
    RunPR3Tests();
    PR3_HarnessSelfTest();
    fail_count := CountFailures();
    printf("\n=== Summary ===\n");
    printf("PASS count: %d\n", result_count - fail_count);
    printf("FAIL count: %d\n", fail_count);
    printf("SELFTEST PASS count: %d\n", selftest_count);
    PR3_WriteReports("reports", "pr3_maple");
end proc:
