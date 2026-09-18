# Teaching Notes — Lecture 08

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the triangle classifier's test table: input | expected | why this row exists.
- Middle: boundary rows highlighted (degenerate, zero, exactly-equal).
- Right: black-box vs white-box columns - which rows only the code's shape suggests.

## Questions to ask students

- Which row would you drop if forced to four - and what does that reveal about risk?
- What input makes this branch run exactly once per session?
- Is the empty case here a legal input or an error - who decides?

## Alternative explanations

- Students new to writing tests: give the table skeleton, they fill rows.
- Advanced: introduce the idea of a coverage sketch - which lines no test touches yet.

## Expected student difficulties

- Testing only normal inputs - force the boundary-row habit with a grudge case.
- Expected values asserted from the buggy behaviour itself - anchor expectations in the spec first.

## Connections to neighbouring lectures

Testing formalises L7's regression instinct; next block: data structures (L9) with their own test habits.

## Quiz answer key

**A1.** What columns does a test table have?
- *Expected:* Input, expected output, and the reason the row exists (which rule/boundary it probes).

**A2.** Give two boundary rows for 'score 0..100'.
- *Expected:* 0 and 100 themselves (accepted), plus -1 and 101 (rejected).

**A3.** Black-box testing uses what as its source of rows?
- *Expected:* The specification only.

**A4.** Where must expected values come from?
- *Expected:* The specification (or hand computation) - never from the program's own output.

**B1.** List four test rows for the triangle classifier (sides -> type).
- *What earns marks:* 3,4,5 scalene; 5,5,5 equilateral; 4,4,7 isosceles; 1,2,8 invalid (triangle inequality).

**B2.** Write one black-box and one white-box row for the fee function with a two-tier schedule.
- *What earns marks:* Black-box: fee at exactly the tier boundary (e.g. 10 hours). White-box: a value that exercises the code's second branch condition ordering.

## Exit ticket - expected answers

1. Name the three test-case classes and one example of each.
   - *Expected:* normal (typical use), boundary (edges: 0, 120), adversarial (empty, negatives, junk)

2. Black-box vs white-box in one sentence each.
   - *Expected:* black-box: from the spec only; white-box: from the code's known branches

3. What makes a randomness test fair?
   - *Expected:* control the seed or test the distribution over many runs, never a single outcome
