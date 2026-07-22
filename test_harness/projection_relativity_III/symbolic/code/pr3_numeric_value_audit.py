#!/usr/bin/env python3
"""Numeric-value audit for PR-III manuscript source.

This audit extracts decimal/scientific numeric literals from the manuscript TeX
and compares them with the locked JSON/CSV/report ledger in the public repository.

It intentionally focuses on decimal values and scientific notation. Exact
integer/fraction structural identities are covered by the Maple and equation
audit layers.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from decimal import Decimal, InvalidOperation, getcontext
from pathlib import Path
from typing import Iterable


getcontext().prec = 140

NUMBER_PATTERN = re.compile(
    r"""
    (?P<sign>[+-]?)
    (?P<mantissa>
        (?:
            \d+\.\d+
            |
            \.\d+
        )
    )
    (?P<ellipsis>\s*(?:\\ldots|\\dots|\.\.\.))?
    (?:
        \s*
        (?:
            \\times\s*10\^\{?(?P<tex_exp>[+-]?\d+)\}?
            |
            [eE](?P<e_exp>[+-]?\d+)
        )
    )?
    """,
    re.VERBOSE,
)

SPLIT_CONTINUATION_PATTERN = re.compile(
    r"""
    \s*(?:[}\)]\s*)*\\\\\s*
    (?:[-+]\s*)?&\s*
    (?P<digits>\d{4,})
    (?:
        \s*
        (?:
            \\times\s*10\^\{?(?P<tex_exp>[+-]?\d+)\}?
            |
            [eE](?P<e_exp>[+-]?\d+)
        )
    )?
    \s*\.?
    """,
    re.VERBOSE,
)

PM_SCALE_PATTERN = re.compile(
    r"\\right\)?\s*\\times\s*10\^\{?(?P<tex_exp>[+-]?\d+)\}?",
    re.DOTALL,
)

LAYOUT_CONTEXT_PATTERNS = [
    r"\\usepackage\[[^]]*(?:margin|paper|textwidth)",
    r"\\setlength",
    r"\\renewcommand\{\\arraystretch\}",
    r"\\def\\",
    r"\\draw",
    r"\\node",
    r"\\begin\{scope\}",
    r"\\begin\{tikzpicture\}",
    r"\\begin\{tabular\}.*p\{",
    r"p\{[0-9.]+\\textwidth\}",
    r"minimum width",
    r"minimum height",
    r"text width",
    r"leftmargin\s*=",
    r"shift=\{",
    r"controls",
    r"ellipse",
    r"arc ",
    r"\bat\s*\(",
]


@dataclass
class NumericRow:
    id: str
    file: str
    line: int
    status: str
    value_text: str
    normalized_decimal: str
    matched_value: str
    matched_source: str
    abs_error: str
    tolerance: str
    context: str


@dataclass
class LedgerValue:
    value: Decimal
    source: str
    text: str


def strip_comments(text: str) -> str:
    rows = []
    for line in text.splitlines():
        out = []
        escaped = False
        for char in line:
            if char == "\\" and not escaped:
                escaped = True
                out.append(char)
                continue
            if char == "%" and not escaped:
                break
            escaped = False
            out.append(char)
        rows.append("".join(out))
    return "\n".join(rows)


def token_tolerance(mantissa: str, exponent: int, ellipsis: bool) -> Decimal:
    fractional_digits = len(mantissa.split(".", 1)[1]) if "." in mantissa else 0
    tolerance = Decimal(10) ** Decimal(exponent - fractional_digits)
    if not ellipsis:
        tolerance = tolerance / Decimal(2)
    if tolerance == 0:
        tolerance = Decimal("1e-120")
    return abs(tolerance)


def normalize_token(match: re.Match[str]) -> tuple[Decimal, Decimal, str]:
    sign = match.group("sign") or ""
    mantissa = match.group("mantissa")
    exp_text = match.group("tex_exp") or match.group("e_exp")
    exponent = int(exp_text) if exp_text is not None else 0
    raw = sign + mantissa
    value = Decimal(raw) * (Decimal(10) ** exponent)
    tolerance = token_tolerance(mantissa, exponent, bool(match.group("ellipsis")))
    return value, tolerance, f"{raw}e{exponent}" if exponent else raw


def normalize_match(text: str, match: re.Match[str]) -> tuple[Decimal, Decimal, str, str]:
    sign = match.group("sign") or ""
    mantissa = match.group("mantissa")
    exponent_text = match.group("tex_exp") or match.group("e_exp")
    exponent = int(exponent_text) if exponent_text is not None else 0
    token = match.group(0).strip()

    pieces: list[str] = []
    scan = match.end()
    continuation_exponent: int | None = None
    while True:
        continuation = SPLIT_CONTINUATION_PATTERN.match(text, scan)
        if continuation is None:
            break
        pieces.append(continuation.group("digits"))
        cont_exp_text = continuation.group("tex_exp") or continuation.group("e_exp")
        if cont_exp_text is not None:
            continuation_exponent = int(cont_exp_text)
        scan = continuation.end()

    if pieces and "." in mantissa:
        integer_part, fractional_part = mantissa.split(".", 1)
        joined_mantissa = f"{integer_part}.{fractional_part}{''.join(pieces)}"
        exponent = continuation_exponent if continuation_exponent is not None else exponent
        raw = sign + joined_mantissa
        value = Decimal(raw) * (Decimal(10) ** exponent)
        tolerance = token_tolerance(joined_mantissa, exponent, bool(match.group("ellipsis")))
        normalized = f"{raw}e{exponent}" if exponent else raw
        return value, tolerance, normalized, f"{token} [joined TeX split]"

    if exponent_text is None:
        tail = text[match.end() : match.end() + 180]
        scale = PM_SCALE_PATTERN.search(tail)
        scale_prefix = tail[: scale.start()] if scale else ""
        row_break_before_scale = "\\\\" in scale_prefix
        pm_context = "\\pm" in scale_prefix if scale and not row_break_before_scale else False
        pm_context = pm_context or "\\pm" in text[max(0, match.start() - 24) : match.start()]
        if scale and pm_context and not row_break_before_scale:
            exponent = int(scale.group("tex_exp"))
            raw = sign + mantissa
            value = Decimal(raw) * (Decimal(10) ** exponent)
            tolerance = token_tolerance(mantissa, exponent, bool(match.group("ellipsis")))
            normalized = f"{raw}e{exponent}"
            return value, tolerance, normalized, f"{token} [scaled by shared TeX exponent]"

    value, tolerance, normalized = normalize_token(match)
    return value, tolerance, normalized, token


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def line_context(text: str, index: int) -> str:
    start = text.rfind("\n", 0, index) + 1
    end = text.find("\n", index)
    if end == -1:
        end = len(text)
    return re.sub(r"\s+", " ", text[start:end]).strip()[:240]


def is_layout_context(context: str) -> bool:
    return any(re.search(pattern, context) for pattern in LAYOUT_CONTEXT_PATTERNS)


def extract_numbers_from_text(text: str, source: str) -> list[LedgerValue]:
    values: list[LedgerValue] = []
    for match in NUMBER_PATTERN.finditer(text):
        try:
            value, _, normalized, token = normalize_match(text, match)
        except (InvalidOperation, ValueError):
            continue
        values.append(LedgerValue(value=value, source=source, text=token or normalized))
    return values


def collect_ledger_values(repo: Path) -> list[LedgerValue]:
    numerical = repo / "test_harness" / "projection_relativity_III" / "numerical"
    payload = repo / "data" / "projection_relativity_III"
    paths: list[Path] = [
        numerical / "MANIFEST_PR3_LOCKED_OUTPUTS.json",
        numerical / "README_PR3_REPRODUCIBILITY.md",
        numerical / "RUN_ORDER.md",
        numerical / "results" / "PR3_FINAL_AUDIT_SUMMARY.md",
        numerical / "schemas" / "pr3_numeric_tolerances.json",
    ]
    paths.extend((payload / "data").glob("*.json"))
    paths.extend((numerical / "results").glob("*.csv"))
    paths.extend((numerical / "results").glob("step_*.md"))

    values: list[LedgerValue] = []
    for path in sorted(set(paths)):
        if path.is_file():
            rel = path.relative_to(repo).as_posix()
            values.extend(extract_numbers_from_text(path.read_text(encoding="utf-8", errors="replace"), rel))

    # Public/paper wording thresholds that are qualitative bounds rather than
    # generated quantities. These still need explicit accounting.
    known_context = {
        "0.04": "paper qualitative strong-residual bound",
        "0.12": "neutrino conservative cosmology ceiling",
        "0.45": "direct beta-decay bound",
        "70": "0nu beta beta comparison scale in meV",
        "2026": "manuscript year",
        "42": "PDF page count",
        "0.000011663788": "diagnostic Fermi constant central value",
        "0.000000000007": "diagnostic Fermi constant uncertainty",
    }
    for text, source in known_context.items():
        try:
            values.append(LedgerValue(value=Decimal(text), source=source, text=text))
        except InvalidOperation:
            pass
    return values


def find_best_match(value: Decimal, tolerance: Decimal, ledger: list[LedgerValue]) -> tuple[LedgerValue | None, Decimal | None]:
    best: LedgerValue | None = None
    best_err: Decimal | None = None
    for item in ledger:
        err = abs(value - item.value)
        if best_err is None or err < best_err:
            best = item
            best_err = err
            if err <= tolerance:
                return best, best_err
    return best, best_err


def find_best_abs_match(value: Decimal, tolerance: Decimal, ledger: list[LedgerValue]) -> tuple[LedgerValue | None, Decimal | None]:
    best: LedgerValue | None = None
    best_err: Decimal | None = None
    abs_value = abs(value)
    for item in ledger:
        err = abs(abs_value - abs(item.value))
        if best_err is None or err < best_err:
            best = item
            best_err = err
            if err <= tolerance:
                return best, best_err
    return best, best_err


def iter_tex_files(tex_root: Path) -> list[Path]:
    return sorted(path for path in tex_root.glob("*.tex") if path.is_file())


def audit(repo: Path, tex_root: Path) -> list[NumericRow]:
    ledger = collect_ledger_values(repo)
    rows: list[NumericRow] = []
    counter = 1
    for path in iter_tex_files(tex_root):
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_comments(raw)
        rel = path.relative_to(tex_root).as_posix()
        for match in NUMBER_PATTERN.finditer(text):
            context = line_context(text, match.start())
            try:
                value, tolerance, normalized, token = normalize_match(text, match)
            except (InvalidOperation, ValueError):
                continue

            if is_layout_context(context):
                best = None
                err = None
                status = "SKIP_LAYOUT"
            else:
                best, err = find_best_match(value, tolerance, ledger)
                matched = best is not None and err is not None and err <= tolerance
                status = "PASS" if matched else "UNMATCHED"
                if status == "UNMATCHED" and value >= 0 and re.search(r"\bbelow\b|\bmagnitude\b|\babsolute\b", context, re.IGNORECASE):
                    abs_best, abs_err = find_best_abs_match(value, tolerance, ledger)
                    if abs_best is not None and abs_err is not None and abs_err <= tolerance:
                        best = abs_best
                        err = abs_err
                        status = "PASS_ABS_CONTEXT"

            rows.append(
                NumericRow(
                    id=f"PR3-NUM-{counter:04d}",
                    file=rel,
                    line=line_number(text, match.start()),
                    status=status,
                    value_text=token,
                    normalized_decimal=str(value),
                    matched_value=best.text if best else "",
                    matched_source=best.source if best else "",
                    abs_error=str(err) if err is not None else "",
                    tolerance=str(tolerance),
                    context=context,
                )
            )
            counter += 1
    return rows


def write_csv(path: Path, rows: list[NumericRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def write_reports(rows: list[NumericRow], outdir: Path, repo: Path, tex_root: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    unmatched = [row for row in rows if row.status == "UNMATCHED"]
    skipped = [row for row in rows if row.status == "SKIP_LAYOUT"]
    checked = [row for row in rows if row.status != "SKIP_LAYOUT"]
    passed = [row for row in rows if row.status.startswith("PASS")]
    status_counts = Counter(row.status for row in rows)
    write_csv(outdir / "numeric_value_inventory.csv", rows)
    if unmatched:
        write_csv(outdir / "numeric_value_unmatched.csv", unmatched)
    else:
        (outdir / "numeric_value_unmatched.csv").write_text(
            "id,file,line,status,value_text,normalized_decimal,matched_value,matched_source,abs_error,tolerance,context\n",
            encoding="utf-8",
        )

    summary = {
        "overall_status": "PASS" if not unmatched else "FAIL",
        "repo": "https://github.com/oshetskiresearch/Projection_Relativity",
        "tex_root": "https://github.com/oshetskiresearch/Projection_Relativity/tree/main/manuscript/projection_relativity_III",
        "numeric_literals_inventoried": len(rows),
        "document_numeric_values_checked": len(checked),
        "matched": len(passed),
        "skipped_layout_literals": len(skipped),
        "unmatched": len(unmatched),
        "status_counts": dict(status_counts),
    }
    (outdir / "numeric_value_audit_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    lines = [
        "# PR-III Numeric Value Audit",
        "",
        f"OVERALL_STATUS: {summary['overall_status']}",
        "",
        "## Summary",
        "",
        f"- Numeric literals inventoried: {len(rows)}",
        f"- Document numeric values checked: {len(checked)}",
        f"- Matched to locked ledger/source: {len(passed)}",
        f"- Layout/diagram literals skipped: {len(skipped)}",
        f"- Unmatched: {len(unmatched)}",
        "",
        "The audit compares manuscript decimal/scientific numeric literals to the public repository's locked JSON/CSV/report ledger using Decimal rounding-aware tolerances. TeX layout dimensions and diagram coordinates are inventoried but excluded from the physics-value pass/fail gate.",
        "",
        "## Unmatched Values",
        "",
    ]
    if unmatched:
        for row in unmatched[:100]:
            lines.append(f"- `{row.value_text}` at `{row.file}:{row.line}` context `{row.context}`")
    else:
        lines.append("No unmatched numeric literals.")
    (outdir / "numeric_value_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True, help="Path to the Projection_Relativity public checkout")
    parser.add_argument("--tex-root", type=Path, required=True, help="Path to manuscript TeX root")
    parser.add_argument("--output-dir", type=Path, default=Path("reports"), help="Output report directory")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    repo = args.repo.resolve()
    tex_root = args.tex_root.resolve()
    harness_root = Path(__file__).resolve().parents[1]
    outdir = args.output_dir if args.output_dir.is_absolute() else harness_root / args.output_dir
    rows = audit(repo, tex_root)
    if not rows:
        print("PR-III numeric value audit: FAIL")
        print(f"No numeric literals found under {tex_root}")
        return 1
    write_reports(rows, outdir, repo, tex_root)
    unmatched = sum(1 for row in rows if row.status == "UNMATCHED")
    skipped = sum(1 for row in rows if row.status == "SKIP_LAYOUT")
    checked = len(rows) - skipped
    status = "PASS" if unmatched == 0 else "FAIL"
    print(f"PR-III numeric value audit: {status}")
    print(f"numeric_literals={len(rows)} checked={checked} skipped_layout={skipped} unmatched={unmatched}")
    print(f"summary={outdir / 'numeric_value_audit.md'}")
    return 0 if unmatched == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
