# Lecture Notes — Lecture 30: Optimization Formulations

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Decision variable** — the quantity you choose (how many posters, which shifts)
- **Objective function** — the quantity to maximise or minimise, written in the variables
- **Constraint** — a limit written in the variables: budget, capacity, non-negativity
- **Feasible solution** — an assignment of variables satisfying every constraint
- **Formulation** — variables + objective + constraints, written before any algorithm
- **Search space** — all candidate assignments; formulation decides its size and shape

## Explanation

Optimisation begins as writing, not coding: name the decision variables (what you control), the objective (what better means, in those variables), and the constraints (budgets, capacities, integrality, non-negativity). Three sentences before any algorithm - because a misspecified objective optimises the wrong thing efficiently. Enumeration solves small spaces honestly; greedy solves structured ones with proof; constraint-style backtracking handles 'find any valid roster' where any feasible answer wins. The formulation also reveals structure: 'minimise the largest share' is binary-searchable because feasibility is monotone in the cap (block III's pattern returning); 'assign people to shifts under bans' is satisfaction, not optimisation. The craft skill is noticing which constraints prune hardest and checking them first - correctness never depends on the order, speed always does.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-117](../../case-studies/student/cs-117.md) (Beginner)
- [cs-118](../../case-studies/student/cs-118.md) (Foundational)
- [cs-119](../../case-studies/student/cs-119.md) (Intermediate)
- [cs-120](../../case-studies/student/cs-120.md) (Expert)

## Common misconceptions

- Optimising an unstated objective - 'best' must be written in the variables before any algorithm.
- Forgetting integrality or non-negativity - the fractional optimum can differ from the real one.
- Confusing satisfaction with optimisation - 'find any valid roster' needs no objective, only feasibility.
- Checking expensive constraints first - order constraints by pruning power, not by narrative.
- Believing formulation is overhead - the same data with a different objective is a different problem.

## Summary and key takeaways

1. Variables, objective, constraints - three sentences before any algorithm.
2. The formulation, not the solver, decides the difficulty.
3. Satisfaction problems need only feasibility; optimisation needs the objective defended.
4. Feasibility that is monotone in a threshold is binary-searchable.
5. Check the priciest constraints first - order affects speed, never correctness.

## Practice questions

- Formulate the poster/flyer problem: variables, objective, constraints - in three sentences, then enumerate.
- Write the shift-schedule constraints for 3 shifts, 2 staff, one ban; find any valid roster by backtracking.
- Re-formulate 'minimise the largest share' and explain why feasibility is monotone in the cap.
- Enrichment: swap the objective (maximise flyers, posters fixed-budget) and describe how the optimum moves.
- Enrichment: list, for a toy problem, which constraint prunes most and why order of checks matters.

## Where this leads

Next lecture: **Strategic Thinking Workshop**. The quiz below checks this lecture's essentials before we build on them.
