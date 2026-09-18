# Teaching Notes — Lecture 26

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the 2x2 table with margins; both conditionals' arrows drawn across different margins.
- Middle: the bus-delay frequency table; the <3 row shaded and its fraction computed.
- Right: the falling product for the birthday complement, term by term.

## Questions to ask students

- P(M|D) and P(D|M) share which cell - and differ by which margin?
- Why does 'usually under 3 minutes' fail at exactly 50% - what would make it fair?
- What does independence claim, and how would the 2x2 expose its failure?

## Alternative explanations

- Simulation cross-check: count conditional frequencies from trials for both conditionals.
- Advanced: base-rate twist - recompute the conditionals with a skewed population.

## Expected student difficulties

- Conditional swap in prose answers - force margin-labelling in every answer.
- Treating sample fractions as laws - compare two days' tables to see the wobble.

## Connections to neighbouring lectures

Probability formalises L25's rates; simulation will stress-test these ratios (L29).

## Quiz answer key

**A1.** What does a frequency table add to raw anecdotes?
- *Expected:* Exact fractions - 'usually' becomes a ratio with a denominator.

**A2.** P(A|B) vs P(B|A): what differs?
- *Expected:* The margin (denominator) - same overlap cell.

**A3.** Define independence operationally.
- *Expected:* P(A|B) = P(A): the evidence changes nothing.

**A4.** State the complement rule.
- *Expected:* P(not A) = 1 - P(A).

**B1.** Delays: 7 of 14 under 3 minutes - verdict on 'usually under 3'?
- *What earns marks:* False: exactly 50%, a coin flip, not a habit.

**B2.** 100 sessions, 40 mobile, 10 double-click, 8 both: both conditionals.
- *What earns marks:* P(M|D) = 8/10 = 0.8; P(D|M) = 8/40 = 0.2.

## Exit ticket - expected answers

1. What is a base rate and what does it do to PPV?
   - *Expected:* prior prevalence; low base rates collapse PPV even with good tests

2. When may two events not be multiplied?
   - *Expected:* when they are dependent — cs-102's paired clicks

3. What did simulation add to the streak question?
   - *Expected:* an empirical check that the counting was right
