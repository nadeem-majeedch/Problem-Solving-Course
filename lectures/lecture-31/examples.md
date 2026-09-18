# Worked Examples — Lecture 31

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Umbrella Decision: expected value with a decision tree](#1) | cs-121 | yes |
| [2. The Game Show Switch: conditional probability decides](#2) | cs-122 | yes |
| [3. The Insurance Riddle: why a bad bet is still rational](#3) | cs-123 | yes |

---

## 1. The Umbrella Decision: expected value with a decision tree (case cs-121)

**Problem.** Carry an umbrella (mild inconvenience, cost 2) or not. Rain ruins the day (cost 10). Forecast says 30% rain. What does expected cost say, and when does it flip?

**Analysis.** EV(carry) = 2. EV(leave) = 0.3 x 10 = 3. Carry wins at 30%. The flip point: p x 10 > 2 -> p > 20%. Decision trees make the two branches explicit; sensitivity (the flip point) is the real answer - a decision that holds across p in 0..20% and 20..100% is more robust than any single number.

**Algorithm.**
1. list acts (carry, leave) and outcomes (rain, dry)
2. multiply outcomes by probabilities, sum per act
3. pick the act with lower expected cost
4. compute the probability where the ranking flips

**Pseudocode.**

```
    EV_carry <- 2
    EV_leave <- p * 10
    IF EV_carry <= EV_leave THEN carry ELSE leave
    flip <- 2 / 10
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
p = 0.3
ev_carry = 2
ev_leave = p * 10
flip = 2 / 10
print(ev_carry < ev_leave, flip)
# expect: True 0.2
```

**Trace (dry run).** At p=30%: carry costs 2, leaving costs 3 -> carry. Below 20% rain, leaving wins. The single-number answer (carry) hides the structure; the flip point (20%) is what a decision-maker actually uses - forecasts move daily, thresholds do not.

**Expected output.** carry the umbrella (EV 2 vs 3); ranking flips below 20% rain chance

**Edge cases.** Costs are utilities, not money - the model assumes they are commensurable. Risk aversion: EV says carry at 21%, but a person may still leave - EV is one decision rule, not a law. Repeated decisions (every day) change the calculus - an ownership argument.

**Complexity.** O(1) per decision; the tree's value is in forcing outcomes OUT of the prose.

## 2. The Game Show Switch: conditional probability decides (case cs-122)

**Problem.** Three doors, one prize. You pick door 1; the host opens door 3 (empty). Should you switch to door 2?

**Analysis.** P(win | switch) = 2/3, P(win | stay) = 1/3. The host's action is information: he always opens an empty door, so his choice is constrained exactly when your first pick was wrong (probability 2/3). Enumerate the 3 equally likely prize positions and count - the enumeration kills the intuition argument.

**Algorithm.**
1. enumerate prize behind doors 1..3 (equally likely)
2. in each case simulate the host's forced behaviour
3. tally wins for stay vs switch

**Pseudocode.**

```
    FOR prize in 1..3
        IF prize = 1 THEN stay wins
        ELSE switch wins
    (host always opens a non-prize, non-picked door)
    WRITE tally
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
stay_wins = switch_wins = 0
for prize in (1, 2, 3):
    if prize == 1:
        stay_wins += 1
    else:
        switch_wins += 1
print(stay_wins, switch_wins)
# expect: 1 2
```

**Trace (dry run).** Prize 1: stay wins. Prize 2: host must open 3 -> switching to 2 wins. Prize 3: host must open 2 -> switching wins. Switch wins 2 of 3 equally likely cases. A 10,000-door version (host opens 9998) makes the 2/3 visceral: your door stays 1/1000, the remaining door absorbs all the rest.

**Expected output.** switch: wins 2/3 vs staying 1/3

**Edge cases.** If the host opens a random door that HAPPENS to be empty, switching gains nothing (50/50) - the answer depends on the host's protocol, an assumption to state. The simulation version needs the protocol encoded exactly; sloppy encodings 'prove' both answers, a memorable failure mode.

**Complexity.** O(1) enumeration; the simulation version is O(trials) and validates the tally.

## 3. The Insurance Riddle: why a bad bet is still rational (case cs-123)

**Problem.** Insurance costs 50; the insured event (probability 1%) costs 4000. EV says decline (-50 vs -40 expected loss). Why do rational people buy, and what decision rule are they using?

**Analysis.** EV(buy) = -50. EV(skip) = 0.01 x (-4000) = -40. Insurance is a negative-EV bet - and still sensible, because a 1% chance of a 4000 loss is ruinous for an individual. The implicit rule is not expected value on money but on utility: avoid catastrophic states. Name the rule you are using; EV is the default, not the law.

**Algorithm.**
1. compute EV of each option
2. note the conflict with intuition
3. introduce utility: the 4000 state is disproportionately bad
4. conclusion: rule choice must be stated, not smuggled

**Pseudocode.**

```
    ev_buy <- -50
    ev_skip <- 0.01 * -4000
    WRITE both, note ev_buy < ev_skip
    (utility view: ruin avoidance may override EV)
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
ev_buy = -50
ev_skip = 0.01 * -4000
print(ev_buy, ev_skip, ev_buy < ev_skip)
# expect: -50 -40.0 True
```

**Trace (dry run).** Buying costs 10 more in expectation - the insurer's margin. The 1% event still ruins a student budget; 50 is a survivable certainty. Same arithmetic, different decision rules: EV for repeatable small-stakes choices, ruin-avoidance for catastrophic ones. Declaring which rule you use IS the decision discipline.

**Expected output.** EV(buy) -50 vs EV(skip) -40: insurance loses on EV, wins on ruin-avoidance

**Edge cases.** At 60% probability the EV rule flips to buy - rule and parameters interact. Pooling risk (many people) is why insurers can sell negative-EV-to-you contracts profitably. Never let 'EV says no' end a discussion about catastrophic stakes - that is the lecture's boundary marker.

**Complexity.** O(1); the hard part is admitting which rule you chose.
