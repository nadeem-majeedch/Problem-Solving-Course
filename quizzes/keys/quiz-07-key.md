# Quiz 7 — Answer Key (instructor only)

Not for publication. Marking notes in *italics*.

## Q1. Choosing a summary (4)

(a) *(2)* The median. Two 900-visit days drag the mean upward — a mean
over 28 days with two 900s sits well above the typical day (with 26
days at ~200: mean ≈ (26×200 + 2×900)/28 ≈ 250); the median stays in
the 200s and describes "a day you might actually get". *(The mark:
median chosen + outlier mechanism; the exact mean arithmetic is a
bonus, not required.)*

(b) *(2)* Any question about *totals or capacity*: "how many total
visits should the library plan staffing for?" or "what is the average
load per day across the month?" — the mean is exactly the total divided
by days, so it is the *right* tool whenever the total is the decision
quantity. *(The mark: a question whose answer is a total/per-day
resource quantity, stated so the mean is visibly correct.)*

## Q2. Percentages and bases (4)

(a) *(1)* 40 × 1.5 = 60 students.

(b) *(2)* The two percentages have different bases: the 50% fall the
year before last applies to the year-before-last's base, not to last
year's 40 — chaining ±50% does not return to the start because after a
50% drop to base B, the 50% rise multiplies 0.5B by 1.5, giving 0.75B,
not B. *(The mark: bases differ; the 0.5/1.5 product arithmetic or an
equivalent concrete-number demo.)*

(c) *(1)* Every percentage statement must carry its *base* (the quantity
the percentage is of) and the direction (increase/decrease) — "rose 50%
from 40" is checkable; "rose 50%" alone is not. *(Accept "compared to
what?" as the answer's core.)*

## Q3. Simulation design (6)

(a) *(3)* One trial: start friend 1 with 2 coins, friend 2 with 3.
While both have coins, flip a fair coin; heads transfers 1 coin from 2
to 1, tails transfers 1 from 1 to 2. The trial ends when either reaches
0 coins; record whether friend 1 holds all 5. *(1 mark for the flip
rule and transfer, 1 for the stopping condition, 1 for what is
recorded.)*

(b) *(2)* Any two of: the coin is fair and flips are independent
(the model — not verified here, stated); the stake is fixed at 1 per
flip (no doubling); "broke" means exactly 0 coins; the *estimator* is
fixed before running — the number of trials does not grow until the
answer "looks nice" (stopping-on-a-nice-answer biases the estimate).
*(Each with its why: the first three define the random process, the
last protects the estimate's honesty.)*

(c) *(1)* Report 0.3987 (10,000 trials): with more trials the estimate
wobbles less — standard error shrinks like 1/√n — so the 10-trial
0.4 is one coin-flip away from anything. *(The mark: the larger sample
+ a variability reason in one sentence.)*

## Q4. Cleaning rules (6)

(a) *(4)* One mark each, justified:

- 3 missing emails — **investigate-first**: is email optional for some
  sign-ups (a legitimate blank) or a collection failure? The fix differs
  (allow-blank vs re-collect); dropping 3 rows for a blank field is the
  classic silent-data-loss move. *(Accept "fix with documented sentinel"
  if the justification says the blank is meaningful.)*
- 5 rows with year = 99 — **fix or drop with evidence**: 99 is a
  sentinel for "not collected"; if year is essential, attempt recovery
  from another column, else drop — but *count and report* the 5.
  *(Investigate-first also acceptable if justified.)*
- 2 exact duplicates — **drop**: exact duplicates double-count real
  sign-ups; removal is mechanical and safe. *(The only free drop.)*
- name = "TEST" — **investigate-first**: almost certainly a test entry,
  but "almost certainly" is a human claim — confirm no real student is
  named Test (it happens), then drop. *(Drop without comment earns 0.)*

(b) *(2)* Deleting data is a decision about *people's real sign-ups*, so
every deletion must be counted, justified, and reported — a cleaning
step that cannot say "I removed these 8 rows for these stated reasons"
is not cleaning, it is loss. *(The mark: deletions must be
accounted/reported; "never delete data" is too strong and earns 1.)*

Grade boundaries suggestion: 16–20 excellent · 11–15 good · 7–10
satisfactory · below 7 revisit lectures 25–28.
