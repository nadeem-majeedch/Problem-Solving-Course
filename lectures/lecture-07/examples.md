# Worked Examples — Lecture 07

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The missing first item: reproduce, hypothesise, isolate](#1) | cs-025 | no |
| [2. The ghost duplicate: aliasing proved by identity](#2) | cs-027 | no |

---

## 1. The missing first item: reproduce, hypothesise, isolate (case cs-025)

**Problem.** Items [2.00, 3.50, 1.25] print a receipt of 4.75 instead of 6.75. Debug it by the method: reproduce, hypothesise, isolate, fix, verify.

**Analysis.** Reproduce: the input is known and deterministic. Hypothesis: the loop never sees the first item (4.75 = 3.50 + 1.25). Isolate: run the smallest input [2.00], which returns 0.0. Root cause: the loop starts at index 1.

**Algorithm.**
1. reproduce with the worked input
2. compute the expected 6.75 by hand
3. hypothesise: first item missing
4. minimal repro [2.00] returning 0.0 confirms
5. fix: start the loop at index 0 (or sum the list)
6. rerun the original input

**Pseudocode.**


    BUGGY:  FOR i FROM 1 TO len(items) - 1   -- skips item 0
    FIXED:  total <- 0
            FOR i FROM 0 TO len(items) - 1
                total <- total + items[i]


**Trace (dry run).** Buggy on [2.00, 3.50, 1.25]: i = 1 adds 3.50, i = 2 adds 1.25, total 4.75. Minimal repro [2.00] gives 0.0. The fixed version gives 6.75 on the original input. The reference prints 4.75 then 6.75 side by side.

**Expected output.** 4.75 6.75

**Edge cases.** A single-item list [x] gives buggy 0.0 vs fixed x: the smallest failing input. The empty list gives 0.0 both ways - the bug hides. A fix must pass the empty case AND the original failing case; one green test is not victory.

**Complexity.** Debugging cost, not runtime: one repro, one minimal input, one rerun. The method's value is that it terminates.

## 2. The ghost duplicate: aliasing proved by identity (case cs-027)

**Problem.** A task board shows one task list twice after a second edit. Prove the cause and fix it.

**Analysis.** The board stores the same list object twice, so appending to it mutates every entry. Proof: an identity check between the two rows returns True. Fix: store a fresh copy per row (or build the row list inside the call).

**Algorithm.**
1. observe the duplicated display
2. hypothesis: shared reference, not a copy
3. prove with the identity check
4. fix: copy on insert
5. verify both calls behave

**Pseudocode.**


    BUGGY:  tags.append(task); board.append(tags)   -- same object every call
    FIXED:  board.append(tags + [task])             -- fresh list per row


**Trace (dry run).** Call 1: board holds [['urgent', 'write']]. Call 2 appends 'review' to the SAME tags object: both rows now show ['urgent', 'write', 'review']. The identity check prints True. After the fix the two rows differ and the check is False.

**Expected output.** duplicated rows with identity True; after the fix the rows differ and the check is False

**Edge cases.** The bug only appears on the SECOND call - first-call testing passes. Related traps: default mutable arguments, lists built by repetition. A function that appends to a parameter should copy first.

**Complexity.** O(k) extra per call for the copy - correctness buys the copying cost.

---

**Python companion.** The fixed loop (starts at index 0) on the minimal two-element repro - the fix you diagnosed today:

```python
lines = ["a", "b"]
echoed = []
for i in range(len(lines)):
    echoed.append(lines[i])
print(len(echoed), echoed[0])
# expect: 2 a
```
