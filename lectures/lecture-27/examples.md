# Worked Examples — Lecture 27

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Room Booking Audit: rule-based cleaning](#1) | cs-105 | yes |
| [2. The Grade Typos: anomaly detection with limits](#2) | cs-106 | yes |
| [3. The Sensor Dropout: missing values as a decision, not an accident](#3) | cs-108 | yes |

---

## 1. The Room Booking Audit: rule-based cleaning (case cs-105)

**Problem.** Bookings with issues: '9:00-10:00' (fine), ' 10:30 - 11:30 ' (padded), '24:00-25:00' (invalid), '9:00-9:00' (empty). Write rules, apply them, report what was dropped and why.

**Analysis.** Cleaning is specification-first: enumerate the defects you will repair (punctuation, case, padding) versus reject (impossible times), then apply. The audit trail - what was dropped and why - is mandatory output; silent cleaning is data destruction.

**Algorithm.**
1. normalise: strip whitespace, single spaces around the dash
2. parse both ends to minutes; check 0 <= start < end <= 24h
3. violations -> reject with reason
4. report kept rows and a drop log

**Pseudocode.**

```
    FOR each booking
        norm <- trim and collapse spaces
        parse start, end to minutes
        IF invalid range THEN log drop WITH reason
        ELSE keep norm
    WRITE kept, drop log
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
raw = ["9:00-10:00", " 10:30 - 11:30 ", "24:00-25:00", "9:00-9:00"]
kept, dropped = [], []
for r in raw:
    norm = " ".join(r.split()).replace(" ", "")
    s, e = norm.split("-")
    sh, sm = map(int, s.split(":"))
    eh, em = map(int, e.split(":"))
    start, end = sh * 60 + sm, eh * 60 + em
    if not (0 <= start < end < 24 * 60):
        dropped.append((r, "invalid range"))
    else:
        kept.append(f"{start:04d}-{end:04d}")
print(kept)
print(dropped)
# expect: ['0540-0600', '0630-0690']
# expect: [('24:00-25:00', 'invalid range'), ('9:00-9:00', 'invalid range')]
```

**Trace (dry run).** '9:00-10:00' -> 540-600 kept. Padded row -> normalised, 630-690 kept. '24:00-25:00' -> 1440-1500: end beyond the day -> dropped. '9:00-9:00' -> start = end -> zero-length -> dropped. Two kept, two dropped with reasons - the log is the deliverable.

**Expected output.** kept: 9:00-10:00 and 10:30-11:30 (normalised); dropped: the invalid and empty ranges

**Edge cases.** The demo prints minute-total form to keep the verified output plain; a production version would format back to HH:MM. '25:00' end with valid start: range check catches it. Midnight ('00:00') is valid as a start. Decide 'equal times' = empty booking (rejected) or a data-entry sign - the rule is the spec.

**Complexity.** O(n) rows, each parsed in constant time.

## 2. The Grade Typos: anomaly detection with limits (case cs-106)

**Problem.** Scores 78, 92, 850, 65, 88, -5. Flag impossible values; then discuss what you can and cannot conclude about suspicious-but-possible ones (e.g. 92 when the class mean is 40).

**Analysis.** Layer 1 is hard rules: scores outside 0..100 are impossible - drop and log. Layer 2 is statistical: 92 is possible but unusual; z-scores can flag it for review, never for automatic deletion. The two layers have different authority - that is the design principle.

**Algorithm.**
1. hard rule: keep only 0 <= s <= 100; log the rest
2. mean and standard deviation of the kept scores
3. z = (s - mean) / sd; flag |z| > 2 for review
4. review list is advisory - humans decide

**Pseudocode.**

```
    valid <- scores in 0..100; log others
    mean, sd <- over valid
    FOR s in valid
        IF |s - mean| / sd > 2 THEN flag s for review
    WRITE valid, flagged
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
scores = [78, 92, 850, 65, 88, -5]
valid = [s for s in scores if 0 <= s <= 100]
mean = sum(valid) / len(valid)
var = sum((s - mean) ** 2 for s in valid) / len(valid)
sd = var ** 0.5
review = [s for s in valid if abs(s - mean) / sd > 2]
print(valid, mean, review)
# expect: [78, 92, 65, 88] 80.75 []
```

**Trace (dry run).** 850 and -5 fail the hard rule (kept list [78, 92, 65, 88]). Mean 80.75, sd ~9.6 - no kept score is beyond 2 sd, so the review list is empty: 92 is fine once the true outliers stop dragging the mean. Instructive: the anomalies distorted the very statistic used to hunt anomalies - clean first, then flag.

**Expected output.** hard-dropped: 850 and -5; statistical review: none after cleaning

**Edge cases.** Single valid score -> sd = 0 -> division by zero in the z-score; guard it (skip the layer). The 2-sd threshold is a policy, not truth. Deleting a flagged-but-possible value silently is the cardinal sin of this lecture.

**Complexity.** O(n); the guard against sd = 0 is where most student implementations break.

## 3. The Sensor Dropout: missing values as a decision, not an accident (case cs-108)

**Problem.** Hourly readings 12.0, 11.5, None, None, 13.0, 12.5. Choose a policy (drop rows, fill zero, carry forward, fill mean), apply it, and state how the choice changes the story.

**Analysis.** There is no policy-free cleaning. Dropping shortens the series (gaps vanish, trends flatten); zero-fill invents a crash; carry-forward freezes the last value through the outage; mean-fill pretends typical weather. The exercise is to SEE the four stories, then pick one and defend it.

**Algorithm.**
1. list the four candidate policies
2. apply each mechanically
3. compare resulting summaries (count, mean)
4. pick one for the report and defend it in one sentence

**Pseudocode.**

```
    FOR each policy in (drop, zero, forward, mean)
        filled <- apply policy to readings
        WRITE policy, count, mean of filled
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
readings = [12.0, 11.5, None, None, 13.0, 12.5]
present = [r for r in readings if r is not None]
drop_mean = sum(present) / len(present)
zero_fill = [r if r is not None else 0 for r in readings]
fwd = []
last = present[0]
for r in readings:
    if r is not None:
        last = r
    fwd.append(last)
mean_fill = [r if r is not None else drop_mean for r in readings]
print(len(present), round(drop_mean, 2))
print(round(sum(zero_fill) / len(zero_fill), 2), round(sum(fwd) / len(fwd), 2), round(sum(mean_fill) / len(mean_fill), 2))
# expect: 4 12.25
# expect: 8.17 12.0 12.25
```

**Trace (dry run).** Drop: 4 readings, mean 12.25. Zero-fill: mean 8.17 - a phantom crash. Carry-forward: 12.0, 11.5, 11.5, 11.5, 13.0, 12.5 -> 12.0 (the frozen hours weigh the mean toward the outage's start). Mean-fill: 12.25 again (by construction). Four policies, three different means - each tells a different story about the outage.

**Expected output.** drop: mean 12.25 (n=4); zero: 8.17; forward: 12.33; mean: 12.25

**Edge cases.** All readings missing -> every policy degenerates: refuse to report rather than divide by zero. Leading missing values break carry-forward (no 'last' yet) - the demo seeds with the first present value. Document the policy ON the chart, not in a footnote.

**Complexity.** O(n) per policy; the cost is in the argument, not the loop.
