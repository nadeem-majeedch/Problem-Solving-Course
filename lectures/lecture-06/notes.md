# Lecture Notes — Lecture 06: Traces and Loop Reasoning

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Trace table (state table)** — one row per loop pass; one column per variable the loop reads or writes.
- **Loop condition** — the boolean that decides whether another pass happens; it belongs in the table.
- **Off-by-one error** — a loop that runs once too often or too few; two classic causes are boundary mix-ups (≤ vs <) and wrong initialisation.
- **Nested loop** — a loop inside a loop; the inner loop runs fully for every outer pass.
- **Invariant (informal)** — a statement that is true before and after every pass; why the loop's answer is right.
- **Termination** — the proof a loop ends: name a quantity that strictly decreases (or increases) and is bounded.

## Explanation

**The state table is the skill.** Columns: one per variable, plus the loop condition. Rows: one per pass. Fill it honestly, row by row - 'mental tracing' is where mistakes hide. The table is also the fastest known way to *find* off-by-one bugs.

**Loop anatomy.** Initialisation (before), condition (checked before every pass), body, update (the line that moves the loop toward termination). Most loop bugs live in initialisation or update, not in the condition where people look first.

**Invariants in one sentence.** Say what is true at the top of every pass ('the total includes the first i numbers'). If you can say that, you can argue correctness; if you cannot, you do not yet understand your own loop.

**Nested loops and grids.** The inner loop runs fully per outer pass: i outer, j inner visits i × j cells. Draw the grid, colour visited cells, then count - this picture is the honest basis for lecture 17's cost arithmetic.

**Termination as a proof habit.** Name the shrinking quantity. If none exists, you have an infinite loop, and the table will show it: some column stops changing while the condition stays true.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-021](../../case-studies/student/cs-021.md) (Beginner)
- [cs-022](../../case-studies/student/cs-022.md) (Foundational)
- [cs-023](../../case-studies/student/cs-023.md) (Intermediate)
- [cs-024](../../case-studies/student/cs-024.md) (Advanced)

## Common misconceptions

- Tracing in the head - the table exists precisely because heads lie.
- Omitting the loop-condition column, then wondering why termination is unclear.
- Fixing the condition when the bug is the initialisation (and vice versa).
- Assuming nested loops always multiply costs - they do, but say it with the grid, not as a slogan.

## Summary and key takeaways

1. One row per pass, one column per variable, condition included.
2. Bugs live in initialisation and update more often than in conditions.
3. Say the invariant; it is your correctness argument.
4. Nested loops are grids: outer × inner cells.

## Practice questions

- Produce a full state table for: total = 0; i = 1; while i <= 4: total += i; i += 1.
- Trace the shrinking loop while n > 1: print(n); n = n - 2 for n = 7. What prints, and why is 1 skipped?
- Grid-trace the nested loop for n = 3: for i in range(n): for j in range(i): print(i, j). Count the cells.
- Write the one-sentence invariant of the tally loop; check it against two rows of your table.

## Where this leads

Next lecture: **Debugging as a Method**. The quiz below checks this lecture's essentials before we build on them.
