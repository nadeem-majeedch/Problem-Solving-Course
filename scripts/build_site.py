#!/usr/bin/env python3
"""Build the public student site into site/.

Publishes every student-facing section: docs, lecture plans, student case
studies, assignments, rubrics, projects, labs, activities, quizzes (without
keys), and resources.

Never publishes: case-studies/instructor/, any keys/ directory, or any text
matching instructor-only solution markers. The leak check at the end of the
build fails hard if such material reaches the output — security comes from
exclusion at build time, not from directory obscurity.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import render as _render  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site"


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

STUDENT_SECTIONS = ["assignments", "projects", "labs", "activities", "quizzes", "resources"]

# Top-nav section marker for each docs page / section ("" = no marker).
DOC_CURRENT = {
    "course-overview.md": "course",
    "learning-outcomes.md": "course",
    "teaching-methodology.md": "course",
    "assessment-plan.md": "course",
    "course-outline.md": "outline",
    "glossary.md": "outline",
    "faq.md": "outline",
    "resources.md": "course",
    "index.md": "course",
    "instructor-guide.md": "course",
}
SECTION_CURRENT = {
    "labs": "course",
    "quizzes": "course",
    "assignments": "course",
    "projects": "course",
    "activities": "course",
    "resources": "course",
    "docs": "course",
}

NAV_DOCS = [
    ("index.md", "Home"),
    ("course-overview.md", "Course Overview"),
    ("learning-outcomes.md", "Learning Outcomes"),
    ("course-outline.md", "Course Outline"),
    ("teaching-methodology.md", "Teaching Methodology"),
    ("assessment-plan.md", "Assessment Plan"),
    ("instructor-guide.md", "Instructor Guide"),
    ("resources.md", "Resources"),
    ("glossary.md", "Glossary"),
    ("faq.md", "FAQ"),
    ("deployment.md", "Deployment"),
    ("case-review.md", "Case Review"),
    ("topic-coverage-heatmap.md", "Topic Heatmap"),
    ("handover-report.md", "Handover Report"),
    ("final-audit-report.md", "Final Audit"),
]

PAGE_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Problem Solving: CS &amp; DS</title>
<link rel="stylesheet" href="{root}assets/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <a class="brand" href="{root}index.html">Problem Solving — CS &amp; DS</a>
  <button id="nav-toggle" class="nav-toggle" aria-expanded="false" aria-controls="top-nav">Menu</button>
  <nav id="top-nav" class="top-nav" aria-label="Main">
    <a href="{root}docs/course-overview.html"{cur_course}>Course</a>
    <a href="{root}docs/course-outline.html"{cur_outline}>Outline</a>
    <a href="{root}catalog.html"{cur_cases}>Cases</a>
    <a href="{root}lectures/lecture-01.html"{cur_lec}>Lectures</a>
    <a href="{root}search.html"{cur_search}>Search</a>
  </nav>
</header>
<div class="layout">
  <nav class="sidebar" aria-label="Section">
{sidebar}
  </nav>
  <main id="main" class="content">
{body}
  </main>
</div>
<footer class="site-footer">
  <p>Problem Solving — Computer Science &amp; Data Science · CC BY 4.0 (content), MIT (tooling) · <a href="{root}index.html">Handbook</a> · <a href="{root}catalog.html">Case catalog</a></p>
</footer>
<script>
(function () {{
  var btn = document.getElementById('nav-toggle');
  var nav = document.getElementById('top-nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function () {{
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }});
}})();
</script>
</body>
</html>
"""

_LEAK_PATTERNS = [
    re.compile(r"Reference solution", re.I),
    re.compile(r"Reveal script", re.I),
    re.compile(r"Reasoning walkthrough", re.I),
]


def page(title: str, body: str, sidebar: str, root: str = "../", current: str = "") -> str:
    """Wrap rendered HTML in the site template.

    ``current`` names the top-nav entry to mark with aria-current="page"
    (one of: course, outline, cases, lec, search) so keyboard and screen
    -reader users always know which section they are in.
    """
    cur = {k: "" for k in ("cur_course", "cur_outline", "cur_cases", "cur_lec", "cur_search")}
    if current:
        cur["cur_" + current] = ' aria-current="page"'
    # strip_h1 removed the document H1 for the <title>; restore it at the
    # top of the content so every page has exactly one top-level heading.
    if "<h1" not in body:
        body = f"<h1>{_esc(title)}</h1>\n" + body
    return PAGE_TMPL.format(title=title, body=body, sidebar=sidebar, root=root, **cur)


