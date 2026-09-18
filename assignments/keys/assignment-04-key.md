# Assignment 4 — Marking Key (instructor only)

Not for publication. Companion to [rubric-04](../rubric-04.md).
The log is student-constructed, so *exact* numbers vary with their
generator; the key below fixes the reference generator and the arithmetic
so markers can sanity-check any submission in minutes.

## Reference generator (deterministic, seed 42)

400 weekday visits split evenly (80/day); 150 weekend (75/76).
Durations: uniform 30–70 for the 93% regular; exactly 15 for the 5%
tours; exactly 240 for the 2% passes — rounded counts: 400×0.05 = 20
tours, 400×0.02 = 8 passes across the week, proportionally on weekends.
30 weekday −1 rows; 8 duplicated rows appended verbatim.

## Task 1 — reference arithmetic (from the reference generator)

- Raw mean (all 558 rows, −1 included as −1): the −1s drag the mean down
  by 30/558 ≈ 0.05 per-row effect — students who accidentally *include*
  −1 get a visibly lower mean; that mistake is diagnostic, not fatal
  (name it in feedback).
- Cleaned mean (drop 8 duplicates, drop or repair 30 −1s, keep
  everything else): ≈ 55 minutes for the reference draw — the claim's
  52 is *under* the cleaned mean because the 240s and the 15s partially
  cancel; whether "52 is defensible" depends on the rounding of the
  typical band (30–70 uniform has mean 50!). Accept "defensible" with
  the uniform-band argument: a 30–70 uniform core alone gives 50; the
  passes push above; the claim is plausible-but-round.
- The three-mean table must differ across variants by construction:
  with-240s ≈ 55–57; without-240s ≈ 49–51; repaired-−1 (median fill)
  between. Any table whose variants do not move means the cleaning did
  not touch the durations — the most common Task-1 failure.

## Task 2 — ledger expectations

Row arithmetic: 558 raw → −8 duplicates = 550 → 30 −1 rows resolved
(drop: 520; or repair: 550) → extreme handling stated (keep-and-label
for 240s is the recommended default: they are real visits). The
reconciliation line must read like "558 − 8 dup − 30 missing = 520" —
any unexplained residue caps the task at band 2.

## Task 3 — simulation reference

- Trial: draw a visit's start from the log's empirical start
  distribution (or uniform over opening minutes if stated), duration
  from the cleaned empirical distribution (resampling with replacement
  is the expected method), repeat for the day's visit count; headcount
  at minute m = visits covering m; peak = max over m.
- Report: five buckets of peak headcount with frequencies summing to
  10,000; seed recorded. Peak concentrates (law of large numbers over
  400 overlapping visits) — a distribution with two comparable modes
  usually means the student simulated per-*minute* arrivals instead of
  per-visit occupancy; check the trial definition first.
- Unjustifyable assumption: the *independence of start times from
  durations* (or the uniform-start assumption); justified by timetable
  data or door-reader timestamps across weeks.

## Task 4 — calibration anchors

Full marks: refuses, e.g., "peak headcount" as a printed promise
(simulation variance too wide for one number), or the mean without the
cleaning note. Zero marks: "the gym is clearly underused" — any claim
the tasks did not measure.

## Common faults to name in feedback

- Duplicates removed *after* computing means but the ledger counts them
  as kept (order-of-operations slip).
- −1 repaired with mean-of-all (contaminated by the −1s themselves —
  the classic self-referential fill; median or group-median is the fix).
- Simulation trial defined but not implemented as defined (the code
  draws durations uniform 30–70 and ignores the tours/passes).
- The notice paragraph repeats "average" with no population or base.
