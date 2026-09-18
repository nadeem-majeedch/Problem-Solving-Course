# Worked Examples — Lecture 04

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. Echo with limits, translated from pseudocode](#1) | cs-013 | yes |
| [2. Course list cleaner: first lists, first filters](#2) | cs-014 | no |
| [3. The change maker: state and arithmetic](#3) | cs-015 | no |
| [4. The meeting scheduler: constraints first](#4) | cs-016 | no |

---

## 1. Echo with limits, translated from pseudocode (case cs-013)

**Problem.** Read lines until the sentinel 'done'; echo each line uppercased, but skip lines longer than 20 characters (count them instead).

**Analysis.** The pseudocode transfers line by line: READ → input(), WRITE → print(), sentinel loop → while True with break. The type lesson: input() gives strings; upper() is a string method - no conversion needed here.

**Algorithm.**
1. loop: read line
2. if line == 'done': stop
3. if len(line) > 20: count skip; continue
4. print(line.upper())

**Pseudocode.**

```
    skipped <- 0
    LOOP
        READ line
        IF line = "done" THEN STOP
        IF length(line) > 20 THEN skipped <- skipped + 1
        ELSE WRITE upper(line)
    WRITE skipped at the end
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
lines = ["coffee", "x" * 21, "tea", "done", "late"]
skipped = 0
for line in lines:
    if line == "done":
        break
    if len(line) > 20:
        skipped += 1
    else:
        print(line.upper())
print(skipped)
# expect: COFFEE
# expect: TEA
# expect: 1
```

**Trace (dry run).** Inputs: 'coffee' → COFFEE; a 21-char line → skipped (count 1); 'done' → stop, then the skip count prints.

**Expected output.** COFFEE then 1

**Edge cases.** 'DONE' uppercase is not the sentinel (case-sensitivity stated); empty line (echo as empty); exactly 20 chars (kept - boundary); no 'done' ever (the loop needs an end-of-input story - state it).

**Complexity.** O(total input length). Python: `while True:` + `break` mirrors the flowchart's loop with two exits.

## 2. Course list cleaner: first lists, first filters (case cs-014)

**Problem.** Given a list of course codes, remove empty strings and duplicates (keeping first occurrences), and report how many entries were dropped.

**Analysis.** Two patterns at once: filter (keep non-empty) and dedupe (seen-set idea, done here with a list to stay in-lecture). The report-the-toll habit starts here: a cleaner that fixes silently is a liar.

**Algorithm.**
1. result <- empty, dropped <- 0
2. for each entry: if empty, dropped += 1
3. elif already in result: dropped += 1
4. else append
5. print result and dropped

**Pseudocode.**

```
    result <- []
    dropped <- 0
    FOR each entry IN codes
        IF entry = "" THEN dropped <- dropped + 1
        ELSE IF entry IN result THEN dropped <- dropped + 1
        ELSE append entry to result
    WRITE result, dropped
```

**Trace (dry run).** ["CS1", "", "MA2", "CS1"]: CS1 kept; "" dropped (1); MA2 kept; CS1 duplicate dropped (2). Result [CS1, MA2], dropped 2.

**Expected output.** ['CS1', 'MA2'] 2

**Edge cases.** All duplicates; empty input list (dropped 0, result []); case differences ('cs1' vs 'CS1' - state whether they match); whitespace-only entries (empty after strip? - the rule must say).

**Complexity.** O(n^2) with the list-membership check; the set version (lecture 13) is O(n) - say so, then wait.

## 3. The change maker: state and arithmetic (case cs-015)

**Problem.** Price 2.35. The customer pays with coins 1.00, 1.00, 0.50. Compute credit as coins arrive, then change as 20/10/5-cent breakdown.

**Analysis.** Running total (credit) plus a breakdown loop - two patterns in one small program. Floating point caution: work in cents (235, 250) so subtraction is exact; this is a modelling decision worth stating.

**Algorithm.**
1. work in integer cents
2. credit <- sum of coins as they are entered
3. change <- credit - price_cents
4. for each denomination 200,100,50,20,10,5: give as many as fit, subtract

**Pseudocode.**

```
    price <- 235 (cents)
    credit <- 0
    FOR each coin inserted: credit <- credit + coin
    change <- credit - price
    FOR each d IN [200, 100, 50, 20, 10, 5]
        WHILE change >= d
            give one d
            change <- change - d
```

**Trace (dry run).** credit = 100 + 100 + 50 = 250. change = 15. 10-cent: one (5 left). 5-cent: one (0). Result: one 10c + one 5c.

**Expected output.** credit 250, change 15 -> [10, 5]

**Edge cases.** Exact payment (change 0 - the breakdown loop must not print); overpay by more than any coin covers; floating-point version (0.1 + 0.2 problems) demonstrated live as the reason for cents; coin list unsorted (why sorted-descending matters).

**Complexity.** O(coins + denominations). The greedy breakdown works for this coin system - lecture 23 returns to when greedy is trustworthy.

## 4. The meeting scheduler: constraints first (case cs-016)

**Problem.** Place requests into 5 slots, 1 hour each, max 2 meetings per slot, respect 'not on Friday'. Print the schedule and the refused requests.

**Analysis.** Data shape: each request has a day and a duration; slots have capacity. The plan: filter illegal requests first, then fill slots in order, tracking load per slot. The refusal list is a first-class output, not an afterthought.

**Algorithm.**
1. load <- [0,0,0,0,0] per slot
2. for each request: if Friday, refuse
3. elif any slot with load < 2: place, load += 1
4. else refuse (full)
5. print schedule and refusals

**Pseudocode.**

```
    FOR each request
        IF request.day = friday THEN refuse (rule)
        ELSE IF exists slot with load < 2 THEN place; load[slot] += 1
        ELSE refuse (full)
    WRITE schedule
    WRITE refused list with reasons
```

**Trace (dry run).** Requests: Mon 1h (slot 1, load 1), Fri 1h (refused-rule), Mon 1h (slot 1, load 2), Tue 1h (slot 2), Wed 1h (slot 3), Tue 1h (slot 2 load 2), Thu 1h (slot 4).

**Expected output.** schedule slots 1-4 used; refused: [Friday request]

**Edge cases.** All requests on one day (capacity binds); empty request list; duration over 1h (out of scope - state it); a refusal reason is required per request - 'refused' alone is not an answer.

**Complexity.** O(requests x slots). Greedy first-fit is fine here; question for fast finishers: when does first-fit waste capacity?
