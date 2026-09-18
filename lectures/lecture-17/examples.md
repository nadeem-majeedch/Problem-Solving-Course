# Worked Examples — Lecture 17

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. Find the First Freeze: scan with early exit](#1) | cs-065 | yes |
| [2. The Course Finder: linear search on an unsorted catalogue](#2) | cs-066 | yes |
| [3. Peak Finding: the first descent marks a peak](#3) | cs-068 | yes |

---

## 1. Find the First Freeze: scan with early exit (case cs-065)

**Problem.** Daily temperatures are 12, 8, 3, -1, -4, 2 degrees. On which day index does the first freeze (temperature at or below 0) occur?

**Analysis.** A linear scan visits days in order and stops at the first hit. The stopping is the whole point: 'first' means we must not keep looking after we find it. The answer is an index, so we track position, not just value.

**Algorithm.**
1. walk the list from index 0
2. at each day, test temperature <= 0
3. on the first hit: record the index and stop
4. if the walk ends with no hit: report 'no freeze'

**Pseudocode.**

```
    idx <- NONE
    FOR i from 0 to length(temps) - 1
        IF temps[i] <= 0 THEN
            idx <- i
            BREAK
    IF idx = NONE THEN WRITE 'no freeze' ELSE WRITE idx, temps[idx]
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
temps = [12, 8, 3, -1, -4, 2]
idx = None
for i, t in enumerate(temps):
    if t <= 0:
        idx = i
        break
print(idx, temps[idx])
# expect: 3 -1
```

**Trace (dry run).** i=0: 12 > 0, continue. i=1: 8 > 0. i=2: 3 > 0. i=3: -1 <= 0 -> idx=3, break. Days 4 and 5 are never examined - that is the early exit paying off.

**Expected output.** first freeze at index 3 (temperature -1)

**Edge cases.** No freeze at all -> idx stays None; the report must say 'no freeze', not crash on None. Everything frozen -> index 0. Exactly 0 degrees counts as a freeze ('at or below' - say it). Empty season -> 'no freeze'.

**Complexity.** O(n) worst case, but best case O(1) when the freeze is early; early exit is free - take it.

## 2. The Course Finder: linear search on an unsorted catalogue (case cs-066)

**Problem.** A catalogue holds (code, title) pairs in no particular order. Find the title for code 'DS2', and define the behaviour for an unknown code.

**Analysis.** Unsorted data leaves no clever move: any correct algorithm must potentially look at every entry, so linear search is optimal here. The interesting design decision is the miss case - return a sentinel ('not offered') rather than crash.

**Algorithm.**
1. for each (code, title) pair in order
2. if the code matches: return the title
3. after the loop: return the 'not offered' sentinel

**Pseudocode.**

```
    FUNCTION find(code)
        FOR each (c, title) in catalogue
            IF c = code THEN RETURN title
        RETURN 'not offered'
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
catalogue = [("CS1", "Problem Solving"), ("DS2", "Statistics"), ("CS3", "Systems")]

def find(code):
    for c, title in catalogue:
        if c == code:
            return title
    return "not offered"

print(find("DS2"), find("XX9"))
# expect: Statistics not offered
```

**Trace (dry run).** find('DS2'): CS1 no, DS2 yes -> 'Statistics' (two comparisons). find('XX9'): all three fail -> sentinel. A miss always costs the full scan - n comparisons.

**Expected output.** Statistics / not offered

**Edge cases.** Empty catalogue -> 'not offered'. Duplicate codes -> the first wins; say so if it matters. If the catalogue were sorted, binary search (lecture 21) would cut the cost to O(log n) - but sorting costs too, so 'unsorted, scan once' can still win overall.

**Complexity.** O(n) time, O(1) space; already optimal for unsorted input.

## 3. Peak Finding: the first descent marks a peak (case cs-068)

**Problem.** In the values 1, 3, 8, 4, 2 find a peak - a value at least as large as its neighbours.

**Analysis.** Walk until the sequence stops rising: the moment a[i] >= a[i+1], position i is a peak (it is >= the next element and, because we kept rising until now, > the previous one). If the walk never descends, the last element is the peak.

**Algorithm.**
1. compare each element with its right neighbour
2. first non-rise -> that index is a peak
3. no non-rise after the full walk -> the last index is a peak

**Pseudocode.**

```
    FOR i from 0 to length(a) - 2
        IF a[i] >= a[i+1] THEN WRITE a[i]; STOP
    WRITE a[last]
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
a = [1, 3, 8, 4, 2]
peak = None
for i in range(len(a) - 1):
    if a[i] >= a[i + 1]:
        peak = i
        break
if peak is None:
    peak = len(a) - 1
print(a[peak])
# expect: 8
```

**Trace (dry run).** i=0: 1 < 3 rise. i=1: 3 < 8 rise. i=2: 8 >= 4 -> peak index 2, value 8. The walk touches 3 comparisons of 5 elements; worst case (strictly rising) touches all.

**Expected output.** a peak is 8 (at index 2)

**Edge cases.** Strictly increasing -> last element is the peak (handled by the fallback). Single element -> it is trivially a peak; the loop range is empty and the fallback fires. Plateaus (equal neighbours): '>= ' accepts the plateau's left edge as a peak - a policy to state.

**Complexity.** O(n) here; lecture 21 revisits this problem with binary search for O(log n) - a first taste of the same problem having algorithms of different cost.
