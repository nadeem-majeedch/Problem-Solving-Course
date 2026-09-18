# Worked Examples — Lecture 32

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Library Robot: capstone run-through](#1) | cs-125 | yes |
| [2. The Open-Day Planner: capstone under time pressure](#2) | cs-126 | yes |
| [3. The Data Clinic: capstone synthesis](#3) | cs-127 | yes |

---

## 1. The Library Robot: capstone run-through (case cs-125)

**Problem.** A robot returns books: requests (minute, shelf) pairs arrive; the robot serves shelves in increasing minute order, one per minute, and idle-waits otherwise. Compute total idle time and the busiest shelf. Full method: model, plan, solve, test, present.

**Analysis.** The capstone rehearses the whole toolbox on one problem: model (a timeline plus a shelf multiset), decompose (serve loop, idle accounting, shelf tally), choose structures (dictionary for counts, pointer for the clock), test (edge cases: no requests, ties, gaps), present (state assumptions, show the trace, defend the choice).

**Algorithm.**
1. sort requests by minute
2. clock advances: serve the earliest request; idle-fill gaps
3. tally shelf visits in a dictionary
4. busiest shelf = max count with a stated tie rule

**Pseudocode.**

```
    sort by minute
    clock <- 0; idle <- 0; tally <- {}
    FOR each request (m, shelf)
        IF m > clock THEN idle += m - clock; clock <- m
        tally[shelf]++ ; clock += 1
    busiest <- argmax tally (tie: smallest shelf id)
    WRITE idle, busiest
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
requests = [(2, "A"), (3, "B"), (7, "A"), (7, "C"), (9, "B")]
requests.sort()
clock = idle = 0
tally = {}
for m, shelf in requests:
    if m > clock:
        idle += m - clock
        clock = m
    tally[shelf] = tally.get(shelf, 0) + 1
    clock += 1
busiest = sorted(tally.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
print(idle, busiest)
# expect: 5 A
```

**Trace (dry run).** clock 0 -> request at 2: idle 2, clock 3. Serve B at 3 (tie with clock: no idle), clock 4. Request at 7: idle 3 (4->7), serve A, clock 8; serve C at 8, clock 9; serve B at 9, clock 10. Tally: A2, B2, C1 -> tie A/B broken alphabetically -> A. Idle total 2 + 3 = 5 minutes.

**Expected output.** total idle 3 minutes; busiest shelf A (tie with B, alphabetical)

**Edge cases.** Empty requests -> idle 0 and no busiest - print 'none'. Two requests at the same minute: sequential service per the one-per-minute rule (state it). Requests arriving during service wait for the NEXT free minute - does your model say that? Capstone assumption-hunting is graded.

**Complexity.** O(k log k) for the sort, O(k) service; the presentation, not the code, is the exam.

## 2. The Open-Day Planner: capstone under time pressure (case cs-126)

**Problem.** Six talks with (start, end, room-needed or None), rooms R1 R2. Fit every talk or report the minimal set to drop. Twenty minutes, method marks for the plan.

**Analysis.** This is interval scheduling plus a resource dimension: sort by end, assign each talk to a free room, drop when both rooms are busy. Greedy by end time remains provably good for 'fit the most talks'; the room constraint adds bookkeeping, not a new algorithm. Under time pressure, the written plan earns marks before any code runs.

**Algorithm.**
1. sort talks by end time
2. two rooms -> two 'free-at' clocks
3. assign each talk to a room free by its start; else drop it (log it)
4. report the schedule and the drop list

**Pseudocode.**

```
    sort by end
    rooms <- [0, 0]
    FOR each talk (s, e)
        pick room with min free-at
        IF free_at <= s THEN assign; free_at <- e
        ELSE drop WITH reason
    WRITE schedule, drops
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
talks = [(9, 10), (9.5, 10.5), (10, 11), (10.5, 11.5), (11, 12), (11.5, 12.5)]
talks = sorted(talks, key=lambda t: t[1])
rooms = [0.0, 0.0]
placed, dropped = [], []
for idx, (s, e) in enumerate(talks):
    r = rooms.index(min(rooms))
    if rooms[r] <= s:
        rooms[r] = e
        placed.append((s, e))
    else:
        dropped.append((s, e))
print(len(placed), len(dropped))
# expect: 6 0
```

**Trace (dry run).** Sorted by end, starts 9, 9.5, 10, 10.5, 11, 11.5 - each talk fits the room freed by the previous (or the second room when they overlap). All 6 placed, 0 dropped. The teaching variant: add a 7th talk (9.2, 10.2) and watch the first drop appear - then argue whether greedy-drop is minimal here.

**Expected output.** all 6 talks placed; nothing dropped (with these arrivals)

**Edge cases.** Talk longer than the day -> immediate drop. Equal end times: order among them is a tie policy. The 'minimal drop set' question is a different (harder) objective than 'fit greedily' - a capstone-grade distinction to articulate.

**Complexity.** O(n log n) sort + O(n x rooms) placement; the marks are in the plan write-up.

## 3. The Data Clinic: capstone synthesis (case cs-127)

**Problem.** One messy table: missing cells, a duplicated row, one impossible value, and a mixed-case category. Clean it with an audit trail, then produce ONE honest summary sentence. All semester, one page.

**Analysis.** Every Block IV skill in sequence: parse, validate, dedupe, normalise categories, choose a missing-value policy, drop-and-log the impossible, aggregate, and summarise with denominator stated. The rubric rewards the audit trail as much as the final number - silent cleaning is failure here.

**Algorithm.**
1. dedupe exact duplicate rows (log count)
2. normalise category case to a canonical form
3. missing -> chosen policy, documented
4. impossible values -> drop with reason
5. aggregate; summarise with n stated

**Pseudocode.**

```
    seen <- set; clean <- []
    FOR each row
        IF row in seen THEN log 'duplicate'; skip
        normalise case
        IF value missing THEN apply policy
        IF value impossible THEN log drop; skip
        append row
    summary <- aggregate(clean)
    WRITE summary WITH n
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
rows = [("Ada", "CS", 80), ("ada", "cs", 80), ("Bo", "DS", None), ("Cy", "DS", 150)]
seen, clean, log = set(), [], []
for name, cat, val in rows:
    key = (name.lower(), cat.lower(), val)
    if key in seen:
        log.append(f"duplicate {name}")
        continue
    seen.add(key)
    if val is None:
        log.append(f"missing {name}")
        continue
    if not 0 <= val <= 100:
        log.append(f"impossible {name}: {val}")
        continue
    clean.append((name.title(), cat.upper(), val))
print(clean, log)
# expect: [('Ada', 'CS', 80)] ['duplicate ada', 'missing Bo', 'impossible Cy: 150']
```

**Trace (dry run).** Row 2 duplicates row 1 after normalisation -> logged. Bo's missing score -> policy: drop and log (never zero-fill silently). Cy's 150 -> impossible -> dropped. One clean row remains: the summary 'Ada, CS, 80 (n=1; 3 rows removed: 1 dup, 1 missing, 1 impossible)' is honest BECAUSE the log is part of the output.

**Expected output.** 1 clean row; audit log: 1 duplicate, 1 missing, 1 impossible

**Edge cases.** Everything-dirty table -> zero rows: report 'no data', not an average of nothing. Normalisation must precede dedupe or duplicates hide. 'Ada CS 80' vs 'Ada CS 85' is NOT a duplicate - keys include the value.

**Complexity.** O(n); the grade lives in what the log says, not what the loop costs.
