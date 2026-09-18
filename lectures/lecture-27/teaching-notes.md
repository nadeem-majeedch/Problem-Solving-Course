# Teaching Notes — Lecture 27

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the defect taxonomy: repairable / rejectable / flaggable - three columns.
- Middle: one row's journey through the cleaning spec, decisions logged.
- Right: the four missing-value policies and each one's mean on the demo series.

## Questions to ask students

- Which defects would you reject vs repair - and what does the log say either way?
- Why must cleaning precede anomaly-hunting (what poisons the detector)?
- Who owns the missing-value policy: the analyst, the client, or the data?

## Alternative explanations

- Audit-trail emphasis: every pair ships their log; the log is graded, not just the table.
- Advanced: argue when mean-fill vs carry-forward changes a TREND, not just a level.

## Expected student difficulties

- Silent dropping - make the log a hard deliverable from day one.
- z-score hunt on dirty data - run the poisoned version once, deliberately.

## Connections to neighbouring lectures

Cleaned tables are what L28's summaries deserve; the anomaly layers return in the capstone clinic (L32).

## Quiz answer key

**A1.** Sort into repair / reject / flag: trailing spaces, age -3, score 92 with class mean 40.
- *Expected:* Repair trailing spaces; reject age -3 (impossible); flag 92 for review.

**A2.** Why ship an audit trail?
- *Expected:* To make every change reconstructible - silent cleaning destroys trust and data.

**A3.** Name three missing-value policies.
- *Expected:* Drop rows, fill (zero/forward/mean), flag-and-keep.

**A4.** Why clean before anomaly-hunting?
- *Expected:* Extremes distort the mean/sd used as the detector.

**B1.** Bookings '9:00-9:00' and '24:00-25:00': classify each and log lines.
- *What earns marks:* Both rejected: zero-length; end beyond day - log reasons.

**B2.** Series 12.0, 11.5, None, None, 13.0: which policy inflates a fake crash?
- *What earns marks:* Zero-fill (mean 7.3 vs 12.17 drop) - state why it misleads.

## Exit ticket - expected answers

1. Why report every cleaning rule?
   - *Expected:* silence is falsification of the analysis; the tally is the audit trail

2. What is a false merge in cs-107?
   - *Expected:* two different students collapsed by a weak matching key

3. When is a gap an anomaly?
   - *Expected:* when it breaks the series' established rhythm — context decides
