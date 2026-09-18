# Teaching Notes — Lecture 06

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the trace table template: iteration | variables | condition | action.
- Middle: the tally trace filled for the first 3 iterations, students complete rows 4-6.
- Right: nested-loop grid drawn as rows x columns shading.

## Questions to ask students

- Which variable is the loop's candidate for termination - what must shrink or grow?
- In the nested loop, how many times does the inner body run in total - can you count it two ways?
- What would the trace look like if the condition were >= instead of >?

## Alternative explanations

- Students who trace in their heads badly: mandate the table for one full week.
- Advanced: give the off-by-one variant and ask for the one-row difference in the trace.

## Expected student difficulties

- Tables filled optimistically ('surely it works') rather than mechanically - grade one table strictly.
- Nested-loop confusion between outer progress and inner reset - shade the grid visually.

## Connections to neighbouring lectures

Tracing is the debugging method's engine; next: a broken program traced to its defect (L7).

## Quiz answer key

**A1.** What are the columns of a trace table?
- *Expected:* Iteration number, each variable's value, the condition's truth, the action taken.

**A2.** What identifies a loop's termination variable?
- *Expected:* The quantity that strictly shrinks (or grows toward) the exit condition.

**A3.** In a 4x3 nested loop (outer 4, inner 3), how many inner-body executions?
- *Expected:* Twelve - count by rows x columns or by summation 3+3+3+3.

**A4.** What changes in the trace if a condition >= becomes > ?
- *Expected:* One boundary iteration flips action; the table shows exactly which row.

**B1.** Trace the tally loop for pages [12, 0, 25] with target 10: give all three rows.
- *What earns marks:* 12: total 12, below 0; 0: total 12, below 1; 25: total 37, below 1 (best 25).

**B2.** Prove the nested grid loop terminates by naming its shrinking quantity.
- *What earns marks:* Unvisited rows (or the row index approaching its bound); the inner loop is bounded per outer pass.

## Exit ticket - expected answers

1. What belongs in every column of a state table?
   - *Expected:* every variable whose value the loop reads or writes, plus the loop condition

2. Give the two classic off-by-one causes.
   - *Expected:* boundary (≤ vs <) and initialisation (starting one early/late)

3. When does a nested loop's inner count matter most?
   - *Expected:* when estimating cost: it multiplies, so grid thinking exposes growth
