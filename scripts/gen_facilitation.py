"""Generate activities/case-facilitation-map.md from live case metadata.

For each lecture: its four cases with difficulty, the course's standard
facilitation cycle (authored once), per-lecture facilitation notes
(authored in NOTES below), and each case's own extension question
(extracted from the instructor bank so it always matches the bank).

Regenerate with:  python scripts/gen_facilitation.py
The output file is generated content: edit NOTES here, not the .md.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUDENT = ROOT / "case-studies" / "student"
INSTRUCTOR = ROOT / "case-studies" / "instructor"
OUT = ROOT / "activities" / "keys" / "case-facilitation-map.md"

# Per-lecture facilitation notes: the one thing to watch, and one
# lecture-specific facilitation move. Authored, keyed by lecture number.
NOTES = {
    1: "First exposure: students read slowly. Run cs-001 as a whole-class think-aloud before the timed attempt on cs-002 — the 5-minute clock is itself new.",
    2: "Pseudocode is the deliverable, not the code. Collect two pseudocode attempts on the board and let the room vote which executes correctly before revealing.",
    3: "Flowcharts: hand out blank diamond/box sheets. The wrong-loop discussions (cs-011) are the lecture's payoff — protect time for them.",
    4: "First real Python. Keep one idle interpreter ready; the reveal for cs-015 should *run*, with the class calling the next output.",
    5: "Remainder arithmetic splits the room. Pair a confident modeller with a hesitant one for cs-020; the cold-start discussion is where understanding lands.",
    6: "Trace discipline: have students cover the code and call the next variable value aloud. cs-024's off-by-one museum is best run gallery-style.",
    7: "Students debug each other today. Enforce hypothesis-before-fix in cs-025–cs-028 discussions; the method is the content.",
    8: "Test tables from requirements only. For cs-029–cs-032, hide each case's code on first display — requirements first, always.",
    9: "Aggregation day. The accumulator table on the board (one column per variable) is the whole lecture — draw it once, reuse for every case.",
    10: "Strings invite off-by-one indexing; cs-038's family of reversals works as a rapid-fire round (90 seconds per variant).",
    11: "Aliasing is invisible on paper. Run cs-044's trap live in the interpreter; ask for predictions *before* each print.",
    12: "Real defects day. Students work in pairs with one machine; rotate the driver role each case to keep both hands on the method.",
    13: "Maps as decisions. cs-052's consensus question rewards asking 'what is the key?' out loud before any attempt.",
    14: "Contracts day: every attempt must name parameters and return before the body. Reject any attempt that starts inside the function.",
    15: "Counting splits into order-matters vs not — make the class *say* which on each case before computing anything.",
    16: "Consolidation. Students pick two of the four cases (their choice); the discussion compares the *methods chosen*, not just answers.",
    17: "Search day: for every case ask 'when can we stop early?' — the early-stop condition is the actual content.",
    18: "Sort keys before sort code: collect the key tuples on the board first; tie-breaks are where cs-071 lives.",
    19: "Invariants as sentences. Each attempt must include one 'always true' sentence; grade the sentence, then the code.",
    20: "Brute force is respectable today — but every attempt must bound the space with arithmetic before enumerating.",
    21: "Binary search on data *and* answers: keep cs-083's answer-search for last; the predicate insight lands only after cs-081's game.",
    22: "Recursion: base case first, on paper, always. cs-085's doll tree drawn by hand precedes any code.",
    23: "Greedy vs DP: run cs-089's conjecture discussion to a standstill before revealing — the failure case is the lecture.",
    24: "Graphs: require the draw (vertices/edges labelled) before any traversal attempt; cs-096's alarm timing becomes concrete on paper.",
    25: "Data day one: every summary proposed must carry 'compared to what?' — cs-097's queue log is the warm-up.",
    26: "Probability day: sample space before formula, every time. cs-104's streak question pairs beautifully with the lab's dice work.",
    27: "Cleaning day: run cs-105–cs-108 as a tribunal — students argue drop/fix/investigate per defect with evidence.",
    28: "Summary honesty: for each case, one student is the 'sceptic' who must find the misleading reading; rotate the role.",
    29: "Simulation day: define one trial *in words* before any code; cs-113's dice calibration sets the pattern for the block.",
    30: "Optimisation: objective + constraint in one sentence each before any solving — cs-117's poster budget makes the habit.",
    31: "Strategy day: expected-value computations are the floor; the discussion lives in what EV leaves out. cs-124's auction rewards devil's advocates.",
    32: "Capstone: 20-minute cases. Run one in full exam style, one as a free-for-all; compare what the timer did to method quality.",
}

CYCLE = """The standard cycle (from the [teaching methodology](../../docs/teaching-methodology.md)):

