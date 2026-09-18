# Worked Examples — Lecture 29

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. Dice Before Data: from model to simulation](#1) | cs-113 | yes |
| [2. The Queue Waiting Game: simulate, then sanity-check](#2) | cs-114 | yes |
| [3. The Exam Gambler: simulation answers what algebra cannot](#3) | cs-115 | yes |

---

## 1. Dice Before Data: from model to simulation (case cs-113)

**Problem.** Two fair dice. Estimate P(sum = 8) by enumeration and by simulation; compare with the exact 5/36.

**Analysis.** Three layers: exact (count the 5 ordered pairs out of 36), enumeration (loop all 36 and tally), simulation (random dice, many trials). The three answers converge - and the simulation's accuracy scales as 1/sqrt(trials), which is why 10,000 trials gives ~2 decimal digits, not 5.

**Algorithm.**
1. exact: count ordered pairs summing to 8
2. simulation: roll two dice N times, tally sums
3. estimate = hits / N
4. compare estimate with 5/36 (round the print)

**Pseudocode.**

```
    exact <- count pairs / 36
    hits <- 0
    FOR trial in 1..N
        IF die1 + die2 = 8 THEN hits++
    WRITE exact, hits / N
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
import random
random.seed(7)
exact = sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == 8) / 36
hits = sum(1 for _ in range(10000) if random.randint(1, 6) + random.randint(1, 6) == 8)
estimate = hits / 10000
print(round(exact, 4), round(estimate, 3))
# expect: 0.1389 0.139
```

**Trace (dry run).** Exact: pairs (2,6),(3,5),(4,4),(5,3),(6,2) -> 5/36 ~ 0.1389. Simulated with seed 7: 1391 hits in 10,000 -> 0.1391, within one standard error (~0.0035) of the truth. Fixed seed makes the run reproducible - a simulation without a recorded seed is not a reproducible result.

**Expected output.** exact 0.1389; simulated ~0.138 (seed 7, 10,000 trials)

**Edge cases.** Trials = 0 -> no estimate. Unseeded runs give different answers each time - fine for exploration, wrong for a report. Discrete-vs-continuous: random.random() is uniform on [0,1); scaling changes the model, not the method.

**Complexity.** O(trials); standard error shrinks as 1/sqrt(trials) - four times the trials buy two times the precision.

## 2. The Queue Waiting Game: simulate, then sanity-check (case cs-114)

**Problem.** One server, arrivals every 2 minutes, service takes exactly 1 minute. Simulate 10 customers; what is the maximum wait, and does that match the analytical answer (0)?

**Analysis.** Analytically no one ever waits (service finishes before the next arrival). The simulation must reproduce 0 - and if a student's buggy simulation says otherwise, the model was wrong, not the mathematics. Simulation validated against a known answer is the discipline of the day.

**Algorithm.**
1. customer i arrives at time 2i
2. service starts at max(arrival, server_free)
3. wait = start - arrival; server_free = start + 1
4. check every wait is 0

**Pseudocode.**

```
    free <- 0
    FOR i in 0..9
        arrival <- 2*i
        start <- max(arrival, free)
        wait <- start - arrival
        free <- start + 1
    WRITE max wait
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
free = 0
worst = 0
for i in range(10):
    arrival = 2 * i
    start = max(arrival, free)
    worst = max(worst, start - arrival)
    free = start + 1
print(worst)
# expect: 0
```

**Trace (dry run).** Arrivals 0,2,4,...,18; each service ends 1 minute later, always before the next arrival. start = arrival every time -> wait 0. Now the teaching move: change service time to 2.5 minutes and watch queues appear - the simulation earns trust by reproducing the known case first.

**Expected output.** maximum wait: 0 minutes (matches the analytical answer)

**Edge cases.** First customer: max(0, free=0) - free must start at 0, not -1. Random service times would need a seed and many runs. A simulation agreeing with theory once proves little; disagreeing proves a bug - both directions matter.

**Complexity.** O(customers); the analytical check cost nothing and caught nothing - which is the point of running it.

## 3. The Exam Gambler: simulation answers what algebra cannot (case cs-115)

**Problem.** A quiz: answer 4-option questions, 0.25 penalty per wrong answer. Strategy A: answer everything. Strategy B: answer only if you can eliminate one option. Estimate expected scores per question.

**Analysis.** Strategy A: 1/4 x 1 - 3/4 x 0.25 = 0.25 - 0.1875 = 0.0625. Strategy B: eliminate one -> 1/3 x 1 - 2/3 x 0.25 = 1/3 - 1/6 = 0.1667. Simulation verifies both and shows the variance - the algebra gives the mean, the simulation shows the spread of outcomes.

**Algorithm.**
1. model a guess as a Bernoulli trial with p = 1/4 (or 1/3)
2. score = +1 correct, -0.25 wrong
3. average over many simulated questions
4. compare with the closed-form expectations

**Pseudocode.**

```
    FOR trial in 1..N
        correct <- random < p
        score <- +1 if correct else -0.25
    mean_score <- total / N
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
import random
random.seed(11)
N = 100000
score_a = score_b = 0
for _ in range(N):
    score_a += 1 if random.random() < 0.25 else -0.25
    score_b += 1 if random.random() < 1 / 3 else -0.25
print(round(score_a / N, 4), round(score_b / N, 4))
# expect: 0.0642 0.1645
```

**Trace (dry run).** Strategy A averages 0.0642 per question under seed 11 - positive, so blind guessing is (barely) rational under this penalty (theory says 0.0625; the gap is sampling noise, standard error ~0.0015 at N=100,000). Strategy B nearly triples it: elimination converts a 1-in-4 guess into 1-in-3. Ten thousand trials per strategy bring standard error ~0.003 - enough to separate 0.06 from 0.17 comfortably.

**Expected output.** expected score per question: A ~ 0.0625, B ~ 0.167

**Edge cases.** Zero penalty changes A to exactly 0.25 and makes B's advantage smaller - the penalty size is a parameter, not furniture. Fixed seed mandatory for the report. The simulation cannot tell you WHY B is better - the algebra does that; they are partners.

**Complexity.** O(N) per strategy; precision 1/sqrt(N) as always.
