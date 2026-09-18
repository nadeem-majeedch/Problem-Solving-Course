# Worked Examples — Lecture 06

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. Trace the tally: loop reasoning on paper](#1) | cs-021 | no |
| [2. Nested loops, traced honestly](#2) | cs-023 | no |

---

## 1. Trace the tally: loop reasoning on paper (case cs-021)

**Problem.** Sum the numbers 1..12, skipping multiples of 3. Predict first, then trace the loop table.

**Analysis.** The loop has one decision inside: include or skip. A trace table with one row per iteration (n, condition, total) turns prediction into evidence. The condition n mod 3 != 0 does the filtering.

**Algorithm.**
1. total <- 0
2. for n in 1..12: if n mod 3 != 0 then total <- total + n
3. return total

**Pseudocode.**


    total <- 0
    FOR n FROM 1 TO 12
        IF n MOD 3 != 0 THEN
            total <- total + n
    WRITE total


**Trace (dry run).** Included: 1, 2, 4, 5, 7, 8, 10, 11. Running total: 1, 3, 7, 12, 19, 27, 37, 48. Skipped at n = 3, 6, 9, 12. Final 48 - matching the reference output.

**Expected output.** 48

**Edge cases.** Limit 0: the loop body never runs, total 0. A multiple of 3 exactly at the boundary (12 here) is skipped - the boundary value is the test that catches >= vs > confusion.

**Complexity.** O(limit). Skipped items cost a condition check but no addition - skipping is not free.

## 2. Nested loops, traced honestly (case cs-023)

**Problem.** With n = 4 rows and the rule 'star when column <= row else dot', what does the double loop print? Trace row 2 by hand.

**Analysis.** Outer loop: rows 1..n. Inner loop: columns 1..2r - 1 - the count grows with r, which is exactly why the trace matters. Character = star if c <= r else dot. Hand-tracing row 2: c runs 1, 2, 3, giving star, star, dot.

**Algorithm.**
1. for each row r in 1..n
2.   line <- empty
3.   for c in 1..2r - 1: append star if c <= r else dot
4.   print line

**Pseudocode.**


    FOR r FROM 1 TO n
        line <- ""
        FOR c FROM 1 TO 2*r - 1
            IF c <= r THEN line <- line + "*"
            ELSE line <- line + "."
        WRITE line


**Trace (dry run).** r = 1: c = 1, giving '*'. r = 2: c = 1, 2, 3, giving '**.'. r = 3: c = 1..5, giving '***..'. r = 4: c = 1..7, giving '****...'. The output matches the reference exactly.

**Expected output.** four lines: * then **. then ***.. then ****...

**Edge cases.** n = 0 prints nothing. The inner bound 2r - 1 is where most wrong traces go: it depends on r, so each row is longer than the last. Predict the shape before tracing.

**Complexity.** O(n^2) characters - the sum 1 + 3 + 5 + ... + (2n - 1) = n^2 is the doubling-grid fact from the lecture.

---

**Python companion.** The nested-grid count from today's shading exercise, executing:

```python
count = 0
for row in range(4):
    for col in range(3):
        count += 1
print(count)
# expect: 12
```
