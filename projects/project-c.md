# Project C — The Campus Network Explorer

**Individual or pairs · First-semester appropriate (with support).**

## The brief

Student clubs keep meeting lists: who attended which club's sessions.
From those lists you can build a *social graph* — people as vertices,
shared-club attendance as edges — and answer questions the clubs
committee actually has: who connects otherwise-separate groups, which
club communities overlap, and how far news travels by word of mouth.

All data is *generated or gathered by you* from the club scenario
below; no external dataset is needed or allowed.

## Part 1 — Data and graph building (week 1–2)

Define a text format for meeting lists (one line per attendance:
`club, student`). Generate or hand-write a consistent dataset of ≥ 6
clubs and ≥ 25 students with deliberately interesting structure: two
clubs that share most members, one "bridge" student in two otherwise
disjoint clusters, and one student who attends exactly once.

- **Program 1:** read the format, build the graph (adjacency map), and
  print a summary (counts, the bridge candidate, isolated students).
- **Test table 1:** ≥ 8 rows — empty file, unknown club, duplicate
  line, self-pair (`club, student` repeated), the bridge student.

## Part 2 — The questions (week 2–3)

Implement, one function each, with stated contracts:

1. **Degrees:** each student's co-attendee count (distinct people they
   share at least one club with). Why is this *not* the same as their
   attendance count?
2. **Reach:** the "word of mouth" set — starting from one student,
   everyone reachable through shared clubs (breadth-first by level),
   and the number of steps.
3. **Bridges:** find students whose removal disconnects a pair that was
   previously connected (brute force is fine at this size — say its
   cost with arithmetic).

## Part 3 — Analysis and honesty (week 3–4)

- **Efficiency section:** for each Part 2 function, what grows (input
  size, edge count) and with what arithmetic; one sentence on which
  function would break first at a real university's scale.
- **One data question answered honestly**, e.g. "does club count
  predict connectedness?" — with the limits of your 25-student data
  stated in the same breath.

## Deliverables (identical to the shared list in
[projects/README.md](README.md))

1. Decomposition document (midpoint): subproblem tree, assumptions,
   test plan — *this project's* concrete version.
2. Working program (Program 1 + the three Part 2 functions).
3. Test table: ≥ 15 rows across both programs, from requirements.
4. Analysis section: efficiency + the data question.

## Scaffolding for first-semester students

- You may implement Part 2 function 3 (bridges) by brute force only —
  no penalty; the cost *statement* is what earns the marks.
- The decomposition document can be submitted once for feedback before
  the midpoint deadline; resubmission with the feedback incorporated
  is allowed and encouraged.
- Work with the graph *drawn* on paper first (vertices and edges for
  your 25 students); the drawing is your test oracle for Parts 1–2.

## Boundaries

- Standard library only (see [Python setup](../resources/python-setup.md)).
- The generated dataset must be included in the submission; markers
  must be able to run the whole pipeline in one command.
