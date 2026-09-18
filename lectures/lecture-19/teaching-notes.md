# Teaching Notes — Lecture 19

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the two-pointer anatomy: left, right, movement rule, invariant - four lines, fixed format.
- Middle: palindrome walk traced; crossing marked as termination.
- Right: pair-sum: each step annotated with WHY discarding an end is safe.

## Questions to ask students

- State the invariant of the pair-sum walk in one sentence.
- Which pointer moves when the sum is too big - and why is that safe?
- What goes wrong if the input is unsorted - exactly which step becomes unjustified?

## Alternative explanations

- Invariant-shy students: allow 'what is true every round' in plain words, then formalise.
- Advanced: the slow/fast cycle detector as a second movement-rule family.

## Expected student difficulties

- Writing loops with no stated invariant - the movement rule then looks arbitrary.
- Off-by-one on crossing: lo < hi vs lo <= hi - trace both on a 2-element input.

## Connections to neighbouring lectures

Invariants are binary search's discipline in miniature; next: brute force as the honest baseline (L20).

## Quiz answer key

**A1.** Define invariant (in one sentence).
- *Expected:* A statement true before and after every loop iteration.

**A2.** What are the two-pointer movement rules' jobs?
- *Expected:* Preserve the invariant while shrinking the range (making progress).

**A3.** Why does pair-sum need sorted input?
- *Expected:* The discard step assumes unsorted ends can be safely rejected - false unsorted.

**A4.** When do the pointers stop?
- *Expected:* They cross (lo >= hi) or the target is found.

**B1.** Walk 'Level' with two pointers: list the comparisons.
- *What earns marks:* L-l (match, case-fold), e-e (match), pointers cross -> palindrome.

**B2.** State the invariant for partition-by-parity and the swap rule.
- *What earns marks:* Everything left of lo is even, right of hi is odd; odd at lo swaps with hi, hi decreases.

## Exit ticket - expected answers

1. State cs-074's invariant in one sentence.
   - *Expected:* the answer pair, if it exists, lies within the current window

2. Why do two pointers give linear cost?
   - *Expected:* each pointer moves at most n times; total moves 2n

3. What ends the slow/fast walk's doubt?
   - *Expected:* the gap strictly shrinks — termination is provable
