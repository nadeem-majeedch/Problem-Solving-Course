# Worked Examples — Lecture 23

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Meeting Room Marathon: greedy by earliest end](#1) | cs-090 | yes |
| [2. The Tolerance Ladder: greedy that must be checked](#2) | cs-091 | yes |
| [3. The Budgeted Syllabus: dynamic programming on weight](#3) | cs-092 | yes |

---

## 1. The Meeting Room Marathon: greedy by earliest end (case cs-090)

**Problem.** Meetings (9,10.5), (9.5,11), (11,12), (10.5,12.5). Book as many non-overlapping meetings as possible in one room.

**Analysis.** Three greedy candidate rules: earliest start, shortest meeting, earliest end. Counterexamples kill the first two; earliest end survives. Proof sketch: the earliest-ending meeting can always replace the first meeting of any optimal schedule without breaking anything - the exchange argument.

**Algorithm.**
1. sort meetings by end time
2. take a meeting iff it starts at/after the last taken end
3. count the taken meetings

**Pseudocode.**

```
    sorted by end
    taken <- 0; last_end <- -infinity
    FOR each meeting (s, e)
        IF s >= last_end THEN taken++; last_end <- e
    WRITE taken
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
meetings = [(9, 10.5), (9.5, 11), (11, 12), (10.5, 12.5)]
ms = sorted(meetings, key=lambda m: m[1])
taken = 0
last_end = float("-inf")
chosen = []
for s, e in ms:
    if s >= last_end:
        taken += 1
        last_end = e
        chosen.append((s, e))
print(taken, chosen)
# expect: 2 [(9, 10.5), (11, 12)]
```

**Trace (dry run).** Sorted by end: (9,10.5), (9.5,11), (11,12), (10.5,12.5). Take (9,10.5). (9.5,11) starts 9.5 < 10.5 -> skip. (11,12) starts 11 >= 10.5 -> take. (10.5,12.5) starts 10.5 < 12 -> skip. Two meetings; note (10.5,12.5) also fits after (9,10.5) - the greedy's choice was the earlier end, which is the whole point.

**Expected output.** 2 meetings: (9, 10.5) and (11, 12)

**Edge cases.** Touching meetings (10,11) then (11,12): 's >= last_end' books both - a policy to state. Empty schedule -> 0. The rule's correctness depends on the exchange argument; for other objectives (minimise total idle time) the same data needs different machinery.

**Complexity.** O(n log n) for the sort, O(n) for the sweep.

## 2. The Tolerance Ladder: greedy that must be checked (case cs-091)

**Problem.** A tolerance budget of 10 units; items cost 4, 5, 6, 7. Maximise how many items fit - then find a cost profile where 'cheapest first' fails.

**Analysis.** For maximising count, cheapest-first IS optimal (exchange argument works). The exercise then breaks it: swap the objective to 'minimise leftover budget' and cheapest-first gives 4+5 = 9 (leftover 1)... but 4+6 = 10 (leftover 0). Greedy correctness is objective-relative - the hardest lesson of the day.

**Algorithm.**
1. maximise count: sort by cost ascending, take while budget lasts
2. minimise leftover: the same greedy misses better pairs - exhibit one
3. moral: prove the rule for YOUR objective, not in general

**Pseudocode.**

```
    sort costs ascending
    taken <- 0; spent <- 0
    FOR each cost
        IF spent + cost <= budget THEN taken++; spent += cost
    WRITE taken, spent, budget - spent
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
costs = [4, 5, 6, 7]
budget = 10
costs.sort()
taken = spent = 0
for c in costs:
    if spent + c <= budget:
        taken += 1
        spent += c
print(taken, spent, budget - spent)
# expect: 2 9 1
```

**Trace (dry run).** Count objective: 4, then 5 (spent 9); 6 would exceed -> 2 items, leftover 1. But for leftover-optimality, 4+6 = 10 beats 4+5 = 9 - the greedy answer is optimal for count and suboptimal for leftover. One data set, two objectives, opposite verdicts.

**Expected output.** 2 items (4 + 5), leftover 1 - optimal for count, NOT for leftover (4+6 fills exactly)

**Edge cases.** Budget 0 -> 0 items. Costs exceeding budget are skipped, not errors. Ties (4,4): either order works for count. The counterexample style - a tiny input where the rule fails - is the standard way to test greedy claims.

**Complexity.** O(n log n) sort dominates; the check-for-counterexample habit costs nothing and saves wrong answers.

## 3. The Budgeted Syllabus: dynamic programming on weight (case cs-092)

**Problem.** Topics with (hours, points): (3,60), (2,50), (4,80), (1,30). Study budget 5 hours; maximise total points (each topic taken at most once).

**Analysis.** 0/1 knapsack. Greedy by points-per-hour takes (1,30),(2,50),(3,60)? Budget 5 -> 1+2 = 3h/80pts, then (3,60) exceeds -> total 80. Optimal is (2,50)+(3,60) = 110. DP over 'best value with j hours' fixes it: dp[j] = max(dp[j], dp[j-h] + p) - iterated hours-high-to-low so each topic is used at most once.

**Algorithm.**
1. dp[0..budget] = 0
2. for each topic (h, p): for j from budget down to h:
3. dp[j] = max(dp[j], dp[j-h] + p)
4. answer dp[budget]

**Pseudocode.**

```
    dp <- array of zeros, size budget+1
    FOR each (h, p) in topics
        FOR j from budget DOWN TO h
            dp[j] <- max(dp[j], dp[j-h] + p)
    WRITE dp[budget]
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
topics = [(3, 60), (2, 50), (4, 80), (1, 30)]
budget = 5
dp = [0] * (budget + 1)
for h, p in topics:
    for j in range(budget, h - 1, -1):
        dp[j] = max(dp[j], dp[j - h] + p)
print(dp[budget])
# expect: 110
```

**Trace (dry run).** After (3,60): dp = [0,0,0,60,60,60]. After (2,50): dp[5] = max(60, dp[3]+50) = 110; dp[2] = 50. After (4,80): nothing beats 110 (needs 4+? ... dp[5] vs dp[1]+80 = 80). After (1,30): dp[5] = max(110, dp[4]+30) = 110. Answer 110 = (2,50)+(3,60).

**Expected output.** 110 points (topics (2,50) and (3,60))

**Edge cases.** Zero-hour topics break the loop guard (range empty) - treat as free points or reject, state it. Budget 0 -> 0 unless a 0-hour topic exists. The descending j-loop is the 0/1 discipline; ascending would allow re-using a topic twice (that variant is a different, legitimate problem - unbounded knapsack).

**Complexity.** O(items x budget) time and O(budget) space - the classic DP price, paid to buy optimality that greedy cannot guarantee here.
