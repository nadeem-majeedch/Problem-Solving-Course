# Teaching Notes — Lecture 07

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the four-step protocol - reproduce, hypothesise, isolate, fix - with today's case under it.
- Middle: hypothesis list from the room, each marked alive/dead as tests run.
- Right: the minimal input that still shows the bug, beside the original input.

## Questions to ask students

- Which single test kills the most hypotheses right now?
- Is the bug in the input, the boundary, or the update rule - what evidence says so?
- After the fix, what regression test do we add so it never returns?

## Alternative explanations

- Students who guess-fix instantly: require the written hypothesis BEFORE allowing any edit.
- Quiet students: hypothesis writing on cards, collected and ranked by the class.

## Expected student difficulties

- Fixing symptoms (special-casing the failing input) - expose it by changing the input slightly.
- Multiple simultaneous defects: teach one-fix-one-test discipline, not shotgun edits.

## Connections to neighbouring lectures

Debugging completes the loop toolkit; next: testing is debugging done before shipping (L8).

## Quiz answer key

**A1.** Name the four debugging steps in order.
- *Expected:* Reproduce, hypothesise, isolate, fix.

**A2.** What makes an input 'minimal' for a bug?
- *Expected:* It still triggers the bug with as little data as possible.

**A3.** What is a regression test?
- *Expected:* A test added for a fixed bug so the fix is checked forever after.

**A4.** Give an example of fixing a symptom instead of the cause.
- *Expected:* Special-casing the exact failing input instead of repairing the boundary condition.

**B1.** The first item is missing from an echoed list. Write two hypotheses and the ONE test that kills one of them fastest.
- *What earns marks:* H1: loop starts at index 1; H2: append happens after an early continue. Test: single-element input - start-at-1 loses it entirely, the continue does not.

**B2.** How does `is` prove a duplicate-list bug that `==` cannot see?
- *What earns marks:* Two variables comparing equal but with different identities are copies; equal identity means shared object - the aliasing witness.

## Exit ticket - expected answers

1. Order the clinic protocol steps.
   - *Expected:* reproduce, hypothesise, cheapest experiment, isolate, fix, re-test

2. Why fix nothing before the hypothesis is confirmed?
   - *Expected:* unconfirmed fixes destroy the evidence and add new defects

3. What is a regression test for?
   - *Expected:* to make a fixed defect fail permanently if it ever returns
