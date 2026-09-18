# Teaching Notes — Lecture 03

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the four flowchart shapes with their meanings, drawn once and referenced all hour.
- Middle: rain-or-shine decision diamonds wired live from student suggestions.
- Right: the ATM loop drawn with both exits marked; termination arrow highlighted.

## Questions to ask students

- Which diamond tests the invariant, and which one tests the exit condition?
- Can two arrows ever enter the same box? What does that mean for the trace?
- Where would an infinite loop hide in this chart - what must shrink?

## Alternative explanations

- Students who draw tangled arrows: limit them to three shapes (box, diamond, arrow) until clean.
- Table-first thinkers: let them express the same logic as an if/else table, then convert.

## Expected student difficulties

- Arrows that skip conditionals entirely ('fall through' diamonds) - trace a failing input to expose it.
- Loop-back arrows drawn to the wrong row - the re-entry point determines the trace.

## Connections to neighbouring lectures

Flowcharts are L2's pseudocode made geometric; next lecture executes the same charts in Python (L4).

## Quiz answer key

**A1.** Which flowchart shape means 'decision'?
- *Expected:* Diamond.

**A2.** Every loop needs an arrow back and what else?
- *Expected:* A termination condition that provably becomes true (something shrinks or grows).

**A3.** Can two arrows leave a process box? Why not?
- *Expected:* No - only diamonds branch; a box does one thing.

**A4.** What does the loop's re-entry point change?
- *Expected:* Which statements repeat - a wrong re-entry skips initialisation or repeats the wrong body.

**B1.** Sketch (or precisely describe) the flowchart for the ATM loop: read request, refuse if over balance, stop on 'stop'.
- *What earns marks:* Start -> read -> diamond 'stop?' -> diamond 'over balance?' (refuse loops back to read) -> deduct -> loop back to read; exit arrow from the stop diamond only.

**B2.** For the dispatch loop, name the quantity that must shrink and where the proof lives in the chart.
- *What earns marks:* Remaining work (items or their sizes) shrinks each pass; the proof is the back-edge re-entering at the test that checks it.

## Exit ticket - expected answers

1. Every decision diamond must have how many exits, and how labelled?
   - *Expected:* exactly two, labelled with mutually exclusive conditions

2. What is the standard proof that a loop terminates?
   - *Expected:* name a quantity that strictly decreases (or increases) and is bounded

3. What is a dead branch and how do flowcharts expose one?
   - *Expected:* an unreachable path; exposed by tracing arrows from start with all conditions
