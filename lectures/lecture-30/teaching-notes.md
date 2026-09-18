# Teaching Notes — Lecture 30

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the formulation sheet: variables / objective / constraints, three lines each.
- Middle: the poster enumeration grid; the integer optimum circled away from the fractional corner.
- Right: backtracking tree for the roster; the first pruned branch marked.

## Questions to ask students

- Which words in the problem statement became which formulation line?
- Why does the integer optimum differ from the fractional one here?
- In backtracking, which constraint pruned the most - did the check order matter?

## Alternative explanations

- Formulation-first drill: three story problems, three formulation sheets, no code.
- Advanced: cap the bids (L30 auction) and watch the optimum hit the boundary.

## Expected student difficulties

- Optimising the unstated objective - the formulation sheet is the fix.
- Forgetting non-negativity/integrality - the fractional optimum then lies.

## Connections to neighbouring lectures

Formulations turn decisions into structure; strategy under uncertainty applies them probabilistically (L31).

## Quiz answer key

**A1.** Name the three formulation lines.
- *Expected:* Decision variables, objective function, constraints.

**A2.** Why does integrality matter in the poster problem?
- *Expected:* The fractional optimum (e.g. all posters) may be unreachable; integer optimum differs.

**A3.** Satisfaction vs optimisation: one sentence each.
- *Expected:* Satisfaction: any feasible answer wins; optimisation: feasible answers are ranked by the objective.

**A4.** How should constraint checks be ordered in backtracking?
- *Expected:* By pruning power - cheapest-and-most-restrictive first; order affects speed only.

**B1.** Posters 3/40 reach, flyers 1/10, budget 12: formulation and optimum.
- *What earns marks:* Maximise 40p+10f s.t. 3p+f<=12, integers >=0 -> p=4, f=0, reach 160.

**B2.** Shifts 1-3, staff {ada, bo}, ada banned from shift 1, no adjacent repeats: one roster.
- *What earns marks:* bo, ada, bo.

## Exit ticket - expected answers

1. Name the three parts of a formulation.
   - *Expected:* decisions, objective, constraints

2. Why is 'minimise cost' often incomplete?
   - *Expected:* unstated service/quality constraints make it meaningless — cs-118

3. How do you verify a claimed optimum?
   - *Expected:* bound argument or exhaustive check on a reduced instance
