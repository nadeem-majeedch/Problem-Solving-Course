# Worked Examples — Lecture 25

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Canteen Queue Log: from log to ledger](#1) | cs-097 | yes |
| [2. Screen Time by Cohort: group, then compare honestly](#2) | cs-098 | yes |
| [3. The Churn Story: pivot and percentage, denominator stated](#3) | cs-099 | yes |

---

## 1. The Canteen Queue Log: from log to ledger (case cs-097)

**Problem.** Log lines like '0812 ada lunch 6.50', '0815 bo snack 2.00', '0809 ada lunch 4.00'. Build per-person totals and the busiest item - decide your cleaning rules first.

**Analysis.** Raw logs are noisy: timestamps may be unsorted, items repeated, prices float. Decide before coding: item names are exact (no normalisation), a 'busiest' tie breaks alphabetically, money is rounded only at print time (never accumulate rounded values). Then the pipeline is: parse -> group -> aggregate -> rank.

**Algorithm.**
1. split each line into (time, person, item, amount)
2. accumulate per-person totals in a dictionary
3. count item occurrences in a second dictionary
4. rank: busiest item with alphabetical tie-break

**Pseudocode.**

```
    totals <- {}; items <- {}
    FOR each log line
        totals[person] += amount
        items[item]++
    busiest <- item with max count (tie: smaller name)
    WRITE totals, busiest
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
lines = ["0812 ada lunch 6.50", "0815 bo snack 2.00", "0809 ada lunch 4.00"]
totals, items = {}, {}
for ln in lines:
    _t, person, item, amt = ln.split()
    totals[person] = totals.get(person, 0.0) + float(amt)
    items[item] = items.get(item, 0) + 1
busiest = sorted(items.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
print(round(totals["ada"], 2), busiest)
# expect: 10.5 lunch
```

**Trace (dry run).** ada: 6.50 + 4.00 = 10.50; bo: 2.00. Items: lunch x2, snack x1 -> 'lunch'. Rounding happens only in the print - the accumulated total is 10.5 exactly here, but with .10+.20-style inputs the print-time rounding is what keeps the ledger honest.

**Expected output.** ada total 10.50; busiest item 'lunch' (2 visits)

**Edge cases.** Malformed line (three fields) -> decide: skip with a flag, never crash mid-log. Tie on item counts -> alphabetical rule already coded. Zero-visitors (empty log) -> empty report, not a KeyError. These three decisions ARE the specification.

**Complexity.** O(n) for n log lines; the ranking is O(u log u) over distinct items.

## 2. Screen Time by Cohort: group, then compare honestly (case cs-098)

**Problem.** (cohort, minutes) pairs: (A, 120), (B, 90), (A, 180), (B, 110), (A, 60). Compare mean screen time per cohort - and state what the comparison cannot tell you.

**Analysis.** Group by cohort, average within. But the honest part: A's mean (120) rides on three points, B's (100) on two - and a mean hides one extreme value. The deliverable is the comparison PLUS its limits; a number without its caveats is a misreport.

**Algorithm.**
1. group minutes by cohort into lists
2. mean = sum/len per cohort
3. report n per cohort alongside the mean
4. state limits: small n, no spread shown

**Pseudocode.**

```
    groups <- map cohort -> list of minutes
    FOR each cohort
        mean <- sum / count
        WRITE cohort, count, mean
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
rows = [("A", 120), ("B", 90), ("A", 180), ("B", 110), ("A", 60)]
groups = {}
for c, m in rows:
    groups.setdefault(c, []).append(m)
for c in sorted(groups):
    v = groups[c]
    print(c, len(v), sum(v) / len(v))
# expect: A 3 120.0
# expect: B 2 100.0
```

**Trace (dry run).** A: (120+180+60)/3 = 120. B: (90+110)/2 = 100. The 180 inflates A - median A is 120 here (no distortion), but with rows (120, 130, 600) the mean 283 would mislead; median 130 would not. Reporting n=3 and n=2 is what lets a reader judge.

**Expected output.** A: mean 120 (n=3); B: mean 100 (n=2)

**Edge cases.** Cohort with one member -> mean defined but fragile - flag it. Empty cohort -> division by zero: exclude with a note, never print nan. What the data cannot say: causation (screen time causes nothing here), cohort mix, or weekend/weekday effects.

**Complexity.** O(n) grouping, O(g) reporting - trivial cost, the care is free but must be spent.

## 3. The Churn Story: pivot and percentage, denominator stated (case cs-099)

**Problem.** Cohorts: A: 40 stayed, 10 left; B: 25 stayed, 25 left. Which cohort has the worse churn rate, and what exactly does the percentage measure?

**Analysis.** Rate = leavers / (leavers + stayers) per cohort. A: 10/50 = 20%; B: 25/50 = 50%. The denominator choice is the whole story: leavers per total (churn rate) differs from leavers per stayer (odds). Saying 'B churns worse' is only true for the stated denominator - write the denominator on the slide.

**Algorithm.**
1. per cohort: total = stayed + left
2. rate = left / total
3. compare rates, not raw counts
4. name the denominator in the conclusion

**Pseudocode.**

```
    FOR each cohort (stayed, left)
        total <- stayed + left
        rate <- left / total
        WRITE cohort, rate as percent
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
cohorts = {"A": (40, 10), "B": (25, 25)}
for c, (stayed, left) in sorted(cohorts.items()):
    total = stayed + left
    print(c, f"{left / total:.0%}", total)
# expect: A 20% 50
# expect: B 50% 50
```

**Trace (dry run).** A: 10/50 = 20%. B: 25/50 = 50%. Both cohorts have 50 members - convenient: raw counts (25 vs 10 leavers) and rates agree in direction here. With sizes 50 vs 5, raw counts would have flipped the story - that is why the rate (and its stated denominator) is the honest unit.

**Expected output.** A 20% churn, B 50% churn (denominator: cohort members)

**Edge cases.** Zero-member cohort -> undefined rate, exclude with a note. Small cohorts (n=5) give unstable rates - 2/5 = 40% is one person from 60%. Percentages of percentages and 'percentage points' get conflated - lecture 28 dissects that trap.

**Complexity.** O(1) per cohort; the intellectual work is in the denominator, not the arithmetic.
