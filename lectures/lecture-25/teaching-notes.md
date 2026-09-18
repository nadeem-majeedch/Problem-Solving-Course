# Teaching Notes — Lecture 25

*Instructor only - not rendered on the public site.*

## Board plan

- Left: one raw log line dissected: fields, types, noise.
- Middle: the pipeline: parse -> group -> aggregate -> rank, with n's annotated.
- Right: the rate-with-denominator template; the denominator slot highlighted.

## Questions to ask students

- What is one record in this dataset - in one sentence, no commas?
- Where does the mean hide its n - and where would you print it?
- Which aggregate answers the staffing question: mean, median, or tail fraction?

## Alternative explanations

- Spreadsheet-fluent students: build the same pivot in code and on paper, compare.
- Advanced: argue the pooled vs per-cohort mean difference on a small sample.

## Expected student difficulties

- Averaging averages across unequal groups - demo the distortion with 2 vs 8 member groups.
- Rounding during accumulation - the print-time-only rule.

## Connections to neighbouring lectures

Grouping sets up the probability reading of the same tables (L26); cleaning arrives next (L27).

## Quiz answer key

**A1.** Define 'one record' for a class register table.
- *Expected:* One student's row: their fields and values.

**A2.** Rate vs count: what does a rate need?
- *Expected:* A stated denominator (per person/day/cohort).

**A3.** What is a pivot?
- *Expected:* Two-way grouping: rows one field, columns another, cells aggregates.

**A4.** Why print n next to every mean?
- *Expected:* So the reader can judge stability; means without n are unauditable.

**B1.** Cohorts A (120, 180, 60) and B (90, 110): means with n, plus one caveat.
- *What earns marks:* A 120 (n=3), B 100 (n=2); caveat: small n, and the 180 inflates A's mean.

**B2.** A: 40 stayed/10 left; B: 25/25. Churn rates and the denominator sentence.
- *What earns marks:* A 20%, B 50% - 'per cohort member' must appear in the claim.

## Exit ticket - expected answers

1. Why state the decision before the computation?
   - *Expected:* the decision determines which aggregate is meaningful

2. Why is the average alone dangerous in cs-098?
   - *Expected:* distributions with the same mean differ; skew hides in the shape

3. What made cs-100's survey skew?
   - *Expected:* voluntary response — collection bias, not analysis error
