"""Shared Markdown-to-HTML renderer for the course site builds.

Implements the small subset of Markdown used in this repository:
headings, paragraphs, bold/italic/code, fenced code blocks, tables,
bullet and numbered lists, blockquotes, and [text](target) links
(including <id> autolinks and image-free inline links only).

No third-party dependencies by design: the build must be reproducible
with a stock Python 3 interpreter.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

# Inline code / code fences must never be processed for markdown inside.
_CODE_FENCE_RE = re.compile(r"^```(\w*)\s*$")
_HEADING_RE = re.compile(r"^(#{1,4})\s+(.*)$")
_TABLE_ROW_RE = re.compile(r"^\|(.*)\|\s*$")
_TABLE_SEP_RE = re.compile(r"^\|[\s:|-]+\|\s*$")
_UL_ITEM_RE = re.compile(r"^[-*]\s+(.*)$")
_OL_ITEM_RE = re.compile(r"^\d+[.)]\s+(.*)$")
_BLOCKQUOTE_RE = re.compile(r"^>\s?(.*)$")
_HR_RE = re.compile(r"^-{3,}\s*$")

_INLINE_CODES = []
_INLINE_CODE_PLACEHOLDER = "\x00CODE{}\x00"

# Inline markdown: escape first, then apply spans.
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
_ITALIC_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
_STRIKE_RE = re.compile(r"~~(.+?)~~")
_CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
_AUTOLINK_RE = re.compile(r"&lt;((?:cs-\d{3})|(?:lecture-\d{2}))&gt;")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def _protect_code_spans(text: str) -> str:
    """Replace inline code spans with placeholders before inline parsing."""
    out = []
    pos = 0
    for m in _CODE_SPAN_RE.finditer(text):
        out.append(text[pos:m.start()])
        token = _INLINE_CODE_PLACEHOLDER.format(len(_INLINE_CODES))
        _INLINE_CODES.append(m.group(1))
        out.append(token)
        pos = m.end()
    out.append(text[pos:])
    return "".join(out)


def _render_inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = _protect_code_spans(text)
    text = _BOLD_RE.sub(r"<strong>\1</strong>", text)
    text = _ITALIC_RE.sub(r"<em>\1</em>", text)
    text = _STRIKE_RE.sub(r"<del>\1</del>", text)
    text = _AUTOLINK_RE.sub(r'<a href="#\1">\1</a>', text)
    text = _LINK_RE.sub(lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>', text)
    for i, code in enumerate(_INLINE_CODES):
        token = _INLINE_CODE_PLACEHOLDER.format(i)
        text = text.replace(token, f"<code>{html.escape(code, quote=False)}</code>")
    return text


def _split_table_row(row: str) -> list[str]:
    return [c.strip() for c in row.strip().strip("|").split("|")]


_PY_KEYWORDS = {
    "def", "return", "if", "elif", "else", "for", "while", "in", "not",
    "and", "or", "break", "continue", "None", "True", "False", "import",
    "from", "class", "lambda", "pass", "with", "as", "try", "except",
    "raise", "global", "nonlocal", "assert", "is", "del", "yield", "async", "await",
}


def _highlight_python(code: str) -> str:
    """Conservative, escape-safe Python highlighting (keywords, strings,
    comments, numbers). Operates on already-escaped text."""
    pattern = re.compile(
        r'("[^"\n]*"|\'[^\'\n]*\')'          # strings (escaped text: quotes intact)
        r"|(#[^\n]*)"                          # comments
        r"|\b(\d+\.?\d*)\b"                   # numbers
    )
    out = []
    pos = 0
    tokens: list[tuple[int, str]] = []
    for m in pattern.finditer(code):
        if m.group(1):
            tokens.append((m.start(), "p-str"))
        elif m.group(2):
            tokens.append((m.start(), "p-com"))
        else:
            tokens.append((m.start(), "p-num"))
    for start, cls in tokens:
        out.append(code[pos:start])
        end = code.find("<", start)
        # find the end of the token text (escaped entities may follow; keep it simple)
        if cls == "p-com":
            end = code.find("\n", start)
            end = len(code) if end == -1 else end
            out.append(f'<span class="{cls}">{code[start:end]}</span>')
            pos = end
            continue
        if cls == "p-str":
            q = code[start]
            end = code.find(q, start + 1)
            end = len(code) if end == -1 else end + 1
            out.append(f'<span class="{cls}">{code[start:end]}</span>')
            pos = end
            continue
        # number: consume digits/dot
        end = start
        while end < len(code) and (code[end].isdigit() or code[end] == "."):
            end += 1
        out.append(f'<span class="{cls}">{code[start:end]}</span>')
        pos = end
    out.append(code[pos:])
    code = "".join(out)
    # keywords last, on text outside spans
    parts = re.split(r'(<span class="p-(?:str|com|num)">.*?</span>)', code)
    for i, part in enumerate(parts):
        if not part.startswith("<span"):
            parts[i] = re.sub(
                r"\b(" + "|".join(sorted(_PY_KEYWORDS)) + r")\b",
                r'<span class="p-key">\1</span>', part)
    return "".join(parts)


def _render_table(rows: list[str]) -> str:
    cells = [_split_table_row(r) for r in rows]
    header = cells[0]
    if len(cells) > 1 and all(re.fullmatch(r":?-{2,}:?", c) for c in cells[1]):
        body = cells[2:]
    else:
        body = cells[1:]

    def _tr(cells_, tag):
        out = ["<tr>"]
        for c in cells_:
            out.append(f"<{tag}>{_render_inline(c)}</{tag}>")
        out.append("</tr>")
        return "".join(out)

    lines = ['<div class="table-wrap"><table>']
    if body or len(cells) > 1:
        lines.append("<thead>" + _tr(header, "th") + "</thead>")
        lines.append("<tbody>")
        for row in body:
            lines.append(_tr(row + [""] * (len(header) - len(row)), "td"))
        lines.append("</tbody>")
    lines.append("</table></div>")
    return "".join(lines)


def render_markdown(text: str) -> str:
    """Render the course Markdown subset to an HTML fragment."""
    # Reset module state so repeated renders are independent.
    _INLINE_CODES.clear()

    lines = text.splitlines()
    out: list[str] = []
    para: list[str] = []
    list_items: list[tuple[str, str]] = []  # (kind, content)
    table_rows: list[str] = []
    quote_lines: list[str] = []
    in_fence = False
    fence_lang = ""
    fence_lines: list[str] = []
    list_kind = ""

    def flush_para():
        nonlocal para
        if para:
            out.append("<p>" + _render_inline(" ".join(para)) + "</p>")
            para = []

    def flush_list():
        nonlocal list_items, list_kind
        if not list_items:
            return
        tag = "ol" if list_kind == "ol" else "ul"
        inner = "".join(f"<li>{_render_inline(c)}</li>" for _, c in list_items)
        out.append(f"<{tag}>{inner}</{tag}>")
        list_items = []
        list_kind = ""

    def flush_table():
        nonlocal table_rows
        if table_rows:
            out.append(_render_table(table_rows))
            table_rows = []

    def flush_quote():
        nonlocal quote_lines
        if quote_lines:
            out.append("<blockquote>" + render_markdown("\n".join(quote_lines)).strip() + "</blockquote>")
            quote_lines = []

    def flush_all():
        flush_para()
        flush_list()
        flush_table()
        flush_quote()

    for raw in lines:
        line = raw.rstrip("\n")

        if in_fence:
            if _CODE_FENCE_RE.match(line.strip()):
                in_fence = False
                lang = fence_lang or "text"
                code = html.escape("\n".join(fence_lines), quote=False)
                if lang == "python":
                    code = _highlight_python(code)
                out.append(f'<pre><code class="language-{lang}">{code}</code></pre>')
                fence_lines = []
            else:
                fence_lines.append(line)
            continue

        m = _CODE_FENCE_RE.match(line.strip())
        if m:
            flush_all()
            in_fence = True
            fence_lang = m.group(1)
            continue

        if _TABLE_ROW_RE.match(line):
            flush_para()
            flush_list()
            flush_quote()
            table_rows.append(line)
            continue
        if table_rows:
            flush_table()

        if _HR_RE.fullmatch(line.strip()) and not line.startswith(" "):
            flush_all()
            out.append("<hr>")
            continue

        m = _HEADING_RE.match(line)
        if m:
            flush_all()
            level = len(m.group(1))
            raw_text = m.group(2).strip()
            content = _render_inline(raw_text)
            slug = re.sub(r"[^a-z0-9]+", "-", raw_text.lower()).strip("-")
            ids = f'id="{slug}"'
            # Numeric alias anchor: documents index headings like
            # "## 2. Title ..." as [text](#2) — make both resolve.
            nm = re.match(r"(\d+)[.:]\s", raw_text)
            if nm:
                ids += f' id="{nm.group(1)}"'
            out.append(f'<h{level} {ids}>{content}</h{level}>')
            continue

        if _BLOCKQUOTE_RE.match(line):
            flush_para()
            flush_list()
            flush_table()
            qm = _BLOCKQUOTE_RE.match(line)
            quote_lines.append(qm.group(1))
            continue
        if quote_lines and line.strip() == "":
            flush_quote()

        m = _UL_ITEM_RE.match(line.strip())
        if m and not line.startswith("    "):
            flush_para()
            flush_table()
            if list_kind and list_kind != "ul":
                flush_list()
            list_kind = "ul"
            list_items.append(("ul", m.group(1)))
            continue

        m = _OL_ITEM_RE.match(line.strip())
        if m and not line.startswith("    "):
            flush_para()
            flush_table()
            if list_kind and list_kind != "ol":
                flush_list()
            list_kind = "ol"
            list_items.append(("ol", m.group(1)))
            continue

        if list_items and line.startswith("  ") and line.strip():
            # Continuation line of a list item.
            k, c = list_items[-1]
            list_items[-1] = (k, c + " " + line.strip())
            continue

        if line.strip() == "":
            flush_para()
            flush_list()
            continue

        flush_list()
        para.append(line.strip())

    if in_fence:
        raise ValueError("Unclosed code fence in markdown input")
    flush_all()
    return "\n".join(out)


def load_and_render(path: Path) -> str:
    return render_markdown(path.read_text(encoding="utf-8"))
