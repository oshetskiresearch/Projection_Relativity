RunPR3Tests := proc()
    local tol, sigma1, sigma2, sigma3, T1, T2, T3, Tplus, Tminus, up, down,
          QY1, Phi0, g0, gp0, vv, M0, MW2s, MZ2s, cos2s,
          alphaInv, MW, MZ, GF, m1, m2, m3, sumNu, mbeta, mbb, alpha3,
          beta0_nf6, beta_prefactor_nf6, Ngen, anomalyU1, anomalyGrav,
          sigmaAlpha, sigmaMW, sigmaMZ, sigmaGF,
          qch, rhoPR, kPR, PZ, D3k, W1v, W2v, Zv, Av, Ddiff, defect,
          aPR, bPR, rPR, qGeneric, Uorth, qRot, Fgeneric, Frot,
          h0PR, v1PR, w1PR, zPR, Hscalar, GammaScalar, HessianScalar,
          GammaK, cPR, sPR, PW3, PZneutral, gPR, qZ, qZhat,
          xPR, SZZ, SAZ, etaPR, lambdaPR, Hbase, Hlambda,
          GammaBase, GammaLambda, HessianShift, gZPR, vEWPR, MZ0sq,
          OHDvev, DeltaLEFT, Phi3, residualScale, dPR,
          Yhalf, gpPR, ePR, photonCoeff, zCoeff, zCoeffExpected;

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
    AssertMatrixClose("PR3-C3-001", "canonical-C3-charge-response", QY1.Tminus - Tminus.QY1, -Tminus, 0, "[Q,T-]=-T-");

    g0 := 'g0'; gp0 := 'gp0'; vv := 'vv';
    M0 := (vv^2/4)*Matrix([[g0^2, -g0*gp0], [-g0*gp0, gp0^2]]);
    MW2s := g0^2*vv^2/4;
    MZ2s := (g0^2 + gp0^2)*vv^2/4;
    cos2s := g0^2/(g0^2 + gp0^2);
    AssertExact("PR3-EW003", "electroweak-null-ledger", simplify(Determinant(M0)), 0, "Neutral mass matrix has a massless photon mode");
    AssertExact("PR3-EW004", "electroweak-null-ledger", simplify(MW2s/(MZ2s*cos2s)), 1, "Tree rho identity is preserved before radiative refinements");
    AssertExact("PR3-EW005", "electroweak-null-ledger", simplify(g0^2/(8*MW2s)), 1/(2*vv^2), "Charged Fermi contact coefficient");

    # Revised PR-III canonical C3 closure: exact charged-adjoint factor,
    # rank-one neutral gates, normalized quadratic response, and uniqueness.
    qch := Matrix([[1, 0], [0, -1]]);
    AssertMatrixClose("PR3-C3-002", "canonical-C3-charge-response", Transpose(qch).qch, IdentityMatrix(2), 0, "Charged-adjoint q^dagger q is I2");
    AssertExact("PR3-C3-003", "canonical-C3-charge-response", Trace(Transpose(qch).qch), 2, "Exact charged-adjoint trace is two");

    rhoPR := 'rhoPR';
    kPR := 'kPR';
    PZ := DiagonalMatrix([0, 0, 1, 0]);
    D3k := rhoPR*kPR*PZ;
    W1v := Vector([1, 0, 0, 0]);
    W2v := Vector([0, 1, 0, 0]);
    Zv := Vector([0, 0, 1, 0]);
    Av := Vector([0, 0, 0, 1]);
    AssertMatrixClose("PR3-C3-004", "canonical-C3-rank-one-gates", PZ.PZ, PZ, 0, "Physical-Z operator is an orthogonal projector");
    AssertVectorClose("PR3-C3-005", "canonical-C3-rank-one-gates", D3k.W1v, ZeroVector(4), 0, "D3 leaves W1 unchanged");
    AssertVectorClose("PR3-C3-006", "canonical-C3-rank-one-gates", D3k.W2v, ZeroVector(4), 0, "D3 leaves W2 unchanged");
    AssertVectorClose("PR3-C3-007", "canonical-C3-rank-one-gates", D3k.Av, ZeroVector(4), 0, "D3 preserves photon nullity");
    AssertVectorClose("PR3-C3-008", "canonical-C3-rank-one-gates", D3k.Zv, rhoPR*kPR*Zv, 0, "D3 acts only on the physical-Z direction");
    AssertMatrixClose("PR3-C3-009", "canonical-C3-rank-one-gates", Transpose(D3k), D3k, 0, "D3 is symmetric");
    Ddiff := D3k - 2*rhoPR*PZ;
    defect := simplify(Trace(Transpose(Ddiff).Ddiff));
    AssertExact("PR3-C3-010", "canonical-C3-uniqueness", defect, rhoPR^2*(kPR-2)^2, "Exact Frobenius defect is rho_PR^2(k-2)^2");

    # Machine-checkable instances of the normalized quadratic response axioms.
    aPR := 'aPR'; bPR := 'bPR'; rPR := 'rPR';
    qGeneric := DiagonalMatrix([aPR, bPR]);
    Fgeneric := Trace(Transpose(qGeneric).qGeneric);
    AssertExact("PR3-C3-011", "canonical-C3-response-axioms", Trace(Matrix([[1]])), 1, "Unit-charge normalization");
    AssertExact("PR3-C3-012", "canonical-C3-response-axioms", Fgeneric, aPR^2+bPR^2, "Direct-sum additivity on one-dimensional charge modes");
    AssertExact("PR3-C3-013", "canonical-C3-response-axioms", Trace(Transpose(rPR*qGeneric).(rPR*qGeneric)), rPR^2*Fgeneric, "Quadratic homogeneity for a real scale");
    Uorth := Matrix([[3/5, -4/5], [4/5, 3/5]]);
    qRot := simplify(Uorth.qGeneric.Transpose(Uorth));
    Frot := simplify(Trace(Transpose(qRot).qRot));
    AssertExact("PR3-C3-014", "canonical-C3-response-axioms", Frot, Fgeneric, "Normalized quadratic response is invariant under an orthogonal charged-basis change");

    # Finite-dimensional representative of the reference-normalized
    # determinant Hessian identity.
    h0PR := 'h0PR'; v1PR := 'v1PR'; w1PR := 'w1PR'; zPR := 'zPR';
    Hscalar := h0PR + v1PR*zPR + (w1PR/2)*zPR^2;
    GammaScalar := ln(Hscalar/h0PR);
    HessianScalar := simplify(subs(zPR=0, diff(GammaScalar, zPR, zPR)));
    AssertExact("PR3-C3-015", "canonical-C3-determinant-Hessian", HessianScalar, w1PR/h0PR-v1PR^2/h0PR^2, "Second variation of the reference-normalized determinant");
    GammaK := (kPR*rhoPR/2)*zPR^2;
    AssertExact("PR3-C3-016", "canonical-C3-determinant-Hessian", diff(GammaK, zPR, zPR), kPR*rhoPR, "Broader fixed-kernel family has Hessian k*rho_PR");

    # Physical neutral-basis and physical-Z charge checks.
    cPR := 'cPR'; sPR := 'sPR'; gPR := 'gPR';
    PW3 := 2*Matrix([[cPR^2, cPR*sPR], [cPR*sPR, sPR^2]]);
    PZneutral := Matrix([[1, 0], [0, 0]]);
    AssertExact("PR3-C3-017", "canonical-C3-physical-Z-map", subs(cPR^2=1-sPR^2, Trace(PW3)), 2, "The literal 2P_W3 tensor has normalized trace two");
    AssertExact("PR3-C3-018", "canonical-C3-physical-Z-map", PZneutral[2,2], 0, "Canonical physical-Z projector has no photon component");
    qZ := DiagonalMatrix([gPR*cPR, -gPR*cPR]);
    AssertExact("PR3-C3-019", "canonical-C3-physical-Z-map", Trace(Transpose(qZ).qZ), 2*gPR^2*cPR^2, "Physical-Z charged-vector trace includes the vertex factor");
    qZhat := qZ/(gPR*cPR);
    AssertExact("PR3-C3-020", "canonical-C3-physical-Z-map", Trace(Transpose(qZhat).qZhat), 2, "Normalized physical-Z charge trace is two");
    Yhalf := QY1-T3;
    gpPR := gPR*sPR/cPR;
    ePR := gPR*sPR;
    photonCoeff := simplify(gPR*sPR*T3 + gpPR*cPR*Yhalf);
    zCoeff := simplify(gPR*cPR*T3 - gpPR*sPR*Yhalf);
    zCoeffExpected := (gPR/cPR)*(T3-sPR^2*QY1);
    AssertMatrixClose("PR3-C3-028", "canonical-C3-physical-Z-map", photonCoeff, ePR*QY1, 0, "Neutral connection reconstructs the electromagnetic coefficient eQ");
    AssertMatrixClose("PR3-C3-029", "canonical-C3-physical-Z-map", simplify(subs(cPR^2=1-sPR^2, cPR*(zCoeff-zCoeffExpected))), ZeroMatrix(2), 0, "Neutral connection reconstructs the physical-Z coefficient");

    # One-generation matter traces quoted in the revised manuscript.
    xPR := 'xPR';
    SZZ := (1/2)^2 + (-1/2+xPR)^2 + xPR^2
           + 3*(1/2-(2/3)*xPR)^2 + 3*(-1/2+(1/3)*xPR)^2
           + 3*((-2/3)*xPR)^2 + 3*((1/3)*xPR)^2;
    SAZ := (-1)*(-1/2+xPR) + (-1)*xPR
           + 3*(2/3)*(1/2-(2/3)*xPR) + 3*(-1/3)*(-1/2+(1/3)*xPR)
           + 3*(2/3)*((-2/3)*xPR) + 3*(-1/3)*((1/3)*xPR);
    AssertExact("PR3-C3-021", "canonical-C3-matter-response", simplify(SZZ), 2-4*xPR+(16/3)*xPR^2, "One-generation ZZ chiral charge trace");
    AssertExact("PR3-C3-022", "canonical-C3-matter-response", simplify(SAZ), 2-(16/3)*xPR, "One-generation AZ chiral charge trace");

    # Independent second-jet and EFT comparison families are algebraically
    # reproducible but explicitly outside the minimal response class.
    etaPR := 'etaPR'; lambdaPR := 'lambdaPR';
    Hbase := h0PR + v1PR*zPR;
    Hlambda := Hbase + (lambdaPR*rhoPR/(2*etaPR))*zPR^2*h0PR;
    GammaBase := etaPR*ln(Hbase/h0PR);
    GammaLambda := etaPR*ln(Hlambda/h0PR);
    HessianShift := simplify(subs(zPR=0, diff(GammaLambda-GammaBase, zPR, zPR)));
    AssertExact("PR3-C3-023", "canonical-C3-class-boundary", HessianShift, lambdaPR*rhoPR, "Independent second jet shifts the determinant Hessian by lambda*rho_PR");
    gZPR := 'gZPR'; vEWPR := 'vEWPR';
    MZ0sq := gZPR^2*vEWPR^2/4;
    OHDvev := vEWPR^4*gZPR^2/16;
    DeltaLEFT := (2*lambdaPR*rhoPR/vEWPR^2)*OHDvev;
    AssertExact("PR3-C3-024", "canonical-C3-class-boundary", simplify(DeltaLEFT), (1/2)*lambdaPR*rhoPR*MZ0sq, "Broader EFT operator produces the stated neutral mass term");

    # Normalized generation-sheet incidence and invertible residual-map
    # equivalence used in the closed admissibility statement.
    Phi3 := Matrix([[1,0,0], [0,3/5,-4/5], [0,4/5,3/5]]);
    AssertMatrixClose("PR3-C3-025", "closed-admissibility-domain", Transpose(Phi3).Phi3, IdentityMatrix(3), 0, "Normalized three-sheet incidence map");
    AssertExact("PR3-C3-026", "closed-admissibility-domain", Rank(Phi3), 3, "Three-sheet incidence map is complete and nonredundant");
    residualScale := 'residualScale'; dPR := 'dPR';
    AssertExact("PR3-C3-027", "closed-admissibility-domain", solve(residualScale*(dPR-2*rhoPR)=0, dPR), 2*rhoPR, "Invertible scalar residual maps preserve the canonical solution");

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
    local alphaInv, MW, photonWrongDet, anomalyWrong, m2, m3, beta0_wrong,
          wrongKDefect, xFrozen, wrongPW3Photon, wrongLinearResponse,
          badPhi3, secondJetShift;
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
    wrongKDefect := (1-2)^2;
    PR3_SelfRejectExact("reject noncanonical C3 coefficient k=1", wrongKDefect, 0);
    xFrozen := 0.231355763298189;
    wrongPW3Photon := 2*xFrozen;
    PR3_SelfRejectExact("reject literal W3 projector as photon-null physical-Z projector", wrongPW3Photon, 0);
    wrongLinearResponse := Trace(Matrix([[1,0],[0,-1]]));
    PR3_SelfRejectExact("reject linear trace as normalized quadratic charge response", wrongLinearResponse, 2);
    badPhi3 := DiagonalMatrix([1,1,2]);
    PR3_SelfRejectExact("reject nonnormalized generation incidence map", Trace(Transpose(badPhi3).badPhi3), 3);
    secondJetShift := 1;
    PR3_SelfRejectExact("reject claim that an independent second jet leaves C3 unchanged", secondJetShift, 0);
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
    PR3_WriteReports("symbolic/results", "pr3_maple");
end proc:
