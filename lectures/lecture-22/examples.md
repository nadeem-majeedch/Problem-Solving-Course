# Worked Examples — Lecture 22

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. Digit Sum, Twice: recursion as self-similar bookkeeping](#1) | cs-086 | yes |
| [2. Power by Halving: divide-and-conquer in one line](#2) | cs-087 | yes |
| [3. The Tower Steps: recursion that repeats itself](#3) | cs-088 | yes |

---

## 1. Digit Sum, Twice: recursion as self-similar bookkeeping (case cs-086)

**Problem.** Compute the digit sum of 49206 - recursively, then with iteration. Both must print the same number.

**Analysis.** The recursive insight: digit_sum(n) = n's last digit + digit_sum(everything before the last digit). The base case stops the shrinking. Writing the same function twice - once recursive, once looped - shows the two are transcriptions of one idea.

**Algorithm.**
1. base case: single-digit n -> n
2. recursive step: n mod 10 + digit_sum(n // 10)
3. iterative twin: accumulate last digits in a loop while n > 0

**Pseudocode.**

```
    FUNCTION dsum(n)
        IF n < 10 THEN RETURN n
        RETURN n mod 10 + dsum(n div 10)
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
def dsum(n):
    if n < 10:
        return n
    return n % 10 + dsum(n // 10)

def dsum_iter(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(dsum(49206), dsum_iter(49206), dsum(0))
# expect: 21 21 0
```

**Trace (dry run).** dsum(49206) = 6 + dsum(4920) = 6 + (0 + dsum(492)) = ... = 6+0+2+9+4 = 21. The call stack piles up five frames, then unwinds adding. dsum(0) -> base case 0 (no digits to strip: the guard n < 10 covers it).

**Expected output.** 21, 21, and 0 for the empty case

**Edge cases.** 0 -> 0 via the base case. Negative numbers break the // direction - out of contract, state it. Deep recursion (a 1000-digit number) hits Python's recursion limit (~1000): the iterative twin has no such ceiling - that asymmetry is worth naming.

**Complexity.** O(digits) either way; recursion adds stack frames, iteration a variable.

## 2. Power by Halving: divide-and-conquer in one line (case cs-087)

**Problem.** Compute 3^13 by repeated squaring, not by twelve multiplications.

**Analysis.** 3^13 = 3^6 x 3^6 x 3 (odd). Halving the exponent gives log2(n) multiplications instead of n. The recursion tree is a single path - no branching, no repeated subproblems - which is why memoisation (lecture 23) is unnecessary here.

**Algorithm.**
1. base: power(x, 0) = 1
2. even exponent: h = power(x, e/2); return h*h
3. odd exponent: return x * power(x, e-1) (or fold the extra x into the even step)

**Pseudocode.**

```
    FUNCTION power(x, e)
        IF e = 0 RETURN 1
        h <- power(x, e div 2)
        IF e is even RETURN h*h ELSE RETURN x*h*h
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
def power(x, e):
    if e == 0:
        return 1
    h = power(x, e // 2)
    if e % 2 == 0:
        return h * h
    return x * h * h

print(power(3, 13), 3 ** 13)
# expect: 1594323 1594323
```

**Trace (dry run).** power(3,13) -> 3 x power(3,6)... via halves 13 -> 6 -> 3 -> 1 -> 0: five frames. Squarings: 3^1=3, 3^2=9, 3^3=27... unwinding: h=3 -> 3*3*3=27? No - trace: e=0:1; e=1: 3*1*1=3; e=3: 3*3*3=27; e=6: 27*27=729; e=13: 3*729*729=1594323. Six squarings, not twelve.

**Expected output.** 1594323 (matches the built-in power)

**Edge cases.** power(x, 0) = 1 for every x (including x=0 - 0^0 = 1 by this contract; say so). Negative exponents out of contract for ints. The naive loop is O(n); halving is O(log n) - for e = 10^9, that is 30 multiplications versus a billion.

**Complexity.** O(log e) multiplications; big integers make each multiply slower as values grow, but the count is the point.

## 3. The Tower Steps: recursion that repeats itself (case cs-088)

**Problem.** Staircase of 8 steps; you climb 1 or 2 at a time. How many distinct ways to the top?

**Analysis.** The last move is a 1 (then ways(7) remain) or a 2 (then ways(6) remain): ways(n) = ways(n-1) + ways(n-2). Plain recursion recomputes the same subproblems exponentially many times - the live exhibit for why memoisation exists.

**Algorithm.**
1. base: ways(1) = 1, ways(2) = 2
2. step: ways(n) = ways(n-1) + ways(n-2)
3. note how many times ways(small) is recomputed when called naively
4. fix: cache each result the first time it is computed

**Pseudocode.**

```
    FUNCTION ways(n)
        IF n <= 2 RETURN n
        RETURN ways(n-1) + ways(n-2)
    (then add a cache table and compare the call counts)
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
calls = {"plain": 0, "memo": 0}

def ways_plain(n):
    calls["plain"] += 1
    if n <= 2:
        return n
    return ways_plain(n - 1) + ways_plain(n - 2)

def ways_memo(n, cache={1: 1, 2: 2}):
    calls["memo"] += 1
    if n in cache:
        return cache[n]
    cache[n] = ways_memo(n - 1) + ways_memo(n - 2)
    return cache[n]

print(ways_plain(8), ways_memo(8), calls["plain"], calls["memo"])
# expect: 34 34 41 13
```

**Trace (dry run).** ways(8) = ways(7)+ways(6) = 21+13 = 34 (both versions agree). But the plain version made 41 calls against the memo's 13 - at n=30 it would be about 1.66 million versus 30. Same answer, wildly different work: the definition did not change, the evaluation did.

**Expected output.** 34 ways; plain recursion made 67 calls, memoised 15

**Edge cases.** ways(0)? The recurrence never needs it (stops at 1 and 2), but define it (1: the empty climb) if you extend the contract. The mutable cache default is deliberate here and harmless - contrast with lecture 14's add_tag bug, where sharing was accidental.

**Complexity.** Plain: O(2^n)-ish (golden-ratio precise). Memoised: O(n) time and space - this is dynamic programming arriving by fix-it ticket, formally next lecture.
