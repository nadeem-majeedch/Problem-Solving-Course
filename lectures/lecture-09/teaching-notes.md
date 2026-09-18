# Teaching Notes — Lecture 09

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the four aggregation patterns named: running total, best-so-far, count-if, derived average.
- Middle: the reading-log trace showing all four accumulators side by side.
- Right: one-pass claim - why the four patterns share a single loop.

## Questions to ask students

- Which pattern needs its initial value chosen most carefully, and why (empty-best problem)?
- What breaks if the average is computed inside the loop instead of after?
- Could we compute all four with two passes? What would it cost?

## Alternative explanations

- Pattern-first students: give the four patterns and let them classify each case example.
- Code-first students: let them write the loop, then name the patterns they just used.

## Expected student difficulties

- Initialising best to 0 breaks all-negative data - use the first element.
- Integer division wrecking averages - cast once, deliberately.

## Connections to neighbouring lectures

Aggregation is the data-flavoured sequel to L6's traces; next: strings get the same one-pass treatment (L10).

## Quiz answer key

**A1.** Name the four aggregation patterns.
- *Expected:* Running total, best-so-far, count-if, derived average.

**A2.** Why initialise best-so-far from the first element, not 0?
- *Expected:* All-negative data would keep 0 as the 'best'.

**A3.** Where is the average computed, and why there?
- *Expected:* After the loop - it needs the final total and count.

**A4.** What does one-pass mean, and what would two passes cost?
- *Expected:* A single loop produces all aggregates; two passes doubles the reading cost (still O(n) but avoidable).

**B1.** Pages [12, 0, 25, 8, 30], target 10: give total, average, best day, days below target.
- *What earns marks:* 75, 15.0, 30, 2.

**B2.** Stock levels [4, 9, 9, 2]: report the argmax with a witness (its index), stating your tie rule.
- *What earns marks:* First-max rule -> value 9 at index 1 (witness); last-max would give index 2 - state the choice.

## Exit ticket - expected answers

1. Name the aggregation pattern for 'which day had the most sales'.
   - *Expected:* argmax: track best-so-far value and its index/key

2. Why reset streak state?
   - *Expected:* a streak is consecutive; a miss must zero the counter, not stop it

3. What is two-pass thinking and when does it pay?
   - *Expected:* compute intermediate aggregates first, then answer; pays when one pass tangles state
