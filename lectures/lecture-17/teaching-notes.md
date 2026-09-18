# Teaching Notes — Lecture 17

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the scan pattern: walk, test, exit-early - with the 'first' vs 'all' distinction boxed.
- Middle: cs-068's peak walk traced; the descent marked the peak.
- Right: best/worst case column for three searches on the same data.

## Questions to ask students

- For which questions is early exit WRONG? (Counting all matches.)
- What precondition did the course finder lack - and what did that cost?
- When is a linear scan provably optimal? (Unsorted, single lookup.)

## Alternative explanations

- Stronger students: derive the expected comparisons for a successful scan (n/2) informally.
- Show the same search as filter-then-first and as explicit loop; compare readability.

## Expected student difficulties

- Returning the value instead of the index (or vice versa) - the spec decides; state it.
- Forgetting the miss case - every search needs a defined 'absent' answer.

## Connections to neighbouring lectures

Scanning is the baseline that sorting will pay for itself against (L18) and halving will beat (L21).

## Quiz answer key

**A1.** When is early exit WRONG in a scan?
- *Expected:* When the question needs all matches (counting, summing).

**A2.** What must every search define for the miss case?
- *Expected:* A sentinel/report ('not found') - never a crash.

**A3.** What precondition would make course-finder faster, and what does it cost?
- *Expected:* Sortedness -> binary search; it costs a sort (O(n log n)) up front.

**A4.** Best vs worst case of a first-match scan?
- *Expected:* Best O(1) (first element), worst O(n).

**B1.** Temps [12, 8, 3, -1, -4]: first freeze index and value - and the 'no freeze' answer for [12, 8].
- *What earns marks:* Index 3, value -1; for [12, 8]: report 'no freeze', not None.

**B2.** Why is a linear scan optimal for ONE lookup in an unsorted catalogue?
- *What earns marks:* Any correct algorithm must potentially inspect every entry - nothing distinguishes positions.

## Exit ticket - expected answers

1. Cost of a full scan vs early exit, in words.
   - *Expected:* always n touches vs stops at the first match; existence searches often exit early

2. What precondition made cs-067 fast?
   - *Expected:* the two halves are each sorted — structure enables strategy

3. Name one search where early exit is wrong.
   - *Expected:* counting all matches; you must see every item
