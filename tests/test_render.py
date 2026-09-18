import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from render import render_markdown  # noqa: E402


def test_headings_and_paragraph():
    out = render_markdown("# Title\n\nSome text here.\n")
    assert '<h1 id="title">Title</h1>' in out  # headings carry slug anchors
    assert "<p>Some text here.</p>" in out


def test_numeric_heading_alias():
    """Headings like '## 2. Title' also get a numeric alias anchor (#2),
    which is how examples.md index tables link to their sections."""
    out = render_markdown("## 2. Hello world\n")
    assert 'id="2-hello-world"' in out
    assert 'id="2"' in out
    # No alias when the heading does not start with a number.
    out2 = render_markdown("## Hello 2 world\n")
    assert 'id="hello-2-world"' in out2
    assert 'id="2"' not in out2


def test_inline_styles_and_code():
    out = render_markdown("This is **bold** and *italic* and `x = 1`.\n")
    assert "<strong>bold</strong>" in out
    assert "<em>italic</em>" in out
    assert "<code>x = 1</code>" in out
    # raw < > should be escaped
    out2 = render_markdown("Use a < b in comparisons.\n")
    assert "&lt;" in out2


def test_links():
    out = render_markdown("[docs](docs/course-overview.md)\n")
    assert '<a href="docs/course-overview.md">docs</a>' in out
    # external links preserved
    out2 = render_markdown("[x](https://example.com)\n")
    assert 'href="https://example.com"' in out2


def test_fenced_code_block_escapes():
    md = "```python\nif a < b:\n    print(a)\n```\n"
    out = render_markdown(md)
    assert "&lt;" in out
    assert "<pre><code" in out


def test_table():
    md = "| A | B |\n| --- | --- |\n| 1 | 2 |\n"
    out = render_markdown(md)
    assert "<table>" in out
    assert "<th>A</th>" in out
    assert "<td>1</td>" in out


def test_lists():
    md = "- one\n- two\n\n1. first\n2. second\n"
    out = render_markdown(md)
    assert "<ul>" in out and "<li>one</li>" in out
    assert "<ol>" in out and "<li>first</li>" in out


def test_blockquote_and_hr():
    md = "> quoted\n\n---\n"
    out = render_markdown(md)
    assert "<blockquote>" in out
    assert "<hr>" in out


def test_unclosed_fence_raises():
    import pytest

    with pytest.raises(ValueError):
        render_markdown("```python\nx = 1\n")


def test_case_title_renders():
    md = "# cs-001 — Title\n\n| Field | Value |\n| --- | --- |\n| id | cs-001 |\n"
    out = render_markdown(md)
    assert "cs-001" in out
    assert "<table>" in out
