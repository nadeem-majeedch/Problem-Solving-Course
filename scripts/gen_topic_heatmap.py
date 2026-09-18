#!/usr/bin/env python3
"""Build the topic-coverage heatmap from case-study metadata.

Outputs (all derived, never hand-edited):
  docs/topic-coverage-heatmap.csv   topics x lectures coverage matrix
  docs/assets/topic-coverage-heatmap.svg  colour heatmap (a11y: real text)
  docs/topic-coverage-heatmap.md    report: method, gaps, concentrations

Taxonomy source: the course's own documentation — docs/learning-outcomes.md,
docs/course-outline.md, and the topic vocabulary already used by the
case pages. Every raw tag on every case page is mapped to exactly one
canonical topic via ALIAS below; an unmapped tag fails the build loudly
instead of being silently dropped. Multiple topics per case are allowed
(set semantics: a case counts once per topic it carries, however many of
its tags map there).

Run from the repository root:  python scripts/gen_topic_heatmap.py
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "case-studies" / "student"

# Canonical topics, in curriculum order (grouped: foundations -> data
# structures -> algorithms -> data science -> strategy). I/O discipline is
# deliberately folded into Problem formulation & requirements: the course
# teaches input/output/edge-case decisions as part of the lecture-01
# INPUTS/OUTPUTS/RULE frame, and no case treats I/O as a standalone topic.
TOPICS = [
    "Problem formulation & requirements",
    "Decomposition & abstraction",
    "Patterns & sequences",
    "Loops & iteration",
    "Conditionals & decisions",
    "Pseudocode & flowcharts",
    "Functions & modular design",
    "Arrays & lists",
    "Strings & text",
    "Dictionaries & sets",
    "Searching (linear & binary)",
    "Sorting",
    "Recursion & divide-and-conquer",
    "Invariants & correctness",
    "Greedy & optimization",
    "Dynamic programming",
    "Graphs & networks",
    "Counting & probability",
    "Simulation",
    "Data analysis",
    "Debugging & testing",
    "Complexity & trade-offs",
    "Ethics & strategic reasoning",
]

# Raw tag -> canonical topic. Keys are the lowercased, stripped tags exactly
# as they appear in case metadata (the complete inventory of 140 tags).
ALIAS: dict[str, str] = {
    # --- formulation / spec / requirements
    "assumptions": "Problem formulation & requirements",
    "boundaries": "Problem formulation & requirements",
    "boundary": "Problem formulation & requirements",
    "constraints": "Problem formulation & requirements",
    "edge cases": "Problem formulation & requirements",
    "formulation": "Problem formulation & requirements",
    "formulations": "Problem formulation & requirements",
    # --- cross-cutting: cases tagged "integration" fuse several threads;
    # counted under problem formulation & requirements (the integrating act).
    "integration": "Problem formulation & requirements",
    "io": "Problem formulation & requirements",
    "preconditions": "Problem formulation & requirements",
    "requirements": "Problem formulation & requirements",
    "sentinels": "Problem formulation & requirements",
    "specification": "Problem formulation & requirements",
    "state": "Problem formulation & requirements",
    "states": "Problem formulation & requirements",
    # --- decomposition / design
    "decomposition": "Decomposition & abstraction",
    "design": "Decomposition & abstraction",
    "modeling": "Decomposition & abstraction",
    "summary design": "Decomposition & abstraction",
    # --- patterns / sequences
    "cycles": "Patterns & sequences",
    "digits": "Patterns & sequences",
    "modulo": "Patterns & sequences",
    "patterns": "Patterns & sequences",
    "rotation": "Patterns & sequences",
    "sequences": "Patterns & sequences",
    "time series": "Patterns & sequences",
    "windows": "Patterns & sequences",
    # --- loops
    "loops": "Loops & iteration",
    "nested loops": "Loops & iteration",
    "termination": "Loops & iteration",
    # --- conditionals / decisions
    "decisions": "Conditionals & decisions",
    "game loop": "Conditionals & decisions",
    "logic": "Conditionals & decisions",
    # --- pseudocode / flowcharts / python
    "flowchart": "Pseudocode & flowcharts",
    "pseudocode": "Pseudocode & flowcharts",
    "python": "Pseudocode & flowcharts",
    # --- functions
    "composition": "Functions & modular design",
    "defaults": "Functions & modular design",
    "functions": "Functions & modular design",
    "mutation": "Functions & modular design",
    "refactoring": "Functions & modular design",
    "reuse": "Functions & modular design",
    # --- arrays & lists
    "aliasing": "Arrays & lists",
    "lists": "Arrays & lists",
    "references": "Arrays & lists",
    "slicing": "Arrays & lists",
    "tuples": "Arrays & lists",
    # --- strings
    "cleaning": "Strings & text",
    "deduplication": "Strings & text",
    "normalisation": "Strings & text",
    "parsing": "Strings & text",
    "strings": "Strings & text",
    # --- dicts & sets
    "dictionaries": "Dictionaries & sets",
    "keys": "Dictionaries & sets",
    "operations": "Dictionaries & sets",
    "queues": "Dictionaries & sets",
    "sets": "Dictionaries & sets",
    "voting": "Dictionaries & sets",
    # --- searching
    "binary search": "Searching (linear & binary)",
    "halving": "Searching (linear & binary)",
    "linear scan": "Searching (linear & binary)",
    "monotonicity": "Searching (linear & binary)",
    "predicates": "Searching (linear & binary)",
    "search": "Searching (linear & binary)",
    "search on answer": "Searching (linear & binary)",
    "search space": "Searching (linear & binary)",
    # --- sorting
    "comparison": "Sorting",
    "intervals": "Sorting",
    "pair scan": "Sorting",
    "selection": "Sorting",
    "sorting": "Sorting",
    "two pointers": "Sorting",
    # --- recursion
    "base case": "Recursion & divide-and-conquer",
    "bases": "Recursion & divide-and-conquer",
    "divide and conquer": "Recursion & divide-and-conquer",
    "recurrence": "Recursion & divide-and-conquer",
    "recursion": "Recursion & divide-and-conquer",
    # --- invariants / correctness
    "counterexamples": "Invariants & correctness",
    "exchange argument": "Invariants & correctness",
    "invariants": "Invariants & correctness",
    "partition": "Invariants & correctness",
    "uniqueness": "Invariants & correctness",
    # --- greedy / optimization
    "greedy": "Greedy & optimization",
    "knapsack": "Greedy & optimization",
    "optimization": "Greedy & optimization",
    "subsets": "Greedy & optimization",
    # --- dynamic programming
    "dp preview": "Dynamic programming",
    "dynamic programming": "Dynamic programming",
    # --- graphs
    "bfs": "Graphs & networks",
    "graphs": "Graphs & networks",
    "matching": "Graphs & networks",
    "neighbours": "Graphs & networks",
    "off-by-one": "Invariants & correctness",
    "shortest path": "Graphs & networks",
    "topological order": "Graphs & networks",
    # --- counting & probability
    "combinations": "Counting & probability",
    "complement": "Counting & probability",
    "conditional probability": "Counting & probability",
    "counting": "Counting & probability",
    "expected value": "Counting & probability",
    "frequencies": "Counting & probability",
    "game theory": "Counting & probability",
    "independence": "Counting & probability",
    "inspection paradox": "Counting & probability",
    "payoffs": "Counting & probability",
    "permutations": "Counting & probability",
    "probability": "Counting & probability",
    "reconstruct": "Patterns & sequences",
    # --- simulation
    "estimation": "Simulation",
    "randomness": "Simulation",
    "simulation": "Simulation",
    # --- data analysis
    "aggregation": "Data analysis",
    "analysis": "Data analysis",
    "anomalies": "Data analysis",
    "averages": "Data analysis",
    "bias": "Data analysis",
    "data": "Data analysis",
    "distributions": "Data analysis",
    "divisors": "Data analysis",
    "false positives": "Data analysis",
    "mean vs median": "Data analysis",
    "percentages": "Data analysis",
    "math": "Complexity & trade-offs",
    "rates": "Data analysis",
    "risk": "Data analysis",
    "skew": "Data analysis",
    "statistics": "Data analysis",
    # --- debugging & testing
    "debugging": "Debugging & testing",
    "hypotheses": "Debugging & testing",
    "method": "Debugging & testing",
    "coverage": "Debugging & testing",
    "regression": "Debugging & testing",
    "testing": "Debugging & testing",
    "tracing": "Debugging & testing",
    "validation": "Debugging & testing",
    # --- complexity & trade-offs
    "arithmetic": "Complexity & trade-offs",
    "brute force": "Complexity & trade-offs",
    "strategy": "Complexity & trade-offs",
    # --- ethics & strategy
    "ethics": "Ethics & strategic reasoning",
    "reasoning": "Ethics & strategic reasoning",
    # --- applied additions (cs-129+): mapped into the existing canonical
    # taxonomy; each tag lands where the curriculum actually teaches it.
    "missing values": "Data analysis",
    "communication": "Problem formulation & requirements",
    "service systems": "Simulation",
    "trade-offs": "Complexity & trade-offs",
    "stakeholders": "Problem formulation & requirements",
    "scheduling": "Greedy & optimization",
    "algorithm selection": "Complexity & trade-offs",
    "leakage": "Debugging & testing",
    "evaluation": "Data analysis",
    "reliability": "Data analysis",
    "inventory": "Greedy & optimization",
}

TIERS = ["Beginner", "Foundational", "Intermediate", "Advanced", "Expert"]


def _esc(s: str) -> str:
    """XML-escape text destined for the SVG (names contain '&' etc.)."""
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def load_cases() -> list[dict]:
    cases = []
    for f in sorted(CASES.glob("cs-*.md")):
        text = f.read_text(encoding="utf-8")
        tier = re.search(r"\|\s*difficulty\s*\|\s*([^|]+)\|", text)
        tags = re.search(r"\|\s*topics\s*\|\s*([^|]+)\|", text)
        lec = re.search(r"\|\s*lecture\s*\|\s*lecture-(\d+)\s*\|", text)
        if not (tier and tags and lec):
            print(f"ERROR: {f.name}: missing metadata row", file=sys.stderr)
            raise SystemExit(1)
        raw = [t.strip().lower() for t in tags.group(1).split(",") if t.strip()]
        mapped = []
        for tag in raw:
            canon = ALIAS.get(tag)
            if canon is None:
                print(f"ERROR: {f.name}: unmapped topic tag {tag!r} — add it "
                      f"to ALIAS in scripts/gen_topic_heatmap.py", file=sys.stderr)
                raise SystemExit(1)
            mapped.append(canon)
        cases.append({
            "id": f.stem,
            "lecture": int(lec.group(1)),
            "tier": tier.group(1).strip(),
            "topics": sorted(set(mapped)),  # set semantics, deduped
        })
    return cases


def build_matrix(cases: list[dict]) -> dict[str, dict[int, Counter]]:
    """matrix[topic][lecture] = Counter of tiers."""
    m: dict[str, dict[int, Counter]] = {t: defaultdict(Counter) for t in TOPICS}
    for c in cases:
        for topic in c["topics"]:
            m[topic][c["lecture"]][c["tier"]] += 1
    return m


def write_csv(matrix, path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["topic"] + [f"lecture-{i:02d}" for i in range(1, 33)]
                   + ["total", "beginner", "foundational", "intermediate",
                      "advanced", "expert"])
        for topic in TOPICS:
            row = [topic]
            tot = Counter()
            for lec in range(1, 33):
                cell = matrix[topic].get(lec, Counter())
                n = sum(cell.values())
                tot += cell
                row.append(f"{n}; " + "/".join(str(cell.get(t, 0)) for t in TIERS))
            row.append(sum(tot.values()))
            row += [tot.get(t, 0) for t in TIERS]
            w.writerow(row)


def _cell_color(n: int) -> str:
    return {0: "#f6f8fa", 1: "#cfe1f5", 2: "#9cc3ec", 3: "#6aa5e0",
            4: "#3f83cf"}.get(n, "#1f5fae")


def write_svg(matrix, n_cases: int, path: Path) -> None:
    CW, CH = 30, 22           # cell size
    LEFT, TOP = 196, 64       # label gutter / header band
    W = LEFT + 32 * CW + 16
    H = TOP + len(TOPICS) * CH + 92
    desc = (f"Heatmap of {n_cases} case studies: one row per canonical "
            "topic, one column per lecture. Cell colour deepens with the "
            "number of cases; the letter in a cell is the dominant "
            "difficulty tier (B beginner, F foundational, I intermediate, "
            "A advanced, E expert). Full numbers are in the companion CSV.")
    heading = f"Topic coverage across the 32 lectures — {n_cases} case studies"
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" '
        f'aria-labelledby="hm-title hm-desc">',
        f'<title id="hm-title">{_esc("Topic coverage across the 32 lectures")}</title>',
        f'<desc id="hm-desc">{_esc(desc)}</desc>',
        '<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{LEFT}" y="24" font-size="15" font-weight="bold" '
        f'fill="#1f2937">{_esc(heading)}</text>',
    ]
    # lecture column headers (rotated for readability)
    for i in range(32):
        x = LEFT + i * CW + CW / 2
        out.append(f'<text x="{x:.1f}" y="{TOP - 8}" font-size="10" '
                   f'fill="#4b5563" text-anchor="start" '
                   f'transform="rotate(-45 {x:.1f} {TOP - 8})">{i + 1:02d}</text>')
    for r, topic in enumerate(TOPICS):
        y = TOP + r * CH
        # wrapped two-line label when long
        if len(topic) > 26 and " " in topic:
            words = topic.split(" ")
            best, score = 0, 10**9
            for k in range(1, len(words)):
                a, b = " ".join(words[:k]), " ".join(words[k:])
                s = abs(len(a) - len(b))
                if s < score:
                    best, score = k, s
            l1, l2 = " ".join(words[:best]), " ".join(words[best:])
            out.append(f'<text x="{LEFT - 8}" y="{y + CH / 2 - 2}" '
                       f'font-size="11" fill="#1f2937" text-anchor="end">{_esc(l1)}</text>')
            out.append(f'<text x="{LEFT - 8}" y="{y + CH / 2 + 10}" '
                       f'font-size="11" fill="#1f2937" text-anchor="end">{_esc(l2)}</text>')
        else:
            out.append(f'<text x="{LEFT - 8}" y="{y + CH / 2 + 4}" '
                       f'font-size="11" fill="#1f2937" text-anchor="end">{_esc(topic)}</text>')
        for c in range(32):
            x = LEFT + c * CW
            cell = matrix[topic].get(c + 1, Counter())
            n = sum(cell.values())
            out.append(f'<rect x="{x}" y="{y}" width="{CW - 1}" height="{CH - 1}" '
                       f'fill="{_cell_color(n)}" stroke="#d0d7de" stroke-width="0.5">'
                       f'<title>{_esc(topic)} — lecture {c + 1:02d}: {n} case(s) — '
                       + _esc(", ".join(f"{t} {cell[t]}" for t in TIERS if cell.get(t)))
                       + "</title></rect>")
            if n:
                dom = max(TIERS, key=lambda t: (cell.get(t, 0), -TIERS.index(t)))
                letter = {"Beginner": "B", "Foundational": "F",
                          "Intermediate": "I", "Advanced": "A",
                          "Expert": "E"}[dom]
                fill = "#ffffff" if n >= 3 else "#1f2937"
                out.append(f'<text x="{x + CW / 2 - 0.5:.1f}" y="{y + CH / 2 + 3.5:.1f}" '
                           f'font-size="10" fill="{fill}" text-anchor="middle">{letter}</text>')
    # legend
    ly = TOP + len(TOPICS) * CH + 26
    out.append(f'<text x="{LEFT}" y="{ly}" font-size="11" fill="#1f2937">Cases per cell:</text>')
    for i, n in enumerate([0, 1, 2, 3, 4, "5+"]):
        x = LEFT + 110 + i * 76
        out.append(f'<rect x="{x}" y="{ly - 12}" width="16" height="16" '
                   f'fill="{_cell_color(n if isinstance(n, int) else 5)}" '
                   f'stroke="#d0d7de"/>')
        out.append(f'<text x="{x + 22}" y="{ly}" font-size="11" fill="#374151">{n}</text>')
    ly2 = ly + 24
    legend = ("Letter = dominant tier: B beginner · F foundational · "
              "I intermediate · A advanced · E expert. Multiple topics per "
              "case allowed (a case counts once per topic it carries).")
    out.append(f'<text x="{LEFT}" y="{ly2}" font-size="11" fill="#1f2937">'
               f'{_esc(legend)}</text>')
    out.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def write_report(matrix, cases: list[dict], path: Path) -> None:
    n_cases = len(cases)
    tier_totals = Counter(c["tier"] for c in cases)
    lec_of = Counter(c["lecture"] for c in cases)
    rows = []
    for topic in TOPICS:
        lec_count = sum(1 for l in range(1, 33) if matrix[topic].get(l))
        tot = sum(sum(matrix[topic][l].values()) for l in range(1, 33))
        mix = Counter()
        for l in range(1, 33):
            mix += matrix[topic][l]
        peaks = [(l, sum(matrix[topic][l].values()))
                 for l in range(1, 33) if sum(matrix[topic][l].values()) >= 3]
        rows.append((topic, lec_count, tot, mix, peaks))
    lines = [
        "# Topic-Coverage Heatmap",
        "",
        f"**Scope:** all {n_cases} case studies "
        f"({', '.join(f'{t} {tier_totals[t]}' for t in TIERS)}). Generated by "
        "`scripts/gen_topic_heatmap.py` from case metadata — regenerate after "
        "any case change; do not hand-edit. Companion files: "
        "[CSV matrix](topic-coverage-heatmap.csv), "
        "[SVG heatmap](assets/topic-coverage-heatmap.svg).",
        "",
        "## Taxonomy source",
        "",
        "The canonical topics are the course's own vocabulary, drawn from",
        "`docs/learning-outcomes.md` and `docs/course-outline.md` (the curriculum",
        "threads every lecture already teaches), not invented for this report.",
        "Each case's free-form topic tags (the full raw-tag inventory) are mapped to",
        "exactly one canonical topic by the alias table in the generator; an",
        "unmapped tag fails the build rather than vanishing from the count.",
        "",
        "## Counting methodology",
        "",
        "- **Multiple topics per case are allowed.** A case counts once per",
        "  canonical topic it carries (set semantics on its tags), so column",
        "  sums exceed the case count — that is coverage, not duplication.",
        "- **Difficulty distribution** is the exact tier vector of the cases",
        "  in each cell (CSV columns `beginner…expert`; the SVG cell letter is",
        "  the dominant tier). Tier totals come from case metadata itself.",
        "- **Primary vs secondary topics are not distinguished:** case metadata",
        "  does not rank its tags, and inventing a ranking would fabricate",
        "  data. The limitation is stated rather than hidden.",
        "",
        "## Coverage matrix (SVG preview is the authoritative rendering)",
        "",
        "| Topic | Lectures touched | Cases | Tier mix (B/F/I/A/E) |",
        "| --- | --- | --- | --- |",
    ]
    for topic, lec_count, tot, mix, peaks in rows:
        mixs = "/".join(str(mix.get(t, 0)) for t in TIERS)
        lines.append(f"| {topic} | {lec_count} | {tot} | {mixs} |")
    gaps = [(t, lc, tot) for t, lc, tot, _, _ in rows if lc <= 5]
    conc = [(t, l, n) for t, _, _, _, pks in rows for l, n in pks]
    lines += [
        "",
        "## Coverage gaps (topic in ≤ 5 lectures)",
        "",
    ]
    if gaps:
        for t, lc, tot in sorted(gaps, key=lambda r: r[1]):
            lines.append(f"- **{t}** — {lc} lecture(s), {tot} case(s) in total.")
    else:
        lines.append("- None: every topic appears in at least 6 lectures.")
    lines += [
        "",
        "## Concentrations (cells with ≥ 3 cases in one lecture)",
        "",
    ]
    if conc:
        for t, l, n in sorted(conc, key=lambda r: (-r[2], r[0])):
            lines.append(f"- **{t}** in lecture {l:02d}: {n} cases.")
    else:
        lines.append("- None: no lecture puts 3+ cases on one topic.")
    over = sorted(rows, key=lambda r: -r[2])[:5]
    lines += [
        "",
        "## Overrepresented topics (most cases overall)",
        "",
    ]
    for t, lc, tot, _, _ in over:
        lines.append(f"- **{t}** — {tot} cases across {lc} lectures.")
    lines += [
        "",
        "## Known limitations",
        "",
        "- Tags reflect author intent at case-writing time; the alias mapping",
        "  is a judgement call per tag (each documented in the generator).",
        "- Lecture cells count the cases *assigned* to that lecture, so a",
        "  topic taught as a thread across blocks (e.g. complexity) looks",
        "  more scattered than the teaching feels.",
        "- The SVG letter shows only the dominant tier of a cell; the full",
        "  tier vector per cell is in the CSV (columns after the lecture",
        "  columns, encoded as `count; b/f/i/a/e`).",
        "",
        f"Lecture case counts span {min(lec_of.values())}–{max(lec_of.values())} "
        f"per lecture (every lecture has cases — the validator enforces it).",
        "",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    cases = load_cases()
    if not cases:
        print("ERROR: no cases found", file=sys.stderr)
        return 1
    matrix = build_matrix(cases)
    write_csv(matrix, ROOT / "docs" / "topic-coverage-heatmap.csv")
    write_svg(matrix, len(cases), ROOT / "docs" / "assets" / "topic-coverage-heatmap.svg")
    write_report(matrix, cases, ROOT / "docs" / "topic-coverage-heatmap.md")
    print(f"topic heatmap written: {len(TOPICS)} topics x 32 lectures over "
          f"{len(cases)} cases (csv, svg, md)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