def write(path: Path, html_text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html_text, encoding="utf-8")


def strip_h1(md_text: str) -> tuple[str | None, str]:
    lines = md_text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return line[2:].strip(), "\n".join(lines[:i] + lines[i + 1 :])
    return None, md_text


def h1_title(md_text: str) -> str:
    t, _ = strip_h1(md_text)
    return t or ""


# ---------- link rewriting ----------

SECTIONS_HTML = {"assignments", "projects", "labs", "activities", "quizzes", "resources", "docs"}


LECTURE_FILES = {  # repo filename -> page label (public files only)
    "plan": "Plan",
    "notes": "Notes",
    "examples": "Examples",
    "quiz": "Quiz",
}
# teaching-notes.md is instructor-only and must never be rendered publicly.
LECTURE_PUBLIC_STEMS = set(LECTURE_FILES)


def lecture_page_stem(lecture_dir: Path, md_file: Path) -> str:
    """Flat site page name for a lecture file, e.g. lecture-03-notes."""
    n = lecture_dir.name.split("-")[1]
    stem = md_file.stem
    return f"lecture-{n}" if stem == "plan" else f"lecture-{n}-{stem}"


def lecture_page_title(md_file: Path, fallback: str) -> str:
    return LECTURE_FILES.get(md_file.stem, fallback)


def html_path_for(repo_rel: Path) -> str | None:
    """Map a repo-relative .md path to its site-root-relative .html path."""
    parts = repo_rel.parts
    if repo_rel == Path("case-studies/CATALOG.md"):
        return "catalog.html"
    if repo_rel == Path("CONTRIBUTING.md"):
        return "docs/contributing.html"
    # Generated data files ship verbatim under docs/ (no .html rewrite).
    if len(parts) >= 2 and parts[0] == "docs" and repo_rel.suffix in {".csv", ".svg", ".png"}:
        return "docs/" + "/".join(parts[1:])
    if len(parts) >= 3 and parts[0] == "case-studies" and parts[1] == "student":
        return "cases/" + repo_rel.stem + ".html"
    if len(parts) >= 3 and parts[0] == "lectures" and parts[1].startswith("lecture-"):
        return "lectures/" + lecture_page_stem(Path("lectures/" + parts[1]), Path(parts[2])) + ".html"
    if len(parts) == 2 and parts[0] in SECTIONS_HTML:
        return parts[0] + "/" + parts[1][:-3] + ".html"
    if len(parts) == 1 and parts[0] == "docs-index-placeholder":
        return "index.html"
    return None


