"""Enrich the instructor solution bank with per-case teaching material.

For every case-studies/instructor/cs-*.md this tool:

* REPLACES the template pseudocode with pseudocode transpiled from that
  case's own verified Python (scripts/pseudocode_gen.py).
* REPLACES Edge cases / Alternative approaches / Common pitfalls /
  Reveal script with per-case text composed from the case's own worked
  instance, expected result, method moves, known wrong turn, code shape,
  and real metadata. No numbers are invented anywhere.
* ADDS three sections: ``Five-minute teaching sequence``,
  ``Difficulty adaptation`` and ``Assessment use``.

Sections not listed above (Reasoning walkthrough, Python, Connections,
Extension challenge, metadata, callout) are preserved verbatim.

Usage:
    python scripts/enrich_bank.py --check   # extraction report only
    python scripts/enrich_bank.py --apply   # rewrite the files
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pseudocode_gen import transpile  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / "case-studies" / "instructor"

SECTIONS = [
    "Reasoning walkthrough",
    "Five-minute teaching sequence",
    "Difficulty adaptation",
    "Reference solution (pseudocode)",
    "Reference solution (Python)",
    "Edge cases",
    "Alternative approaches",
    "Common pitfalls",
    "Reveal script",
    "Assessment use",
    "Connections",
    "Extension challenge",
]

NEW_SECTIONS = ["Five-minute teaching sequence", "Difficulty adaptation", "Assessment use"]
REPLACED = ["Reference solution (pseudocode)", "Edge cases", "Alternative approaches",
            "Common pitfalls", "Reveal script"]

THEMES = {
    "modelling, rules, and decisions": {
        "question": "Which quantity does the rule attach to, and what exactly does one application of the rule change?",
        "hint": "Turn the story into entities, quantities, and one precise rule before computing anything.",
        "simplify": "Give the rule list with one line blank and let the class compute that line together.",
    },
    "aggregation over a sequence": {
        "question": "What must the loop remember between two items — and what can it safely forget?",
        "hint": "Choose the accumulator and its starting value first; the loop body writes itself after that.",
        "simplify": "Fill the accumulator table for the first two items together; pairs complete the rest.",
    },
    "systematic debugging": {
        "question": "What does the wrong output tell you about where the program's state first leaves the intended path?",
        "hint": "Split the program at the first line where the actual value stops matching the expected value.",
        "simplify": "Hand over the trace table with two cells left to fill.",
    },
    "test design from requirements": {
        "question": "Which input would you hand this program to make it fail fastest?",
        "hint": "Aim at boundaries and rule intersections, not at random values.",
        "simplify": "Start from a given test table with one deliberately impossible row to find.",
    },
    "string transformation and checking": {
        "question": "What is the smallest unit of text a decision attaches to — character, token, or whole string?",
        "hint": "Normalise first (case, separators), then decide; two rules stop fighting once the text is normalised.",
        "simplify": "Use a five-character string and mark the decision on each character.",
    },
    "list surgery and slicing": {
        "question": "Does this operation need a copy, a view, or in-place surgery — and who else can still see the list?",
        "hint": "Decide the aliasing question first; every later bug hides behind a shared reference.",
        "simplify": "Use index cards as list cells and physically reorder them.",
    },
    "mappings and sets": {
        "question": "What is the key, and what belongs to its value — a membership fact or a running total?",
        "hint": "Sketch the map's keys first; the update rule for the values follows from that sketch.",
        "simplify": "Pre-populate the map with the first two entries and let students add the third.",
    },
    "decomposition into functions": {
        "question": "Which single responsibility resists decomposition — and what does each piece hand to the next?",
        "hint": "Name the pieces by what they return, not by what they do internally.",
        "simplify": "Provide the function signatures; students fill in one body each.",
    },
    "counting and probability": {
        "question": "Are you counting arrangements, selections, or successes — and does order matter here?",
        "hint": "Fix the sample space first; every shortcut is a claim about that space.",
        "simplify": "List the outcomes for a reduced instance and count them by hand.",
    },
    "scans, search, and sorted arrays": {
        "question": "What ordering or condition lets you stop early — and what must be true at the moment you stop?",
        "hint": "State what the scan knows at position i before writing the update rule.",
        "simplify": "Trace three positions by hand before any code is written.",
    },
    "invariants and two pointers": {
        "question": "What must stay true about the two regions after every single move?",
        "hint": "Write the invariant as a sentence, then check every pointer move against it.",
        "simplify": "Move physical markers along a printed row of values.",
    },
    "brute force and search spaces": {
        "question": "What is the search space, and in what order will you try it?",
        "hint": "Bound the space first: count the candidates before generating any of them.",
        "simplify": "Reduce the space (three candidates instead of the full set) and enumerate by hand.",
    },
    "binary search on data or answers": {
        "question": "What switches exactly once — and can your test actually see it?",
        "hint": "The predicate is monotone; you are searching for the boundary, not for a value.",
        "simplify": "Play the game on 1..8 with the shrinking interval written on the board.",
    },
    "recursion and dynamic programming": {
        "question": "What is the smallest instance you can already solve — and how does a bigger one shrink onto it?",
        "hint": "Write the base case and the self-reference before writing any code.",
        "simplify": "Unroll one level of the call tree for them; they draw the second level.",
    },
    "graphs and traversal": {
        "question": "What are the vertices, what are the edges, and what does distance mean in this story?",
        "hint": "Draw the graph first; the traversal order then answers the actual question asked.",
        "simplify": "Provide the drawn five-node graph; students only run the traversal.",
    },
    "simulation and randomness": {
        "question": "What is one trial, what is random inside it, and what are you averaging over?",
        "hint": "Write one trial as a sentence containing a coin or a roll, then loop that sentence.",
        "simplify": "Run the first ten trials on paper with a given die sequence.",
    },
}

# Confident, shape-based cost statements (never invented Big-O).
def cost_note(shape: dict) -> str | None:
    if shape["sort"]:
        return "the sort dominates the cost: n log n in the input size, everything after it is one cheap pass"
    if shape["halving"]:
        return "logarithmic: the interval (or exponent) halves every step, so doubling the input adds one step"
    if shape["nested_for"]:
        return "quadratic in the worst case: the nested passes revisit the data once per element"
    if shape["branching_recursion"] and not shape["memo"]:
        return "exponential without memoisation: each call spawns the same work again; a table of solved subproblems removes the repeat"
    if shape["memo"]:
        return "one entry per distinct subproblem once memoised — the table, not the recursion depth, sets the cost"
    if shape["single_for"]:
        return "linear: one visit per item, a constant amount of work per visit"
    return None


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _a(noun: str) -> str:
    return "an" if noun[:1].lower() in "aeiou" else "a"


def parse_case(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    secs = {}
    matches = list(re.finditer(r"^## (.+?)$", text, re.M))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        secs[m.group(1).strip()] = text[m.end():end].strip()
    head = text[: matches[0].start()]

    meta = dict(re.findall(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", secs.get("", ""), re.M)) if "" in secs else {}
    rw = secs["Reasoning walkthrough"]
    instance = _norm(re.search(r"\*\*Worked instance\.\*\* (.+)", rw).group(1))
    expected = _norm(re.search(r"\*\*Expected result\.\*\* (.+)", rw).group(1))
    theme = _norm(re.search(r"\*\*Method — (.+?)\.\*\*", rw).group(1))
    moves = re.findall(r"^\d+\. (.+)$", rw, re.M)
    stuck = _norm(secs["Reasoning walkthrough"].split("**Where this class gets stuck.**")[1])
    wrong_m = re.search(r"Expect the first five minutes to produce (.+?) as the most common wrong turn", stuck)
    wrong_turn = _norm(wrong_m.group(1)) if wrong_m else ""
    better = _norm(stuck.split("Expect the first five minutes")[0]).rstrip(";. ")

    py = re.search(r"## Reference solution \(Python\)\n\n```python\n(.*?)```", text, re.S).group(1)
    prompt = _norm(re.search(r"Discussion prompt for after the reveal: \*\*(.+?)\*\*", secs["Connections"]).group(1))
    prompt = prompt.strip().strip('"').strip()  # the connection line already carries quotes
    ext = _norm(secs["Extension challenge"].split("\n")[0])

    return {
        "sid": path.stem, "head": head, "secs": secs, "text": text,
        "difficulty": meta.get("difficulty", ""), "topics": meta.get("topics", ""),
        "objective": meta.get("objective", ""), "instance": instance,
        "expected": expected, "theme": theme, "moves": moves,
        "stuck": stuck, "wrong_turn": wrong_turn, "better": better,
        "code": py, "prompt": prompt, "ext": ext,
    }


def shape_of(code: str) -> dict:
    tree = ast.parse(code)
    shape = {"while": False, "recursion": False, "dict": False, "sort": False,
             "float": False, "nested_for": False, "single_for": False,
             "halving": False, "memo": False, "branching_recursion": False,
             "index_arith": False, "alias_mutate": False, "stringy": False,
             "enumerate_pairs": False}
    fns = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    names = {f.name for f in fns}
    src = code
    shape["while"] = any(isinstance(n, ast.While) for n in ast.walk(tree))
    shape["sort"] = "sorted(" in src or ".sort(" in src
    shape["float"] = "round(" in src or any(isinstance(n, ast.Constant) and isinstance(n.value, float)
                                            for n in ast.walk(tree))
    shape["memo"] = "lru_cache" in src or "memo" in src
    shape["stringy"] = any(m in src for m in (".split(", ".lower(", ".strip(", ".join(", ".isalnum", ".isdigit"))

    for f in fns:
        for n in ast.walk(f):
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in names:
                shape["recursion"] = True
                if sum(1 for c in ast.walk(f) if isinstance(c, ast.Call)
                       and isinstance(c.func, ast.Name) and c.func.id == f.name) > 1:
                    shape["branching_recursion"] = True
            if isinstance(n, (ast.Dict, ast.DictComp)):
                shape["dict"] = True
            if isinstance(n, ast.Subscript) and isinstance(n.slice, (ast.Slice,)):
                shape["enumerate_pairs"] = True
            if isinstance(n, ast.BinOp) and isinstance(n.op, (ast.Add, ast.Sub)):
                t = ast.dump(n)
                if "'USub'" in t or re.search(r"BinOp\(left=Name", ast.dump(n.left) if isinstance(n.left, ast.BinOp) else ""):
                    shape["index_arith"] = True
    # index arithmetic like i-1 / i+1 / len(s)-1
    shape["index_arith"] = bool(re.search(r"\w\s*[-+]\s*1\b", src)) or shape["index_arith"]
    shape["alias_mutate"] = bool(re.search(r"\.(append|pop|insert|remove|sort)\(", src))
    shape["halving"] = bool(re.search(r"//\s*2|\*\s*0\.5|/\s*2\b", src))
    # single vs nested for: walk each function, look for For directly containing For
    seen_single = seen_nested = False
    for f in fns:
        for n in ast.walk(f):
            if isinstance(n, ast.For):
                inner = any(isinstance(c, ast.For) for c in ast.walk(n) if c is not n)
                if inner:
                    seen_nested = True
                else:
                    seen_single = True
    shape["nested_for"], shape["single_for"] = seen_nested, seen_single and not seen_nested
    return shape


def inst_short(instance: str, n: int = 88) -> str:
    if len(instance) <= n:
        return instance
    cut = instance[:n].rsplit(" ", 1)[0]
    return cut + "…"


def exp_short(expected: str, n: int = 64) -> str:
    e = expected.strip().rstrip(")")  # avoid a stray closing paren in prose
    if len(e) <= n:
        return e
    return e[:n].rsplit(" ", 1)[0].rstrip(",;.") + "…"


def edge_cases(c: dict, shape: dict) -> list[str]:
    data_noun = c["topics"].split(",")[0].strip() or "input"
    out = []
    if shape["while"]:
        out.append("Termination: name the update that guarantees the loop ends, and check it on the smallest input.")
    elif shape["recursion"]:
        out.append("Base case: what is the smallest input, and does every path reach it?")
    if shape["dict"]:
        out.append("First occurrence of a key not yet in the map — the default path must produce a defined answer.")
    if shape["sort"]:
        out.append("Ties: two equal values may swap order in the input; the stated rule must pin the output.")
    out.append(f"Empty or single-item {data_noun}: decide what is returned and what must NOT be printed.")
    if shape["index_arith"]:
        out.append("Boundary positions: the first item, the last item, and the position one past each end (the i-1 / i+1 arithmetic).")
    else:
        out.append("Degenerate values: zero, negatives, and duplicates among the instance's data.")
    if shape["float"]:
        out.append("Rounding: say where values are rounded and why a last digit may differ between two correct attempts.")
    return out[:5]


def alternatives(c: dict, shape: dict) -> list[str]:
    out = []
    if c["better"] and c["better"].lower() != c["wrong_turn"].lower():
        out.append(c["better"][0].upper() + c["better"][1:] + ".")
    t = c["theme"]
    if t == "aggregation over a sequence":
        out.append("Several passes with built-in helpers (a sum here, a max there) instead of one pass with several accumulators — clearer to read, more visits over the data.")
    elif t == "recursion and dynamic programming":
        out.append("Iterative table versus recursive formulation: same recurrence, different order of filling it; the loop version cannot overflow any call stack.")
    elif shape["while"]:
        out.append("Rewrite the while-loop as a bounded for-loop over the data (or vice versa) and compare which version makes termination obvious.")
    else:
        out.append("Loop-first formulation versus a comprehension/direct-expression formulation — same result, different emphasis on state versus intent.")
    if shape["sort"]:
        out.append("Sort first, then scan once, versus scanning with extra bookkeeping and no sort: the sort pays for itself only when later steps reuse the order.")
    elif shape["dict"]:
        out.append("A plain list of (key, value) pairs instead of a map: fine at this size, but every lookup becomes a scan.")
    elif shape["recursion"]:
        out.append("An explicit stack or a plain loop instead of the recursion: identical visits, no call-stack growth.")
    else:
        out.append("A table filled by hand before any code: for the size of instance here it is both a solution and the test oracle.")
    note = cost_note(shape)
    if note:
        out.append(f"**Cost.** {note[0].upper() + note[1:]}; the alternatives shift exactly this cost.")
    return out


def pitfalls(c: dict, shape: dict) -> list[str]:
    out = []
    if c["wrong_turn"]:
        out.append(c["wrong_turn"][0].upper() + c["wrong_turn"][1:] + ".")
    if shape["while"]:
        out.append("An update path that never moves the state — the loop that never ends; test on an interval of size two.")
    if shape["dict"]:
        out.append("Reading a key before it exists (the first occurrence) instead of using the default path.")
    if shape["alias_mutate"]:
        out.append("Mutating the caller's list when the result was meant to be a fresh one — the demo where the input 'changes by itself'.")
    if shape["float"]:
        out.append("Comparing floating-point values for exact equality instead of a tolerance (or rounding at the very end, not mid-computation).")
    if shape["index_arith"]:
        out.append("Off-by-one at the boundary: the update that is correct for the middle of the data and wrong at the two ends.")
    out.append("Reporting the answer without the rule that produced it — the decision becomes uncheckable.")
    return out[:5]


def reveal(c: dict) -> str:
    th = THEMES.get(c["theme"], {})
    question = th.get("question", "What does the answer look like, and which rule produces it?")
    return "\n".join([
        "1. Display the case and start the timer (5 minutes). While students work,",
        "   circulate and read shoulders; pick one conventional attempt and one",
        "   surprising one for the board.",
        f"2. Ask first: '{question}'",
        f"3. Walk the worked instance ({inst_short(c['instance'])}) on the board",
        "   under the stated rule before any code appears; the class calls the",
        "   next state at each step.",
        f"4. Surface the wrong turn directly: '{c['wrong_turn']}' — ask the room",
        "   which quiet assumption it makes.",
        "5. Show the reference Python, run it on the worked instance, and let the",
        "   class compare with their own answers.",
        f"6. Close by naming the technique — \"{c['theme']}\" — and hand over the",
        f"   discussion prompt: **\"{c['prompt']}\"**",
    ])


def _watchfor(c: dict, shape: dict) -> str:
    """A case-specific 'what usually goes wrong in minute 1–3' sentence."""
    noun = c["topics"].split(",")[0].strip() or "input"
    if shape["while"]:
        return f"the {noun} update that looks right but stalls on the smallest instance — have them test an interval of size two"
    if shape["recursion"] and shape["branching_recursion"]:
        return f"writing the recursive calls before the base case exists — the tree that never bottoms out"
    if shape["recursion"]:
        return f"solving the big instance first instead of naming the base case for the smallest {noun}"
    if shape["dict"]:
        return f"reading {_a(noun)} {noun} key before it exists — the first occurrence needs the default path"
    if shape["sort"]:
        return f"forgetting the tie-break — two equal {noun} values must still be ordered deterministically"
    if shape["float"]:
        return f"rounding mid-computation on the {noun} values instead of once at the end"
    if shape["alias_mutate"] and shape["index_arith"]:
        return f"mutating the {noun} collection while scanning it — the shift that corrupts the remaining positions"
    if shape["alias_mutate"]:
        return f"mutating the {noun} collection the caller still holds while scanning it"
    if shape["nested_for"]:
        return f"recomputing the {noun} comparison instead of remembering what the first pass already knew"
    if shape["index_arith"]:
        return f"the boundary positions of the {noun} data — first, last, and one past each end"
    return f"a rule that reads correctly but computes on the wrong quantity in the {noun} data"


def five_minutes(c: dict, shape: dict) -> str:
    diff = c["difficulty"]
    tail = ("plan 12–15 minutes total: the 5-minute box covers restatement and the"
            " first approach only, and the discussion carries the load"
            if diff in ("Advanced", "Expert") else
            "keep the reveal inside 10 minutes so the exit question still fits")
    noun = c["topics"].split(",")[0].strip() or "input"
    watch = _watchfor(c, shape)
    return "\n".join([
        f"Minute 0–1 — **Read and analyse.** Expect inputs, outputs, and at least",
        f"one stated assumption named; the deciding quantity here is the {noun}",
        "rule. Watch for: retelling the story without extracting the decision.",
        f"Minute 1–3 — **Develop an approach.** Expect a rule or a first-step",
        f"computation on the instance; a correct rule with an arithmetic slip is",
        f"partial credit. Watch for: {watch}.",
        "Minute 3–5 — **Compare and write.** Expect the update rule or loop",
        "skeleton written down, pairs comparing orders of operations. If most",
        "pairs stall, give the structure hint from the difficulty ladder",
        "(below) whole-class rather than pair by pair.",
        f"Reveal and discuss — {tail}.",
    ])


def adaptation(c: dict) -> str:
    th = THEMES.get(c["theme"], {})
    simplify = th.get("simplify", "Shrink the instance and re-run the cycle.")
    h1 = c["moves"][0].rstrip(".") if c["moves"] else "Restate inputs, outputs, and assumptions."
    h2 = th.get("hint", "Re-derive the rule from the smallest instance.")
    return "\n".join([
        f"- **Simplify.** {simplify} Then shrink the instance: run only the first",
        f"  step of {inst_short(c['instance'], 60)} and enlarge after success.",
        f"- **Extend.** {c['ext']}",
        "- **Hints (progressive).**",
        f"  1. *Re-orient:* \"{h1}.\"",
        f"  2. *Structure:* \"{h2}\"",
        f"  3. *Near-answer:* the common wrong turn is '{c['wrong_turn']}' — undo",
        "     that choice and re-derive the step it breaks.",
    ])


def assessment(c: dict, shape: dict) -> str:
    d = c["difficulty"]
    if d in ("Beginner", "Foundational"):
        use = ("exit-ticket ready: the answer is checkable in one line, so the case"
              " doubles as a 2-minute whole-class check")
    elif d == "Intermediate":
        use = ("pair-then-solo: collect two rules per pair, compare them on the"
              " board, and score only the reasoning")
    else:
        use = ("discussion-grade: mark assumption quality and rule precision rather"
              " than the final number, and expect the full cycle to run long")
    move1 = c["moves"][1] if len(c["moves"]) > 1 else "the stated method moves"
    move2 = c["moves"][2] if len(c["moves"]) > 2 else move1
    if shape["dict"]:
        follow = ("A key appears that was never seen before: which line of your rule"
                  " handles it, and what does it output?")
    elif shape["while"]:
        follow = ("Which update line guarantees termination? Delete it mentally:"
                  " what goes wrong first?")
    elif shape["recursion"]:
        follow = "State the base case, then give an input that would never reach it if you can."
    elif shape["sort"]:
        follow = ("Two equal values swap places in the input: does the output change?"
                  " Justify with the stated rule.")
    elif shape["float"]:
        follow = ("Where does rounding happen, and which digit may differ between"
                  " two correct implementations?")
    else:
        follow = ("State the deciding rule in one sentence and apply it to a"
                  " half-size version of the worked instance.")
    return "\n".join([
        f"- **Formative use.** {use}.",
        "- **Mini-rubric (10 points).**",
        "  - *Structure (2):* inputs, outputs, and the binding constraint named before any computation.",
        f"  - *Method (3):* the stated moves executed — especially \"{move1.rstrip('.')}\"",
        f"    and \"{move2.rstrip('.')}\".",
        f"  - *Result (3):* the worked instance computed correctly ({exp_short(c['expected'])}),",
        "    and the answer survives the smallest and the boundary input.",
        "  - *Communication (2):* assumptions stated; the answer reports which rule produced it.",
        f"- **Follow-up check.** {follow}",
    ])


def build_file(c: dict) -> str:
    shape = shape_of(c["code"])
    secs = dict(c["secs"])
    secs.pop("", None)  # stray metadata section if any
    # Replacements
    secs["Reference solution (pseudocode)"] = transpile(c["code"])
    secs["Edge cases"] = "\n".join("- " + e for e in edge_cases(c, shape))
    secs["Alternative approaches"] = "\n".join("- " + a for a in alternatives(c, shape))
    secs["Common pitfalls"] = "\n".join("- " + p for p in pitfalls(c, shape))
    secs["Reveal script"] = reveal(c)
    # New sections
    secs["Five-minute teaching sequence"] = five_minutes(c, shape)
    secs["Difficulty adaptation"] = adaptation(c)
    secs["Assessment use"] = assessment(c, shape)

    parts = [c["head"].rstrip("\n")]
    for name in SECTIONS:
        if name not in secs:
            raise ValueError(f"{c['sid']}: missing section {name}")
        parts.append(f"\n## {name}\n\n{secs[name].strip()}\n")
    return "\n".join(parts) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    files = sorted(BANK.glob("cs-*.md"))
    problems = []
    wrong_missing = []
    for f in files:
        c = parse_case(f)
        if not c["wrong_turn"]:
            wrong_missing.append(c["sid"])
        try:
            new_text = build_file(c)
        except Exception as e:  # noqa: BLE001
            problems.append((c["sid"], repr(e)[:100]))
            continue
        if args.apply:
            f.write_text(new_text, encoding="utf-8")
    print(f"cases: {len(files)}; build failures: {len(problems)} {problems[:5]}")
    print(f"cases without a parsed wrong-turn sentence: {len(wrong_missing)} {wrong_missing[:8]}")
    if args.check:
        for sid in ("cs-001", "cs-036", "cs-049", "cs-081"):
            print(f"===== preview {sid} (pseudocode + reveal):")
            c = parse_case(BANK / f"{sid}.md")
            print(transpile(c["code"])[:600])
            print(reveal(c)[:600])


if __name__ == "__main__":
    main()
