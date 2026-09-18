"""Generate projection-ready HTML slide decks for all 32 lectures.

Design decisions (see slides/README.md):

* Output: one self-contained HTML file per lecture in ``slides/decks/``
  (arrow keys / space / click advance, printable to PDF). No toolchain,
  no network, no proprietary app.
* Source of truth: the curriculum itself. Titles, objectives, worked
  examples, exit questions, case sequences and difficulties are
  extracted from ``lectures/lecture-NN/`` and ``case-studies/`` so a
  deck cannot drift from the material.
* Student/instructor separation: decks show only student-facing content
  (case prompt, examples *problem/algorithm/trace* level, discussion
  prompts, exit question). Every reveal slide is a stub pointing the
  instructor at the instructor distribution; no solution content is
  embedded. Verified Python from the worked examples is included —
  it is already published in the public build.

Regenerate with:  python scripts/gen_slides.py
"""

from __future__ import annotations

import html
import re
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pseudocode_gen import transpile  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LECTURES = ROOT / "lectures"
CASES = ROOT / "case-studies" / "student"
OUT = ROOT / "slides" / "decks"

CSS = """/* Problem Solving — CS & DS · course slide design language */
:root{--ink:#1c2430;--paper:#f7f5f0;--accent:#0f6b5c;--accent2:#b3541e;
 --soft:#e7e2d8;--code:#12202b;--codetext:#e8eef2}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{font-family:Georgia,'Times New Roman',serif;color:var(--ink);
 background:var(--paper);overflow:hidden}
.deck{height:100vh;scroll-snap-type:y mandatory;overflow-y:scroll}
.slide{height:100vh;scroll-snap-align:start;padding:6vh 7vw;display:flex;
 flex-direction:column;justify-content:center;page-break-after:always}
.slide>*{max-width:52rem}
h1{font-size:2.6rem;line-height:1.15;color:var(--accent)}
h2{font-size:1.9rem;margin-bottom:1rem;color:var(--accent);
 border-bottom:3px solid var(--soft);padding-bottom:.3rem}
h3{font-size:1.25rem;margin:.9rem 0 .4rem;color:var(--accent2)}
p,li{font-size:1.28rem;line-height:1.5}
ul,ol{margin-left:1.4rem;margin-top:.4rem}
li{margin:.35rem 0}
.small{font-size:1.02rem;color:#5a5f66}
.kicker{text-transform:uppercase;letter-spacing:.18em;font-size:.95rem;
 color:var(--accent2);margin-bottom:1rem;font-family:sans-serif}
code{font-family:'Cascadia Code',Consolas,monospace}
p code,li code{background:var(--soft);padding:.05em .3em;border-radius:4px;
 font-size:1.05em}
pre{background:var(--code);color:var(--codetext);padding:1rem 1.2rem;
 border-radius:8px;overflow:auto;margin:.6rem 0;font-size:1.02rem;
 line-height:1.45;max-width:52rem}
pre code{background:none;color:inherit}
pre .k{color:#7fd0b2}pre .s{color:#f0b27a}pre .c{color:#8aa39a;font-style:italic}
pre .n{color:#a8c7e8}pre .o{color:#d9b8ff}
table{border-collapse:collapse;margin:.6rem 0;font-size:1.1rem}
th,td{border:1.5px solid var(--ink);padding:.35rem .8rem;text-align:left}
th{background:var(--soft)}
.case{border-left:6px solid var(--accent2);background:#fff;
 padding:1rem 1.4rem;border-radius:0 8px 8px 0;margin:.8rem 0}
.case .tag{font-family:sans-serif;font-size:.85rem;letter-spacing:.12em;
 text-transform:uppercase;color:var(--accent2)}
.timer{display:inline-block;background:var(--accent);color:#fff;
 font-family:sans-serif;font-weight:bold;padding:.35rem .9rem;
 border-radius:999px;margin:.6rem 0;font-size:1.05rem}
.notes{display:none}
footer{position:fixed;bottom:1.2vh;right:2vw;font-family:sans-serif;
 font-size:.85rem;color:#8a8f96}
.hint{position:fixed;bottom:1.2vh;left:2vw;font-family:sans-serif;
 font-size:.85rem;color:#8a8f96}
@media print{.deck{overflow:visible;height:auto}
 .slide{page-break-after:always;height:100vh}.hint,footer{display:none}}
"""

