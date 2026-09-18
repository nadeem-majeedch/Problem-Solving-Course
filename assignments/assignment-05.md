# Assignment 5 — Choose, Justify, Prove (Block IV)

**Due: week 30 · Weight: see [assessment plan](../docs/assessment-plan.md) ·
Covers LO8, LO10, LO12 · Submit code + report.**

Two problems, one skill: *arguing* that your choice is right — with
correctness reasoning and cost arithmetic — rather than merely having it
pass tests. Both problems have several defensible solutions; the marks
are in the comparison.

## Problem 1 — The overdue sweep (10 marks)

The library runs nightly. Given: `loans`, a list of `(member_id, days_late)`
with up to 10,000 entries, possibly with a member appearing many times, and
a rules function `fine(days_late)` identical to lecture 01's tiered rule
(0.50/day for 1–7, 1.00/day for 8–30, capped at 10.00).

Produce: total fines per member, the member with the maximum total
(ties: all of them), and the count of members with total ≥ 20.

(a) Give two *different* algorithmic approaches (e.g. single-pass with a
    map vs sort-then-group) and state each one's cost with a one-line
    arithmetic justification. *(4)*
(b) Implement the one you would actually run. Justify the choice in
    three sentences using your (a) arithmetic — not "it felt faster".
    *(3)*
(c) Prove-by-invariant: state the invariant your aggregation loop
    maintains and argue the final map is correct when the loop ends.
    *(2)*
(d) The tie rule: name the input that tests it and the expected output.
    *(1)*

## Problem 2 — The seating swap (10 marks)

The exam hall has n×n desks. Some adjacent pairs of desks (sharing an
edge) are "linked" (shared scratch space) and the invigilator requires:
no two linked desks both occupied... the actual rule: *every occupied
desk must have at most one occupied linked neighbour*. Given n ≤ 8 and
the linked-pairs list, decide whether k students can be seated, and if
so, output one seating.

(a) Formulate as a search problem: what is one candidate solution, and
    what is the search space's size in the worst case? *(3)*
(b) Implement backtracking with at least one pruning rule; state the
    rule and why it never discards a solution. *(4)*
(c) Report: for n = 4, 6, 8 with ~2n linked pairs, the node counts with
    and without pruning. One sentence on the growth you observe. *(2)*
(d) Your classmate proposes testing all C(n², k) seat choices instead.
    In two sentences: when is that actually the better plan? *(1)*

## Independent-reasoning component

Problem 1(c)'s invariant and Problem 2(b)'s pruning argument must be
your own sentences about your own code — paraphrased textbook prose
scores zero on those marks even when the code is perfect. State any
collaboration in one line at the top (see
[integrity](../docs/assessment-plan.md)).

## Submission checklist

- Both programs runnable (standard library only) with the test inputs
  included.
- The (a) cost table with arithmetic, and the (c)/(b) reasoning
  sentences.
- Node-count table for 2(c) from an actual instrumented run.
- Length guide: code + 3–5 report pages.
