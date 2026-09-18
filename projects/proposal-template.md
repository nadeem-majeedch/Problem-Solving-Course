# Project Proposal Template

Copy this template into `proposal.md` (or the equivalent form your
institution uses) and fill every section. Length guide: **one page** —
a proposal that does not fit on one page is a project that does not fit
in four weeks.

Deadline: week 26 (see the [project timeline](README.md)). Submit to
your instructor for approval; unapproved proposals fall back to
[Project A](project-a.md) or [Project B](project-b.md).

---

## 1. The problem (≤ 3 sentences)

What question does the project answer, for whom, and why does it need a
*program* rather than a spreadsheet? State the concrete deliverable:
"given X, the program produces Y".

## 2. Decomposition sketch (≤ 6 boxes)

The subproblem tree at first draft: 4–6 subproblems, each small enough
that you can imagine testing it alone. Mark the one you expect to be
hardest, and say why in one line.

## 3. Data plan (≤ 4 lines)

Where the data comes from: generated (state the generator's rules),
gathered (state the collection method and the format), or given (state
the format). State the size. No external datasets that you cannot
redistribute inside the submission.

## 4. The tool you will reuse (≤ 3 lines)

Which course technique carries the project (aggregation, maps, search,
simulation, graphs, greedy/backtracking) and which lecture taught it.
If you cannot name the lecture, the project is not yet scoped — talk to
your instructor *before* submitting.

## 5. Test plan (≤ 5 lines)

Three test rows you can already write (input → expected output) *before
any code exists*. If you cannot write three, the deliverable in §1 is
not concrete enough.

## 6. Risks and the fallback (≤ 3 lines)

The two things most likely to go wrong (data quality, a function you
do not yet know how to write, scope creep), and what you will cut first
if week 3 arrives with Part 2 unfinished. Cutting is planning, not
failure — say the cut order now.

## 7. Team (1 line)

Individual, or pair with the work split named (who owns which
subproblem from §2). Pairs submit one proposal; both names appear on
every deliverable.

---

## Instructor use (not part of the student page)

Approval checklist — the proposal is approved when all six hold:

- [ ] §1 names input → output concretely (no "analyse the data" verbs).
- [ ] §2's tree has leaves small enough for one test each.
- [ ] §3's data exists or its generator is specified.
- [ ] §4 names a course technique and lecture.
- [ ] §5 has three writable rows.
- [ ] §6's cut order is stated.

Common approval failures: scope ("a full scheduling system"), missing
data plan, and §4 naming a technique the course has not taught
(approve only with the replacement named).
