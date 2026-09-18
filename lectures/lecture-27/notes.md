# Lecture Notes — Lecture 27: Tables, Cleaning, and Anomalies

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Cleaning** — making data fit its specification: normalise, repair, or reject with a log
- **Normalisation** — canonical formatting: trimming, casing, units, date formats
- **Impossible value** — a value violating a hard rule (age -3); reject, never repair silently
- **Anomaly** — a possible but surprising value; flag for review, do not auto-delete
- **Missing-value policy** — the declared rule for blanks: drop, fill (and how), or flag
- **Audit trail** — the list of every change and rejection, shipped with the cleaned data

## Explanation

Real tables arrive broken: padded strings, duplicated rows, negative ages, blanks that mean three different things. Cleaning is a specification activity: enumerate what counts as repaired (normalisation), rejected (impossible values), and flagged (possible-but-odd), then apply and LOG. The audit trail is not bureaucracy; it is the difference between cleaning and data destruction - a reader must be able to reconstruct what happened to every row. The hardest decisions are policy, not code: a missing value dropped shortens the series and flattens trends; zero-filled it invents a crash; mean-filled it invents calm. Each choice changes the summary, so the choice ships with the data. Anomalies split into two authority layers: hard rules reject (age -3), statistical flags only nominate (a score 2 sd out) - and clean first, because outliers distort the very statistics used to hunt them.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-105](../../case-studies/student/cs-105.md) (Beginner)
- [cs-106](../../case-studies/student/cs-106.md) (Foundational)
- [cs-107](../../case-studies/student/cs-107.md) (Intermediate)
- [cs-108](../../case-studies/student/cs-108.md) (Advanced)

## Common misconceptions

- Cleaning silently - unlogged changes make the dataset unauditable and the analysis untrustworthy.
- Auto-deleting anomalies - statistical flags nominate; hard rules reject; humans decide between them.
- Hunting outliers before cleaning - the extreme values distort the very mean and sd used to flag.
- Zero-filling missing values by habit - a blank is not a zero; each policy changes the story.
- Assuming one normalisation fits all fields - casing rules for names differ from codes differ from dates.

## Summary and key takeaways

1. Clean to a written specification: normalise, reject impossibles, flag surprises.
2. The audit trail ships with the data - silent cleaning is data destruction.
3. Missing-value policies change summaries; declare the policy beside the result.
4. Hard rules reject; statistical flags only nominate.
5. Clean before anomaly-hunting - outliers poison the detectors.

## Practice questions

- Write the cleaning spec for a timestamp column (three defects you will repair, two you will reject).
- Clean 6 rows with one duplicate, one impossible, one missing; ship the table AND the log.
- Apply all four missing-value policies to one series; report each policy's mean.
- Enrichment: explain why the z-score hunt must run after removing hard-rule violations.
- Enrichment: draft the one-paragraph audit summary a reviewer would need to trust your table.

## Where this leads

Next lecture: **Summaries That Don't Mislead**. The quiz below checks this lecture's essentials before we build on them.
