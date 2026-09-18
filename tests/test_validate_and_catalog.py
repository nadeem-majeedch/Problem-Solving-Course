import shutil
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import validate  # noqa: E402
import generate_catalog  # noqa: E402
import audit_site  # noqa: E402


@pytest.fixture()
def mini_repo(tmp_path):
    """A minimal valid repo slice: one lecture, one paired case, catalog."""
    (tmp_path / "lectures" / "lecture-01").mkdir(parents=True)
    (tmp_path / "case-studies" / "student").mkdir(parents=True)
    (tmp_path / "case-studies" / "instructor").mkdir(parents=True)
    (tmp_path / "lectures" / "lecture-01" / "plan.md").write_text(
        "# Lecture 01 — Thinking in Problems\n\n"
        "## Position in the course\n\nx\n\n"
        "## Learning objectives\n\nx\n\n"
        "## Case sequence\n\ncs-001 cs-002 cs-003 cs-004\n\n"
        "## Timing plan (120 minutes)\n\nx\n\n"
        "## Board plan\n\nx\n\n"
        "## Differentiation\n\nx\n\n"
        "## Common misconceptions\n\nx\n\n"
        "## Homework and preparation\n\nx\n",
        encoding="utf-8",
    )
    student = (
        "# cs-001 — First Case\n\n"
        "| Field | Value |\n| --- | --- |\n"
        "| id | cs-001 |\n| difficulty | Beginner |\n"
        "| topics | decomposition |\n| lecture | lecture-01 |\n"
        "| estimated time | 5-minute attempt + 10-minute discussion |\n"
        "| prerequisites | none |\n"
        "| objective | solve a small instance by hand |\n"
        "| solution | held by the instructor; discussed after the attempt |\n\n"
        "## Problem\n\nDo a thing.\n\n"
        "## Examples\n\nIn: 1. Out: 2.\n\n"
        "## What to notice\n\nSomething.\n\n"
        "## Discussion starter\n\nAsk this.\n\n"
        "## Hints and extension\n\n- First nudge: read twice.\n"
    )
    instructor = (
        "# cs-001 — First Case\n\n"
        "| Field | Value |\n| --- | --- |\n"
        "| id | cs-001 |\n| difficulty | Beginner |\n"
        "| topics | decomposition |\n| lecture | lecture-01 |\n"
        "| estimated time | 5-minute attempt + 10-minute discussion |\n"
        "| prerequisites | none |\n"
        "| objective | solve a small instance by hand |\n\n"
        "## Reasoning walkthrough\n\n"
        + "word " * 50
        + "\n\n## Five-minute teaching sequence\n\nMinute 0–1 read.\n\n"
        "## Difficulty adaptation\n\nSimplify by shrinking the instance.\n\n"
        "## Reference solution (Python)\n\n```python\nx = 1\n```\n\n"
        "## Reference solution (pseudocode)\n\n```\nSET x TO 1\n```\n\n"
        "## Edge cases\n\nEmpty input.\n\n"
        "## Alternative approaches\n\nOther ways.\n\n"
        "## Common pitfalls\n\nIndexing.\n\n"
        "## Reveal script\n\nSay this.\n\n"
        "## Assessment use\n\nExit-ticket ready.\n\n"
        "## Connections\n\nLinks to cs-002.\n\n"
        "## Extension challenge\n\nTry a stranger input.\n"
    )
    for i in range(1, 5):
        sid = f"cs-{i:03d}"
        (tmp_path / "case-studies" / "student" / f"{sid}.md").write_text(
            student.replace("cs-001", sid), encoding="utf-8"
        )
        (tmp_path / "case-studies" / "instructor" / f"{sid}.md").write_text(
            instructor.replace("cs-001", sid), encoding="utf-8"
        )
    (tmp_path / "case-studies" / "CATALOG.md").write_text(
        "# Case-Study Catalog\n\ncs-001 cs-002 cs-003 cs-004\n", encoding="utf-8"
    )
    return tmp_path


def run_validator(root: Path):
    errors, warnings = [], []
    old_root = validate.ROOT
    validate.ROOT = root
    validate.errors = errors
    validate.warnings = warnings
    try:
        cases = validate.check_cases()
        validate.check_lecture_plans(cases)
    finally:
        validate.ROOT = old_root
        validate.errors, validate.warnings = [], []
    return errors, warnings


def test_mini_repo_passes(mini_repo):
    errors, _ = run_validator(mini_repo)
    assert errors == []


def test_missing_solution_detected(mini_repo):
    (mini_repo / "case-studies" / "instructor" / "cs-001.md").unlink()
    errors, _ = run_validator(mini_repo)
    assert any("cs-001" in e and "no instructor solution" in e for e in errors)


def test_bad_difficulty_detected(mini_repo):
    f = mini_repo / "case-studies" / "student" / "cs-001.md"
    f.write_text(f.read_text(encoding="utf-8").replace("Beginner", "Easy"), encoding="utf-8")
    errors, _ = run_validator(mini_repo)
    assert any("difficulty" in e for e in errors)


