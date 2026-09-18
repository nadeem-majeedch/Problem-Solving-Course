import shutil
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import build_site  # noqa: E402
import build_instructor  # noqa: E402

# End-to-end builds need the full repo (128 cases + 32 plans). They are
# gated so the suite stays green while content is being authored and
# activate automatically once the content phase completes.
CASES_READY = len(list((REPO / "case-studies" / "student").glob("cs-*.md"))) >= 128
LECTURES_READY = len(list((REPO / "lectures").glob("lecture-*"))) >= 32
CONTENT_READY = CASES_READY and LECTURES_READY

needs_content = pytest.mark.skipif(not CONTENT_READY, reason="course content not fully authored yet")


@pytest.fixture()
def build_env(tmp_path, monkeypatch):
    """Point both builders at a temp output dir."""
    out = tmp_path / "site"
    monkeypatch.setattr(build_site, "ROOT", REPO)
    monkeypatch.setattr(build_site, "OUT", out)
    monkeypatch.setattr(build_instructor, "OUT", out)
    monkeypatch.setattr(build_instructor, "ROOT", REPO)
    yield out


@needs_content
def test_public_build_excludes_instructor(build_env):
    out = build_env
    rc = build_site.main()
    assert rc == 0, "public build must succeed on the real repo"
    htmls = list(out.rglob("*.html"))
    assert len(htmls) > 100, "expected the full course site"
    # No instructor directory anywhere in output
    assert not (out / "instructor").exists()
    for p in out.rglob("*.html"):
        assert "instructor" not in p.parts, p


@needs_content
def test_public_build_leak_check_contents(build_env):
    out = build_env
    rc = build_site.main()
    assert rc == 0
    for p in out.rglob("*.html"):
        text = p.read_text(encoding="utf-8")
        for pat in build_site._LEAK_PATTERNS:
            assert not pat.search(text), f"leak in {p}: {pat.pattern}"


@needs_content
def test_public_build_navigation_intact(build_env):
    out = build_env
    rc = build_site.main()
    assert rc == 0
    index = (out / "index.html").read_text(encoding="utf-8")
    assert "style.css" in index, "index must link the stylesheet"
    # every docs nav page built
    for name in ("course-overview", "course-outline", "teaching-methodology",
                 "assessment-plan", "instructor-guide", "resources",
                 "glossary", "faq", "learning-outcomes"):
        assert (out / "docs" / f"{name}.html").exists(), f"missing docs page {name}"
    # catalog present
    assert (out / "catalog.html").exists()
    # case pages exist for every student case
    n_cases = len(list((REPO / "case-studies" / "student").glob("cs-*.md")))
    assert len(list((out / "cases").glob("cs-*.html"))) == n_cases


@needs_content
def test_instructor_build_contains_solutions(build_env):
    out = build_env
    # instructor build reuses the public render, then adds solutions
    rc = build_instructor.main()
    assert rc == 0
    assert (out / "instructor").exists(), "instructor build must include solutions"
    files = list((out / "instructor").rglob("cs-*.html"))
    assert files, "instructor build must include solution pages"
    n_solutions = len(list((REPO / "case-studies" / "instructor").glob("cs-*.md")))
    assert len(files) == n_solutions
