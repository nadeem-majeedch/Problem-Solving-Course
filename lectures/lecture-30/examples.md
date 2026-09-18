# Worked Examples — Lecture 30

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Poster Budget: turn a wish into a formulation](#1) | cs-117 | yes |
| [2. The Shift Schedule: constraints as first-class citizens](#2) | cs-118 | yes |
| [3. The Auction Bluff: optimise what you control](#3) | cs-124 | yes |

---

## 1. The Poster Budget: turn a wish into a formulation (case cs-117)

**Problem.** Posters cost 3 each and reach 40 students; flyers cost 1 and reach 10. Budget 12. Maximise reach. Write the objective, the constraint, and the decision variables - then solve.

**Analysis.** Formulation first: variables p, f (counts); maximise 40p + 10f subject to 3p + f <= 12, p, f >= 0 integers. Solution shape: every pound on posters buys 13.3 impressions vs 10 for flyers - but integrality bites: p=4 uses the whole budget (160); p=3 leaves 3 -> 3 flyers -> 150. Exhaustive check over a tiny space settles it.

**Algorithm.**
1. name the decision variables
2. write objective and constraint formally
3. enumerate the small feasible space (p = 0..4, f = 0..12)
4. keep the best feasible reach

**Pseudocode.**

```
    best <- 0
    FOR p in 0..4
        FOR f in 0..(budget - 3*p)
            reach <- 40*p + 10*f
            best <- max(best, reach)
    WRITE best
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
best = 0
best_pf = (0, 0)
for p in range(13):
    for f in range(13):
        if 3 * p + f <= 12:
            reach = 40 * p + 10 * f
            if reach > best:
                best, best_pf = reach, (p, f)
print(best, best_pf)
# expect: 160 (4, 0)
```

**Trace (dry run).** p=4, f=0: cost 12, reach 160. p=3, f=3: cost 12, reach 150. p=0, f=12: 120. The ratio rule points to posters; the integer check confirms 4 posters exactly spend the budget. The formulation - not the enumeration - is the transferable skill.

**Expected output.** maximum reach 160 with 4 posters, 0 flyers

**Edge cases.** Budget 0 -> reach 0 (legitimate). Non-integer counts would relax to a linear program - a different problem class. Listing the constraints COMPLETELY (integrality!) is what keeps the enumeration honest.

**Complexity.** O(budget^2) enumeration here; the formulation scales to solvers when the space explodes.

## 2. The Shift Schedule: constraints as first-class citizens (case cs-118)

**Problem.** Three shifts, two staff (ada, bo), each shift needs exactly one person, nobody works two adjacent shifts, ada cannot take shift 1. Find any valid roster.

**Analysis.** This is a constraint-satisfaction problem, not an optimisation: any valid roster wins. Backtracking - try, check, undo - is the general tool. The violation order matters for speed: checking 'ada cannot take shift 1' first prunes half the tree immediately.

**Algorithm.**
1. variables: who covers shifts 1..3
2. domains: {ada, bo} minus immediate constraints
3. backtrack: assign shift by shift, reject on adjacency violation
4. first complete valid assignment is reported

**Pseudocode.**

```
    FUNCTION solve(assign)
        IF all shifts assigned RETURN assign
        s <- next shift
        FOR each person allowed on s
            IF not adjacent-conflict THEN
                result <- solve(assign + {s: person})
                IF result exists RETURN result
        RETURN failure
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
def solve():
    for s1 in ("bo",):
        for s2 in ("ada", "bo"):
            for s3 in ("ada", "bo"):
                roster = (s1, s2, s3)
                if len(set(roster)) == 3 or roster[0] == roster[1] or roster[1] == roster[2]:
                    continue
                if "ada" == roster[0]:
                    continue
                return roster
    return None

print(solve())
# expect: ('bo', 'ada', 'bo')
```

**Trace (dry run).** Shift 1: ada excluded -> bo. Shift 2: ada (bo would clash with shift 1). Shift 3: ada? clashes with shift 2 -> bo. Roster (bo, ada, bo) - valid: adjacent pairs differ, ada never on shift 1. One constraint (ada's ban) halved the search at the root.

**Expected output.** valid roster: shift 1 bo, shift 2 ada, shift 3 bo

**Edge cases.** All-bo schedule fails adjacency immediately - backtracking would undo and retry. No-solution instances must terminate with 'impossible', not loop forever. Constraint ORDER (cheapest, most-pruning first) is the craft skill; correctness does not depend on it, speed does.

**Complexity.** Exponential worst case, but pruning makes toy instances instant - the general shape behind schedulers and solvers.

## 3. The Auction Bluff: optimise what you control (case cs-124)

**Problem.** You bid for one of two identical items against one rival. Your value 100, budget cap 80. Sealed bid. What should you bid - and which part of that question is actually optimisable?

**Analysis.** You control your bid, not the rival's. With an unknown rival, no bid guarantees winning; the optimisable object is expected value under assumptions about the rival. Assume the rival bids uniformly on 0..100: bidding b wins with probability b/100, paying your bid when you win -> expected surplus (100 - b) x b/100, maximised at b = 50 - but the budget caps b at 80, which does not bind. The lesson: separate decision variables from environmental assumptions.

**Algorithm.**
1. write surplus as a function of the bid under the rival model
2. maximise over the feasible bids (0..budget)
3. state the assumption that made it calculable

**Pseudocode.**

```
    best <- 0
    FOR b in 0..80
        win_prob <- b / 100
        surplus <- (100 - b) * win_prob
        best <- max(best, surplus)
    WRITE best bid
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
best_bid, best_val = 0, -1
for b in range(81):
    val = (100 - b) * b / 100
    if val > best_val:
        best_val, best_bid = val, b
print(best_bid, best_val)
# expect: 50 25.0
```

**Trace (dry run).** Surplus b(100-b)/100 is a parabola peaking at b=50 -> expected surplus 25. Bid 80 wins 80% of the time but surplus (20)x0.8 = 16. Bid 10 wins rarely but cheaply -> 9. The cap at 80 never binds; under a cap of 30 it would - re-run the loop and watch the answer move.

**Expected output.** bid 50 (expected surplus 25 under the uniform-rival assumption)

**Edge cases.** Change the rival model -> change the answer; the model is an assumption to declare. Risk of overpaying (winner's curse) is not in this simple model - flag it as out-of-scope rather than silently ignored.

**Complexity.** O(budget) enumeration; closed-form parabola vertex exists (enrichment: calculus).
