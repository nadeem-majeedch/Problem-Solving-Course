# Worked Examples — Lecture 28

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Salary Parable: mean vs median under skew](#1) | cs-109 | yes |
| [2. The Percentage Maze: percentages of what?](#2) | cs-110 | yes |
| [3. The Waiting-Time Twist: averages that hide the experience](#3) | cs-111 | yes |

---

## 1. The Salary Parable: mean vs median under skew (case cs-109)

**Problem.** Salaries 30k, 32k, 35k, 38k, 200k. Which summary survives, and how would each be (mis)used?

**Analysis.** Mean = 67k - a number nobody earns, dragged by the 200k. Median = 35k - the middle experience. Neither lies; each answers a different question (total payroll vs typical person). Misuse is quoting the one that flatters your story while calling it 'the average'.

**Algorithm.**
1. compute mean and median
2. note the gap as a skew alarm
3. state which question each answers

**Pseudocode.**

```
    mean <- sum / n
    median <- middle of sorted values
    WRITE both AND the gap
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
sal = [30, 32, 35, 38, 200]
mean = sum(sal) / len(sal)
sorted_sal = sorted(sal)
median = sorted_sal[len(sorted_sal) // 2]
print(mean, median)
# expect: 67.0 35
```

**Trace (dry run).** Mean: 335/5 = 67. Median: middle of the sorted five = 35. The 67k 'average salary' is 32k above the highest non-outlier - the gap between mean and median IS the skew detector; report both or report the median.

**Expected output.** mean 67k, median 35k - the 32k gap is the skew alarm

**Edge cases.** Even counts: median is the mean of the two middle values (define it). n=1: mean = median - no alarm possible, no confidence either. Small n makes every summary fragile: with n=5, one joiner moves the median by a whole rank.

**Complexity.** O(n) mean, O(n log n) median by sorting (O(n) selection exists - enrichment).

## 2. The Percentage Maze: percentages of what? (case cs-110)

**Problem.** A price rises 20%, then falls 20%. Back to the start? And: churn fell from 10% to 8% - is that '2%' or '20%' better?

**Analysis.** 100 -> 120 -> 96: a 4% net loss, because the second 20% applies to a different base. Churn: 10 -> 8 is 2 percentage points but (10-8)/10 = 20% relative. Mixing the two units is how numbers mislead without a single false digit.

**Algorithm.**
1. compound the changes multiplicatively: (1+r1) x (1+r2)
2. distinguish percentage points (absolute) from percent (relative)
3. restate each claim in both units

**Pseudocode.**

```
    price <- 100 * (1 + 0.20) * (1 - 0.20)
    points <- 10 - 8
    relative <- (10 - 8) / 10
    WRITE price, points, relative
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
price = 100 * 1.20 * 0.80
points = 10 - 8
relative = (10 - 8) / 10
print(price, points, relative)
# expect: 96.0 2 0.2
```

**Trace (dry run).** 120 x 0.8 = 96 - the -20% had a bigger base than the +20%. Churn: 'down 2 points' and 'down 20 percent' are both true; a report that swaps them silently inflates or deflates the achievement five-fold.

**Expected output.** price ends at 96 (not 100); churn: -2 points = -20% relative

**Edge cases.** Compounding order does not matter for products ((1+r1)(1+r2) is symmetric) but the BASES differ - that is the trap, not the order. 'Doubled' (100% relative) from a tiny base is a classic headline trick. Always ask: percentage of WHAT.

**Complexity.** O(1); the skill is vocabulary discipline, not arithmetic.

## 3. The Waiting-Time Twist: averages that hide the experience (case cs-111)

**Problem.** Waiting times (minutes): 684 customers' experiences compress to: most wait 2, a few wait 60+. Report honestly: which average, and what must accompany it?

**Analysis.** With a heavy tail, the mean (say 11.4 minutes over 684 customers) describes the queue's total cost, while the median (2) describes the typical customer. Both are true; quoting only the median hides the rage quota, quoting only the mean hides the good service. The honest bundle: median + mean + the tail fraction.

**Algorithm.**
1. compute median, mean, and share of waits above a pain threshold
2. report all three with denominators
3. explain what decision each number serves

**Pseudocode.**

```
    median <- middle wait
    mean <- total / count
    tail <- share of waits > 30
    WRITE median, mean, tail
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
waits = [2, 2, 2, 3, 4, 5, 60, 70]
med = sorted(waits)[len(waits) // 2]
mean = sum(waits) / len(waits)
tail = sum(1 for w in waits if w > 30) / len(waits)
print(med, round(mean, 1), tail)
# expect: 4 18.5 0.25
```

**Trace (dry run).** Median 4 ('half the queue waits 4 minutes or less'), mean 18.5 (the tail dominates total waiting), tail 25% (1 in 4 waits over half an hour). A press office quoting the median and an ops team quoting the mean are both right - the report needs both plus the tail share.

**Expected output.** median 3 min, mean 18.5 min, 25% wait over 30 min

**Edge cases.** Mean without the tail fraction invites 'the average wait is fine' - the exact misleading summary this lecture bans. Even-count medians interpolate - define once, use always. Threshold choice (30 min) must be justified, not tuned to flatter.

**Complexity.** O(n log n) with the sort; all three summaries from one pass over sorted data.
