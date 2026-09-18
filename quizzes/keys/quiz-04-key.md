# Quiz 4 — Answer Key (instructor only)

Not for publication. Marking notes in *italics*.

## Q1. Aliasing (4)

(a) *(2)* Output: `[1, 2, 3, 4]`. Mechanism: `b = a` copies the
*reference*, not the list, so both names point at one object and the
append is visible through both.

(b) *(2)* `b = a.copy()` (or `b = list(a)`, or `b = a[:]`).
*Accept any genuine copy. `b = a + []` also produces a new list — award
the mark if the student can say *why* it copies; without that, deduct 1:
the correct output by luck is not the mental model.*

## Q2. Dictionary reasoning (5)

(a) *(2)* `{'ann': 3, 'bo': 2, 'cy': 1}` *(key order may vary in the
answer; the mapping is what is graded)*.

(b) *(3)* Model pseudocode:

```
best_name TO null; best_count TO 0
FOR EACH (name, count) IN tally DO
    IF count > best_count THEN
        best_name TO name; best_count TO count
END FOR
OUTPUT best_name
```

*State-a-tie-rule is explicit in the question; the scan above already
implements "first name wins ties" (strict >) — award the 3 marks for a
correct scan plus a stated rule, 2 for a correct scan with an unstated
rule. Strict `>` gives 'ann' on the example (3 > 2); accept `>=` only
with the tie rule named as "last wins" — and then the example's winner
is still 'ann' since no tie occurs. Common error: initialising
best_count to −1 with a comment "just in case" — no deduction, but the
cleaner form is 0 since counts start at 1.*

## Q3. Debug a function (5)

(a) *(1)* Any input where the answer is the second value: `[3, 7]` →
expected 3, returns 7. *(Also `[5, 9, 2]` → expected 5. Award for any
input whose expected second-largest differs from the largest.)*

(b) *(2)* The loop keeps *one* champion: `best` is overwritten whenever
anything bigger appears, so the previous champion — the true
second-largest candidate — is lost. The mechanism is the missing
second accumulator, not the comparison itself.

(c) *(2)* Model:

```python
def second_largest(nums):
    best = nums[0]
    second = None
    for n in nums[1:]:
        if n > best:
            second = best
            best = n
        elif second is None or n > second:
            second = n
    return second
```

*Accept the two-variable family of fixes. Deduct 1 for solutions that
sort and index [-2] — correct, but the question said "track two values";
the sorting version is O(n log n) and skips the invariant thinking.
Deduct 1 if duplicates are silently mishandled and the student's (a)
test did not cover the case (their test suite must match their fix).*

## Q4. Functions and contracts (6)

(a) *(2)* The function *computes* a result (deduplicated, sorted list)
but *prints* it instead of returning it — the caller cannot use the
value, and the count is inaccessible. *(One sentence; "it prints instead
of returns" is the core; the second printed value compounds it.)*

(b) *(2)* e.g. `dedupe(names) -> list` (lowercases, removes duplicates,
returns them) and `sorted_with_count(names) -> (list, int)` — or any
two-way split where each function returns its result and does not print.
*The essential property: values cross function boundaries by return, not
by print. Names are free.*

(c) *(2)* Boundary of dedup: the all-duplicates list `["ann", "ann",
"ann"]` → `["ann"]` (count 1); or the empty list; or the
differing-case duplicate `["Ann", "ann"]` which *is* a duplicate after
lowercasing — the sneakiest valid row. *(Any one with its expected
output.)*

Grade boundaries suggestion: 15–20 excellent · 10–14 good · 7–9
satisfactory · below 7 revisit lectures 11–14.
