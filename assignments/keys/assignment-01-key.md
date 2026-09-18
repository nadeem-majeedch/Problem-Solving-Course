# Assignment 1 — Marking Key (instructor only)

Not for publication. Companion to [rubric-01](../rubric-01.md).

## Task 1 — what a strong tree looks like

Inputs → validation → purchase cost (quantity × 40) → discount decision
(≥ 5) → bonus decision (attendance ≥ 8 AND purchase ≥ 2, applied after
purchase) → shortfall check (12 − 3 = 9 needed) → recommendation.

Leaves small enough for one pseudocode block each. Strong submissions also
isolate "is attendance counted per calendar month?" as its own subproblem —
that is the assumption (marked for impact).

Assumptions most submissions must state:

1. The 10% discount applies to the whole purchase, not per credit.
2. The bonus credit is earned once, not per credit above 2.
3. Attendance (9) is fixed regardless of credits bought this month.
4. Credits do not expire mid-month.

The impact-marked assumption is usually 2: if the bonus stacked, the
cheapest path to 12 changes.

## Task 2 — reference arithmetic

Cost(q) = 40q if q < 5, else 0.9 × 40q = 36q. Bonus: +1 credit if
q ≥ 2 and attendance ≥ 8 (true for Priya).

| Buy q | Cost | Credits after (3 + q + bonus) | Meets 12? |
| --- | --- | --- | --- |
| 6 | 216 | 10 | no |
| 7 | 252 | 11 | no |
| 8 | 288 | 12 | **yes** |
| 9 | 324 | 13 | yes (surplus) |

Without discount thinking: 9 × 40 = 360. The recommendation under these
rules: **buy 8 for 288**. Submissions that use ≥ 5 → discount but forget
the bonus cap at 1 will recommend 8 with cost 288 anyway — the answer is
robust, which is worth noting in feedback.

## Task 3 — expected flowchart shape

Compute q → cost → discount gate at 5 → credits = 3 + q + (bonus if q ≥ 2)
→ compare with 12 → recommend minimum q meeting 12. The genuinely contested
branch: whether "end the month with at least 12" permits buying 8 with the
bonus credit arriving before month end — a timing question the scenario
does not settle. Accept either resolution if named.

## Task 4 — the hostile friend, resolved

The friend's case: buy 5 (cost 180, discounted) + 3 separately (120) = 300
for 8 credits + bonus — worse than 288, so under these rules bulk wins.
The cleaner divergence: a student with attendance 7 buys 8 for 288 and ends
on 11 — the friend's "buy fewer, top up later" intuition (two purchases of
5 and 4: 180 + 160 = 340) is *still worse*. The honest flip: make the
discount threshold 5 *per purchase* and remove the bonus → two purchases
(5 credits 180, 4 credits 160) total 340 vs single 320: bulk still wins.
The real flip requires a rule like "discount on credits beyond 4 only"
(5×40 + 4×36 = 344 — no). The strongest submissions discover that under
almost any monotone discount, one purchase never loses — and say so.
Award the band on the quality of the discovered divergence, not on
reaching this note's conclusion.

## Common faults to name in feedback

- Discount computed as 40 − 10% then × q (unit confusion).
- Bonus applied before the purchase-size test (order).
- "Assume everything is normal" as an assumptions section (vague).
- Flowchart recommending a q never enumerated in task 2 (inconsistency).
