# Worked Examples — Lecture 21

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Course Finder, revisited: sorted catalogue](#1) | cs-066 | yes |
| [2. The First Bad Version: find the boundary](#2) | cs-082 | yes |
| [3. Book Allocation: binary search on the answer](#3) | cs-083 | yes |

---

## 1. The Course Finder, revisited: sorted catalogue (case cs-066)

**Problem.** The catalogue from lecture 17 is now sorted by code: CS1, CS3, DS2. Find 'DS2' in at most two comparisons.

**Analysis.** Sortedness buys power: one comparison against the middle discards half the data. 3 entries -> middle CS3 -> 'DS2' > 'CS3' -> only DS2 remains. The loop keeps halving: the invariant 'if the target exists, it lies within [lo, hi]' survives every step.

**Algorithm.**
1. lo at 0, hi at the last index
2. probe the middle element m
3. equal -> found; too small -> lo = m+1; too big -> hi = m-1
4. lo > hi -> the target is absent

**Pseudocode.**

```
    lo <- 0; hi <- last
    WHILE lo <= hi
        m <- middle of lo..hi
        IF a[m] = target RETURN m
        IF a[m] < target THEN lo <- m + 1 ELSE hi <- m - 1
    RETURN 'absent'
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
codes = ["CS1", "CS3", "DS2"]
lo, hi = 0, len(codes) - 1
probes = 0
found = None
while lo <= hi:
    m = (lo + hi) // 2
    probes += 1
    if codes[m] == "DS2":
        found = m
        break
    if codes[m] < "DS2":
        lo = m + 1
    else:
        hi = m - 1
print(found, probes)
# expect: 2 2
```

**Trace (dry run).** lo=0, hi=2 -> middle 1 ('CS3'). 'DS2' > 'CS3' -> lo=2. lo=hi=2 -> middle 2 ('DS2') -> found at index 2 after two probes; the print confirms probes=2 and found=2. Half the catalogue discarded per probe.

**Expected output.** found at index 2 after 2 probes

**Edge cases.** Absent target: 'CS2' between CS1 and CS3 -> lo and hi cross -> 'absent' after log2(n) probes. One element -> one probe. The midpoint must never be computed with rounding that excludes an endpoint - the (lo+hi)//2 idiom, tested against both odd and even lengths.

**Complexity.** O(log n): a million sorted entries need 20 probes. Linear scan needed a million. That is the sort of factor that changes what is feasible.

## 2. The First Bad Version: find the boundary (case cs-082)

**Problem.** Commits 1..10; every commit from some point on is bad. Badness probe answers True/False. Locate the first bad commit in as few probes as possible.

**Analysis.** The predicate 'is bad' is monotone: F F F T T T. Any monotone predicate over a sorted order is binary-searchable - the target is not a value but the boundary. Maintain the invariant: lo is always a good-or-unknown position, hi is always bad-or-unknown.

**Algorithm.**
1. lo at 1, hi at n
2. probe the middle; bad -> hi = m (boundary at or left)
3. good -> lo = m + 1 (boundary strictly right)
4. lo = hi -> that is the first bad commit

**Pseudocode.**

```
    lo <- 1; hi <- n
    WHILE lo < hi
        m <- middle
        IF is_bad(m) THEN hi <- m ELSE lo <- m + 1
    RETURN lo
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
bad_from = 7

def is_bad(m):
    return m >= bad_from

lo, hi = 1, 10
while lo < hi:
    m = (lo + hi) // 2
    if is_bad(m):
        hi = m
    else:
        lo = m + 1
print(lo)
# expect: 7
```

**Trace (dry run).** lo=1 hi=10 m=5: good -> lo=6. m=8: bad -> hi=8. lo=6 hi=8 m=7: bad -> hi=7. lo=6 hi=7 m=6: good -> lo=7. lo=hi=7 -> answer 7. Four probes instead of seven linear checks - and 20 probes instead of a million for n=10^6.

**Expected output.** first bad commit: 7

**Edge cases.** All good (bad_from = n+1) -> the loop ends with lo = n+1, outside 1..n - the caller must decide whether that means 'no bad version'. All bad -> answer 1. The shrink must guarantee progress: hi = m (not m-1) because m itself may be the boundary.

**Complexity.** O(log n) probes - the classic 'binary search on the answer' template that returns in lecture 30 (optimisation formulations).

## 3. Book Allocation: binary search on the answer (case cs-083)

**Problem.** Book pages 10, 20, 30, 40 and 2 students; each student gets a contiguous run. Minimise the largest share.

**Analysis.** Feasibility is monotone: if a largest-share cap of X works, any bigger cap works. So binary search X between max(pages) (nobody can hold a whole book otherwise) and sum(pages) (one student holds all). The feasibility test is a greedy sweep - two ideas composing, exactly the lecture's point.

**Algorithm.**
1. feasible(cap): sweep books, start a new student when the cap would overflow
2. count students used; feasible iff <= 2
3. binary search the smallest feasible cap

**Pseudocode.**

```
    FUNCTION feasible(cap)
        students <- 1; load <- 0
        FOR each book
            IF load + book > cap THEN students++; load <- 0
            load <- load + book
        RETURN students <= 2
    binary search smallest cap with feasible(cap)
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
pages = [10, 20, 30, 40]

def feasible(cap, students_max=2):
    students, load = 1, 0
    for p in pages:
        if load + p > cap:
            students += 1
            load = 0
        load += p
    return students <= students_max

lo, hi = max(pages), sum(pages)
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid
    else:
        lo = mid + 1
print(lo)
# expect: 60
```

**Trace (dry run).** cap=60: load 10,30,60 -> 40 overflows -> student 2 gets 40 -> 2 students, feasible. cap=59: 10,30 -> 40 overflows at 30+40 -> 60 > 59, so student 1 holds 40, student 2 holds 40... recount: 10+20+30 = 60 > 59 -> split after 20: 30, then 30+40 = 70 > 59 -> third student -> infeasible. Answer 60 (shares 60 and 40).

**Expected output.** minimum largest share: 60

**Edge cases.** More students than books -> each gets one book, answer max(pages). One student -> sum(pages). The sweep's greedy is provably optimal for this feasibility test - if it were not, binary search on the answer would still be sound but the test would lie.

**Complexity.** O(n log(sum)) - the log factor from the cap search, the linear factor from each feasibility sweep.