JS = """document.addEventListener('keydown',e=>{
 const d=document.querySelector('.deck');
 if(['ArrowRight','PageDown',' '].includes(e.key)){d.scrollBy({top:innerHeight,behavior:'smooth'});e.preventDefault()}
 if(['ArrowLeft','PageUp'].includes(e.key)){d.scrollBy({top:-innerHeight,behavior:'smooth'});e.preventDefault()}
 if(e.key==='Home')d.scrollTo({top:0,behavior:'smooth'});
 if(e.key==='End')d.scrollTo({top:d.scrollHeight,behavior:'smooth'});
});
"""

def esc(s: str) -> str:
    return html.escape(s, quote=False)


def clean_code(code: str) -> str:
    """Drop validator-only marker lines (# expect: ...) from slide code."""
    lines = [l for l in code.splitlines() if not l.strip().startswith("# expect:")]
    return "\n".join(lines)


def hl(code: str) -> str:
    """Minimal, safe Python highlighter for slide code blocks."""
    out = []
    for line in code.rstrip().splitlines():
        line = esc(line)
        line = re.sub(r"(&quot;[^&]*?&quot;|'[^']*?')", r'<span class="s">\1</span>', line)
        line = re.sub(r"(#\b.*)$", r'<span class="c">\1</span>', line)
        line = re.sub(r"\b(def|return|if|elif|else|for|while|in|not|and|or|break|continue|None|True|False|import|from)\b",
                      r'<span class="k">\1</span>', line)
        line = re.sub(r"\b(\d+\.?\d*)\b", r'<span class="n">\1</span>', line)
        out.append(line)
    return "\n".join(out)


