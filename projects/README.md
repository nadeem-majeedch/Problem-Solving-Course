# Term Project

The term project is worth 30% (see the
[assessment plan](../docs/assessment-plan.md)). You choose **one** project:

- **[Project A](project-a.md)** — *The Canteen Data Mini-Study*: collect or
  generate a small dataset, clean it, answer three questions, and defend
  the cleaning. Suited to second-semester students.
- **[Project B](project-b.md)** — *The Campus Route Planner*: model the
  campus as a weighted graph, implement search, and analyse alternative
  costs. Suited to third-semester students.
- **Your own proposal** — write a one-page proposal with the same
  deliverables and get explicit approval by the week-26 deadline.

## Deliverables (identical for every project)

1. **Decomposition document** (midpoint, week 28 — worth 5 of the 30
   points): subproblem tree, assumptions, data plan, test plan.
2. **Working program**: runnable with the Python available in the course
   lab (standard library only; see [Python setup](../resources/python-setup.md)).
3. **Test table**: at least 15 rows, from requirements, with the run output.
4. **Analysis section**: efficiency (what grows, with arithmetic) and one
   data-oriented question your project answers honestly, with limitations.

## Timeline

| Week | Milestone |
| --- | --- |
| 24 | Project briefs released; choose and register your choice |
| 26 | Own-proposal deadline (approved or you fall back to A/B) |
| 28 | Decomposition document due (5 points) |
| 32 | Final submission: program + test table + analysis |

## Rules

- Work may be done in pairs for Project A only; Project B is individual.
  Pairs state the work split in the decomposition document.
- You may reuse course case ideas but not case solutions: the program must
  contain at least one design decision the course material did not make
  for you, named in the analysis.
- All data is generated or collected by you under your project's data
  rules; no external datasets are required or accepted in place of the
  data plan.
- The [rubric](project-rubric.md) is published in advance; grade against yourself
  before submitting.

## Integrity

Standard course integrity applies (see the
[assessment plan](../docs/assessment-plan.md)): state any help in one line
at the top. Generated data must be reproducible — a grader re-running your
generator (or your collection script) must get your data.