def test_leak_into_student_detected(mini_repo):
    f = mini_repo / "case-studies" / "student" / "cs-001.md"
    f.write_text(
        f.read_text(encoding="utf-8") + "\n## Edge cases\n\nleak\n", encoding="utf-8"
    )
    errors, _ = run_validator(mini_repo)
    assert any("instructor-only" in e for e in errors)


def test_lecture_missing_case_reference(mini_repo):
    p = mini_repo / "lectures" / "lecture-01" / "plan.md"
    p.write_text(p.read_text(encoding="utf-8").replace("cs-004", "removed"), encoding="utf-8")
    errors, _ = run_validator(mini_repo)
    assert any("cs-004" in e for e in errors)


def test_catalog_generator(mini_repo):
    old_root = generate_catalog.ROOT
    generate_catalog.ROOT = mini_repo
    try:
        rc = generate_catalog.main()
    finally:
        generate_catalog.ROOT = old_root
    assert rc == 0
    catalog = (mini_repo / "case-studies" / "CATALOG.md").read_text(encoding="utf-8")
    assert "128" not in catalog  # only 4 cases in the fixture
    for sid in ("cs-001", "cs-002", "cs-003", "cs-004"):
        assert sid in catalog


# ---------- solution execution checks ----------


def run_solution_checks(root: Path):
    errors, warnings = [], []
    old_root = validate.ROOT
    validate.ROOT = root
    validate.errors = errors
    validate.warnings = warnings
    try:
        validate.check_solutions_runnable()
    finally:
        validate.ROOT = old_root
        validate.errors, validate.warnings = [], []
    return errors, warnings


def test_solutions_pass_on_clean_fixture(mini_repo):
    errors, _ = run_solution_checks(mini_repo)
    assert errors == []


def test_stdin_solution_detected(mini_repo):
    f = mini_repo / "case-studies" / "instructor" / "cs-001.md"
    text = f.read_text(encoding="utf-8").replace("x = 1", "name = input()")
    f.write_text(text, encoding="utf-8")
    errors, _ = run_solution_checks(mini_repo)
    assert any("stdin" in e for e in errors)


def test_nondeterministic_solution_detected(mini_repo):
    f = mini_repo / "case-studies" / "instructor" / "cs-001.md"
    text = f.read_text(encoding="utf-8").replace("x = 1", "print(id(object()))")
    f.write_text(text, encoding="utf-8")
    errors, _ = run_solution_checks(mini_repo)
    assert any("not deterministic" in e for e in errors)


def test_missing_python_fence_detected(mini_repo):
    f = mini_repo / "case-studies" / "instructor" / "cs-001.md"
    text = f.read_text(encoding="utf-8").replace("## Reference solution (Python)", "## Reference Python")
    f.write_text(text, encoding="utf-8")
    errors, _ = run_solution_checks(mini_repo)
    assert any("no 'Reference solution (Python)' code fence" in e for e in errors)


# ---------- learning-design checks ----------


def write_design_docs(root: Path, lo_text: str, assess_text: str) -> None:
    (root / "docs").mkdir(exist_ok=True)
    (root / "docs" / "learning-outcomes.md").write_text(lo_text, encoding="utf-8")
    (root / "docs" / "assessment-plan.md").write_text(assess_text, encoding="utf-8")


def test_learning_design_passes_complete_docs(mini_repo):
    lo = "".join(f"\n## LO{i} — Outcome {i}\n\nText.\n" for i in range(1, 11))
    assess = " ".join(f"LO{i}" for i in range(1, 11))
    write_design_docs(mini_repo, lo, assess)
    errors, warnings = [], []
    old_root = validate.ROOT
    validate.ROOT = mini_repo
    validate.errors = errors
    validate.warnings = warnings
    try:
        cases = validate.check_cases()
        validate.check_learning_design(cases)
    finally:
        validate.ROOT = old_root
        validate.errors, validate.warnings = [], []
    assert errors == []


def test_learning_design_flags_unassessed_outcome(mini_repo):
    lo = "".join(f"\n## LO{i} — Outcome {i}\n\nText.\n" for i in range(1, 11))
    assess = " ".join(f"LO{i}" for i in range(1, 10))  # LO4 missing -> also undefined
    write_design_docs(mini_repo, lo.replace("## LO4", "## LOX"), assess)
    errors, warnings = [], []
    old_root = validate.ROOT
    validate.ROOT = mini_repo
    validate.errors = errors
    validate.warnings = warnings
    try:
        cases = validate.check_cases()
        validate.check_learning_design(cases)
    finally:
        validate.ROOT = old_root
        validate.errors, validate.warnings = [], []
    assert any("LO4" in e for e in errors)  # missing definition and unassessed


# ---------- built-site audit ----------


def test_audit_fails_without_site(tmp_path):
    old = audit_site.SITE
    audit_site.SITE = tmp_path / "does-not-exist"
    try:
        assert audit_site.main() == 1
    finally:
        audit_site.SITE = old


def test_audit_fails_on_empty_site(tmp_path):
    old = audit_site.SITE
    (tmp_path / "site").mkdir()
    audit_site.SITE = tmp_path / "site"
    try:
        assert audit_site.main() == 1
    finally:
        audit_site.SITE = old