def section(text: str, heading: str) -> str:
    m = re.search(r"## " + re.escape(heading) + r"\n(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1).strip() if m else ""


def first_items(block: str, n: int = 6) -> list[str]:
    items = []
    for line in block.splitlines():
        m = re.match(r"^[-*] (.+)$", line.strip())
        if m:
            items.append(m.group(1))
        if len(items) >= n:
            break
    return items


def load_lecture(n: int) -> dict:
    d = LECTURES / f"lecture-{n:02d}"
    plan = (d / "plan.md").read_text(encoding="utf-8")
    notes = (d / "notes.md").read_text(encoding="utf-8")
    examples = (d / "examples.md").read_text(encoding="utf-8")
    title = re.match(r"# Lecture \d+ — (.+)", plan).group(1)
    objectives = first_items(section(plan, "Learning objectives"), 5)
    definitions = []  # (term, text)
    for line in section(notes, "Definitions").splitlines():
        m = re.match(r"^[-*] \*\*(.+?)\*\*[ —:：]*(.*)$", line.strip())
        if m and m.group(2):
            definitions.append((m.group(1), m.group(2)))
    misconceptions = first_items(section(notes, "Common misconceptions"), 4)
    exit_q = []
    fm = section(plan, "Formative assessment")
    for m in re.finditer(r"^\d+\. (.+?)(?:\n\s*\*Expected: (.+?))?\*?\n?$", fm, re.M):
        if m.group(1).strip():
            exit_q.append((m.group(1).strip().rstrip("*"), (m.group(2) or "").strip()))
    # worked examples: numbered sections with Problem/Algorithm/Python blocks
    ex = []
    for m in re.finditer(r"^## \d+\. (.+?) \(case (cs-\d+)\)\n(.*?)(?=\n## \d+\. |\Z)",
                         examples, re.S | re.M):
        name, sid, body = m.group(1), m.group(2), m.group(3)
        prob = re.search(r"\*\*Problem\.\*\* (.+)", body)
        trace = re.search(r"\*\*Trace[^.]*\.\*\* (.+)", body)
        exp = re.search(r"\*\*Expected output\.\*\* (.+)", body)
        py = re.search(r"```python\n(.*?)```", body, re.S)
        cost = re.search(r"\*\*Complexity\.\*\* (.+)", body)
        ex.append({"name": name, "sid": sid,
                   "problem": prob.group(1).strip() if prob else "",
                   "trace": trace.group(1).strip() if trace else "",
                   "expected": exp.group(1).strip() if exp else "",
                   "cost": cost.group(1).strip() if cost else "",
                   "python": py.group(1) if py else ""})
    cases = []
    for sid in re.findall(r"\| (cs-\d+) \|", plan):
        ct = (CASES / f"{sid}.md").read_text(encoding="utf-8")
        diff = re.search(r"\|\s*difficulty\s*\|\s*(\w+)", ct).group(1)
        title_c = re.match(r"# cs-\d+ — (.+)", ct).group(1)
        problem = section(ct, "Problem")
        examples_c = section(ct, "Examples")
        prompt = section(ct, "Discussion starter")
        first_par = re.search(r"^(.+?)\n\n", problem, re.S)
        cases.append({"sid": sid, "title": title_c, "difficulty": diff,
                      "problem": (first_par.group(1).strip() if first_par else problem.strip()),
                      "examples": examples_c.strip(), "prompt": prompt.strip()})
    return {"n": n, "title": title, "objectives": objectives,
            "definitions": definitions, "misconceptions": misconceptions,
            "exit_q": exit_q, "examples": ex, "cases": cases}


def slide(kicker: str, body: str, notes: str = "") -> str:
    n = f'\n<div class="notes">{esc(notes)}</div>' if notes else ""
    return f'<section class="slide"><div class="kicker">{esc(kicker)}</div>{body}{n}</section>'


def deck_html(d: dict) -> str:
    s: list[str] = []
    n = d["n"]
    # 1 · Title + objectives
    s.append(slide("Problem Solving — CS & DS", 
        f"<h1>Lecture {n:02d} — {esc(d['title'])}</h1>"
        f"<h3>Learning objectives</h3><ul>"
        + "".join(f"<li>{esc(o)}</li>" for o in d["objectives"]) + "</ul>"
        + '<p class="small">Case-based lecture: you attempt, we discuss, then we reveal.</p>'))
    # 2 · Agenda = the case sequence
    s.append(slide("Today",
        "<h2>The plan</h2><ul>"
        + "".join(f"<li>Four cases: " + ", ".join(f"<code>{c['sid']}</code>" for c in d["cases"]) + "</li>"
                  "<li>Each: 5-minute attempt → discussion → reveal → prompt</li>"
                  "<li>Worked examples in between — ask anything</li>"
                  "<li>Break mid-lecture · exit question at the end</li>")
        + "</ul>"))
    # 3 · Definitions
    if d["definitions"]:
        rows = "".join(f"<li><strong>{esc(t)}</strong> — {esc(x)}</li>"
                       for t, x in d["definitions"][:6])
        s.append(slide("Key definitions", f"<h2>Key definitions</h2><ul>{rows}</ul>",
                       "Explain each in one breath; the cases will do the heavy lifting."))
    # 4+ · Worked examples
    for e in d["examples"]:
        body = (f"<h2>{esc(e['name'])}</h2>"
                f"<div class='case'><span class='tag'>{e['sid']}</span>"
                f"<p>{esc(e['problem'])}</p></div>")
        if e["python"]:
            body += f"<pre><code>{hl(clean_code(e['python']))}</code></pre>"
        if e["expected"]:
            body += f"<p><strong>Expected:</strong> <code>{esc(e['expected'])}</code></p>"
        if e["cost"]:
            body += f"<p class='small'>Cost: {esc(e['cost'])}</p>"
        s.append(slide("Worked example", body))
    # Case slides: prompt + attempt instruction
    for c in d["cases"]:
        body = (f"<div class='case'><span class='tag'>Case {c['sid']} · "
                f"{c['difficulty']}</span><h2>{esc(c['title'])}</h2>"
                f"<p>{esc(c['problem'])}</p></div>")
        if c["examples"]:
            exl = [l for l in c["examples"].splitlines() if l.strip()][:4]
            body += "<ul>" + "".join(f"<li><code>{esc(l.strip('- '))}</code></li>" for l in exl) + "</ul>"
        body += (f"<span class='timer'>⏱ 5 minutes — attempt now</span>"
                 f"<p class='small'>Pseudocode, flowchart or Python. State one assumption. "
                 f"Compare with your neighbour at minute 4.</p>")
        s.append(slide(f"Case attempt · lecture {n:02d}", body))
        # Discussion slide (student-facing prompt only)
        s.append(slide("Discussion",
            f"<h2>{esc(c['sid'])} — discuss</h2>"
            f"<ul><li>What did the deciding quantity turn out to be?</li>"
            f"<li>Which assumption shaped your answer?</li>"
            f"<li>{esc(c['prompt'])}</li></ul>"
            f"<p class='small'>Instructor: the reveal, the reasoning section and "
            f"common wrong turns are in the instructor distribution for {c['sid']} "
            f"— not embedded in this deck.</p>"))
    # Misconceptions
    if d["misconceptions"]:
        s.append(slide("Check yourself",
            "<h2>Common misconceptions</h2><ul>"
            + "".join(f"<li>{esc(m)}</li>" for m in d["misconceptions"]) + "</ul>"))
    # Summary + exit (expected answers live in the hidden notes layer only)
    exit_items = "".join(f"<li>{esc(q)}</li>" for q, a in d["exit_q"][:3])
    exit_notes = " ".join(a for q, a in d["exit_q"][:3] if a)
    s.append(slide("Summary",
        f"<h2>Summary &amp; exit question</h2>"
        f"<ul><li>Named technique today: <strong>{esc(d['title'])}</strong></li>"
        f"<li>Four cases attempted — methods before answers</li></ul>"
        f"<h3>Exit question (choose one, 60 seconds)</h3><ol>{exit_items}</ol>",
        notes="Expected answers (instructor): " + exit_notes))
    body = "\n".join(s)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lecture {n:02d} — {esc(d['title'])} · Slides</title>
<style>{CSS}</style></head>
<body><div class="deck">{body}</div>
<div class="hint">→ / space: next · ←: back · Home/End: jump · Ctrl+P → PDF</div>
<footer>L{n:02d} · Problem Solving — CS &amp; DS</footer>
<script>{JS}</script></body></html>"""


def index_html(count: int) -> str:
    rows = "".join(
        f"<li><a href='lecture-{n:02d}-slides.html'>Lecture {n:02d}</a></li>"
        for n in range(1, 33))
    return f"""<!DOCTYPE html>
<html lang=\"en\"><head><meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Slide Decks · Problem Solving — CS &amp; DS</title>
<style>body{{font-family:Georgia,serif;max-width:46rem;margin:8vh auto;padding:0 1.5rem;
color:#1c2430;background:#f7f5f0}}h1{{color:#0f6b5c}}li{{margin:.3rem 0;font-size:1.1rem}}
a{{color:#0f6b5c}}.k{{text-transform:uppercase;letter-spacing:.15em;font-size:.85rem;color:#b3541e}}
</style></head><body>
<p class=\"k\">Problem Solving — CS &amp; DS</p>
<h1>Slide decks ({count} lectures)</h1>
<p>Projection decks generated from the lecture material. Keys: → / space next,
← back, Home/End jump, Ctrl+P prints to PDF. Each deck is self-contained —
no network needed.</p>
<ol>{rows}</ol>
</body></html>"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for n in range(1, 33):
        d = load_lecture(n)
        (OUT / f"lecture-{n:02d}-slides.html").write_text(deck_html(d), encoding="utf-8")
    (OUT / "index.html").write_text(index_html(32), encoding="utf-8")
    print(f"wrote {len(list(OUT.glob('lecture-*.html')))} decks + index to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
