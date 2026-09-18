# Quiz 7 — Data and Simulation (Lectures 25–28)

**Time: 20 minutes · Closed book · Answer all questions.**

## Q1. Choosing a summary (4 marks)

A library records daily visits. One month's data contains: typical days
around 200 visits, plus two exam-week days with 900 visits each.

(a) Which summary — mean or median — better represents a *typical* day here?
    Justify in one sentence. *(2)*
(b) Give one question about this data for which the mean is the *right*
    summary despite the outliers. *(2)*

## Q2. Percentages and bases (4 marks)

A notice claims: "Attendance rose 50% this year! Last year 40 students
attended the workshop."

(a) How many attended this year? *(1)*
(b) The same notice later says "Attendance fell 50% the year before last."
    Why can the two percentages not be chained as "back to where we started"
    without care? *(2)*
(c) One sentence: what must every percentage statement carry to be
    checkable? *(1)*

## Q3. Simulation design (6 marks)

Two friends flip a fair coin; heads the first wins 1 from the second, tails
the second wins 1 from the first. They stop when one of them is broke. The
first starts with 2 coins, the second with 3. You must estimate, by
simulation, the probability that the *first* friend ends with all 5 coins.

(a) Describe one trial of the simulation precisely: what is random, what is
    recorded, when does the trial end? *(3)*
(b) Name two decisions in the design that must be fixed *before* running,
    and say why. *(2)*
(c) The estimate from 10 trials is 0.4 and from 10,000 trials is 0.3987.
    Which do you report, and why, in one sentence? *(1)*

## Q4. Cleaning rules (6 marks)

A spreadsheet of workshop sign-ups has columns `name`, `email`, `year`.
Defects found: 3 rows with missing `email`; 5 rows with `year` = 99; 2 rows
that are exact duplicates of other rows; 1 row where `name` is "TEST".

(a) Classify each defect: drop, fix, or investigate-first — with a one-line
    justification each. *(4)*
(b) State the general rule this table illustrates about deleting data. *(2)*
