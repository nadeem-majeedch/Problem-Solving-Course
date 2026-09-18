# Worked Examples — Lecture 26

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Survey Skew: weighted averages and representativeness](#1) | cs-100 | yes |
| [2. The Late Bus Frequency: histogram as a hypothesis test](#2) | cs-101 | yes |
| [3. The Double-Click Question: conditional counting](#3) | cs-102 | yes |

---

## 1. The Survey Skew: weighted averages and representativeness (case cs-100)

**Problem.** Sample: 8 first-years (avg mood 6), 2 third-years (avg mood 8). Overall average mood - naive or weighted, and which is right?

**Analysis.** Both are 'right' for different questions: the pooled mean of the 10 respondents is (8x6 + 2x8)/10 = 6.4; weighting first-years and third-years equally gives 7 - a statement about cohorts, not people. With 8:2 sampling, the naive pooled mean is biased toward whichever group showed up. Name the population, then pick.

**Algorithm.**
1. pooled mean: sum over all respondents / count
2. group-weighted mean: equal weight per group
3. state which population each estimates
4. report the sample sizes that create the skew

**Pseudocode.**

```
    pooled <- (n1*mean1 + n2*mean2) / (n1 + n2)
    weighted <- (mean1 + mean2) / 2
    WRITE both WITH what each estimates
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
m1, n1 = 6.0, 8
m2, n2 = 8.0, 2
pooled = (n1 * m1 + n2 * m2) / (n1 + n2)
weighted = (m1 + m2) / 2
print(round(pooled, 2), round(weighted, 2))
# expect: 6.4 7.0
```

**Trace (dry run).** Pooled: (48 + 16)/10 = 6.4 - dominated by the eight first-years. Weighted: (6+8)/2 = 7 - treats the cohorts as equally important regardless of who answered. Same data, two honest answers to two different questions.

**Expected output.** pooled mean 6.4 (per respondent); cohort-balanced 7.0 (per cohort)

**Edge cases.** A group with n=0 has no mean - exclude and say so. The deeper fix is better sampling, not fancier arithmetic: reweighting cannot recover information never collected (lecture 28's headline).

**Complexity.** O(1) - the difficulty is conceptual, not computational.

## 2. The Late Bus Frequency: histogram as a hypothesis test (case cs-101)

**Problem.** Minutes-late over 14 days: 2, 0, 5, 3, 0, 7, 4, 1, 2, 6, 3, 0, 9, 2. Build the frequency table. Is 'usually less than 3 minutes late' a fair claim?

**Analysis.** Count each value, read the shape. Below-3 days: 2,0,1,2,0,0,2 -> 7 of 14 = 50% - exactly half, so 'usually less than 3' is a coin-flip claim, not a habit. The frequency table converts anecdote into arithmetic.

**Algorithm.**
1. tally minutes in a dictionary
2. present as a frequency table (value: count)
3. answer the claim with the exact fraction
4. report the fraction with its denominator

**Pseudocode.**

```
    freq <- {}
    FOR each delay: freq[delay]++
    under3 <- sum of counts for delays < 3
    WRITE table, under3, under3 / n
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
delays = [2, 0, 5, 3, 0, 7, 4, 1, 2, 6, 3, 0, 9, 2]
freq = {}
for d in delays:
    freq[d] = freq.get(d, 0) + 1
under3 = sum(c for d, c in freq.items() if d < 3)
print(under3, len(delays), f"{under3 / len(delays):.0%}")
# expect: 7 14 50%
```

**Trace (dry run).** Tally: 0x3, 1x1, 2x3, 3x2, 4x1, 5x1, 6x1, 7x1, 9x1. Under 3: 0s, 1s, 2s = 3+1+3 = 7. 7/14 = 50%. The claim 'usually less than 3' is false by the data - it is exactly even. Also visible: the tail (7, 9) is where the anger lives, though it is 2 days of 14.

**Expected output.** 7 of 14 days under 3 minutes - 50%, not 'usually'

**Edge cases.** All distinct values -> table of 1s, shape message still readable. The bucket choice (<3 vs <=3) changes the verdict - 3 IS late by the claim's wording. Zero-delay days count as 'under 3'; state it.

**Complexity.** O(n) tally + O(u) report; the histogram is one of the cheapest, most honest tools in the kit.

## 3. The Double-Click Question: conditional counting (case cs-102)

**Problem.** Of 100 sessions: 40 were mobile, and 10 sessions double-clicked. 8 of the double-clicks were mobile. P(mobile | double-click) vs P(double-click | mobile) - compute both, and why do they differ?

**Analysis.** P(M|D) = 8/10 = 0.8; P(D|M) = 8/40 = 0.2. Same overlap (8), different denominators - that is the whole of conditional probability in one table. Confusing the two is the classic prosecutor's-fallacy shape: 'most double-clicks are mobile' does not mean 'most mobile sessions double-click'.

**Algorithm.**
1. draw the 2x2 table (mobile x double-click)
2. P(M|D) = overlap / double-click column
3. P(D|M) = overlap / mobile row
4. point at the denominator swap

**Pseudocode.**

```
    GIVEN overlap, n_double, n_mobile
    p_m_given_d <- overlap / n_double
    p_d_given_m <- overlap / n_mobile
    WRITE both WITH denominators named
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
overlap, n_double, n_mobile = 8, 10, 40
p_m_given_d = overlap / n_double
p_d_given_m = overlap / n_mobile
print(round(p_m_given_d, 2), round(p_d_given_m, 2))
# expect: 0.8 0.2
```

**Trace (dry run).** The 2x2: mobile-double 8, mobile-single 32, desktop-double 2, desktop-single 58. Down the double-click column: 8/10 = 0.8. Across the mobile row: 8/40 = 0.2. The numerators match; only the conditioning differs.

**Expected output.** P(mobile | double-click) = 0.8; P(double-click | mobile) = 0.2

**Edge cases.** Zero denominator (no double-clicks at all) -> conditional undefined - say 'no evidence', not 0. Small samples make both ratios jumpy. Base rates: 0.8 sounds damning until you notice 40% of everything is mobile - lecture 26's recurring moral.

**Complexity.** O(1) after the table exists; building the 2x2 from raw events is O(n).
