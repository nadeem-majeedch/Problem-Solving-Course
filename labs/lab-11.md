# Lab 11 — Binary Search Everywhere (Lecture 21 follow-up)

**Machine lab · 2 hours · Pairs.** Two searches today: one on *data*
(sorted catalogue), one on *answers* (a hidden threshold). Same loop,
different predicate — after this lab the pattern, not the array, is the
point. Submit: the checkpoints at the end.

## Setup

- Python 3 as `python`; work in `lab11/`.

## Part A — Search the data (25 min)

A1. Implement `first_ge(items, target)`: given a sorted list, return the
    index of the first item ≥ target, or `len(items)` if none. Write the
    loop with the invariant as a comment: `items[lo] is the first
    possible answer; items[hi] is known ≥ target or out of range` — in
    *your own words*, before coding.
A2. Test at the boundaries: empty list, single item, target before all,
    after all, exact hit at 0, at last, duplicate targets (which index
    is "first"? — say what your loop guarantees).
A3. Count probes on a 1000-item catalogue. Your count must be ≤ 10 —
    state why 10 is the right ceiling without mentioning code.

## Part B — Search the answer (35 min)

B1. The scenario: the campus bridge takes time T to cross; a delivery
    must leave by deadline D; walking speed varies. The hidden function
    `feasible(t)` (instructor-provided `bridge.py`) answers "can a
    delivery leaving at time t make it by D?" — true for early t, false
    for late t. Find the *latest* feasible departure time with the same
    loop shape as Part A. You may call `feasible` at most 10 times.
B2. Before coding: write the predicate's monotone claim in one sentence
    ("if time t works, then every earlier time works because …"). Your
    loop's correctness *is* this sentence.
B3. The instructor's `bridge.py` includes a decoy: a feasible() that is
    almost monotone (one glitch at a random t). Run against it; explain
    the observed failure in terms of your B1 sentence (the glitch breaks
    the *claim*, so the loop's contract is void — the code was fine).

## Part C — Instrument and prove (25 min)

C1. Add a call counter to both searches. Verify: Part A on 1000 items
    uses ⌈log₂ 1001⌉ probes or fewer; B1 uses ≤ 10 calls. Report the
    actual numbers.
C2. Break a bound on purpose: change the update to `hi = mid - 1` in the
    "first ≥" search and find an input that returns the wrong answer
    *and* one that loops forever. Which one you get depends on the
    parity of the interval — show both.
C3. Hand the instrumented searches to another pair with *no*
    documentation. Their job: reconstruct the invariant from behaviour
    alone; your job: how close did they get?

## Part D — Transfer (10 min)

D1. List two campus-scale questions that are "first position where a
    monotone predicate flips" but involve no sorted array. One sentence
    each on where the monotonicity comes from.
D2. cs-083 (book allocation) searched the *answer* "minimum possible
    maximum load". One sentence: why could its feasibility predicate be
    checked greedily?

## Checkpoints (submit these as your report)

1. `first_ge` with your own-words invariant comment.
2. The A2 boundary table with actual outputs.
3. Your A3 probe count and its arithmetic justification.
4. The B1 answer with your call count; the B2 monotone sentence.
5. The B3 glitch explanation.
6. C1's instrumented numbers; the C2 two failing inputs.
7. The C3 reconstruction notes.
8. D1/D2.

## What completion looks like

Completion-graded as in Lab 1. The graded artefact is the *invariant
sentence*: code that passes all tests with no invariant stated earns
half; code with a correct invariant and one failing boundary earns full
credit and one fix away from correct.