1. **Display** the student page full-screen. Nothing else is visible.
2. **Minute 0–1** — read and analyse: inputs, outputs, the deciding quantity.
3. **Minute 1–3** — develop an approach; instructor circulates, reading shoulders.
4. **Minute 3–5** — compare with the neighbour or write the pseudocode.
5. **Reveal and discuss** — two contrasting attempts to the board first,
   then the case's reasoning walkthrough; close by naming the technique.
6. **Discussion prompt** — the case's own prompt (in its Connections section)
   as the bridge to the next case.

The per-case five-minute sequences, hint ladders, watch-fors and rubric
notes live in each instructor solution page (see the
[solution bank overview](../../docs/instructor-guide.md#the-solution-bank-in-brief)).
"""

DIFF_ORDER = ["Beginner", "Foundational", "Intermediate", "Advanced", "Expert"]


def parse_student(path: Path) -> dict:
    t = path.read_text(encoding="utf-8")
    title = re.match(r"# (cs-\d+) — (.+)", t).group(2)
    meta = dict(re.findall(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$",
                           t.split("## Problem")[0], re.M))
    return {"sid": path.stem, "title": title, "difficulty": meta.get("difficulty", "")}


def parse_extension(path: Path) -> str:
    t = path.read_text(encoding="utf-8")
    m = re.search(r"## Extension challenge\n\n(.+?)\n", t)
    return m.group(1).strip() if m else ""


def main() -> None:
    by_lecture: dict[int, list[dict]] = {}
    for f in sorted(STUDENT.glob("cs-*.md")):
        c = parse_student(f)
        c["ext"] = parse_extension(INSTRUCTOR / f.name)
        lec = int(f.read_text(encoding="utf-8").split("lecture-")[1][:2])
        by_lecture.setdefault(lec, []).append(c)

    lines = [
        "# Case Facilitation Map — Lecture by Lecture",
        "",
        "Instructor-facing map of the four cases per lecture with facilitation",
        "notes and each case's extension question. Difficulty comes from the",
        "case metadata; extensions come from the instructor bank, so the two",
        "always agree with the case pages themselves.",
        "",
        "> **Instructor only.** This page is excluded from the public site and",
        "> links to solution-adjacent material.",
        "",
        CYCLE,
    ]
    for lec in sorted(by_lecture):
        cases = sorted(by_lecture[lec], key=lambda c: c["sid"])
        cases.sort(key=lambda c: DIFF_ORDER.index(c["difficulty"]))
        lines.append(f"## Lecture {lec:02d}")
        lines.append("")
        lines.append(f"**Facilitation note.** {NOTES[lec]}")
        lines.append("")
        lines.append("| Case | Difficulty | Extension question (optional, after the reveal) |")
        lines.append("| --- | --- | --- |")
        for c in cases:
            ext = c["ext"].rstrip(".") if c["ext"] else "—"
            lines.append(f"| [{c['sid']} — {c['title']}](../../case-studies/student/{c['sid']}.md) "
                         f"| {c['difficulty']} | {ext} |")
        lines.append("")
        lines.append("*Release extensions only after the reveal; they are enrichment, not "
                     "assessment.*")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(by_lecture)} lectures)")


if __name__ == "__main__":
    main()
