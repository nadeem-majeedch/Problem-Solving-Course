# Worked Examples — Lecture 02

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. Largest of three, at three precision levels](#1) | cs-005 | no |
| [2. Password rules: order of tests](#2) | cs-006 | no |
| [3. The vending machine as a state machine](#3) | cs-007 | no |
| [4. Shuffle with a no-adjacent-artist rule](#4) | cs-008 | no |

---

## 1. Largest of three, at three precision levels (case cs-005)

**Problem.** Read three numbers; output the largest. Make the pseudocode precise enough that a classmate translates it without questions.

**Analysis.** Level 1 (vague): 'compare them and output the biggest' - not executable. Level 2 (precise): carry the winner of the first pair into a comparison with the third. Level 3 (testable): ties resolved - on equal values, keep the first; the trace proves it.

**Algorithm.**
1. read a, b, c
2. best <- a
3. if b > best then best <- b
4. if c > best then best <- c
5. write best

**Pseudocode.**

```
    READ a, b, c
    best <- a
    IF b > best THEN best <- b
    IF c > best THEN best <- c
    WRITE best
```

**Trace (dry run).** (12, 7, 9): best = 12; 7 > 12? no; 9 > 12? no. Output 12. (7, 7, 3): best = 7; 7 > 7? no (strict compare keeps first); output 7.

**Expected output.** 12  (and 7 for the tie case)

**Edge cases.** All equal; negatives only (-3, -9, -1 → -1); two equal maxima; inputs that are not numbers (validation, next case). The 2-compare chain generalises to n numbers with n-1 compares - the argmax pattern of lecture 9.

**Complexity.** n - 1 comparisons for n numbers; can 2 compares ever suffice for 3 numbers? (No - a pigeonhole argument students can find themselves.)

## 2. Password rules: order of tests (case cs-006)

**Problem.** Password valid when: 8-12 characters, at least one digit, starts with a letter. Output exactly one message naming the FIRST failing rule.

**Analysis.** The spec's 'first failing rule' forces a test order. We choose length → starts-with-letter → contains-digit; any order is legal if stated, but swapping two silently is a defect. Early exit: stop at the first failure.

**Algorithm.**
1. check length 8-12; if short/long, report and stop
2. check first char is a letter; report and stop if not
3. scan for any digit; report pass only if found

**Pseudocode.**

```
    READ p
    IF length(p) < 8 OR length(p) > 12 THEN WRITE "too short or long"
    ELSE IF NOT letter(first(p)) THEN WRITE "must start with a letter"
    ELSE IF no digit in p THEN WRITE "must contain a digit"
    ELSE WRITE "pass"
```

**Trace (dry run).** "klass7a!" fails length (7) → message 1. "Password1" passes all → pass. "1secure9" fails rule 2 → message 2. "abcdefgh" passes 1-2, fails 3 → message 3.

**Expected output.** four different messages for the four traces

**Edge cases.** Exactly 8 and exactly 12 chars (boundaries); 13 chars (just outside); a 12-char password with the digit last; empty string (fails rule 1 without indexing errors - order matters for safety too: never test first(p) before length).

**Complexity.** O(length) for the digit scan; the rest constant.

## 3. The vending machine as a state machine (case cs-007)

**Problem.** Pseudocode for buying a snack: insert coins until credit >= price, then vend and give change; refuse when sold out (before accepting money).

**Analysis.** State: credit (starts 0), stock. Events: insert coin, request vend. The lesson: check stock BEFORE the coin loop; the loop's invariant is 'credit < price and machine still waiting' at the top of every pass.

**Algorithm.**
1. if stock = 0: return coins, refuse
2. credit <- 0
3. while credit < price: read coin, credit += coin
4. vend; change <- credit - price; stock -= 1

**Pseudocode.**

```
    IF stock = 0 THEN WRITE "sold out, coins returned"; STOP
    credit <- 0
    WHILE credit < price
        READ coin
        credit <- credit + coin
    WRITE "vend", change = credit - price
    stock <- stock - 1
```

**Trace (dry run).** price 1.80, coins 1.00, 1.00: credit 0 → 1.00 (loop again) → 2.00 (exit). Vend, change 0.20, stock 3 → 2.

**Expected output.** vend, change 0.20, stock 2  |  sold out, coins returned (stock 0 case)

**Edge cases.** Exact payment (change 0); sold out before first coin; refund-request mid-loop (extension); a coin larger than the price in one step; infinite loop if coins are never inserted - the WHILE condition names the exit.

**Complexity.** O(coins inserted). The real content is the state table: credit and stock per event.

## 4. Shuffle with a no-adjacent-artist rule (case cs-008)

**Problem.** Playlist A(pop), B(pop), C(jazz), D(pop), E(jazz). Order all songs once so no two same-artist songs are adjacent; state the repair rule when impossible.

**Analysis.** Greedy: lay songs out round-robin by artist (pop, jazz, pop, jazz, pop) so identical artists spread. Feasibility fact worth stating: possible iff the largest artist group ≤ ceil(n/2); the repair rule for over-majority is 'reinsert into the largest gaps'.

**Algorithm.**
1. group songs by artist
2. interleave groups round-robin, largest first
3. if two same-artist end up adjacent, reinsert one into an earlier gap
4. if largest group > ceil(n/2), report impossible

**Pseudocode.**

```
    GROUP songs by artist, largest group first
    result <- empty
    WHILE any group non-empty
        FOR each group (in round-robin order)
            IF group non-empty THEN append one song to result
    CHECK adjacency; repair or report impossible
```

**Trace (dry run).** Groups: pop {A, B, D}, jazz {C, E}. Round-robin: A, C, B, E, D. Adjacency check: no same-artist pair. Done.

**Expected output.** A, C, B, E, D

**Edge cases.** All same artist (impossible - report, do not loop forever); exactly half/half; random order instead of round-robin (why random alone fails: B and D can land adjacent). Randomness needs the repair pass - a lesson cs-032 formalises.

**Complexity.** O(n) passes for the interleave; the feasibility bound is the intellectual content.

---

**Python companion.** Optional preview - the champion pattern from today's pseudocode, executable:

```python
a, b, c = 7, 12, 9
best = a
if b > best:
    best = b
if c > best:
    best = c
print(best)
# expect: 12
```
