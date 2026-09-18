# Projects — Instructor Notes (keys only, not published)

Companion to [project-rubric](../project-rubric.md). Common patterns and
viva questions.

## Project A patterns

- **Undisclosed negatives:** students "fix" negative counts without
  reporting. Check `clean.py` for a `dropped/fixed` counter — absence is
  an integrity deduction under criterion 4, not criterion 1.
- **Weekday effect that isn't:** if the effect is applied multiplicatively
  to a small range it can vanish in noise — exactly what Part 3 Q2 is
  designed to expose. A submission claiming stability across 5 seeds
  without a spread number is over-claiming; probe in the viva.
- **Profile honesty:** best-day/best-item answers computed *after* cleaning
  differ from naive totals; both are acceptable if the choice is stated.

## Project B patterns

- **Priority-rule backfire:** earliest-first starves 90-minute sessions on
  popular days; longest-first rejects short urgent ones. Ask which rule
  they chose and *why*; submissions that cannot name a concrete placement
  or rejection from their own runs lose criterion 2 marks.
- **Validator cheating the contract:** a `validate.py` that imports the
  scheduler's data structures has broken the two-representation point.
  It must parse the schedule file.
- **Budget interaction:** rejections caused by budget vs by conflicts are
  different causes; reports that merge them ("couldn't schedule") are
  incomplete but common.

## Project C patterns

- **Graph built wrong silently:** the classic C defect is an adjacency
  map keyed by club instead of student, or edges added *within* a club
  as pairs of attendees but missed for clubs of one. Ask: "who is the
  bridge student?" — a correct Part 1 names them from the summary; a
  broken one re-derives from the raw file.
- **Degree confusion:** submissions that report attendance count as
  co-attendee count have missed Part 2 Q1's distinction (the question
  is stated precisely so the confusion is discoverable, not a trap).
  Criterion 2 marks, not criterion 1.
- **Reach without levels:** BFS implemented but steps unrecorded is
  half the function's contract; the level count is what makes the
  word-of-mouth story concrete.
- **Bridges by hand:** brute-force removal over 25 students is fine;
  submissions that "eyeballed" the bridge student from the drawing
  must show the code path or lose the cost-statement marks — the
  *statement* (how many removal-trials, how many BFS runs each) is
  the deliverable.
- **Generated data too clean:** datasets with no duplicates and no
  single-attendance students make every test row vacuous. The brief
  mandates both structures — check the dataset, not just the code.

## Viva questions (pick 2, ~5 minutes)

1. Change the seed: which of your conclusions survives, which doesn't?
   *(Project C variant: delete the bridge student from the dataset —
   what does your program now report for the disjoint clusters?)*
2. Where exactly does your program's complexity show up if requests
   double?
3. What does your solution silently assume about the data that your
   generator guarantees — and would break in a real dataset?
