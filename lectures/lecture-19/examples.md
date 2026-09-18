# Worked Examples — Lecture 19

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Palindrome Walk: two pointers closing in](#1) | cs-073 | yes |
| [2. The Pair Sum Contract: two pointers on sorted data](#2) | cs-074 | yes |
| [3. Partition by Parity: evens left, odds right, one pass](#3) | cs-075 | yes |

---

## 1. The Palindrome Walk: two pointers closing in (case cs-073)

**Problem.** Is 'Level' a palindrome? Compare characters from both ends, ignoring case.

**Analysis.** One pointer at each end walks inward. The invariant: every pair already checked matched. If the pointers cross with no mismatch, the whole word matched. Half the comparisons of the naive reverse-and-compare.

**Algorithm.**
1. left at 0, right at last index
2. compare (case-folded) characters
3. mismatch -> not a palindrome; match -> move both inward
4. pointers cross -> palindrome

**Pseudocode.**

```
    lo <- 0; hi <- last
    WHILE lo < hi
        IF lower(word[lo]) != lower(word[hi]) THEN RETURN false
        lo <- lo + 1; hi <- hi - 1
    RETURN true
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
word = "Level"
lo, hi = 0, len(word) - 1
ok = True
while lo < hi:
    if word[lo].lower() != word[hi].lower():
        ok = False
        break
    lo += 1
    hi -= 1
print(ok)
# expect: True
```

**Trace (dry run).** 'L' vs 'l' -> equal after case-fold. 'e' vs 'e' equal. lo=2, hi=2 -> cross, stop. True. For a mismatching word like 'Levelup', the first comparison already fails.

**Expected output.** True ('Level' is a palindrome, case-insensitively)

**Edge cases.** Empty string -> pointers start crossed -> True (vacuously a palindrome: state it). One character -> True. Spaces and punctuation ('never odd or even') need a normalisation pass first - a policy decision before any code.

**Complexity.** O(n) time but only n/2 comparisons, O(1) extra space - the reverse-compare alternative also reads O(n) but copies the string.

## 2. The Pair Sum Contract: two pointers on sorted data (case cs-074)

**Problem.** Sorted values 1, 3, 4, 6, 8. Find a pair summing to 10, or report none.

**Analysis.** Start with the extremes. If the sum is too small, only a larger left value can help; too big, only a smaller right value. The invariant - 'if a valid pair exists, it lies between lo and hi' - is preserved by every step, so the pointers can safely discard one end each round.

**Algorithm.**
1. lo at the first, hi at the last element
2. sum too small -> lo += 1; too big -> hi -= 1
3. equal -> report the pair
4. crossed -> no pair exists

**Pseudocode.**

```
    lo <- 0; hi <- last
    WHILE lo < hi
        s <- a[lo] + a[hi]
        IF s = target THEN RETURN (a[lo], a[hi])
        IF s < target THEN lo <- lo + 1 ELSE hi <- hi - 1
    RETURN 'none'
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
a = [1, 3, 4, 6, 8]
lo, hi = 0, len(a) - 1
found = None
while lo < hi:
    s = a[lo] + a[hi]
    if s == 10:
        found = (a[lo], a[hi])
        break
    if s < 10:
        lo += 1
    else:
        hi -= 1
print(found)
# expect: (4, 6)
```

**Trace (dry run).** 1+8=9 < 10 -> lo=1. 3+8=11 > 10 -> hi=3. 3+6=9 < 10 -> lo=2. 4+6=10 -> found. Four rounds; the sorted-ness is what makes each discard safe - on unsorted data the same steps prove nothing.

**Expected output.** pair found: 4 + 6 = 10

**Edge cases.** No pair (e.g. target 20) -> pointers cross, report 'none'. Two elements only -> one round. Duplicates: 'sum to 10 in [5, 5, 5]' - lo and hi can hold equal values; the lo < hi guard still allows using two different 5s. Unsorted input must be sorted first (O(n log n)).

**Complexity.** O(n) after sorting - each round removes one element from consideration for good; the all-pairs alternative is O(n^2).

## 3. Partition by Parity: evens left, odds right, one pass (case cs-075)

**Problem.** Rearrange 3, 1, 2, 4 so all even numbers precede all odd numbers. Order within each group does not matter.

**Analysis.** Because internal order is free, swapping is allowed - that is what makes one pass possible. Invariant: everything left of lo is even, everything right of hi is odd. Each swap grows one of the two settled regions.

**Algorithm.**
1. lo at 0, hi at the last slot
2. a[lo] even -> lo += 1 (left region grows)
3. a[lo] odd -> swap with a[hi], hi -= 1 (right region grows; the swapped-in value is re-tested)
4. lo meets hi -> partitioned

**Pseudocode.**

```
    lo <- 0; hi <- last
    WHILE lo < hi
        IF a[lo] is even THEN lo <- lo + 1
        ELSE swap a[lo], a[hi]; hi <- hi - 1
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
a = [3, 1, 2, 4]
lo, hi = 0, len(a) - 1
while lo < hi:
    if a[lo] % 2 == 0:
        lo += 1
    else:
        a[lo], a[hi] = a[hi], a[lo]
        hi -= 1
print(a)
# expect: [4, 2, 1, 3]
```

**Trace (dry run).** a[0]=3 odd -> swap with a[3]=4: [4,1,2,3], hi=2. a[0]=4 even -> lo=1. a[1]=1 odd -> swap with a[2]=2: [4,2,1,3], hi=1. lo=1 meets hi=1 -> stop. Evens {4,2} lead.

**Expected output.** [4, 2, 1, 3] - all evens before all odds

**Edge cases.** All even -> lo walks to the end, no swaps. All odd -> hi walks to the start. Empty list -> loop never runs. This partition is the engine inside quicksort - same skeleton, different test.

**Complexity.** O(n) time, O(1) space, single pass - each step settles one element permanently.
