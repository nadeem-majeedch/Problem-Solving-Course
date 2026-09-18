# Worked Examples — Lecture 12

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The median that lies](#1) | cs-045 | no |
| [2. The phantom zero](#2) | cs-046 | no |
| [3. The swap that wasn't](#3) | cs-047 | no |
| [4. The regression zoo: three defects, one protocol](#4) | cs-048 | no |

---

## 1. The median that lies (case cs-045)

**Problem.** A statistics function returns the wrong median for even-length input (right for odd). Diagnose; decide the empty case.

**Analysis.** Reproduce: even length. Hypothesis: code takes one middle element instead of averaging the two. Cheapest experiment: odd vs even lengths in one run. Fix: (sorted[n//2 - 1] + sorted[n//2]) / 2. Empty: define or reject - the spec must say.

**Algorithm.**
1. repro: even-length list
2. experiment: odd vs even
3. fix: average the two middles
4. re-test odd, even, empty

**Pseudocode.**

```
    s <- sort(xs); n <- length(s)
    IF n = 0 THEN reject (or define)
    ELSE IF n is odd THEN RETURN s[n div 2]
    ELSE RETURN (s[n div 2 - 1] + s[n div 2]) / 2
```

**Trace (dry run).** [1,2,3] → 2 ✓. [1,2,3,4] → (2 + 3)/2 = 2.5 ✓ after the fix; the buggy version returned one element.

**Expected output.** 3 for odd; 2.5 for even; empty: define or reject

**Edge cases.** n = 1; n = 2; duplicates; unsorted input (the defect hides on pre-sorted data - the repro must use unsorted).

**Complexity.** O(n log n); selection algorithms (lecture 18's kth-element) do better - a teaser.

## 2. The phantom zero (case cs-046)

**Problem.** Readings [0, 5, 0, 7] with 'stop reading at 0'. The reference prints [] (eaten) vs [0, 5, 0, 7] (kept).

**Analysis.** The sentinel 0 is indistinguishable from a legitimate 0 reading. Fixes: count-first, text sentinel ('end'), or EOF - each with a cost the answer defends.

**Algorithm.**
1. repro: [0, 5] loses everything
2. alternatives: count-first / text sentinel / EOF
3. re-test with zeros inside the data

**Pseudocode.**

```
    # broken: WHILE reading != 0: collect
    # fixed (count-first):
    READ count
    FOR i IN 1..count
        READ r; collect r
```

**Trace (dry run).** Broken: first item 0 → collect nothing → []. Fixed: count 4 → [0, 5, 0, 7].

**Expected output.** [] (broken) vs [0, 5, 0, 7] (fixed)

**Edge cases.** All zeros; no zeros; empty input; the meta-lesson: sentinels are a design smell - the contract, not the loop, is the defect.

**Complexity.** O(n) either way; the content is contract design.

## 3. The swap that wasn't (case cs-047)

**Problem.** Tuple-assignment swaps inside a loop that also reassigns indices: the reference prints [3, 2, 3] - one element duplicated, one lost. Diagnose with a memory diagram.

**Analysis.** Tuple assignment itself is correct (right side first, then bind). The defect: targets computed *before* an index reassignment, used *after* - stale bindings. The signature (duplicate + missing) points at writing to a moved target.

**Algorithm.**
1. repro: smallest misfiring list
2. diagram: bindings of i, j, a per line
3. isolate the reassignment that moves the target
4. fix: freeze targets before updates

**Pseudocode.**

```
    # suspect: swap uses i, j; then i <- i + 1; then another swap reuses stale j
    FIX: perform swaps before index updates (or snapshot the targets)
```

**Trace (dry run).** [1, 2, 3] with mis-sequenced swaps → [3, 2, 3]: position 2 written twice, position 0 never.

**Expected output.** [3, 2, 3] (buggy) vs the intended swap after the fix

**Edge cases.** i = j (self-swap - harmless); aliasing two names to one list; the general rule: in loops that mutate, sequence is everything.

**Complexity.** Constant; binding-order reasoning returns in cs-048 and cs-055.

## 4. The regression zoo: three defects, one protocol (case cs-048)

**Problem.** Snippets: (a) counter defined outside a function, (b) shared default list, (c) range(len(xs)) deletion loop. Reference: crash 'list index out of range'; fixed [1, 5] and [1, 2] [1, 2].

**Analysis.** (c) is the crash: removing while iterating range(len(xs)) walks stale indices past the shrinking list - iterate a copy or build anew. (a) is scope (a global read behind a function's back). (b) is the shared default - created once, shared forever; fix: default None, create inside.

**Algorithm.**
1. each snippet: reproduce, hypothesise, experiment, fix, re-test
2. (c) fix: build a keep-list
3. (b) fix: None default
4. (a) fix: pass in, return out

**Pseudocode.**

```
    # (c) broken: FOR i IN 0..len-1: IF bad(xs[i]) THEN remove xs[i]
    # (c) fixed:  keep <- []; FOR x IN xs: IF NOT bad(x) THEN append to keep
    # (b) broken: FUNCTION f(x, acc = []): append x; RETURN acc
    # (b) fixed:  FUNCTION f(x, acc = none): IF acc is none THEN acc <- []
```

**Trace (dry run).** (c) xs = [1,5,9], remove >4: i=1 removes 5 → [1,9]; i=2 out of range → crash. Fixed: keep [1].

**Expected output.** buggy crashed: list index out of range | fixed: [1, 5] and [1, 2] [1, 2]

**Edge cases.** Removing every item; none; nested mutation during iteration; the meta-rule: never mutate what you are iterating.

**Complexity.** All O(n); three defect classes in one hour, each fixed under the full protocol.

---

**Python companion.** The repaired median (even-length branch included) - the defect you fixed today, corrected:

```python
def median(xs):
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2

print(median([3, 1, 2]), median([4, 1, 3, 2]))
# expect: 2 2.5
```
