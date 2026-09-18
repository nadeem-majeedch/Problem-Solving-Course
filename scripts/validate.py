#!/usr/bin/env python3
"""Validate the course repository: structure, case metadata, pairing,
links, lecture plans, learning design, runnable solution programs, and
content-separation rules.

Exits non-zero on any error. Errors are never silently skipped;
judgement-call findings are reported as warnings for instructor review.
"""

from __future__ import annotations

import contextlib
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


# ---------- required files ----------

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    ".gitignore",
    "docs/index.md",
    "docs/course-overview.md",
    "docs/learning-outcomes.md",
    "docs/course-outline.md",
    "docs/teaching-methodology.md",
    "docs/assessment-plan.md",
    "docs/instructor-guide.md",
    "docs/resources.md",
    "docs/glossary.md",
    "docs/faq.md",
    "case-studies/CATALOG.md",
    "scripts/render.py",
    "scripts/build_site.py",
    "scripts/build_instructor.py",
    "scripts/generate_catalog.py",
    "scripts/gen_topic_heatmap.py",
    "scripts/audit_site.py",
    "scripts/qa_report.py",
    "scripts/validate.py",
    "docs/deployment.md",
    "docs/case-review.md",
    "docs/handover-report.md",
    "docs/instructor-reports/expert-tier-rationale.md",
    "docs/instructor-reports/quiz-answer-key-audit.md",
    "docs/instructor-reports/lab-expected-output-audit.md",
    "docs/topic-coverage-heatmap.md",
    "docs/topic-coverage-heatmap.csv",
    "docs/assets/topic-coverage-heatmap.svg",
    "assets/css/style.css",
    "resources/python-setup.md",
    "resources/pseudocode-style.md",
    ".github/workflows/validate.yml",
    ".github/workflows/pages.yml",
]

REQUIRED_LECTURE_HEADINGS = [
    "## Position in the course",
    "## Learning objectives",
    "## Case sequence",
    "## Timing plan (120 minutes)",
    "## Board plan",
    "## Differentiation",
    "## Common misconceptions",
    "## Homework and preparation",
]

REQUIRED_CASE_SECTIONS = [
    "## Problem",
    "## Examples",
    "## What to notice",
    "## Discussion starter",
    "## Hints and extension",
]

REQUIRED_SOLUTION_SECTIONS = [
    "## Reasoning walkthrough",
    "## Five-minute teaching sequence",
    "## Difficulty adaptation",
    "## Reference solution (Python)",
    "## Reference solution (pseudocode)",
    "## Edge cases",
    "## Alternative approaches",
    "## Common pitfalls",
    "## Reveal script",
    "## Assessment use",
    "## Connections",
    "## Extension challenge",
]

DIFFICULTIES = {"Beginner", "Foundational", "Intermediate", "Advanced", "Expert"}

# Course-level minimum per tier (the case-study specification). Enforced
# only when the corpus is full-sized so miniature test fixtures stay valid.
MIN_CASES_BY_DIFFICULTY = {
    "Beginner": 20,
    "Foundational": 25,
    "Intermediate": 25,
    "Advanced": 20,
    "Expert": 10,
}
TIER_ORDER = ["Beginner", "Foundational", "Intermediate", "Advanced", "Expert"]

STUDENT_LEAK_PATTERNS = [
    ("solution heading", re.compile(r"^## (Reasoning walkthrough|Reference solution|Edge cases|Alternative approaches|Common pitfalls|Reveal script|Connections)\b", re.M)),
    ("solution phrase", re.compile(r"\bReference solution\b", re.I)),
    ("reveal script phrase", re.compile(r"\bReveal script\b", re.I)),
]

MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

# The case-study specification's minimum is 100 unique cases. The corpus
# now carries 144; both sides (student/instructor) must match this set.
EXPECTED_CASES = 144


def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception as e:
        err(f"{p}: unreadable ({e})")
        return ""


# ---------- required files ----------

