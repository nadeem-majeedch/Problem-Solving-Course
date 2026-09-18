#!/usr/bin/env python3
"""Build the instructor distribution into public_instructor/.

Everything the public site has, plus case solutions and all answer keys.
NOT for public deployment. See docs/instructor-guide.md.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_site as public  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public_instructor"

INSTRUCTOR_SECTIONS = [
    "case-studies/instructor",
    "quizzes/keys",
    "assignments/keys",
    "labs/keys",
    "projects/keys",
    "activities/keys",
]


def render_dir_section(section: str) -> None:
    src = ROOT / section
    if not src.exists():
        return
    files = sorted(src.glob("*.md"))
    if not files:
        return
    for f in files:
        md = f.read_text(encoding="utf-8")
        title, rest = public.strip_h1(md) or (f.stem, md)
        title = title or f.stem
        body = public._render.render_markdown(public.rewrite_links(f, rest))
        # Pages land two levels below OUT: instructor/<section>/file.html.
        # rewrite_links emits hrefs relative to where the source page would
        # live in the PUBLIC build (one level above the instructor pages),
        # so normalise every relative href (strip its leading ../) and
        # re-prefix the correct ../../ for the deeper instructor location.
        body = re.sub(r'(href=")(?!https?:|/|#)(?:\.\./)*', r'\1../../', body)
        sb = (
            '<div class="side-group"><div class="side-heading">Instructor</div>'
            '<a class="side-link" href="../../catalog.html">Catalog</a>'
            "</div>"
        )
        dst = OUT / "instructor" / section.replace("case-studies/instructor", "case-solutions").replace("/", "-")
        public.write(dst / (f.stem + ".html"), public.page(title, body, sb, root="../../"))


def copy_raw_instructor() -> None:
    mapping = [
        ("lectures", "lectures"),
        ("case-studies/instructor", "case-studies/instructor"),
        ("quizzes/keys", "quizzes/keys"),
        ("assignments/keys", "assignments/keys"),
        ("labs/keys", "labs/keys"),
        ("projects/keys", "projects/keys"),
        ("activities/keys", "activities/keys"),
        ("docs/instructor-reports", "docs/instructor-reports"),
        ("slides/decks", "slides/decks"),
    ]
    for src, dst in mapping:
        s = ROOT / src
        if s.exists():
            shutil.copytree(s, OUT / dst, dirs_exist_ok=True)


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # Reuse the public builders, pointed at the instructor output.
    public.OUT = OUT
    public.build_docs()
    public.build_lectures()
    # Instructor distribution additionally renders the teaching notes.
    for lecture_dir in sorted((ROOT / "lectures").glob("lecture-*")):
        tn = lecture_dir / "teaching-notes.md"
        if not tn.exists():
            continue
        n = int(lecture_dir.name.split("-")[1])
        md = tn.read_text(encoding="utf-8")
        title, rest = public.strip_h1(md) or ("Teaching notes", md)
        body = public._render.render_markdown(public.rewrite_links(tn, rest))
        public.write(
            OUT / "lectures" / f"lecture-{n:02d}-teaching-notes.html",
            public.page(title, body, public.lecture_sidebar(n, current="teaching-notes", available={"plan", "teaching-notes"})),
        )
    public.build_cases()
    public.build_sections()
    public.build_catalog()
    public.build_index()
    public.build_slides()
    # Search runs over the whole instructor distribution, so instructors can
    # find solutions by topic; this page is never part of the public build.
    public.build_search()

    for section in INSTRUCTOR_SECTIONS:
        render_dir_section(section)
    copy_raw_instructor()
    shutil.copytree(ROOT / "assets" / "css", OUT / "assets", dirs_exist_ok=True)

    n = sum(1 for _ in OUT.rglob("*.html"))
    print(f"public_instructor/ built: {n} pages + raw markdown for LMS upload.")
    print("NOT for public deployment - see docs/instructor-guide.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
