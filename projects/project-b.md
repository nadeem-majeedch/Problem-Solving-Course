# Project B — The Scheduler (two programs, one decision)

**Pairs recommended · Combines everything from Block IV.**

## The brief

The department runs help sessions and must staff a single tutor room.
Conflicting constraints, a budget, and a deadline — the classic
scheduling problem in miniature.

## The data

Write `generate.py` producing `requests.json`: 30–50 help-session
requests, each with a student id, a topic from a fixed list, a preferred
day and hour, and a duration of 30/60/90 minutes. Constraints the data
must respect: no more than 8 requests in any one hour, and a stated mix
of topics (e.g. at least 20% recursion).

## Part 1 — The greedy scheduler (program)

`greedy.py` schedules sessions one room, one tutor:

- sort requests by a stated priority rule (you choose: earliest, longest,
  or most-constrained first — state and justify it);
- place each request in the first non-conflicting slot on its preferred
  day; else first free slot anywhere that week; else reject with reason;
- tutor hours must stay under a budget parameter (default 20 h/week);
- output: schedule table plus placement/rejection summary.

## Part 2 — The validator (independent program)

`validate.py` reads a schedule file (not the scheduler's memory!) and
checks every rule from scratch: overlaps, budget, room capacity,
double-booked students. It reports every violation with row references.
This is a lab-2 style spec: two representations, one contract.

## Part 3 — The trade-off memo (report)

- Run the greedy scheduler on 3 seeds. Report placements, rejections,
  and tutor-hours. Where does the priority rule help and where does it
  backfire (give one concrete example from your runs)?
- Name one change that would need a different algorithm class entirely
  (e.g. allowing two rooms to swap sessions) and explain, in one
  paragraph, why greedy can no longer guarantee anything about it.
- State what an optimal scheduler would have to consider that yours
  does not.

## Analysis section

- Complexity of the scheduler in terms of requests n and slots s, and
  of the validator in terms of schedule entries.
- The named design decision (priority rule, rejection policy, or budget
  interaction) with its effect on your numbers.
- Limits: request sizes where your design degrades.

## Data rules

- Same integrity bar as Project A: documented generator, seeds, and no
  silent fixes anywhere.
