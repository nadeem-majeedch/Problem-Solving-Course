#!/usr/bin/env python3
"""Run the full quality-assurance suite and write qa-report.md.

Orchestrates the real checks (never reimplements them): every stage is the
same command CI runs, executed as a subprocess so its PASS/FAIL output is
captured verbatim. Then it collects course inventory numbers and turns any
warnings into a review list with recommended corrections.

Stages
  1. generate_catalog.py   case catalog regeneration (metadata errors fail)
  2. validate.py           structure, cases, pairing, learning design,
                           runnable solutions, links
  3. pytest tests/ -q      tooling tests
  4. gen_slides.py         slide decks regenerate from lecture sources
  5. build_site.py         public build with its built-in leak check
  6. audit_site.py         built-artifact audit (links, nav, a11y, leaks)

Usage:
    python scripts/qa_report.py            # write qa-report.md, exit 0/1
    python scripts/qa_report.py --stdout   # print the report instead
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "qa-report.md"

STAGES = [
    ("Catalog regeneration", ["python", "scripts/generate_catalog.py"]),
    ("Topic-coverage heatmap regeneration (fails on unmapped tags)",
     ["python", "scripts/gen_topic_heatmap.py"]),
    ("Content validation (structure, cases, learning design, solutions, links)",
     ["python", "scripts/validate.py"]),
    ("Tooling tests", ["python", "-m", "pytest", "tests/", "-q"]),
    ("Slide-deck regeneration", ["python", "scripts/gen_slides.py"]),
    ("Public site build (includes leak check)", ["python", "scripts/build_site.py"]),
    ("Built-site audit (coverage, links, navigation, a11y)", ["python", "scripts/audit_site.py"]),
]


def run_stage(name: str, cmd: list[str]) -> tuple[bool, str, str]:
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=1200)
        out = (r.stdout or "") + (r.stderr or "")
        return r.returncode == 0, out, ""
    except subprocess.TimeoutExpired:
        return False, "", "timed out after 1200 s"
    except Exception as e:
        return False, "", f"{type(e).__name__}: {e}"


def inventory() -> list[tuple[str, str]]:
    import collections

    lectures = sorted(p for p in (ROOT / "lectures").glob("lecture-*") if p.is_dir())
    student = sorted((ROOT / "case-studies" / "student").glob("cs-*.md"))
    instructor = sorted((ROOT / "case-studies" / "instructor").glob("cs-*.md"))
    tiers = collections.Counter()
    per_lec: dict[str, int] = collections.Counter()
    for f in student:
        m = re.search(r"\|\s*difficulty\s*\|\s*(\w+)", f.read_text(encoding="utf-8"))
        tiers[m.group(1) if m else "?"] += 1
        n = int(f.stem.split("-")[1])
        per_lec[f"lecture-{(n - 1) // 4 + 1:02d}"] += 1
    rows = [
        ("Lectures (2 h each)", str(len(lectures))),
        ("Lecture teaching pack files", str(len(list((ROOT / "lectures").glob("lecture-*/[a-z]*.md"))))),
        ("Case studies (student / instructor)",
         f"{len(student)} / {len(instructor)}"),
        ("Difficulty distribution", ", ".join(
            f"{t}: {tiers.get(t, 0)}" for t in
            ("Beginner", "Foundational", "Intermediate", "Advanced", "Expert"))),
        ("Labs / quizzes / assignments / projects",
         f"{len(list((ROOT / 'labs').glob('lab-*.md')))}/"
         f"{len(list((ROOT / 'quizzes').glob('quiz-*.md')))}/"
         f"{len(list((ROOT / 'assignments').glob('assignment-*.md')))}/"
         f"{len([p for p in (ROOT / 'projects').glob('project-*.md') if p.stem != 'project-rubric'])}"),
        ("Slide decks", str(len(list((ROOT / 'slides' / 'decks').glob('lecture-*-slides.html'))))),
        ("Public site pages", str(len(list((ROOT / 'site').rglob('*.html'))))),
    ]
    return rows


def parse_validate_output(out: str) -> tuple[int, int, list[str]]:
    errors = re.findall(r"ERROR:\s*(.*)", out)
    warns = re.findall(r"WARN:\s*(.*)", out)
    return len(errors), len(warns), warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()

    lines: list[str] = []
    all_ok = True
    stage_results: list[tuple[str, bool, str]] = []
    validate_warnings: list[str] = []

    for name, cmd in STAGES:
        ok, out, err = run_stage(name, cmd)
        stage_results.append((name, ok, out or err))
        if name.startswith("Content validation"):
            _e, _w, validate_warnings = parse_validate_output(out or "")
        if not ok:
            all_ok = False

    lines.append("# Quality-Assurance Report")
    lines.append("")
    lines.append(f"**Status: {'PASS' if all_ok else 'FAIL'}** · generated "
                 f"{datetime.now().strftime('%Y-%m-%d %H:%M')} by `scripts/qa_report.py`")
    lines.append("")

    lines.append("## Stage results")
    lines.append("")
    lines.append("| # | Stage | Result |")
    lines.append("| --- | --- | --- |")
    for i, (name, ok, _) in enumerate(stage_results, 1):
        lines.append(f"| {i} | {name} | {'✅ PASS' if ok else '❌ FAIL'} |")
    lines.append("")

    for name, ok, out in stage_results:
        if not ok:
            lines.append(f"## Failure detail — {name}")
            lines.append("")
            lines.append("```")
            lines.append(out.strip()[-3000:])
            lines.append("```")
            lines.append("")

    # Inventory (facts only; computed from the sources of truth).
    lines.append("## Course inventory")
    lines.append("")
    lines.append("| Item | Count |")
    lines.append("| --- | --- |")
    for k, v in inventory():
        lines.append(f"| {k} | {v} |")
    lines.append("")

    # Validation findings requiring human review (validator warnings).
    lines.append("## Findings for instructor review")
    lines.append("")
    if validate_warnings:
        lines.append("These are judgement-call findings (warnings), not build failures. "
                     "Each names the case and the numbers involved so the author can "
                     "confirm or fix the worked instance.")
        lines.append("")
        lines.append("| # | Finding | Recommended action |")
        lines.append("| --- | --- | --- |")
        for i, w in enumerate(validate_warnings, 1):
            lines.append(f"| {i} | {w} | "
                         "Re-run the demo and align the 'Expected result.' line "
                         "with the program output, or reword the prose |")
    else:
        lines.append("None. All checks passed with no judgement-call findings.")
    lines.append("")

    lines.append("## Reproduce")
    lines.append("")
    lines.append("```bash")
    lines.append("python scripts/qa_report.py")
    lines.append("```")
    lines.append("")
    lines.append("Each stage can also be run individually; see `docs/deployment.md`.")

    report = "\n".join(lines) + "\n"
    if args.stdout:
        # Windows consoles may default to a non-UTF-8 code page; the report
        # contains ✓/✅ glyphs, so print without ever crashing on encoding.
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        print(report)
    else:
        REPORT.write_text(report, encoding="utf-8")
        print(f"qa-report.md written ({'PASS' if all_ok else 'FAIL'})")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
