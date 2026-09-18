# Worked Examples — Lecture 05

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The pager schedule as a cycle](#1) | cs-017 | no |
| [2. Digits, sums, and the divisible-by-3 rule](#2) | cs-018 | no |

---

## 1. The pager schedule as a cycle (case cs-017)

**Problem.** On-call duty rotates among 5 people daily; person 1 is on call on day 1. Who is on call on day 47? And what changes if rotation skips weekends (day 1 = Monday)?

**Analysis.** The plain rotation is a cycle of length 5: day n maps to ((n - 1) mod 5) + 1. The minus-one/plus-one shifts keep person 1 on day 1; forgetting them is the classic off-by-one. The weekend variant needs a second model: count only the weekdays before day n, then apply the same cycle formula to that count.

**Algorithm.**
1. subtract 1 from the day number (convert to a 0-based cycle position)
2. take the remainder mod 5
3. add 1 back
4. weekend variant: weekdays = weeks * 5 + min(remainder_days, 5), then reuse the cycle formula

**Pseudocode.**


    FUNCTION on_call(day)
        RETURN ((day - 1) MOD 5) + 1

    FUNCTION on_call_weekdays(day)
        (weeks, rem) <- DIVMOD(day - 1, 7)
        weekdays <- weeks * 5 + MIN(rem, 5)
        RETURN (weekdays MOD 5) + 1


**Trace (dry run).** Day 47: (47 - 1) mod 5 = 46 mod 5 = 1, so person 2. Weekend variant: divmod(46, 7) = (6, 4), so weekdays = 30 + 4 = 34; 34 mod 5 = 4, so person 5. The reference code prints 2 then 5.

**Expected output.** 2 then 5

**Edge cases.** Day 1 itself must return person 1 (the -1/+1 discipline). Day 0 and negative days are outside the spec - say so. If day 1 were a Wednesday the weekday count needs an offset; the assumption 'day 1 is Monday' must be written down.

**Complexity.** O(1) for both variants - arithmetic beats simulating day by day.

## 2. Digits, sums, and the divisible-by-3 rule (case cs-018)

**Problem.** Peel the digits of 4723 by arithmetic and sum them. Is 4723 divisible by 3?

**Analysis.** Peeling: n mod 10 is the last digit; n div 10 removes it. Repeat until n reaches 0. The digit sum doubles as the divisibility rule: a number is divisible by 3 exactly when its digit sum is.

**Algorithm.**
1. total <- 0
2. while n > 0: total <- total + (n mod 10); n <- n div 10
3. return total

**Pseudocode.**


    FUNCTION digit_sum(n)
        total <- 0
        WHILE n > 0
            total <- total + (n MOD 10)
            n <- n DIV 10
        RETURN total


**Trace (dry run).** 4723: digit 3, n becomes 472. 472: digit 2, n 47. 47: digit 7, n 4. 4: digit 4, n 0. Sum 3 + 2 + 7 + 4 = 16. 16 mod 3 = 1, so not divisible by 3.

**Expected output.** 16 then False

**Edge cases.** n = 0 must return 0 (the loop never runs). Negative numbers: the spec covers n >= 0, or take the absolute value first - either is fine if stated. Leading zeros do not exist in this model: the digit sum of 10^k is 1 for any k.

**Complexity.** O(d) where d is the digit count (about log10 of n) - logarithmic in the value, which surprises students.

---

**Python companion.** The digit-peel loop from today's staircase, executing:

```python
n = 4723
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)
# expect: 16
```
