with(LinearAlgebra):
with(StringTools):

results := table():
result_count := 0:
selftest_rows := []:
selftest_count := 0:
current_section := "":

ToFlatString := proc(x)
    local s;
    try
        s := convert(evalf(x, 20), string);
    catch:
        try
            s := convert(x, string);
        catch:
            s := "unprintable";
        end try;
    end try;
    s := SubstituteAll(s, "\n", " ");
    s := SubstituteAll(s, "\r", " ");
    return s;
end proc:

Csv := proc(x)
    local s;
    s := ToFlatString(x);
    s := SubstituteAll(s, "\"", "\"\"");
    return cat("\"", s, "\"");
end proc:

ResetPR3HarnessState := proc()
    global results, result_count, selftest_rows, selftest_count, current_section;
    results := table();
    result_count := 0;
    selftest_rows := [];
    selftest_count := 0;
    current_section := "";
end proc:

AddResult := proc(id, section, kind, status, actual, expected, err, tol, note)
    global results, result_count, current_section;
    result_count := result_count + 1;
    results[result_count] := table();
    results[result_count]["id"] := id;
    results[result_count]["section"] := section;
    results[result_count]["kind"] := kind;
    results[result_count]["status"] := status;
    results[result_count]["actual"] := ToFlatString(actual);
    results[result_count]["expected"] := ToFlatString(expected);
    results[result_count]["error"] := ToFlatString(err);
    results[result_count]["tolerance"] := ToFlatString(tol);
    results[result_count]["note"] := note;
    if section <> current_section then
        current_section := section;
        printf("\n=== %s ===\n", section);
    end if;
    printf("%s: %s - %s\n", status, id, note);
end proc:

CountFailures := proc()
    global results, result_count;
    local i, n;
    n := 0;
    for i to result_count do
        if results[i]["status"] = "FAIL" then
            n := n + 1;
        end if;
    end do;
    return n;
end proc:

MaxAbsMatrix := proc(A)
    local i, j, err;
    err := 0;
    for i to RowDimension(A) do
        for j to ColumnDimension(A) do
            err := max(err, abs(evalf(A[i,j])));
        end do;
    end do;
    return err;
end proc:

MaxAbsVectorDiff := proc(A, B)
    local i, err;
    err := 0;
    for i to Dimension(A) do
        err := max(err, abs(evalf(A[i] - B[i])));
    end do;
    return err;
end proc:

AssertClose := proc(id, section, actual, expected, tol, note)
    local err, status;
    err := abs(evalf(actual - expected));
    if evalb(err <= tol) then status := "PASS"; else status := "FAIL"; end if;
    AddResult(id, section, "numeric", status, actual, expected, err, tol, note);
end proc:

AssertExact := proc(id, section, actual, expected, note)
    local err, status;
    err := simplify(actual - expected);
    if evalb(err = 0) then status := "PASS"; else status := "FAIL"; end if;
    AddResult(id, section, "exact", status, actual, expected, err, 0, note);
end proc:

AssertTrue := proc(id, section, condition, note)
    local status;
    if evalb(condition) then status := "PASS"; else status := "FAIL"; end if;
    AddResult(id, section, "predicate", status, condition, true, 0, 0, note);
end proc:

AssertMatrixClose := proc(id, section, actual, expected, tol, note)
    local err, status;
    err := MaxAbsMatrix(actual - expected);
    if evalb(err <= tol) then status := "PASS"; else status := "FAIL"; end if;
    AddResult(id, section, "matrix", status, actual, expected, err, tol, note);
end proc:

AssertVectorClose := proc(id, section, actual, expected, tol, note)
    local err, status;
    err := MaxAbsVectorDiff(actual, expected);
    if evalb(err <= tol) then status := "PASS"; else status := "FAIL"; end if;
    AddResult(id, section, "vector", status, actual, expected, err, tol, note);
end proc:

PR3_SelfAssert := proc(label, condition)
    global selftest_rows, selftest_count;
    if evalb(condition) then
        selftest_count := selftest_count + 1;
        selftest_rows := [op(selftest_rows), [label, "PASS"]];
        printf("SELFTEST PASS: %s\n", label);
    else
        selftest_rows := [op(selftest_rows), [label, "FAIL"]];
        error "Harness self-test failed: %1", label;
    end if;
end proc:

PR3_SelfRejectClose := proc(label, got, wrong_expected, tol)
    local err;
    err := abs(evalf(got - wrong_expected));
    PR3_SelfAssert(label, evalb(err > tol));
end proc:

PR3_SelfRejectExact := proc(label, got, wrong_expected)
    local delta;
    delta := simplify(got - wrong_expected);
    PR3_SelfAssert(label, not evalb(delta = 0));
end proc:

PR3_WriteReports := proc(report_dir, prefix)
    global results, result_count, selftest_rows, selftest_count;
    local i, pass_count, fail_count, fh, summary_path, csv_path, validation_path;
    if not FileTools:-Exists(report_dir) then
        FileTools:-MakeDirectory(report_dir);
    end if;

    fail_count := CountFailures();
    pass_count := result_count - fail_count;

    summary_path := cat(report_dir, "/", prefix, "_summary.md");
    csv_path := cat(report_dir, "/", prefix, "_results.csv");
    validation_path := cat(report_dir, "/", prefix, "_harness_validation.md");

    fh := fopen(summary_path, WRITE, TEXT);
    fprintf(fh, "# PR-III Maple Test Summary\n\n");
    fprintf(fh, "Execution engine: Maple\n\n");
    fprintf(fh, "- Total tests: %d\n", result_count);
    fprintf(fh, "- Passed: %d\n", pass_count);
    fprintf(fh, "- Failed: %d\n", fail_count);
    fprintf(fh, "- Negative controls passed: %d\n\n", selftest_count);
    if fail_count = 0 then
        fprintf(fh, "OVERALL_STATUS: PASS\n");
    else
        fprintf(fh, "OVERALL_STATUS: FAIL\n");
    end if;
    fclose(fh);

    fh := fopen(csv_path, WRITE, TEXT);
    fprintf(fh, "id,section,kind,status,actual,expected,error,tolerance,note\n");
    for i to result_count do
        fprintf(fh, "%s,%s,%s,%s,%s,%s,%s,%s,%s\n",
            Csv(results[i]["id"]), Csv(results[i]["section"]),
            Csv(results[i]["kind"]), Csv(results[i]["status"]),
            Csv(results[i]["actual"]), Csv(results[i]["expected"]),
            Csv(results[i]["error"]), Csv(results[i]["tolerance"]),
            Csv(results[i]["note"]));
    end do;
    fclose(fh);

    fh := fopen(validation_path, WRITE, TEXT);
    fprintf(fh, "# PR-III Maple Harness Self-Validation\n\n");
    fprintf(fh, "The self-tests are negative controls: they insert known-bad equations and confirm the harness rejects them.\n\n");
    fprintf(fh, "```text\nSELFTEST PASS count: %d\n```\n\n", selftest_count);
    fprintf(fh, "| selftest_label | status |\n");
    fprintf(fh, "| --- | --- |\n");
    for i to nops(selftest_rows) do
        fprintf(fh, "| %s | %s |\n", selftest_rows[i][1], selftest_rows[i][2]);
    end do;
    fclose(fh);
end proc:
