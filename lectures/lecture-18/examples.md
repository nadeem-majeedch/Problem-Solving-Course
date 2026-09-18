# Worked Examples — Lecture 18

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. Rank the Leaderboard: sort with a two-part key](#1) | cs-069 | yes |
| [2. The Meeting Merge: the merge step by hand](#2) | cs-070 | yes |
| [3. Closest Pair, Small n: brute force and its price](#3) | cs-071 | yes |

---

## 1. Rank the Leaderboard: sort with a two-part key (case cs-069)

**Problem.** Players: ada 90, bo 75, cy 90. Rank by score, highest first; ties broken alphabetically.

**Analysis.** The tie rule turns a one-key sort into a two-key sort: primary -score (negation flips descending to ascending), secondary name. Stating the tie policy is part of the specification, not an implementation detail.

**Algorithm.**
1. build (name, score) records
2. sort with key (-score, name)
3. the negated score gives descending order without a custom comparator

**Pseudocode.**

```
    ranked <- sort players by (-score, name)
    WRITE ranked
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
players = [("ada", 90), ("bo", 75), ("cy", 90)]
ranked = sorted(players, key=lambda p: (-p[1], p[0]))
print(ranked)
# expect: [('ada', 90), ('cy', 90), ('bo', 75)]
```

**Trace (dry run).** Keys: ada (-90, 'ada'), bo (-75, 'bo'), cy (-90, 'cy'). Ascending key order puts -90 before -75; the -90 pair is ordered by name: ada, cy. bo trails.

**Expected output.** ada (90), cy (90), bo (75)

**Edge cases.** All equal scores -> pure alphabetical order. Negative scores work (negation still flips). Non-numeric 'scores' (like grade letters) cannot be negated - then sort in two stable passes instead (name first, then score) and rely on sort stability.

**Complexity.** O(n log n) comparisons - the sorting cost dominates; the key is computed once per element.

## 2. The Meeting Merge: the merge step by hand (case cs-070)

**Problem.** Two rooms' meeting start times are already sorted: 9, 10, 12 and 9.5, 11. Produce one sorted list.

**Analysis.** Both inputs are sorted, so we never need to compare anything except the two front items: repeatedly take the smaller front. This is the merge step of mergesort - worth knowing by hand before seeing the full sort.

**Algorithm.**
1. keep one finger on each list
2. compare fronts; move the smaller into the output
3. when one list runs out, append the rest of the other

**Pseudocode.**

```
    WHILE both lists non-empty
        IF front(a) <= front(b) THEN move front(a) to output
        ELSE move front(b) to output
    APPEND leftovers
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
a = [9, 10, 12]
b = [9.5, 11]
merged = []
i = j = 0
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1
merged.extend(a[i:])
merged.extend(b[j:])
print(merged)
# expect: [9, 9.5, 10, 11, 12]
```

**Trace (dry run).** 9 <= 9.5 take 9. 10 > 9.5 take 9.5. 10 <= 11 take 10. 12 > 11 take 11. b exhausted -> append leftover [12]. Five comparisons for five outputs.

**Expected output.** 9, 9.5, 10, 11, 12

**Edge cases.** An empty room -> the other list passes through unchanged (the extend handles it). Equal times: '<=' takes from a first - with records, that keeps a's entries ahead, which is what 'stable' means. Unsorted input would break the invariant: merge assumes sorted.

**Complexity.** O(n + m) - linear in the output size; no element is compared twice.

## 3. Closest Pair, Small n: brute force and its price (case cs-071)

**Problem.** Points (0,0), (3,4), (1,1). Which two are closest?

**Analysis.** Three points give three pairs - try them all. The brute-force pattern (all pairs, keep the best) is correct and, for small n, unbeatable in simplicity. Its cost grows as n squared, which is the number to keep in mind.

**Algorithm.**
1. for every pair i < j: compute the distance
2. keep the smallest seen so far (champion)
3. report the champion pair

**Pseudocode.**

```
    best <- NONE
    FOR i from 0 to n-1
        FOR j from i+1 to n-1
            d <- distance(p[i], p[j])
            IF best = NONE OR d < best.d THEN best <- (d, i, j)
    WRITE best pair
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
points = [(0, 0), (3, 4), (1, 1)]
best = None
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        d = (dx * dx + dy * dy) ** 0.5
        if best is None or d < best[0]:
            best = (d, points[i], points[j])
print(best[1], best[2])
# expect: (0, 0) (1, 1)
```

**Trace (dry run).** Pairs: (0,0)-(3,4): 5.0. (0,0)-(1,1): ~1.414 -> new champion. (3,4)-(1,1): ~3.606, not better. Champion stands: the origin pair. Squaring distances instead of sqrt-ing is a common micro-optimisation - the ordering is the same.

**Expected output.** closest pair: (0, 0) and (1, 1)

**Edge cases.** Two points -> that pair, trivially. Duplicate points -> distance 0 wins. Ties -> the first pair encountered wins (say so). For large n this is O(n^2); divide-and-conquer does better, but that machinery is not worth it at n = 3.

**Complexity.** O(n^2) pairs - fine for a classroom, hopeless for a million points; knowing WHERE the wall is, is the lecture's point.
