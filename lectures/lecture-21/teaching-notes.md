# Teaching Notes — Lecture 21

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the halving picture: a strip folded in half per probe, 1M -> 20 probes.
- Middle: the invariant written above the loop, maintained at each branch.
- Right: 'binary search on the answer': the cap axis with feasible/infeasible shading.

## Questions to ask students

- What exactly does the invariant guarantee at loop exit?
- Why must the book-allocation cap start at max(pages), not 0?
- Which off-by-one does (lo+hi)//2 hide, and on which input sizes does it bite?

## Alternative explanations

- Guess-my-number as the warm-up: the class plays it, then formalises the strategy.
- Advanced: argue the exact probe count for n = 1000 (ceil(log2(n+1))).

## Expected student difficulties

- Binary searching unsorted data because 'it usually works' - kill that with a counterexample.
- Feasibility sweep bugs: students forget the running-load reset rule.

## Connections to neighbouring lectures

Halving is the split step of divide-and-conquer, arriving next (L22); the cap-search returns in optimisation (L30).

## Quiz answer key

**A1.** What precondition does binary search need?
- *Expected:* Sorted data (or a monotone yes/no predicate).

**A2.** Write the loop invariant.
- *Expected:* If the target exists, it lies within lo..hi.

**A3.** What does (lo + hi) // 2 do at even widths?
- *Expected:* Picks the left-middle (rounds down) - consistent, but test both parities.

**A4.** Probes for a million items: about how many?
- *Expected:* 20 (log2(10^6) ~ 20).

**B1.** First bad version among 1..10, bad from 7: list the probes.
- *What earns marks:* m=5 good -> lo=6; m=8 bad -> hi=8; m=7 bad -> hi=7; m=6 good -> lo=7 = answer.

**B2.** Why start the cap search at max(pages), not 0?
- *What earns marks:* A student must hold the biggest book - smaller caps are infeasible by definition.

## Exit ticket - expected answers

1. Why must the predicate be monotone for binary search?
   - *Expected:* so that one test discards half the space forever

2. What is searched in search-on-the-answer?
   - *Expected:* the feasibility boundary over candidate answers, not the items

3. How many halvings for 1,000,000?
   - *Expected:* about 20 — log2 of a million
