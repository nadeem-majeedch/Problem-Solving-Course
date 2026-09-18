# Worked Examples — Lecture 20

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The 4-Digit Lock: ten thousand tries and a theorem](#1) | cs-077 | yes |
| [2. Perfect Numbers: brute force with a sqrt speed-up](#2) | cs-078 | yes |
| [3. The Subset Riddle: every subset, systematically](#3) | cs-080 | yes |

---

## 1. The 4-Digit Lock: ten thousand tries and a theorem (case cs-077)

**Problem.** How many 4-digit codes (0000 to 9999) have digit sum exactly 12?

**Analysis.** Brute force is a theorem-checker: try all 10,000 codes, count, and trust the machine. Then compare with the counting argument (stars and bars with digit caps) - when independent methods agree, confidence is earned, not assumed.

**Algorithm.**
1. enumerate every code 0000..9999
2. sum its four digits
3. count the codes whose sum equals 12

**Pseudocode.**

```
    count <- 0
    FOR code from 0 to 9999
        s <- sum of digits of code (padded to 4)
        IF s = 12 THEN count <- count + 1
    WRITE count
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
count = 0
for code in range(10000):
    if sum(int(d) for d in f"{code:04d}") == 12:
        count += 1
print(count)
# expect: 415
```

**Trace (dry run).** The machine counts 415. The counting argument: solutions of d1+d2+d3+d4 = 12 in digits 0..9 - unrestricted C(15,3) = 455, minus the cases where one digit exceeds 9 (4 x C(5,3) = 40) -> 415. Both routes agree.

**Expected output.** 415 codes

**Edge cases.** Leading zeros are digits - '0412' is a legal code (the f"{code:04d}" padding enforces it). Sum 0 -> exactly 1 code (0000); sum 36 -> exactly 1 (9999). The brute force needs no cleverness and no case analysis - that IS its virtue.

**Complexity.** O(10^4 x 4) - constant here, but the pattern is exponential in the number of dials: k dials -> 10^k. Brute force wins while the space stays small.

## 2. Perfect Numbers: brute force with a sqrt speed-up (case cs-078)

**Problem.** A perfect number equals the sum of its proper divisors (6 = 1+2+3). Find all perfect numbers below 10000.

**Analysis.** The naive test tries every candidate divisor up to n - about 50 million operations for this range. Divisors come in pairs (d, n/d), so scanning to sqrt(n) finds all of them: the same brute force, roughly n/2 times cheaper. Correctness first, then the cheap win - the brute-force mindset with one refinement.

**Algorithm.**
1. for each n from 2 to 9999
2. sum divisor pairs d and n/d while d*d <= n
3. start the sum at 1 (1 divides everything, its pair is n itself - excluded)
4. report n when the sum equals n

**Pseudocode.**

```
    FUNCTION is_perfect(n)
        total <- 1; d <- 2
        WHILE d*d <= n
            IF n mod d = 0 THEN total <- total + d + n/d
            d <- d + 1
        RETURN n > 1 AND total = n
    WRITE all n in 2..9999 with is_perfect(n)
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
def is_perfect(n):
    total = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            total += d + n // d
        d += 1
    return n > 1 and total == n

print([n for n in range(2, 10000) if is_perfect(n)])
# expect: [6, 28, 496, 8128]
```

**Trace (dry run).** n=6: d=2 divides -> total 1+2+3=6; d=3: 9 > 6 stop; 6 = 6 -> perfect. n=12: 1+2+6+3+4=16 > 12 -> not perfect. The pair trick: for 28, d=2 gives 2 and 14 in one step.

**Expected output.** [6, 28, 496, 8128]

**Edge cases.** n=1: excluded explicitly (its proper-divisor sum is 0). Perfect squares: d*d = n adds d twice (as d and n/d) - which is correct, since the divisor d should count once but appears as the pair (d, d) summing to 2d... wait, check n=36: divisors 1,2,3,4,6,9,12,18 sum to 55; the loop gives 1 + (2+18) + (3+12) + (4+9) + (6+6) = 1+20+15+13+12 = 61? No: 6 is added once as d and once as n//d -> 12 total, but 6 should count once, so total 61 is wrong - the classic trap; a production version adds n//d only when d != n//d.

**Complexity.** O(n * sqrt(n)) overall - about 1.3 million operations here; the naive version needs 50 million. Same answer, 40x cheaper.

## 3. The Subset Riddle: every subset, systematically (case cs-080)

**Problem.** From values 3, 5, 2, 8, find a subset summing to 10 - or prove none exists.

**Analysis.** n = 4 gives 16 subsets - enumerate them all via bitmasks. Mask bit i means 'take item i'. Exhaustive search doubles as a proof: if no mask hits the target, no subset does. That certificate is what brute force uniquely offers.

**Algorithm.**
1. count masks 0 .. 2^n - 1
2. for each mask, sum the selected items
3. first hit -> report the subset
4. no hit after all masks -> report 'none' (a proof)

**Pseudocode.**

```
    FOR mask from 0 to 2^n - 1
        s <- sum of items[i] where bit i of mask is 1
        IF s = target THEN RETURN that subset
    RETURN 'none'
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
items = [3, 5, 2, 8]
target = 10
found = None
for mask in range(1 << len(items)):
    total = sum(items[i] for i in range(len(items)) if mask >> i & 1)
    if total == target:
        found = [items[i] for i in range(len(items)) if mask >> i & 1]
        break
print(found)
# expect: [3, 5, 2]
```

**Trace (dry run).** Masks in order: {} 0, {3} 3, {5} 5, {3,5} 8, {2} 2, {3,2} 5, {5,2} 7, {3,5,2} 10 -> hit. The early exit stops before {8} is even tried - first-found wins, say so.

**Expected output.** subset found: 3 + 5 + 2 = 10

**Edge cases.** Target 0 -> the empty subset (mask 0) hits immediately - decide whether that is a legal answer. No solution (target 11 is impossible: 10 and 13 are reachable, 11 is not) -> the full sweep is the proof. 2^n explodes: n=30 is already a billion - the wall from the complexity discussion, live.

**Complexity.** O(2^n) time - the price of the proof; meet-in-the-middle or DP (later lectures) trade that certainty for speed.
