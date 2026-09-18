# Worked Examples — Lecture 11

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The queue reorder: rotations as slices](#1) | cs-041 | no |
| [2. Deduplication patterns: order vs sorted](#2) | cs-042 | no |
| [3. Rotate and roll: left, right, and wraparound](#3) | cs-043 | no |
| [4. The aliasing trap: [[0]*3]*2](#4) | cs-044 | no |

---

## 1. The queue reorder: rotations as slices (case cs-041)

**Problem.** Queue [A, B, C, D, E], k = 2 (last 2 to front). What do k = 0, 5, 7 give?

**Analysis.** Last-k-to-front IS a rotation: lst[-k:] + lst[:-k], with k reduced mod len. The reference prints all four cases.

**Algorithm.**
1. k <- k mod len (guard k = 0)
2. result <- lst[-k:] + lst[:-k]

**Pseudocode.**

```
    k <- k mod length(queue)
    IF k = 0 THEN result <- queue
    ELSE result <- last k items + first (len - k) items
```

**Trace (dry run).** k=2: [D,E] + [A,B,C]. k=0: unchanged. k=5: 0 mod 5 → unchanged. k=7: 2 mod 5 → same as k=2.

**Expected output.** 0 unchanged | 2 [D,E,A,B,C] | 5 unchanged | 7 [D,E,A,B,C]

**Edge cases.** k = 0 and k = len (identity - the mod guard avoids [-0:] oddities); k negative (define or reject); empty queue.

**Complexity.** O(n); the in-place three-reversal rotation (O(1) extra space) is the enrichment extension.

## 2. Deduplication patterns: order vs sorted (case cs-042)

**Problem.** [3, 1, 3, 2, 1, 3] → order-preserving dedupe, and the sorted-unique variant. Reference: [3, 1, 2] and [1, 2, 3].

**Analysis.** Two specs wearing one name. Order-preserving: seen-set + append. Sorted: sort then squeeze. Choosing the wrong one is a spec defect, not a coding one.

**Algorithm.**
1. order-preserving: keep x if not seen
2. sorted: sort a copy, keep items differing from predecessor

**Pseudocode.**

```
    seen <- empty set; keep <- []
    FOR x IN xs
        IF x not in seen THEN append x to keep; add x to seen
    WRITE keep
    WRITE sort(keep)
```

**Trace (dry run).** 3 new, 1 new, 3 seen, 2 new, 1/3 seen → [3, 1, 2]; sorted [1, 2, 3].

**Expected output.** [3, 1, 2] [1, 2, 3]

**Edge cases.** Empty list; all duplicates; already unique; string case-sensitivity (the ladder returns).

**Complexity.** O(n) with a seen-set; the naive 'not in keep' is O(n^2) - measurable at n = 10,000.

## 3. Rotate and roll: left, right, and wraparound (case cs-043)

**Problem.** [1, 2, 3, 4, 5]: rotate left by 2 → [3,4,5,1,2]; right by 2 → [4,5,1,2,3].

**Analysis.** Left by k: lst[k:] + lst[:k]. Right by k = left by (len - k). One operation, two sign conventions - the duality is the insight.

**Algorithm.**
1. left(k): lst[k:] + lst[:k]
2. right(k): left(len - k)

**Pseudocode.**

```
    FUNCTION rotL(lst, k): RETURN lst[k:] + lst[:k]
    FUNCTION rotR(lst, k): RETURN rotL(lst, length(lst) - k)
```

**Trace (dry run).** left 2 → [3,4,5]+[1,2]. right 2 = left 3 → [4,5]+[1,2,3]. Matches the reference.

**Expected output.** [3, 4, 5, 1, 2] | [4, 5, 1, 2, 3]

**Edge cases.** k = len (identity); k > len (reduce mod); k = 0; in-place requirement changes everything (three-reversal trick - enrichment).

**Complexity.** O(n); in-place three-reversal is O(n) time, O(1) extra space.

## 4. The aliasing trap: [[0]*3]*2 (case cs-044)

**Problem.** grid = [[0]*3]*2; grid[0][0] = 9. What does grid hold? Then the correct construction - and the same assignment there?

**Analysis.** [[0]*3]*2 repeats the *reference* to one inner list: two rows, one object. The fix builds a fresh row per iteration. The reference prints exactly this pair, with 'is'-checks confirming the diagnosis.

**Algorithm.**
1. diagnose: grid[0] is grid[1] → True
2. fix: [[0]*3 for _ in range(2)]
3. re-run; verify one row changes

**Pseudocode.**

```
    grid <- two rows sharing ONE inner list
    grid[0][0] <- 9              # visible through BOTH rows
    FIX: build each row separately
```

**Trace (dry run).** Shared: [[9,0,0],[9,0,0]]. Independent: [[9,0,0],[0,0,0]].

**Expected output.** [[9, 0, 0], [9, 0, 0]]  then  [[9, 0, 0], [0, 0, 0]]

**Edge cases.** Deep nesting (shallow copy leaves inner aliases); tuples (immutable, no trap); multiplication of mutable references repeats the reference.

**Complexity.** Constant per assignment; the defect class returns as cs-047's swap and cs-027's ghost duplicate.

---

**Python companion.** Today's aliasing exhibit, executing - the sticky-note proof:

```python
a = [1, 2]
b = a
b.append(3)
print(a, b is a)
# expect: [1, 2, 3] True
```
