# Lecture Notes — Lecture 25: Thinking with Data

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Record** — one row of a table: the values describing one entity (one student, one sale)
- **Grouping** — splitting records into buckets by a shared field before aggregating
- **Aggregation** — collapsing many values into one summary: total, average, maximum, count
- **Rate vs count** — a rate divides by its base (per person, per day); a count does not
- **Pivot** — a two-way grouping: rows for one field, columns for another, cells holding aggregates
- **Denominator** — the 'per what' of a rate; the first thing a reader must know

## Explanation

Data problems start before code: what is one record, what is being aggregated, and per what? Grouping by a field then collapsing each group (total, mean, count) answers most first questions about a dataset; a pivot adds the second dimension (rows = cohort, columns = month). The craft is in the details that sound pedantic until they bite: counts versus rates (the rate's denominator must be stated on the slide), means that hide their n, and totals accumulated before any rounding. We rehearse the pipeline - parse, group, aggregate, rank - on canteen logs, screen-time rows, and churn tables, and every deliverable includes its caveats: how many records fed each number, and what the comparison cannot say (causation, cohort mix). The advanced step is choosing the aggregation that matches the decision: a mean for capacity planning, a median for a typical experience, a tail fraction for the angry minority.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-097](../../case-studies/student/cs-097.md) (Beginner)
- [cs-098](../../case-studies/student/cs-098.md) (Foundational)
- [cs-099](../../case-studies/student/cs-099.md) (Intermediate)
- [cs-100](../../case-studies/student/cs-100.md) (Expert)

## Common misconceptions

- Reporting rates without denominators - '20%' of what population?
- Averaging averages - groups of different sizes need weighting, not naive averaging.
- Rounding during accumulation - round only at presentation.
- Reading causation from a grouped comparison - the pivot shows association, never mechanism.
- Treating the mean as the default summary - pick per question (total cost vs typical experience).

## Summary and key takeaways

1. Decide what one record is, then what 'per what' means - before any code.
2. Group, aggregate, rank: most first data questions are this pipeline.
3. Counts and rates answer different questions; the denominator goes on the slide.
4. Mean for totals, median for typical, tail fraction for the outliers that matter.
5. Every deliverable states its n and what the comparison cannot say.

## Practice questions

- Group the screen-time rows by cohort and report mean with n; add the median for cohort A.
- Pivot a mini log: rows = person, columns = item, cells = visit counts.
- Convert three raw counts into rates with the denominator written out.
- Enrichment: argue which aggregate (mean/median/tail) a canteen manager needs for staffing, and why.
- Enrichment: find a 4-row dataset where 'average of averages' differs from the true pooled mean.

## Where this leads

Next lecture: **Counting and Probability in Data**. The quiz below checks this lecture's essentials before we build on them.
