# Assignment 3 — Marking Key (instructor only)

Not for publication. Companion to [rubric-03](../rubric-03.md).

## Part A — reference

(a) V1: one pass for the average (n visits) + one pass to search (≤ n) =
    2n. V2: each of n elements triggers an n-visit average + 1 compare =
    n(n + 1) ≈ n². V3: sort ≈ n log n, search log n — but see (c): only
    correct because it sorts a *copy* first.

(b) Expected pattern: V1 grows ~10× from n=1,000 → 10,000; V2 grows
    ~100×. Students using lists of even numbers get integer averages;
    e.g. `list(range(0, 4*n, 2))` has average 2n−2, present in the list
    (good for a hit-case), or shift one element to force a miss-case.
    Ratios, not absolute times, carry the marks — machine-dependent
    constants cancel.

(c) Concrete example where the average exists but unsorted search fails:
    `marks = [2, 4, 8, 2]` — average = 4, present, but a binary search on
    the *unsorted* list examines 4 or 8 first and can miss 4 (e.g. lo=0,
    hi=3, mid=1 sees 4 — luck; mid=2 sees 8, discards the half containing
    4 — miss). The fix V3 already contains: it sorts the copy before
    searching, so the monotone precondition holds. Submissions that
    produce "average absent" lists missed the point — the defect being
    probed is the precondition, not existence.

(d) Accept V1 (linear, no preprocessing — right for a one-off query) or
    V3 (pays off when many queries hit the same list); the justification
    matters, not the choice. "V2 never" unless the report argues a
    per-element freshness constraint, which this scenario does not have.

## Part B — reference

(a) State: `remaining` minutes, init 120. Decision: `need ≤ remaining` →
    serve, `remaining −= need`; else refer and stop (arrival order).
    Stopping rule: first non-fit ends the slot; later patients are not
    attempted (the stated policy — worth flagging in class: a "skip and
    try next" policy is a different, defensible model).

(b)

| arrival | need | fits? | remaining after |
| --- | --- | --- | --- |
| 1 | 15 | yes | 105 |
| 2 | 20 | yes | 85 |
| 3 | 30 | yes | 55 |
| 4 | 20 | yes | 35 |
| 5 | 15 | yes | 20 |
| 6 | 30 | no (30 > 20) | referred |

Five served; the sixth patient is referred.

(c) Shortest-first order `[15, 15, 20, 20, 30, 30]`: 15→105, 15→90,
    20→70, 20→50, 30→20, 30 refused. Five served — the same count as (b).
    Honest reports must notice the tie and resist inventing an
    improvement. Fairness: shortest-first reorders *earlier* arrivals
    behind later ones; waiting-time fairness argues against it even when
    throughput ties — the trace is the evidence, the fairness sentence is
    the judgement.

(d) Any arrival set already filling 120 in arrival order (e.g.
    `[15, 20, 30, 20, 15]` = 100 … not exact; use `[30, 30, 30, 30]`
    exactly = 120, or `[15, 30, 30, 20, 15]` = 110 — inexact; cleanest:
    `[30, 30, 30, 30]`) — no reordering can serve more than "all".
    Equally acceptable: the argument that when every prefix of arrival
    order is optimal, reordering cannot help. Award reasoning quality.

## Common faults to name in feedback

- Timing V2 at n = 10,000 without noticing it takes ~100× longer (the
  surprise is the learning; let them report it).
- "Binary search needs sorted data" quoted without the concrete list —
  the task demanded the instance.
- Traces that let the refused patient consume partial time (the policy
  says refer).
- (c) claiming shortest-first "clearly serves more" without checking —
  this instance ties; checking is the entire exercise.
