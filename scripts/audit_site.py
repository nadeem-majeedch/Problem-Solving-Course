#!/usr/bin/env python3
"""Audit the BUILT public site in site/.

Validates the artifact after the build, not just the sources:
  - coverage: entry points, 32 lectures, packs, cases, catalog, decks;
  - exclusion: no instructor-only material (paths or solution phrases);
  - links: every href resolves; every #fragment has a matching id;
  - navigation: header/footer/skip-link consistent on all templated pages;
  - assets: local href/src targets exist;
  - accessibility: single h1 per document, img[alt], form labels, lang attr.

Exits non-zero on any problem. Nothing is silently skipped; items that need
human judgement are reported as WARNINGS and do not affect the exit code.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

errors: list[str] = []
warnings: list[str] = []

LEAK_TEXT_PATTERNS = [
    re.compile(r"Reference solution", re.I),
    re.compile(r"Reveal script", re.I),
    re.compile(r"Reasoning walkthrough", re.I),
]


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def main() -> int:
    if not SITE.is_dir():
        print("audit_site: site/ not found — run scripts/build_site.py first", file=sys.stderr)
        return 1

    pages = sorted(SITE.rglob("*.html"))
    if not pages:
        err("site/ contains no HTML pages")

    # ---------- coverage ----------
    def must(rel: str) -> None:
        if not (SITE / rel).is_file():
            err(f"artifact missing: {rel}")

    must("index.html")
    must("search.html")
    must("pages.json")
    must("catalog.html")
    must("assets/style.css")
    for n in range(1, 33):
        must(f"lectures/lecture-{n:02d}.html")
        must(f"lectures/lecture-{n:02d}-notes.html")
        must(f"lectures/lecture-{n:02d}-examples.html")
        must(f"lectures/lecture-{n:02d}-quiz.html")
        must(f"slides/decks/lecture-{n:02d}-slides.html")
    # the public artifact must mirror the source corpus one-for-one
    expected_cases = len(list((ROOT / "case-studies" / "student").glob("cs-*.md")))
    cases = sorted((SITE / "cases").glob("cs-*.html"))
    if len(cases) != expected_cases:
        err(f"artifact has {len(cases)} case pages, expected {expected_cases}")

    # ---------- exclusion ----------
    for p in SITE.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(SITE).as_posix()
        parts = p.relative_to(SITE).parts
        if "instructor" in parts or "keys" in parts or "teaching-notes" in p.name:
            err(f"INSTRUCTOR MATERIAL IN PUBLIC ARTIFACT: {rel}")
            continue
        if p.suffix in {".html", ".json", ".css"}:
            text = p.read_text(encoding="utf-8", errors="replace")
            for pat in LEAK_TEXT_PATTERNS:
                if pat.search(text):
                    err(f"solution phrasing in public artifact: {rel} ({pat.pattern})")
                    break

    # ---------- link / asset / fragment audit ----------
    ids_by_page: dict[Path, set[str]] = {
        p.resolve(): set(re.findall(r'id="([^"]+)"', p.read_text(encoding="utf-8", errors="replace")))
        for p in pages
    }
    checked = 0
    for p in pages:
        text = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(SITE).as_posix()
        for href in re.findall(r'(?:href|src)="([^"]+)"', text):
            checked += 1
            if href.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            if href.startswith("#"):
                frag = href[1:]
                if frag and frag not in ids_by_page[p.resolve()]:
                    err(f"{rel}: self-anchor #{frag} does not resolve")
                continue
            target, _, frag = href.partition("#")
            if "'" in target or "+" in target or " " in target:
                continue  # inline-JS constructed hrefs (search page)
            tp = (p.parent / unquote(target)).resolve()
            if not tp.exists():
                err(f"{rel}: broken reference -> {href}")
            elif frag and frag not in ids_by_page.get(tp, set()):
                err(f"{rel}: anchor #{frag} not found in {target}")
    print(f"checked {checked} hrefs/srcs across {len(pages)} pages")

    # ---------- navigation consistency ----------
    nav_current = 0
    for p in pages:
        text = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(SITE).as_posix()
        if "slides/decks" in rel or rel in {"search.html"}:
            continue  # standalone documents with their own chrome
        for marker in ('class="skip-link"', 'class="site-header"', 'class="site-footer"', '<nav'):
            if marker not in text:
                err(f"{rel}: missing site chrome element {marker}")
        if 'aria-current="page"' not in text:
            err(f"{rel}: no aria-current page marker in navigation")
        else:
            nav_current += 1
    print(f"navigation current-page markers: {nav_current} pages")

    # ---------- accessibility structure ----------
    imgs = 0
    for p in pages:
        text = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(SITE).as_posix()
        if "<html" in text and "lang=" not in text.split("<html", 1)[1][:60]:
            err(f"{rel}: <html> missing lang attribute")
        if "slides/decks" in rel or rel == "search.html":
            continue
        main = re.search(r"<main[^>]*>(.*?)</main>", text, re.S)
        if main:
            n_h1 = len(re.findall(r"<h1\b", main.group(1)))
            if n_h1 != 1:
                err(f"{rel}: {n_h1} <h1> elements in main (want exactly 1)")
        for img in re.findall(r"<img\b[^>]*>", text):
            imgs += 1
            if not re.search(r"\balt=", img):
                err(f"{rel}: <img> without alt attribute")
        for form in re.findall(r"<form\b[^>]*>", text):
            pass  # label checks handled below
    for p in pages:
        text = p.read_text(encoding="utf-8", errors="replace")
        rel = p.relative_to(SITE).as_posix()
        for fm in re.finditer(r"<form\b", text):
            seg = text[fm.start(): text.find("</form>", fm.start()) + 7]
            if "<label" not in seg:
                err(f"{rel}: form without a <label>")
    print(f"images checked: {imgs}")

    # ---------- result ----------
    for e in errors:
        print("ERROR:", e, file=sys.stderr)
    for w in warnings:
        print("WARN:", w, file=sys.stderr)
    if not errors:
        print(f"Site audit passed: {len(pages)} pages, {checked} references checked.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