def check_required_files() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            err(f"missing required file: {rel}")


# ---------- case checks ----------

def case_files() -> tuple[list[Path], list[Path]]:
    student = sorted((ROOT / "case-studies" / "student").glob("cs-*.md"))
    instructor = sorted((ROOT / "case-studies" / "instructor").glob("cs-*.md"))
    return student, instructor


student_meta: dict[str, dict] = {}


def check_distribution(cases: dict[str, dict]) -> None:
    """Tier counts must meet the specification minima. Only enforced on a
    full-sized corpus so miniature test fixtures are not required to carry
    a complete course worth of cases."""
    student = cases.get("student", {})
    if len(student) < 32:
        return
    counts = {t: 0 for t in TIER_ORDER}
    for sid, f in student.items():
        meta = parse_meta_table(read(f)) or {}
        tier = meta.get("difficulty")
        if tier in counts:
            counts[tier] += 1
    for tier in TIER_ORDER:
        if counts[tier] < MIN_CASES_BY_DIFFICULTY[tier]:
            err(
                f"difficulty distribution fails: {tier} has {counts[tier]} cases, "
                f"needs at least {MIN_CASES_BY_DIFFICULTY[tier]}"
            )


def parse_meta_table(text: str) -> dict[str, str] | None:
    """Parse the Field/Value metadata table that follows the title."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == "| Field | Value |":
            meta = {}
            for ln in lines[i + 1 :]:
                if not ln.strip().startswith("|"):
                    break
                m = re.match(r"\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|?\s*$", ln)
                if m:
                    meta[m.group(1).strip().lower()] = m.group(2)
            return meta if meta else None
    return None


def check_cases() -> dict[str, dict]:
    student, instructor = case_files()
    student_ids, instructor_ids = {}, {}

    for f in student:
        text = read(f)
        sid = f.stem
        m = re.match(r"^# (cs-\d{3}) — .+", text)
        if not m:
            err(f"{f.name}: must start with '# cs-NNN — Title'")
            continue
        if m.group(1) != sid:
            err(f"{f.name}: title id {m.group(1)} != filename {sid}")
        student_ids[sid] = f

        meta = parse_meta_table(text)
        if not meta:
            err(f"{f.name}: missing | Field | Value | metadata table")
            continue
        for key in ("id", "difficulty", "lecture", "topics", "estimated time",
                    "prerequisites", "objective", "solution"):
            if key not in meta:
                err(f"{f.name}: metadata missing '{key}'")
        if meta.get("difficulty") not in DIFFICULTIES:
            err(f"{f.name}: bad difficulty {meta.get('difficulty')!r}")
        if meta.get("id") != sid:
            err(f"{f.name}: metadata id {meta.get('id')!r} != filename {sid}")
        student_meta[sid] = meta
        lec = meta.get("lecture", "")
        if not re.fullmatch(r"lecture-\d{2}", lec):
            err(f"{f.name}: bad lecture reference {lec!r}")
        elif not (ROOT / "lectures" / lec).exists():
            err(f"{f.name}: lecture {lec} does not exist")

        for sec in REQUIRED_CASE_SECTIONS:
            if f"\n{sec}\n" not in text:
                err(f"{f.name}: missing section {sec!r}")

        for name, pat in STUDENT_LEAK_PATTERNS:
            if pat.search(text):
                err(f"{f.name}: instructor-only {name} found in student file")

    for f in instructor:
        text = read(f)
        sid = f.stem
        m = re.match(r"^# (cs-\d{3}) — .+", text)
        if not m:
            err(f"{f.name}: must start with '# cs-NNN — Title'")
            continue
        if m.group(1) != sid:
            err(f"{f.name}: title id {m.group(1)} != filename {sid}")
        instructor_ids[sid] = f
        meta = parse_meta_table(text)
        if not meta:
            err(f"{f.name}: missing metadata table")
        else:
            if meta.get("id") != sid:
                err(f"{f.name}: metadata id {meta.get('id')!r} != filename {sid}")
            if meta.get("difficulty") not in DIFFICULTIES:
                err(f"{f.name}: bad difficulty {meta.get('difficulty')!r}")
            for key in ("estimated time", "prerequisites", "objective"):
                if key not in meta:
                    err(f"{f.name}: metadata missing '{key}'")
            smeta = student_meta.get(sid)
            if smeta is not None:
                if smeta.get("difficulty") != meta.get("difficulty"):
                    err(f"{sid}: difficulty differs between student and instructor pages")
                if smeta.get("lecture") != meta.get("lecture"):
                    err(f"{sid}: lecture differs between student and instructor pages")
        for sec in REQUIRED_SOLUTION_SECTIONS:
            if f"\n{sec}\n" not in text:
                err(f"{f.name}: missing section {sec!r}")
        mwalk = re.search(r"## Reasoning walkthrough\n(.+?)(?=\n## )", text, re.S)
        if not mwalk or len(mwalk.group(1).split()) < 40:
            err(f"{f.name}: Reasoning walkthrough too short (min 40 words)")

    only_s = set(student_ids) - set(instructor_ids)
    only_i = set(instructor_ids) - set(student_ids)
    for sid in sorted(only_s):
        err(f"{sid}: student file has no instructor solution")
    for sid in sorted(only_i):
        err(f"{sid}: instructor solution has no student file")

    if len(student_ids) != len(student):
        err("duplicate case id in student filenames")
    if len(instructor_ids) != len(instructor):
        err("duplicate case id in instructor filenames")

    return {"student": student_ids, "instructor": instructor_ids}


# ---------- lecture plans ----------

def check_lecture_plans(cases: dict[str, dict]) -> None:
    plans = sorted((ROOT / "lectures").glob("lecture-*"))
    for d in plans:
        if not re.fullmatch(r"lecture-\d{2}", d.name):
            err(f"unexpected lecture folder name: {d.name}")
            continue
        plan = d / "plan.md"
        if not plan.exists():
            err(f"{d.name}: missing plan.md")
            continue
        text = read(plan)
        if not text.startswith("# Lecture "):
            err(f"{d.name}: plan must start with '# Lecture NN — Title'")
        for h in REQUIRED_LECTURE_HEADINGS:
            if h not in text:
                err(f"{d.name}: missing heading {h!r}")
        # case references: a lecture must reference exactly the cases that
        # declare it in their metadata (4 base cases per lecture plus any
        # applied-case additions the curriculum maps to this lecture).
        refs = set(re.findall(r"cs-\d{3}", text))
        n = int(d.name.split("-")[1])
        expected = {
            sid
            for sid, f in cases["student"].items()
            if (parse_meta_table(read(f)) or {}).get("lecture") == d.name
        }
        missing = expected - refs
        if missing:
            err(f"{d.name}: plan does not reference its cases {sorted(missing)}")
        extra = refs - expected
        if extra:
            err(f"{d.name}: references foreign cases {sorted(extra)}")
        # referenced cases must name this lecture in metadata (checked via
        # `expected` construction above; the symmetric direction follows)
        for sid in sorted(expected):
            sf = cases["student"].get(sid)
            if sf is not None:
                meta = parse_meta_table(read(sf)) or {}
                if meta.get("lecture") != d.name:
                    err(f"{sid}: metadata lecture {repr(meta.get('lecture'))} != {d.name}")


def check_examples() -> None:
    """Verify examples.md files: structure, trace hygiene, runnable Python.

    Every ```python block in the examples must run without error and must
    not print to stdout. A verified trace example ends its block with a
    comment '# expect: ...' line per printed output; the harness compares
    program output against the expectations and fails on mismatch.
    """
    for d in sorted((ROOT / "lectures").glob("lecture-*")):
        ex = d / "examples.md"
        if not ex.exists():
            err(f"{d.name}: missing examples.md")
            continue
        text = read(ex)
        if not text.startswith("# Worked Examples — Lecture "):
            err(f"{d.name}: examples.md must start with '# Worked Examples — Lecture NN'")
        # table with the example column present
        if "| Example |" not in text or "| Python? |" not in text:
            err(f"{d.name}: examples.md missing the example index table")
        # split into python fences and run them in order, collecting expects
        blocks = re.findall(r"```python\r?\n(.*?)```", text, re.S)
        ran = 0
        for i, code in enumerate(blocks):
            g: dict = {"__name__": "__main__"}
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    exec(compile(code, f"{d.name}:block{i + 1}", "exec"), g)
            except Exception as e:
                err(f"{d.name}: python block {i + 1} failed: {type(e).__name__}: {e}")
                continue
            ran += 1
            printed = [l for l in buf.getvalue().splitlines() if l.strip()]
            expects = re.findall(r"# expect: (.+)", code)
            if expects:
                if [e.strip() for e in expects] != [p.strip() for p in printed]:
                    err(f"{d.name}: python block {i + 1} output mismatch: expected {expects}, got {printed}")
            elif printed:
                err(f"{d.name}: python block {i + 1} printed without # expect markers: {printed[:3]}")
        if ran and ran == len(blocks):
            pass
        if not blocks:
            err(f"{d.name}: examples.md has no python blocks to verify")


def check_pack() -> None:
    """Student pack files (notes/examples/quiz) and instructor teaching notes.

    Pack files are required for every lecture; each must start with the
    right H1. Traces in examples must not contain unexplained None lines.
    """
    h1_starts = {
        "notes.md": "# Lecture Notes — Lecture ",
        "examples.md": "# Worked Examples — Lecture ",
        "quiz.md": "# Quiz — Lecture ",
        "teaching-notes.md": "# Teaching Notes — Lecture ",
    }
    for d in sorted((ROOT / "lectures").glob("lecture-*")):
        if not re.fullmatch(r"lecture-\d{2}", d.name):
            continue
        n = int(d.name.split("-")[1])
        for fname, prefix in h1_starts.items():
            f = d / fname
            if not f.exists():
                err(f"{d.name}: missing {fname}")
                continue
            text = read(f)
            if not text.startswith(prefix):
                err(f"{d.name}: {fname} must start with {prefix!r}NN")
            elif not text.startswith(prefix + f"{n:02d}"):
                err(f"{d.name}: {fname} H1 number does not match its folder")
        notes = d / "notes.md"
        if notes.exists():
            nt = read(notes)
            for h in ("## Definitions", "## Explanation", "## Examples", "## Common misconceptions", "## Summary and key takeaways", "## Practice questions"):
                if h not in nt:
                    err(f"{d.name}: notes.md missing heading {h!r}")
        quiz = d / "quiz.md"
        if quiz.exists():
            qt = read(quiz)
            for h in ("## Section A", "## Section B", "## Exit ticket", "## Homework"):
                if h not in qt:
                    err(f"{d.name}: quiz.md missing heading {h!r}")


# ---------- learning design ----------

LO_IDS = [f"LO{i}" for i in range(1, 11)]


def check_learning_design(cases: dict[str, dict]) -> None:
    """Curriculum-coherence checks that go beyond file existence.

    Hard errors: missing/gapped learning-outcome definitions, an outcome
    never assessed, a lecture with no cases. Warnings: per-lecture tier
    pattern deviations, capstone lectures without an Advanced+ case —
    these need a human judgement call, so they inform but do not block.
    """
    lo_text = read(ROOT / "docs" / "learning-outcomes.md")
    for lo in LO_IDS:
        if not re.search(rf"^## {lo}\b", lo_text, re.M):
            err(f"learning-outcomes.md: missing section for {lo}")
    assessed = read(ROOT / "docs" / "assessment-plan.md")
    for lo in LO_IDS:
        if lo not in assessed:
            err(f"assessment-plan.md: outcome {lo} is never assessed")

    # Per-lecture case counts and difficulty vectors. Lectures are taken
    # from the filesystem: a missing lecture folder is already an error via
    # check_lecture_count, and an existing folder with no cases is a gap.
    # The 4-per-lecture / one-Beginner design applies to the base corpus
    # (cs-001..cs-128); cs-129+ are applied-case additions mapped onto
    # existing lectures, so they are excluded from that pattern check.
    student = cases.get("student", {})
    by_lec: dict[str, list[str]] = {}
    base_lec: dict[str, list[str]] = {}
    for sid, _f in student.items():
        meta = student_meta.get(sid, {})
        num = int(sid.split("-")[1])
        by_lec.setdefault(meta.get("lecture", ""), []).append(meta.get("difficulty", ""))
        if num <= 128:
            base_lec.setdefault(meta.get("lecture", ""), []).append(meta.get("difficulty", ""))
    for d in sorted((ROOT / "lectures").glob("lecture-*")):
        if not d.is_dir() or not re.fullmatch(r"lecture-\d{2}", d.name):
            continue
        lec = d.name
        n = int(lec.split("-")[1])
        tiers = by_lec.get(lec, [])
        base = base_lec.get(lec, [])
        if not tiers:
            err(f"{lec}: no cases assigned")
            continue
        if len(tiers) != len(base):
            # informational, not a warning: applied additions are a
            # documented part of the design (see docs/course-outline.md)
            print(f"note: {lec} carries {len(tiers)} cases "
                  f"({len(base)} base + {len(tiers) - len(base)} applied)")
        counts = {t: base.count(t) for t in TIER_ORDER}
        counts = {t: c for t, c in counts.items() if c}
        if counts.get("Beginner", 0) != 1:
            warn(f"{lec}: tier vector {counts} deviates from the intended "
                 f"one-Beginner-per-lecture design")
        if n >= 25 and not (counts.get("Advanced") or counts.get("Expert")):
            warn(f"{lec}: capstone-skill lecture without an Advanced+ case")


# ---------- solution programs ----------

FENCE_RE = re.compile(r"## Reference solution \(Python\)\n+```python\n(.*?)```", re.S)


def _numbers(s: str) -> set:
    out = set()
    for tok in re.findall(r"\d+(?:\.\d+)?", s):
        try:
            v = float(tok)
        except ValueError:
            continue
        out.add(int(v) if v == int(v) else round(v, 4))
    return out


def check_solutions_runnable() -> None:
    """Execute every instructor reference program in an isolated process.

    Checks (each failure is an ERROR, never a silent skip):
      - the program compiles and runs to completion within the timeout;
      - it does not read stdin (cases must be self-contained);
      - randomness is seeded, so output is reproducible;
      - output is deterministic across two runs.

    Additionally compares numbers in the 'Expected result.' prose against
    the program's output. Prose may legitimately narrate rules rather
    than repeat the demo instance, so a mismatch is a WARNING listing the
    case for instructor review — not a hard failure.
    """
    import subprocess

    for f in sorted((ROOT / "case-studies" / "instructor").glob("cs-*.md")):
        text = read(f).replace("\r\n", "\n")
        m = FENCE_RE.search(text)
        if not m:
            err(f"{f.name}: no 'Reference solution (Python)' code fence")
            continue
        code = m.group(1)
        if re.search(r"\binput\s*\(", code):
            err(f"{f.name}: solution reads stdin; cases must be self-contained")
            continue
        if "import random" in code and not re.search(r"\bseed\b", code):
            err(f"{f.name}: uses randomness without a seed (output not reproducible)")
        outs = []
        for _ in range(2):
            try:
                r = subprocess.run(
                    [sys.executable, "-I", "-c", code],
                    capture_output=True, text=True, timeout=20,
                )
            except subprocess.TimeoutExpired:
                err(f"{f.name}: solution timed out (20s)")
                break
            if r.returncode != 0:
                tail = (r.stderr or "").strip().splitlines()
                err(f"{f.name}: solution crashed: {tail[-1] if tail else 'nonzero exit'}")
                break
            outs.append(r.stdout)
        else:
            if not outs[0].strip():
                warn(f"{f.name}: solution demo run prints nothing")
            if outs[0] != outs[1]:
                err(f"{f.name}: solution output is not deterministic across runs")
            em = re.search(r"\*\*Expected result\.\*\*(.+)", text)
            if em and outs[0].strip():
                prose, produced = _numbers(em.group(1)), _numbers(outs[0])
                # Compare only when BOTH sides carry numbers: outputs like
                # star patterns or ['AI'] legitimately contain none.
                if prose and produced and not (prose & produced):
                    warn(
                        f"{f.name}: Expected-result prose shares no number with "
                        f"the program output — check that the worked instance "
                        f"matches the demo run (prose {sorted(prose)[:6]}, "
                        f"output {sorted(produced)[:6]})"
                    )


# ---------- links ----------

def md_files() -> list[Path]:
    skip_parts = {".git", "site", "public_instructor", ".freebuff", "__pycache__"}
    out = []
    for p in ROOT.rglob("*.md"):
        if skip_parts & set(p.parts):
            continue
        out.append(p)
    return out


def check_links() -> None:
    for p in md_files():
        text = read(p)
        for m in MD_LINK_RE.finditer(text):
            target = m.group(1).split("#")[0]
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not target:
                continue
            resolved = (p.parent / target).resolve()
            if not resolved.exists():
                err(f"{p.relative_to(ROOT)}: broken link -> {target}")


# ---------- catalog ----------

def check_lecture_count() -> None:
    n = len([p for p in (ROOT / "lectures").glob("lecture-*") if p.is_dir()])
    if n != 32:
        err(f"expected 32 lecture folders, found {n}")


def check_catalog() -> None:
    cat = ROOT / "case-studies" / "CATALOG.md"
    text = read(cat)
    student, _ = case_files()
    for f in student:
        sid = f.stem
        if sid not in text:
            err(f"CATALOG.md is missing case {sid}")


# ---------- main ----------

def check_case_count(cases: dict[str, dict]) -> None:
    """Both sides must carry exactly the same contiguous id range
    cs-001 .. cs-NNN, where NNN is the highest case actually present —
    metadata-driven, so appended cases extend the corpus without edits."""
    sides = ("student", "instructor")
    present = [set(cases.get(s, {})) for s in sides]
    if not present[0]:
        return
    n_max = max(int(sid.split("-")[1]) for sid in present[0])
    expected = {f"cs-{i:03d}" for i in range(1, n_max + 1)}
    for side, have in zip(sides, present):
        missing = sorted(expected - have)
        extra = sorted(have - expected)
        if missing:
            err(
                f"missing {side} case files ({len(missing)}): "
                + ", ".join(missing[:8])
                + (" ..." if len(missing) > 8 else "")
            )
        if extra:
            err(
                f"unexpected {side} case files: " + ", ".join(extra[:8])
            )
        if have != expected:
            err(
                f"{side} case ids are not the contiguous range "
                f"cs-001..cs-{n_max:03d} (count {len(have)})"
            )


def main() -> int:
    check_required_files()
    check_lecture_count()
    cases = check_cases()
    check_case_count(cases)
    check_distribution(cases)
    check_lecture_plans(cases)
    check_learning_design(cases)
    check_examples()
    check_solutions_runnable()
    check_pack()
    check_links()
    check_catalog()

    if errors:
        print(f"VALIDATION FAILED — {len(errors)} error(s):")
        for e in errors:
            print("  ERROR:", e)
    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print("  WARN:", w)
    if not errors:
        n = len(cases.get("student", {}))
        print(f"Validation passed: 32 lectures, {n} paired case studies, links OK, catalog OK.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
