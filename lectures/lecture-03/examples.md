# Worked Examples — Lecture 03

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. Rain or shine: decisions to diamonds](#1) | cs-010 | no |
| [2. The ATM loop, arrows and all](#2) | cs-009 | no |
| [3. Dispatch loop: proving termination](#3) | cs-011 | no |
| [4. Guess and check as a loop](#4) | cs-012 | no |

---

## 1. Rain or shine: decisions to diamonds (case cs-010)

**Problem.** Picnic decision: go if temperature is 18-28 and no rain; if rain but warm, go with a tent; otherwise cancel. Flowchart it, then trace three days.

**Analysis.** Extract decisions first: 'is t in [18, 28]?' (two comparisons), 'is it raining?' (one diamond). Structure the two diamonds so both exits are used - a common draft leaves the 'warm and raining' path dead.

**Algorithm.**
1. diamond 1: warm? (18 <= t <= 28)
2. diamond 2 (if warm): raining?
3. rain → tent; dry → go; cold → cancel

**Pseudocode.**

```
    READ t, raining
    IF 18 <= t <= 28 THEN
        IF raining THEN WRITE "go with tent"
        ELSE WRITE "go"
    ELSE WRITE "cancel"
```

**Trace (dry run).** (24, dry) → go. (24, rain) → tent. (15, dry) → cancel. Each trace follows named arrows.

**Expected output.** go / go with tent / cancel

**Edge cases.** t = 18 and t = 28 exactly (both 'warm' - boundary convention stated); t = 28.5 (cancel - even though 'nearly warm'); the dead-branch draft where rain is checked before warmth.

**Complexity.** Constant; the lesson is diamond wiring, not cost.

## 2. The ATM loop, arrows and all (case cs-009)

**Problem.** Cash machine: allow withdrawals while the balance lasts and at most 3 per session; refuse amounts over balance without ending the session.

**Analysis.** Two loop conditions (balance sufficient, count < 3) combine into one WHILE with AND - and the flowchart shows why: the loop-back arrow must carry both checks. Termination: session count strictly increases to 3.

**Algorithm.**
1. count <- 0
2. while count < 3: read amount; if amount <= balance: pay, count += 1; else refuse (no count change)
3. print balance and session end

**Pseudocode.**

```
    count <- 0
    WHILE count < 3
        READ amount
        IF amount <= balance THEN
            balance <- balance - amount
            count <- count + 1
        ELSE WRITE "refused"
    WRITE balance
```

**Trace (dry run).** balance 100, requests 40, 90, 30: 40 ok (count 1), 90 refused, 30 ok (count 2). Loop ends by count, balance 30.

**Expected output.** refused / balance 30

**Edge cases.** Refusals must not consume the count (a classic draft bug); exact balance withdrawal to 0; three refused requests in a row - loop still ends (count never moves; termination is by count, not by success).

**Complexity.** O(requests). The flowchart question: draw where the 'refused' arrow re-enters.

## 3. Dispatch loop: proving termination (case cs-011)

**Problem.** A dispatch system processes queued jobs; every processed job may enqueue 0-2 smaller sub-jobs. Flowchart the loop and argue it terminates.

**Analysis.** Loop: while queue non-empty, take one job, process it, enqueue its sub-jobs. Naive reading suggests it may never end; the resolution: each sub-job is strictly smaller (bounded size), so total work is finite. In the flowchart the argument is concrete: the 'queue length' counter can rise, but the 'remaining size budget' strictly falls.

**Algorithm.**
1. while queue non-empty and size budget > 0
2. take job; process; enqueue sub-jobs with smaller sizes
3. decrease budget by the job's size

**Pseudocode.**

```
    WHILE queue not empty
        job <- take first
        PROCESS job
        FOR each sub in subjobs(job)
            IF size(sub) < size(job) THEN enqueue sub
        budget <- budget - size(job)
    WRITE "all dispatched"
```

**Trace (dry run).** Queue [J1(4)]: process J1, enqueue J1a(2), J1b(1). Process J1a (no subs), then J1b. Queue drains; budget 4 → 2 → 0.

**Expected output.** all dispatched

**Edge cases.** A job with no sub-jobs (leaf); a sub-job equal in size (refused by the guard - otherwise infinite); empty initial queue (loop never runs). The termination argument is the deliverable.

**Complexity.** O(total size). This is the first occurrence of 'the loop ends because something provably shrinks'.

## 4. Guess and check as a loop (case cs-012)

**Problem.** Number game: the program holds a secret 1-50; the player guesses; feedback 'higher'/'lower'/'correct'. Flowchart the game loop including a maximum of 7 guesses.

**Analysis.** Loop with three exits (win, out of guesses, continue). The flowchart forces clarity: which diamond owns each exit. The strategy discussion (halving) is deliberately saved for lecture 21; today the loop structure is the point.

**Algorithm.**
1. tries <- 0
2. while tries < 7 and not correct: read guess; compare; give feedback; tries += 1
3. win or lose message

**Pseudocode.**

```
    tries <- 0
    WHILE tries < 7
        READ guess
        IF guess = secret THEN WRITE "correct"; STOP
        ELSE IF guess < secret THEN WRITE "higher"
        ELSE WRITE "lower"
        tries <- tries + 1
    WRITE "out of guesses"
```

**Trace (dry run).** secret 23, guesses 10 (higher), 40 (lower), 23 (correct) on try 3 - loop exits early via the STOP arrow.

**Expected output.** higher / lower / correct

**Edge cases.** Guess outside 1-50 (invalid - re-ask or count it? state the rule); exactly 7 wrong guesses; first guess correct (loop body runs once). The 7-guess guarantee is log2(50) - a teaser for lecture 21.

**Complexity.** At most 7 feedback rounds by the rules; a halving strategy needs ceil(log2(50)) = 6.

---

**Python companion.** Optional preview - today's rain-or-shine diamond logic as decisions:

```python
rain = True
tent = False
if rain:
    if tent:
        print("go with tent")
    else:
        print("cancel")
else:
    print("go")
# expect: cancel
```
