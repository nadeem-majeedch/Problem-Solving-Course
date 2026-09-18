# Quiz 8 — Answer Key (instructor only)

Not for publication. Marking notes in *italics*.

## Q1. Formulation (5)

(a) *(2)* Objective: maximise the number of events funded. Constraint:
total cost of the chosen events is at most 300 (each event is fully
funded or not funded — there is no partial funding). *(Accept "maximise
count subject to total cost ≤ 300".)*

(b) *(2)* Cheapest-first: 40 + 55 + 80 = 175 → 3 events funded, leaving
125 unused; no fourth event fits (next is 120 → 295 for four events!).
*Recheck: 40+55+80+120 = 295 ≤ 300 — four events fit. The optimal
selection is {40, 55, 80, 120} with objective value 4 events, 5
unspent.* *(The 2 marks: optimal count 4; any consistent valid set.
Award 1 for "3 events, 175" — a correct greedy run that stopped one
step early — with the feedback that the greedy continues while it
fits.)*

(c) *(1)* Lecture 23's greedy technique; cheapest-first works here
because all costs are positive and equal in value contribution (each
event adds 1 to the count), so taking the cheapest remaining event
first never blocks a better future choice — the exchange argument.
*(1 mark for naming greedy/lecture-23; the why is generous.)*

## Q2. Expected value (5)

(a) *(3)* EV = (1/200)×50 + 10×(1/20)×5 − 2
= 0.25 + (0.5 × 5 ... recompute carefully: ten prizes of 5, each with
probability 1/20, treated as separate non-overlapping draws:
10 × (1/20 × 5) = 10 × 0.25 = 2.50. First term: 50/200 = 0.25.
EV = 0.25 + 2.50 − 2 = **+0.75**.

*(3 marks: both prize terms (2, one each), cost subtraction (1). The
question's "separate, non-overlapping draws" instruction is what makes
10 × 1/20 legitimate — if a student adds a "can't win twice"
correction, they have made the problem harder than stated; award per
the stated model and note the modelling fork in feedback.)*

(b) *(1)* Yes: EV = +0.75 per ticket, so on expected value alone buying
wins 0.75 per ticket in the long run.

(c) *(1)* Any of: entertainment value, cash-flow/variance (a 50 prize
is lumpy), risk attitude, one-shot vs long-run (EV arguments are about
repetition — a single ticket buyer may reasonably weigh regret).
*(Any one, one sentence.)*

## Q3. Strategy under uncertainty (5)

(a) *(2)* Outcomes: A-live-accurate, A-live-degrades, B performs as
piloted (and any graded mix); unknown: A's live-traffic behaviour (and
B's longer-run behaviour). *(The mark: outcomes separated from the
unknown — naming that the *probability* of A's live success is the
missing quantity.)*

(b) *(2)* The pilot's value is the expected improvement in the decision
— it converts "ship A blind" into a conditional choice, and its value
is bounded by the loss the blind choice would have incurred; you would
pay for it up to that expected savings. *(The mark: value-of-information
framing — pay ≤ expected savings; a concrete story (e.g. "if A is
likely to degrade, avoid shipping it") earns the mark via reasoning.)*

(c) *(1)* Lecture 31, strategy under uncertainty (decision analysis /
value of information).

## Q4. The 20-minute final (5)

(a) *(2)* Expected subproblems (any four): define "sandwich sales" from
the data (columns, units); clean last month's data (typos, missing
days); aggregate per weekday; identify trend vs weekday pattern;
produce next week's ranking with assumptions; state the confidence/
limits of the prediction. *(2 marks for 4+ subproblems that cover
data → model → output; 1 mark for 2–3.)*

(b) *(2)* Riskiest assumptions, expected: (i) last month's pattern
persists next week (no menu change, no one-off event); (ii) the data is
complete and honest (every sale recorded, days not missing) — the two
that most often break the prediction in practice. *(Any two argued
assumptions; "the data is good" needs its risk named.)*

(c) *(1)* Lecture 01's rule: state your assumptions explicitly — they
determine whether the method can work at all before any code runs.
*(Accept "assumptions first" / decomposition-with-assumptions
phrasings.)*

Grade boundaries suggestion: 15–20 excellent · 10–14 good · 6–9
satisfactory · below 6 revisit the capstone cases (cs-125–cs-128).
