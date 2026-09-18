# Worked Examples — Lecture 01

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The coffee card, modelled honestly](#1) | cs-001 | no |
| [2. The elevator: movement vs stops](#2) | cs-002 | no |
| [3. Which vending machine? Writing the rules](#3) | cs-003 | no |
| [4. The library fine, one ambiguity at a time](#4) | cs-004 | no |

---

## 1. The coffee card, modelled honestly (case cs-001)

**Problem.** A cafe card gives every 10th drink free (buy 9, the 10th costs nothing). Price 3.50 per paid drink; the student wants 22 drinks this month. What do they pay?

**Analysis.** Two readings of the rule exist: (R1) a free drink still earns a stamp, or (R2) only paid drinks earn stamps. We state R2 as the assumption: stamps accrue on paid drinks only. Then the count is mechanical: every 9 paid drinks, the next drink is free.

**Algorithm.**
1. count drinks wanted, one at a time
2. if the stamp counter has reached 9, this drink is free and the counter resets
3. otherwise it is paid and earns a stamp
4. total = paid drinks x price

**Pseudocode.**

```
    stamps <- 0
    paid <- 0
    free <- 0
    FOR each of the 22 wanted drinks
        IF stamps = 9 THEN
            free <- free + 1
            stamps <- 0
        ELSE
            paid <- paid + 1
            stamps <- stamps + 1
        WRITE paid, free, paid * price
```

**Trace (dry run).** Drinks 1-9: paid 1..9, stamps 1..9. Drink 10: stamps = 9, so free (stamps reset). Drinks 11-19: paid again (stamps 1..9). Drink 20: free. Drinks 21-22: paid (stamps 1..2). Final: paid = 20, free = 2, total = 20 x 3.50 = 70.00.

**Expected output.** (20, 2, 70.0)

**Edge cases.** 22 drinks is just past a free drink (20 paid). At exactly 9 or 10 drinks the boundary bites: 10 drinks means 9 paid + 1 free; 9 drinks means 9 paid, 0 free. Zero drinks must give (0, 0, 0.00). Under reading R1 (free drinks earn stamps) the same month costs less - the assumption is worth real money.

**Complexity.** O(wanted) time, O(1) space; a closed form (paid = wanted - wanted // 10) exists and is worth deriving as a check.

## 2. The elevator: movement vs stops (case cs-002)

**Problem.** An elevator serves requests in press order: [3, 7, 3, 1, 5]. 3 s per floor moved, 6 s per stop (including the first). Total time?

**Analysis.** Model: time = (floors moved between successive requests) x 3 + (number of stops) x 6. Stops = number of requests (the pressed floors), movement = sum of |difference| between consecutive entries.

**Algorithm.**
1. pair consecutive requests
2. sum absolute floor differences
3. add 6 s per request
4. output the total

**Pseudocode.**

```
    moves <- 0
    FOR each pair (a, b) of consecutive requests
        moves <- moves + |b - a|
    total <- moves * 3 + len(requests) * 6
```

**Trace (dry run).** Pairs: (3,7)=4, (7,3)=4, (3,1)=2, (1,5)=4. Moves = 14. Time = 14 x 3 = 42 plus 5 x 6 = 30. Total 72 s.

**Expected output.** 72

**Edge cases.** A repeated request ([3, 7, 3]) costs a stop but zero movement. A single request has no pairs: movement 0, one stop. An empty request list should return 0 - and exposes whether your model counts a 'stop' for a non-trip. Debate: reordering stops to minimise movement is the tour problem - deliberately out of scope today.

**Complexity.** O(n) time for n requests; the *optimisation* of ordering is a different (harder) problem, previewed in Block III.

## 3. Which vending machine? Writing the rules (case cs-003)

**Problem.** Machine A sells at 2.00, exact coins only. Machine B sells at 2.30 and gives change. The student holds specific coins. Write decision rules covering exact match, overpay possible, overpay impossible, and B sold out.

**Analysis.** The deliverable is the rule list, not code. Order matters: check affordability before preference, and state the tie-breaks. Rules: (1) If A's price is payable exactly with held coins, prefer A. (2) Else if B is in stock and the student can pay at least B's price, use B. (3) Else no purchase.

**Algorithm.**
1. compute whether coins sum exactly to A's price
2. compute whether coins cover B's price
3. decide in that order and name the deciding rule

**Pseudocode.**

```
    IF sum(coins) = priceA THEN use A (exact match)
    ELSE IF stockB > 0 AND sum(coins) >= priceB THEN use B (change given)
    ELSE no purchase
```

**Trace (dry run).** Holding 2.50 against A=2.00: not exact (rule 1 fails), B covered (rule 2) → machine B. Holding 2.00 against A=2.00 → machine A. Holding 1.80 against both → no purchase.

**Expected output.** machine B / machine A / no purchase (per the three traces)

**Edge cases.** Exact machine sold out; coins cover both prices (prefer A - cheaper, no change queue); coins exceed A but not exactly (the trap: A refuses overpayment, so rule 1's 'exactly' is load-bearing).

**Complexity.** Constant time; the difficulty is specification completeness, not cost.

## 4. The library fine, one ambiguity at a time (case cs-004)

**Problem.** Fines: 0.50/day for days 1-7, 1.00/day for days 8-30, cap 10.00. Returned on day 5, day 12, day 40 - and on the due date itself?

**Analysis.** First ambiguity: is the due date day 0 (return day free) or day 1? We set return-day = day 0, so a return 'on day k' accrues k charged days. Second: cap applies to the total, per loan. Third: waived conditions (e.g. closure days) are out of scope and stated as an assumption.

**Algorithm.**
1. determine charged days k
2. fine = 7 x 0.50 for the first week portion plus 1.00 for days 8..k
3. apply cap 10.00

**Pseudocode.**

```
    IF k = 0 THEN fine <- 0
    ELSE
        fine <- min(k, 7) * 0.50 + max(0, k - 7) * 1.00
        fine <- min(fine, 10.00)
```

**Trace (dry run).** k=5: 5 x 0.50 = 2.50. k=12: 7 x 0.50 + 5 x 1.00 = 8.50, and the '7.00' reading corresponds to charging only 5 of the over-week days - our rule gives 8.50; state which reading you defend. k=40: 3.50 + 33.00 = 36.50 → capped 10.00.

**Expected output.** 2.50; 8.50 (our reading); 10.00; due-date return 0.00

**Edge cases.** k = 7 exactly (3.50), k = 8 (4.50 - the tier jumps by 1.00, not 0.50), k = 31+ beyond the stated schedule (cap already binds), negative k is invalid input.

**Complexity.** Constant time. The pedagogical content is the two contested readings, not the arithmetic.

---

**Python companion.** Optional preview - Python arrives in Lecture 04. The block below runs the coffee-card arithmetic you solved on paper, so you can verify your own answer:

```python
wanted = 22
price = 3.50
paid = wanted - wanted // 10
free = wanted // 10
print(paid, free, paid * price)
# expect: 20 2 70.0
```