def rewrite_links(src_md: Path, text: str) -> str:
    """Rewrite internal .md links of a source file to site .html links."""

    def repl(m: re.Match) -> str:
        label, target, frag = m.group(1), m.group(2), m.group(3) or ""
        if target.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        resolved = (src_md.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            return m.group(0)  # outside the repo (generated paths) - leave as-is
        site_path = html_path_for(resolved.relative_to(ROOT))
        if site_path is None:
            return m.group(0)  # no site equivalent (e.g., anchors-only links)
        # rewrite to the site-relative href of the target page
        rel = _posix_rel(src_md, site_path)
        return f"[{label}]({rel}{frag})"

    return re.sub(r"\[([^\]]+)\]\(([^)#]+)(#[^)]*)?\)", repl, text)


def _posix_rel(src_md: Path, site_path: str) -> str:
    import posixpath

    src_site = site_out_path(src_md)
    if src_site is None:
        return site_path
    return posixpath.relpath(site_path, posixpath.dirname(src_site))


def site_out_path(src_md: Path) -> str | None:
    try:
        repo_rel = src_md.resolve().relative_to(ROOT)
    except ValueError:
        return None
    if repo_rel == Path("docs/index.md"):
        return "index.html"
    p = html_path_for(repo_rel)
    return p


# ---------- sidebars ----------

def docs_sidebar(current: str, prefix: str = "") -> str:
    rows = []
    # The handbook index is rendered at the site root (docs/index.md →
    # index.html), so its href depends on which copy of the sidebar is built.
    home_href = "index.html" if prefix == "docs/" else "../index.html"
    for fname, label in NAV_DOCS:
        href = home_href if fname == "index.md" else prefix + fname.replace(".md", ".html")
        cls = "side-link current" if fname == current else "side-link"
        rows.append(f'<a class="{cls}" href="{href}">{label}</a>')
    return '<div class="side-group"><div class="side-heading">Handbook</div>' + "\n".join(rows) + "</div>"


def lecture_sidebar(n: int, current: str = "plan", available: set[str] | None = None) -> str:
    available = available or {"plan"}
    rows = []
    for i in range(1, 33):
        cls = "side-link current" if i == n and current == "plan" else "side-link"
        rows.append(f'<a class="{cls}" href="lecture-{i:02d}.html">Lecture {i:02d}</a>')
    out = ['<div class="side-group"><div class="side-heading">Lectures</div>' + "\n".join(rows) + "</div>"]
    pages = []
    for stem, label in LECTURE_FILES.items():
        if stem not in available:
            continue
        href = f"lecture-{n:02d}.html" if stem == "plan" else f"lecture-{n:02d}-{stem}.html"
        # The "This lecture" group only lists this lecture's pages, so the
        # current-page test needs no lecture comparison.
        cls = "side-link current" if current == stem else "side-link"
        pages.append(f'<a class="{cls}" href="{href}">{label}</a>')
    out.append('<div class="side-group"><div class="side-heading">This lecture</div>' + "\n".join(pages) + "</div>")
    return "\n".join(out)


def section_sidebar(section: str, files: list[Path], current: Path, root_prefix: str) -> str:
    rows = []
    for f in files:
        cls = "side-link current" if f == current else "side-link"
        href = root_prefix + section + "/" + f.stem + ".html"
        rows.append(f'<a class="{cls}" href="{href}">{h1_title(f.read_text(encoding="utf-8")) or f.stem}</a>')
    return (
        '<div class="side-group"><div class="side-heading">'
        + section.capitalize()
        + "</div>"
        + "\n".join(rows)
        + "</div>"
    )


def cases_sidebar() -> str:
    return (
        '<div class="side-group"><div class="side-heading">Cases</div>'
        '<a class="side-link" href="../catalog.html">Full catalog</a>'
        '<a class="side-link" href="../docs/course-outline.html">By lecture</a>'
        "</div>"
    )


# ---------- builders ----------

def build_docs() -> None:
    for fname, _ in NAV_DOCS:
        src = ROOT / "docs" / fname
        md = src.read_text(encoding="utf-8")
        title, rest = strip_h1(md) or (fname, md)
        title = title or fname
        body = _render.render_markdown(rewrite_links(src, rest))
        if fname == "index.md":
            continue  # rendered to site root by build_index
        out_path = OUT / "docs" / (fname[:-3] + ".html")
        write(out_path, page(title, body, docs_sidebar(fname), current=DOC_CURRENT.get(fname, "course")))
    # The topic-coverage heatmap page (public: counts and tiers only) and
    # its companion data files. Instructor-only audit reports deliberately
    # live in docs/instructor-reports/ — never built, never listed.
    hm = ROOT / "docs" / "topic-coverage-heatmap.md"
    md = hm.read_text(encoding="utf-8")
    title, rest = strip_h1(md) or ("Topic-Coverage Heatmap", md)
    body = _render.render_markdown(rewrite_links(hm, rest))
    write(OUT / "docs" / "topic-coverage-heatmap.html",
          page(title, body, docs_sidebar("topic-coverage-heatmap.md"), current="course"))
    (OUT / "docs" / "topic-coverage-heatmap.csv").write_text(
        (ROOT / "docs" / "topic-coverage-heatmap.csv").read_text(encoding="utf-8"),
        encoding="utf-8")
    assets_src = ROOT / "docs" / "assets"
    if assets_src.exists():
        shutil.copytree(assets_src, OUT / "docs" / "assets", dirs_exist_ok=True)
    # CONTRIBUTING.md is linked from the handbook; ship it as a site page.
    src = ROOT / "CONTRIBUTING.md"
    md = src.read_text(encoding="utf-8")
    title, rest = strip_h1(md) or ("Contributing", md)
    body = _render.render_markdown(rewrite_links(src, rest))
    write(OUT / "docs" / "contributing.html", page(title, body, docs_sidebar("contributing.html"), current="course"))

def build_lectures() -> None:
    for lecture_dir in sorted((ROOT / "lectures").glob("lecture-*")):
        n = int(lecture_dir.name.split("-")[1])
        files = [p for p in sorted(lecture_dir.glob("*.md")) if p.stem in LECTURE_PUBLIC_STEMS]
        available = {p.stem for p in files}
        for md_file in files:
            md = md_file.read_text(encoding="utf-8")
            title, rest = strip_h1(md) or ("", md)
            title = title or lecture_page_title(md_file, lecture_dir.name)
            body = _render.render_markdown(rewrite_links(md_file, rest))
            stem = lecture_page_stem(lecture_dir, md_file)
            sb = lecture_sidebar(n, current=md_file.stem, available=available)
            write(OUT / "lectures" / (stem + ".html"), page(title, body, sb, current="lec"))


def build_cases() -> None:
    for f in sorted((ROOT / "case-studies" / "student").glob("cs-*.md")):
        md = f.read_text(encoding="utf-8")
        title, rest = strip_h1(md) or (f.stem, md)
        body = _render.render_markdown(rewrite_links(f, rest))
        write(OUT / "cases" / (f.stem + ".html"), page(title, body, cases_sidebar(), current="cases"))


def build_sections() -> None:
    for section in STUDENT_SECTIONS:
        src_dir = ROOT / section
        files = sorted(p for p in src_dir.glob("*.md"))
        for f in files:
            md = f.read_text(encoding="utf-8")
            title, rest = strip_h1(md) or (f.stem, md)
            body = _render.render_markdown(rewrite_links(f, rest))
            sb = section_sidebar(section, files, f, root_prefix="../")
            write(OUT / section / (f.stem + ".html"), page(title, body, sb, current=SECTION_CURRENT.get(section, "")))


def build_slides() -> None:
    """Copy the generated slide decks into the public site (student-facing).

    The decks keep their repository path (slides/decks/…) so every link —
    including the landing page and slides/README.md — stays valid.
    """
    src = ROOT / "slides" / "decks"
    if not src.exists():
        print("note: slides/decks missing — run scripts/gen_slides.py first", file=sys.stderr)
        return
    shutil.copytree(src, OUT / "slides" / "decks", dirs_exist_ok=True)


def build_catalog() -> None:
    src = ROOT / "case-studies" / "CATALOG.md"
    md = src.read_text(encoding="utf-8")
    title, rest = strip_h1(md) or ("Case-Study Catalog", md)
    body = _render.render_markdown(rewrite_links(src, rest))
    rows = [
        '<a class="side-link" href="docs/course-outline.html" aria-current="page">Course Outline</a>',
        '<a class="side-link" href="docs/teaching-methodology.html">Methodology</a>',
    ]
    sb = '<div class="side-group"><div class="side-heading">Course</div>' + "\n".join(rows) + "</div>"
    write(OUT / "catalog.html", page(title, body, sb, root="", current="cases"))


# ---------- search index + search page ----------

def _searchable_text(html_text: str) -> str:
    """Visible text of a rendered page (tags stripped, whitespace squeezed)."""
    text = re.sub(r"<script.*?</script>", " ", html_text, flags=re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _snippet(text: str, pos: int, width: int = 160) -> str:
    start = max(0, pos - width // 2)
    return ("…" if start else "") + text[start : pos + width // 2].strip() + "…"


def build_search() -> None:
    """Write pages.json (URL -> title + visible text) and search.html.

    The search is a small dependency-free client-side script; the index
    contains only text the student could already see on the page, so it
    leaks nothing.
    """
    index: dict[str, dict[str, str]] = {}
    for p in sorted(OUT.rglob("*.html")):
        rel = p.relative_to(OUT).as_posix()
        if rel in EXCLUDED_FROM_SEARCH:
            continue
        html_text = p.read_text(encoding="utf-8")
        m = re.search(r"<title>(.*?) — Problem Solving", html_text)
        title = m.group(1) if m else rel
        text = _searchable_text(html_text)
        # Drop boilerplate that would otherwise match every query.
        for noise in ("Skip to content Main nav", "Problem Solving — Computer Science & Data Science"):
            text = text.replace(noise, " ")
        index[rel] = {"t": title, "x": text}
    index_data = json.dumps(index, ensure_ascii=False)
    search_html = SEARCH_TMPL.replace("__INDEX__", index_data)
    write(OUT / "search.html", search_html)
    (OUT / "pages.json").write_text(index_data, encoding="utf-8")


SEARCH_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Search — Problem Solving: CS &amp; DS</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <a class="brand" href="index.html">Problem Solving — CS &amp; DS</a>
  <nav class="top-nav" aria-label="Main">
    <a href="docs/course-overview.html">Course</a>
    <a href="docs/course-outline.html">Outline</a>
    <a href="catalog.html">Cases</a>
    <a href="lectures/lecture-01.html">Lectures</a>
    <a href="search.html" aria-current="page">Search</a>
  </nav>
</header>
<main id="main" class="content search-page">
<h1>Search the course</h1>
<p>Searches every public page of this site — lectures, case studies, labs,
quizzes, assignments, projects, activities, and the handbook. All matching
happens in your browser; no data leaves your machine.</p>
<form class="search-form" role="search" onsubmit="return false">
  <label for="q" class="side-heading">Search words</label>
  <input id="q" class="search-box" type="search" autocomplete="off"
         placeholder="e.g. binary search, cs-017, debugging, greedy">
</form>
<p id="status" class="search-status" role="status" aria-live="polite">Ready.</p>
<ul id="results" class="results"></ul>
</main>
<footer class="site-footer">
  <p>Problem Solving — Computer Science &amp; Data Science · CC BY 4.0 (content), MIT (tooling) · <a href="index.html">Handbook</a> · <a href="catalog.html">Case catalog</a></p>
</footer>
<script>
(function () {
  "use strict";
  var INDEX = __INDEX__;
  var BOX = document.getElementById("q");
  var STATUS = document.getElementById("status");
  var OUT_ = document.getElementById("results");
  function esc(s) {
    return s.replace(/[&<>]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c];
    });
  }
  function find(terms) {
    var hits = [];
    for (var url in INDEX) {
      if (!Object.prototype.hasOwnProperty.call(INDEX, url)) continue;
      var doc = INDEX[url];
      var hay = (doc.t + " " + doc.x).toLowerCase();
      var score = 0, ok = true;
      for (var i = 0; i < terms.length; i++) {
        var pos = hay.indexOf(terms[i]);
        if (pos === -1) { ok = false; break; }
        score += doc.t.toLowerCase().indexOf(terms[i]) !== -1 ? 10 : 1;
      }
      if (ok) hits.push([score, url, doc]);
    }
    hits.sort(function (a, b) { return b[0] - a[0]; });
    return hits;
  }
  function snippet(doc, terms) {
    var x = doc.x;
    var best = -1;
    for (var i = 0; i < terms.length; i++) {
      var pos = x.toLowerCase().indexOf(terms[i]);
      if (pos !== -1 && (best === -1 || pos < best)) best = pos;
    }
    if (best === -1) return "";
    var start = Math.max(0, best - 80);
    var frag = x.slice(start, best + 120);
    var low = frag.toLowerCase();
    for (var j = 0; j < terms.length; j++) {
      var at = low.indexOf(terms[j]);
      while (at !== -1) {
        frag = frag.slice(0, at) + "<mark>" + frag.slice(at, at + terms[j].length) + "</mark>" + frag.slice(at + terms[j].length);
        low = frag.toLowerCase();
        at = low.indexOf(terms[j], at + 5 + terms[j].length);
      }
    }
    return (start ? "…" : "") + frag + "…";
  }
  function run() {
    var raw = BOX.value.trim().toLowerCase();
    OUT_.innerHTML = "";
    var terms = raw.split(/\\s+/).filter(Boolean);
    if (!terms.length) { STATUS.textContent = "Ready."; return; }
    if (terms.length > 8) terms = terms.slice(0, 8);
    var hits = find(terms);
    if (!hits.length) {
      STATUS.textContent = "No pages matched all words. Try fewer or different words.";
      return;
    }
    STATUS.textContent = hits.length + " page" + (hits.length === 1 ? "" : "s") + " matched.";
    var frag = document.createDocumentFragment();
    for (var i = 0; i < Math.min(hits.length, 40); i++) {
      var li = document.createElement("li");
      li.innerHTML = '<a href="' + hits[i][1] + '">' + esc(hits[i][2].t) + "</a>" +
        '<span class="r-snippet">' + snippet(hits[i][2], terms) + "</span>";
      frag.appendChild(li);
    }
    OUT_.appendChild(frag);
  }
  var timer = null;
  BOX.addEventListener("input", function () {
    if (timer) clearTimeout(timer);
    timer = setTimeout(run, 150);
  });
  run(); // honour a ?q= deep link (prefill only; typing still searches live)
  var pre = new URLSearchParams(location.search).get("q");
  if (pre) { BOX.value = pre; run(); }
})();
</script>
</body>
</html>
"""

# Searchable public sections; teaching material never enters the index
# (it is not built into site/ at all — see the leak check below).
EXCLUDED_FROM_SEARCH: set[str] = set()


def build_index() -> None:
    """Render docs/index.md into the landing page, adding hero and grids."""
    src = ROOT / "docs" / "index.md"
    md = src.read_text(encoding="utf-8")
    title, rest = strip_h1(md) or ("Home", md)
    body = _render.render_markdown(rewrite_links(src, rest))
    n_cases = len(list((ROOT / "case-studies" / "student").glob("cs-*.md")))
    hero = (
        '<div class="hero">'
        '<p class="tagline">A complete 32-lecture course in computational '
        "thinking: every session is built around live case studies — students "
        "get five minutes to attack a real problem, then the class dissects "
        "the solution and its alternatives together.</p>"
        '<p class="audience">Designed for 1st–3rd-semester Computer Science '
        "and Data Science students; no prior programming required.</p>"
        '<ul class="hero-stats">'
        "<li>32 lectures × 2 h</li>"
        f"<li>{n_cases} case studies</li>"
        "<li>12 labs · 8 quizzes · 6 assignments · 3 projects</li>"
        "</ul>"
        '<p class="cta-row">'
        '<a class="btn" href="lectures/lecture-01.html">Start with Lecture 01</a> '
        '<a class="btn ghost" href="docs/course-overview.html">Course overview</a> '
        '<a class="btn ghost" href="catalog.html">Browse all cases</a>'
        "</p>"
        "</div>"
    )
    body = hero + body + lecture_grid_html()
    sb = docs_sidebar("index.md", prefix="docs/")
    write(OUT / "index.html", page(title, body, sb, root="", current="course"))


def lecture_grid_html() -> str:
    """Hero, stats, goals, the 32-lecture grid, and materials links.

    Everything is derived from course-outline.md (single source of truth)
    plus the case catalog, so the landing page cannot drift from the
    curriculum.
    """
    outline = (ROOT / "docs" / "course-outline.md").read_text(encoding="utf-8")
    blocks = re.findall(
        r"## (Block [IVX]+ — [^\n]+)\n\n([^#]+?)\n(\| Lec \|[^\n]+\|\n\| --- \|[^\n]+\|\n(?:\|[^\n]+\n)+)",
        outline,
    )
    n_cases = len(list((ROOT / "case-studies" / "student").glob("cs-*.md")))
    parts: list[str] = []
    total = 0
    for head, intro, table in blocks:
        bm = re.match(r"Block ([IVX]+) — ([^(]+)\((Lectures [0-9–-]+)\)", head)
        if not bm:
            continue
        bname, theme, span = bm.group(1).strip(), bm.group(2).strip(), bm.group(3).strip()
        parts.append(f'<section class="block-head"><h2 id="block-{bname.lower()}">{bname} · {span}</h2><p>{_esc(theme)}</p></section>')
        rows = re.findall(
            r"\| \[(\d+)\]\([^)]*\) \| ([^|]+) \| cs-(\d+) – cs-(\d+) \| ([^|]+) \|",
            table,
        )
        lis = []
        for num, t, c1, c2, span_txt in rows:
            total += 1
            lis.append(
                f'<li><a href="lectures/lecture-{int(num):02d}.html">'
                f'<span class="lecture-num">Lecture {int(num):02d}</span>'
                f'<span class="lecture-title">{_esc(t.strip())}</span>'
                f'<span class="lecture-meta">Cases cs-{c1}–cs-{c2}</span>'
                f"</a></li>"
            )
        parts.append(f'<ul class="lecture-grid">' + "".join(lis) + "</ul>")
    if total != 32:
        raise SystemExit(f"landing page: expected 32 lecture rows in course-outline.md, found {total}")

    goals = (
        '<section><h2 id="learning-goals">Learning goals</h2>'
        "<p>Graduates of this course can turn a messy problem into a method:</p>"
        "<ul>"
        "<li>Analyse a problem — inputs, outputs, constraints, assumptions, edge cases.</li>"
        "<li>Decompose it, design an algorithm, and express it as pseudocode or a flowchart.</li>"
        "<li>Trace, debug, and test before trusting a solution.</li>"
        "<li>Reason about efficiency and compare alternative approaches honestly.</li>"
        "<li>Apply searching, sorting, recursion, greedy and dynamic-programming thinking, graphs, and simulation to real data-oriented problems.</li>"
        "</ul></section>"
    )
    materials = (
        '<section><h2 id="materials">Learning materials</h2>'
        '<ul class="materials-grid">'
        '<li><a href="catalog.html"><span class="m-title">Case-study catalog</span>'
        f'<span class="m-desc">All {n_cases} cases by lecture and difficulty.</span></a></li>'
        '<li><a href="labs/lab-01.html"><span class="m-title">Labs</span><span class="m-desc">12 hands-on machine sessions.</span></a></li>'
        '<li><a href="quizzes/quiz-01.html"><span class="m-title">Quizzes</span><span class="m-desc">8 self-check quizzes (answers discussed in class).</span></a></li>'
        '<li><a href="assignments/assignment-01.html"><span class="m-title">Assignments</span><span class="m-desc">6 graded assignments with rubrics.</span></a></li>'
        '<li><a href="projects/project-a.html"><span class="m-title">Projects</span><span class="m-desc">3 project options with proposal template and rubric.</span></a></li>'
        '<li><a href="activities/README.html"><span class="m-title">In-class activities</span><span class="m-desc">Case relay, complexity duel, sketch-that-flow.</span></a></li>'
        '<li><a href="resources/python-setup.html"><span class="m-title">Resources</span><span class="m-desc">Python setup and pseudocode style guide.</span></a></li>'
        '<li><a href="slides/decks/index.html"><span class="m-title">Slide decks</span><span class="m-desc">Projection-ready decks for all 32 lectures.</span></a></li>'
        "</ul></section>"
    )
    return "".join(parts) + goals + materials


# ---------- leak check ----------

def leak_check() -> int:
    problems: list[str] = []
    for p in OUT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(OUT).as_posix()
        parts = p.relative_to(OUT).parts
        if "instructor" in parts or "keys" in parts or "teaching-notes" in rel:
            problems.append(f"LEAK (path): {rel}")
            continue
        if p.suffix in {".html", ".md", ".txt", ".css"}:
            text = p.read_text(encoding="utf-8", errors="replace")
            for pat in _LEAK_PATTERNS:
                m = pat.search(text)
                if m:
                    problems.append(f"LEAK (text {pat.pattern!r} at ...{text[max(0,m.start()-40):m.end()+40]!r}): {rel}")
                    break
            if p.suffix == ".html":
                # Accessibility guard: a meaningful image without alt text
                # must fail the build, never reach students silently.
                for img in re.findall(r"<img\b[^>]*>", text):
                    if not re.search(r"\balt=\"", img):
                        problems.append(f"A11Y (img missing alt): {rel}")
    for pr in problems:
        print(pr, file=sys.stderr)
    return 1 if problems else 0


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(ROOT / "assets" / "css", OUT / "assets", dirs_exist_ok=True)
    build_docs()
    build_lectures()
    build_cases()
    build_sections()
    build_catalog()
    build_index()
    build_slides()
    build_search()
    rc = leak_check()
    if rc == 0:
        n = sum(1 for _ in OUT.rglob("*.html"))
        print(f"site/ built: {n} pages (student-facing only)")
    else:
        print("Public build FAILED leak check — instructor material detected.", file=sys.stderr)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
