# Lecture Notes — Lecture 05: Numbers, Remainders, and Cycles

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Integer division `//`** — division keeping only the whole part: `17 // 5` is 3.
- **Remainder (modulo) `%`** — what is left after whole divisions: `17 % 5` is 2.
- **Cycle** — a pattern repeating every k steps; `n % k` names the position inside the cycle.
- **Digit extraction** — `n % 10` is the last digit of n; `n // 10` removes it.
- **Divisor** — d divides n exactly when `n % d == 0`.
- **Simulation** — stepping a process rule by rule, as it would happen, instead of computing a formula.
- **Recurrence** — a rule that defines a term from earlier terms (Josephus idea preview).

## Explanation

**Remainder is a design tool.** Whenever life repeats in cycles - weekdays, shifts, seats, keyboards - `n % k` names the position in the cycle and `n // k` counts completed laps. One operator replaces a wall of special cases.

**Digits without strings.** `n % 10` is the last digit; `n // 10` chops it off. Repeat to visit every digit. Doing this with arithmetic (not `str(n)`) builds the exact muscle lecture 20's number-theory scans need.

**Reconstructing the input.** cs-019 runs the machine backwards: given outputs, rebuild inputs. Reversible thinking doubles your test design power - you can generate cases where you *know* the answer.

**Simulation vs formula.** Some processes (Josephus ring) yield to simulation at small scale and to a table of values at larger scale; the pattern in the table replaces the loop. Knowing when mathematics replaces iteration is the advanced move.

**Honesty about mod zero.** `n % k` with k = 0 is an error, and `n % 1` is always 0 - quick sanity checks when reading other people's cycle code.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-017](../../case-studies/student/cs-017.md) (Beginner)
- [cs-018](../../case-studies/student/cs-018.md) (Foundational)
- [cs-019](../../case-studies/student/cs-019.md) (Intermediate)
- [cs-020](../../case-studies/student/cs-020.md) (Advanced)

## Common misconceptions

- Treating % as trivia to memorise instead of a cycle-position tool.
- Starting cycles at 1 vs 0 - state the convention before computing.
- Extracting digits with strings when the arithmetic is the point of the exercise.
- Simulating the Josephus ring for large n instead of tabulating small cases and finding the pattern.

## Summary and key takeaways

1. n % k positions you in a cycle; n // k counts completed laps.
2. n % 10 and n // 10 visit digits without strings.
3. Tabulate small cases; let patterns replace loops.
4. Reversing a process (outputs to inputs) doubles your testing power.

## Practice questions

- Tabulate n mod 7 for n = 1..21; mark where the pager rotation pattern repeats.
- Extract and sum the digits of 90210 using // and % only.
- Reconstruct a number whose digits multiply to 24 and whose digit sum is 9 (two solutions exist).
- Simulate the Josephus ring for n = 6, k = 3; record the elimination order by hand.

## Where this leads

Next lecture: **Traces and Loop Reasoning**. The quiz below checks this lecture's essentials before we build on them.
