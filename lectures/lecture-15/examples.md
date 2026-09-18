# Worked Examples — Lecture 15

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The locker problem: divisors leave squares open](#1) | cs-057 | yes |
| [2. Team photo: count first, then block](#2) | cs-058 | yes |
| [3. The committee draw: complements and stars](#3) | cs-059 | yes |
| [4. The birthday question: product of complements](#4) | cs-060 | yes |

---

## 1. The locker problem: divisors leave squares open (case cs-057)

**Problem.** 100 lockers, 100 students; student i toggles every i-th locker. Which lockers end open?

**Analysis.** Locker n is toggled once per divisor of n. Divisors pair (d, n/d); the pair is odd-sized exactly when d = n/d, i.e. n is a perfect square. So squares stay open - a counting argument, verified by simulation.

**Algorithm.**
1. argue: toggles(n) = number of divisors of n
2. divisor pairs (d, n/d) - odd count iff n is a square
3. verify: simulate 100 students over 100 lockers

**Pseudocode.**

```
    open <- list of n falses
    FOR student i in 1..100
        FOR locker j in i, 2i, 3i .. 100
            open[j] <- NOT open[j]
    WRITE positions where open is true
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
open_lockers = [False] * 101
for student in range(1, 101):
    for locker in range(student, 101, student):
        open_lockers[locker] = not open_lockers[locker]
squares = [n for n in range(1, 101) if open_lockers[n]]
print(squares[:5], squares[-1], len(squares))
# expect: [1, 4, 9, 16, 25] 100 10
```

**Trace (dry run).** Locker 6: students 1, 2, 3, 6 toggle it - four toggles -> closed. Locker 9: students 1, 3, 9 - three toggles -> open. Ten squares between 1 and 100: 1, 4, 9, ... 100.

**Expected output.** open lockers: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

**Edge cases.** Locker 1 toggled once (open). Zero 'lockers' - vacuous. The simulation must agree with the divisor argument; if they disagree, the argument is wrong, not the machine.

**Complexity.** Simulation O(n log n) (harmonic sum); the mathematical answer is O(1) - reasoning beats brute force.

## 2. Team photo: count first, then block (case cs-058)

**Problem.** 5 students line up for a photo; P and Q refuse to stand together. How many acceptable lineups?

**Analysis.** Complement counting: all lineups (5! = 120) minus lineups with P and Q adjacent. Glue them into a block: 4 units, arranged 4! ways, times 2 for internal order = 48. Answer 120 - 48 = 72.

**Algorithm.**
1. count all arrangements: 5!
2. count forbidden: glue PQ into one block -> 4! x 2
3. subtract
4. sanity-check both counts are integers and the answer is smaller than 5!

**Pseudocode.**

```
    total    <- 5! = 120
    blocked  <- 4! * 2 = 48
    answer   <- total - blocked
    WRITE answer
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
import math
total = math.factorial(5)
blocked = math.factorial(4) * 2
print(total, blocked, total - blocked)
# expect: 120 48 72
```

**Trace (dry run).** 120 total. Forbidden: treat PQ as one unit among 4 units -> 24 orders, x2 (PQ or QP) = 48. 72 acceptable. Cross-check for n=3 with P,Q,R: 6 - 2*2 = 2, namely P R Q and Q R P - confirmed by hand.

**Expected output.** 72

**Edge cases.** If P refuses Q but Q does not refuse P, the block count is the same (adjacency is symmetric). Two separate feuds: inclusion-exclusion - do not double-count lineups violating both.

**Complexity.** O(1) with the counting argument; enumerating 120 lineups is fine too but does not scale.

## 3. The committee draw: complements and stars (case cs-059)

**Problem.** A committee of 4 from 6 CS and 4 DS students. How many committees include at least one of each programme?

**Analysis.** Complement again: total C(10,4) = 210 minus all-CS C(6,4) = 15 minus all-DS C(4,4) = 1. 210 - 16 = 194. The complement is tiny where the direct count has many cases - that is the method.

**Algorithm.**
1. total = C(10,4)
2. forbidden = all-CS + all-DS
3. answer = total - forbidden

**Pseudocode.**

```
    C(n, k) via factorials
    total     <- C(10, 4)
    forbidden <- C(6, 4) + C(4, 4)
    WRITE total - forbidden
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
import math
c = math.comb
total = c(10, 4)
forbidden = c(6, 4) + c(4, 4)
print(total, forbidden, total - forbidden)
# expect: 210 16 194
```

**Trace (dry run).** C(10,4) = 210. All-CS: C(6,4) = 15. All-DS: C(4,4) = 1. The cases are disjoint (a committee cannot be both all-CS and all-DS), so simple subtraction is valid.

**Expected output.** 194

**Edge cases.** If the committee were larger than one programme's size (say 5 from 4 DS), all-DS is impossible and contributes 0 - C(4,5) = 0. Ensure your formula handles that, not crashes.

**Complexity.** O(1) arithmetic via factorials; a brute-force enumeration would touch all 210 committees.

## 4. The birthday question: product of complements (case cs-060)

**Problem.** How many people are needed for a shared-birthday chance above 50%, assuming 365 equally likely days and no leap days?

**Analysis.** P(no share) = 365/365 x 364/365 x ... (365-k+1)/365. Multiply until the product drops below 1/2; the answer is 23. The simulation cross-checks the closed computation.

**Algorithm.**
1. multiply the falling product
2. stop when P(no share) < 0.5
3. report the count
4. verify with a random-birthday simulation

**Pseudocode.**

```
    p <- 1
    n <- 0
    WHILE p >= 0.5
        n <- n + 1
        p <- p * (366 - n) / 365
    WRITE n
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
p = 1.0
n = 0
while p >= 0.5:
    n += 1
    p *= (366 - n) / 365
print(n, round(1 - p, 3))
# expect: 23 0.507
```

**Trace (dry run).** At n=22 the product is still above 0.5; the 23rd factor (344/365 = 0.943) pushes it to 0.4927 - below one half. So 23 people give P(shared) ~ 0.507. Simulation with many trials agrees.

**Expected output.** 23 people (P(shared) ~ 50.7%)

**Edge cases.** Two people: P = 1/365 ~ 0.27%. Every term after 365 would be non-positive - the loop must stop at 366 people; real classes cap far earlier. Leap days change constants, not the method.

**Complexity.** O(answer) for the product, O(trials x n) for the simulation - both trivial here.
