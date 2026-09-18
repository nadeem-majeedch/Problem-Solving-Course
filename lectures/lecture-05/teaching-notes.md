# Teaching Notes — Lecture 05

*Instructor only - not rendered on the public site.*

## Board plan

- Left: division with remainder drawn as a number line with jump-length 3.
- Middle: the digit-peel loop (4723 -> 3 -> 472 -> ...) as a shrinking staircase.
- Right: the divisible-by-3 rule verified on 4723 (sum 16 -> no).

## Questions to ask students

- What does n % 10 give you, always? What does n // 10 do to the number?
- Why is 'digit sum divisible by 3' equivalent to 'n divisible by 3' - can you show it on two digits?
- What is the cycle length of on-call duty with 5 people? Of weekdays? What changed?

## Alternative explanations

- Students weak on mod: use clock arithmetic first (13:00 + 15 hours = 4:00).
- Strong students: derive the closed form for the pager (day-1 mod 5) and prove it matches the loop.

## Expected student difficulties

- Confusing / with // in Python - the float result breaks the staircase; catch it live.
- Off-by-one in cycle maths: day 1 vs day 0 indexing - settle the convention on the board.

## Connections to neighbouring lectures

Remainder is L4's first arithmetic tool with structure; next: traces make loop behaviour predictable (L6).

## Quiz answer key

**A1.** What do n % 10 and n // 10 give, always?
- *Expected:* The last digit, and the number without its last digit.

**A2.** A duty roster cycles through 5 people starting with person 1 on day 1. Who has day 47?
- *Expected:* Person ((47-1) mod 5) + 1 = person 2.

**A3.** State the divisibility-by-3 rule and verify on 4723.
- *Expected:* Digit sum divisible by 3 iff n is; 4+7+2+3=16 -> not divisible.

**A4.** What is the off-by-one risk in cycle maths?
- *Expected:* Day-1 vs day-0 indexing: fix the convention, then compute (day - start) mod length.

**B1.** Trace the digit-peel loop for 4723: list each step's digit and remaining number.
- *What earns marks:* 3 (472), 2 (47), 7 (4), 4 (0) - sum 16.

**B2.** With weekend-skip (Mon-Fri duty only), what must change in the pager formula?
- *What earns marks:* Advance the day counter only on weekdays - keep a separate workday count; modular arithmetic alone is no longer enough.

## Exit ticket - expected answers

1. Compute 17 mod 5 and 17 // 5, and say what each means for a 5-day cycle.
   - *Expected:* 2 and 3: day-before-cycle position and completed cycles

2. Why is remainder better than an if-chain for schedules?
   - *Expected:* one expression handles all positions; no special cases to maintain

3. What replaced a loop in the Josephus analysis?
   - *Expected:* a table of small cases plus a conjecture (mathematics replacing simulation)
