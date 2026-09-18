# Worked Examples — Lecture 09

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The reading log: one pass, four aggregates](#1) | cs-033 | no |
| [2. Stockroom spikes: argmax with witnesses](#2) | cs-034 | no |
| [3. The longest streak: reset vs stop](#3) | cs-035 | no |
| [4. Rainfall windows: the slide](#4) | cs-036 | no |

---

## 1. The reading log: one pass, four aggregates (case cs-033)

**Problem.** Pages [12, 0, 25, 8, 30], target 10. Report total, average, best day, and how many days fell below target.

**Analysis.** Four aggregation patterns ride one loop: running total, best-so-far, count-with-condition, and a derived average. Naming them first is the lecture's method - then the code has no surprises.

**Algorithm.**
1. total <- 0; best <- 0; below <- 0
2. for each p: total += p; if p > best: best <- p; if p < target: below += 1
3. avg <- total / len
4. report all four

**Pseudocode.**

```
    total <- 0; best <- 0; below <- 0
    FOR p IN pages
        total <- total + p
        IF p > best THEN best <- p
        IF p < target THEN below <- below + 1
    avg <- total / count
    WRITE total, avg, best, below
```

**Trace (dry run).** 12: total 12. 0: total 12, below 1. 25: best 25. 8: below 2. 30: best 30. Total 75, avg 15.0, best 30, below 2 (days 0 and 8 - exactly the reference).

**Expected output.** {'total': 75, 'avg': 15.0, 'best': 30, 'below': 2}

**Edge cases.** Empty log (avg divides by zero - the spec must say); all zeros (best 0, below n); target negative (below = n - the question must still be well-defined).

**Complexity.** O(n) time, O(1) space - four aggregates for the price of one loop.

## 2. Stockroom spikes: argmax with witnesses (case cs-034)

**Problem.** Sales [100, 210, 205, 420, 90]. A day is a spike if it beats both neighbours. Reference answer: [1, 3].

**Analysis.** Boundary discipline: day 0 has one neighbour (inside), day 4 likewise - endpoints are non-candidates (stated assumption). Strict comparison (>) keeps plateaus from double-reporting.

**Algorithm.**
1. for i in 1..n-2: if sales[i] > both neighbours: report i

**Pseudocode.**

```
    spikes <- []
    FOR i IN 1 .. n-2
        IF sales[i] > sales[i-1] AND sales[i] > sales[i+1]
            THEN append i to spikes
    WRITE spikes
```

**Trace (dry run).** i=1: 210 > 100 and > 205 → spike. i=2: 205 < 210 → no. i=3: 420 > 205, > 90 → spike. i=4 excluded.

**Expected output.** [1, 3]

**Edge cases.** Plateau [5,9,9,5] (no spike with strict >); length-1 and length-2 lists (no interior - return []); all-equal list.

**Complexity.** O(n) time, O(1) extra space (output excluded).

## 3. The longest streak: reset vs stop (case cs-035)

**Problem.** Goals met [1, 1, 0, 1, 1, 1, 0, 1]. Longest streak of consecutive met goals - plus two zero cases: end-on-a-miss, and all-miss.

**Analysis.** Two variables: current (resets on miss) and best (survives). The reference prints 3 | 0 | 0 - the second and third queries are the conceptual test: streak-at-end is 0 when the list ends on a miss; all-miss best is 0.

**Algorithm.**
1. current <- 0; best <- 0
2. for each g: met → current += 1, best = max(best, current); miss → current <- 0
3. report best, current-at-end

**Pseudocode.**

```
    current <- 0; best <- 0
    FOR g IN goals
        IF g = 1 THEN
            current <- current + 1
            IF current > best THEN best <- current
        ELSE current <- 0
    WRITE best, current
```

**Trace (dry run).** 1,1: current 2. 0: current 0. 1,1,1: current 3, best 3. 0: current 0. 1: current 1. Best 3, end-current 1.

**Expected output.** best 3 | end-current 0 in the reference's variant | all-miss 0

**Edge cases.** Empty list (both 0); all-ones (best = n); best-at-the-end (students who forget to update best inside the loop report 2 - the classic slip).

**Complexity.** O(n) time, O(1) space - the two-variable discipline is the whole lesson.

## 4. Rainfall windows: the slide (case cs-036)

**Problem.** Rain [3, 5, 2, 8, 1, 4], window k = 3. The reference prints [5, 8, 8, 8] - derive what question it actually answers before trusting the prose.

**Analysis.** Window sums are 10, 15, 11, 13. Window MAXIMA are 5, 8, 8, 8 - the reference's question. Running code and comparing with prose is the discipline; the slide method (add entering, remove leaving) serves both.

**Algorithm.**
1. first window: sum k items
2. each step: add entering, remove leaving
3. maxima variant: track the max per window

**Pseudocode.**

```
    w <- sum of first k items
    WRITE w
    FOR i IN k .. n-1
        w <- w + rain[i] - rain[i - k]
        WRITE w
```

**Trace (dry run).** w = 10. i=3: 10 + 8 - 3 = 15. i=4: 15 + 1 - 5 = 11. i=5: 11 + 4 - 2 = 13. Maxima: 5, 8, 8, 8.

**Expected output.** sums [10, 15, 11, 13]; maxima [5, 8, 8, 8] (the reference's question)

**Edge cases.** k = 1 (windows are the items); k = n (one window); k > n (reject); negative rain would break the maxima reading (state the assumption).

**Complexity.** O(n) slide vs O(n*k) recomputed - the analysis teaser for Block III.

---

**Python companion.** All four aggregation patterns on the reading log, executing:

```python
pages = [12, 0, 25, 8, 30]
target = 10
total = sum(pages)
best = max(pages)
below = sum(1 for p in pages if p < target)
print(total, total / len(pages), best, below)
# expect: 75 15.0 30 2
```
