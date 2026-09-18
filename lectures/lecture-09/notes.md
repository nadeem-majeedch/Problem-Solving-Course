# Lecture Notes — Lecture 09: Aggregation Patterns

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Running total** — a variable updated inside a loop so its final value summarises the whole sequence.
- **Count** — a running total restricted to items meeting a condition.
- **Min / Max / Argmax** — the smallest/largest value; argmax is the *position or key* of the maximum.
- **Streak** — the number of consecutive items meeting a condition; state resets on a miss.
- **Window (k-slice)** — the sum/aggregate of k consecutive items; the window slides one step at a time.
- **Two-pass thinking** — first compute an intermediate aggregate (e.g. total), then answer the real question from it.
- **Best-so-far** — the pattern 'if candidate is better than best: best = candidate' - the core of argmax.

## Explanation

**Name the pattern before writing the loop.** 'Which day had the most sales?' is argmax; 'how many rainy days' is count; 'longest run of goals met' is streak. The pattern decides the state variables - once named, the loop writes itself.

**Argmax needs two variables.** best value AND best position/key. Forgetting the second is the classic cs-034 slip: students report 420 but not *where* it happened.

**Streaks reset, they do not stop.** A miss zeroes the current streak but the *best* streak survives in a second variable. cs-035's zeros (3 | 0 | 0) make reset-vs-stop visible on three separate queries.

**Windows slide, they do not restart.** cs-036: window sum of [3,5,2,8,1,4] with k=3 goes 10, 15, 11, 13 - each step adds the entering item and subtracts the leaving one. Recomputing each sum from scratch is correct but hides the structure.

**Two-pass honesty.** cs-033's stats dict (total, avg, best, below) is one pass; the *window* question needed two passes. Saying which is which - and why - is the lecture's analysis habit.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-033](../../case-studies/student/cs-033.md) (Beginner)
- [cs-034](../../case-studies/student/cs-034.md) (Foundational)
- [cs-035](../../case-studies/student/cs-035.md) (Intermediate)
- [cs-036](../../case-studies/student/cs-036.md) (Advanced)

## Common misconceptions

- Recomputing totals inside the loop instead of maintaining them.
- Forgetting to reset streak state after a miss.
- Confusing max with argmax - the value versus its position.
- Sliding windows by recomputing each sum from scratch and calling it 'fine'.

## Summary and key takeaways

1. Name the pattern (total/count/min/argmax/streak/window), then write the loop.
2. Argmax tracks the value AND its position.
3. Streaks reset on miss; the best streak lives in a second variable.
4. Windows slide by adding one and removing one.

## Practice questions

- For sales [100, 210, 205, 420, 90]: report total, max, argmax, count above 200, and the best 2-day window.
- Goals [1,1,0,1,1,1,0,1]: current streak, longest streak, and where the longest streak ends.
- Rain [3,5,2,8,1,4], k=3: list every window sum by the slide method (add one, remove one).
- Pages [12,0,25,8,30], target 10: count below, sum above, and argue which pattern answers 'how unusual is 0?'.

## Where this leads

Next lecture: **Strings Under the Lens**. The quiz below checks this lecture's essentials before we build on them.
