# Worked Examples — Lecture 08

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The triangle classifier: building the test table](#1) | cs-029 | no |
| [2. Black box vs white box on the fee function](#2) | cs-031 | no |

---

## 1. The triangle classifier: building the test table (case cs-029)

**Problem.** Classify triangles: scalene, isosceles, equilateral, impossible (degenerate), invalid. Design the test table before the classifier.

**Analysis.** The classes partition all inputs, so the table needs one row per class plus the boundaries: a degenerate triangle (1 + 2 = 3) sits exactly on the impossible boundary, and zero or negative sides are invalid before geometry starts. Test order matters: invalid first, then impossible, then the shape classes.

**Algorithm.**
1. list the output classes
2. choose one representative input per class
3. add boundary inputs (degenerate sums, zero sides)
4. order the checks: invalid, impossible, equilateral, isosceles, scalene

**Pseudocode.**


    IF MIN(a, b, c) <= 0 THEN "invalid"
    ELSE IF a+b <= c OR a+c <= b OR b+c <= a THEN "impossible"
    ELSE IF a = b AND b = c THEN "equilateral"
    ELSE IF a = b OR b = c OR a = c THEN "isosceles"
    ELSE "scalene"


**Trace (dry run).** (3, 4, 5) scalene. (5, 5, 5) equilateral. (2, 2, 3) isosceles. (1, 2, 3) impossible (1 + 2 = 3, degenerate). (1, 1, 10) impossible. (0, 4, 4) invalid. Six rows cover every class and boundary.

**Expected output.** six verdict lines matching the reference

**Edge cases.** The degenerate case (1, 2, 3) is the boundary that catches <= vs < in the impossibility test. Equilateral is also isosceles under the loose definition - the spec must say which way the class goes; ours says equilateral wins.

**Complexity.** O(1) per input; the intellectual work is the table, not the branches.

## 2. Black box vs white box on the fee function (case cs-031)

**Problem.** fee(x): 0 below 3, 2 up to 5, 5 above. A buggy version charges 0 at exactly x = 3. Which suite finds it - black box or white box?

**Analysis.** Black-box suites sample typical values and often miss exact boundaries. White-box testing reads the branch structure: the buggy condition is x <= 3, so x = 3 itself is the discriminating input. Band boundaries (3, 5, and just beyond) are the cheapest strong inputs.

**Algorithm.**
1. black box: pick typical values (-1, 9) - they agree, defect hidden
2. white box: read the branches; target each boundary
3. suite: 3, 3.01, 5, 5.01
4. compare buggy and correct on each input

**Pseudocode.**


    correct: IF x < 3 -> 0; ELSE IF x <= 5 -> 2; ELSE 5
    buggy:   IF x <= 3 -> 0; ELSE IF x <= 5 -> 2; ELSE 5
    -- they disagree exactly when x = 3


**Trace (dry run).** x = -1: 0 vs 0, agree. x = 3: 2 vs 0 - disagree, the boundary found. x = 5: 2 vs 2. x = 5.01: 5 vs 5. Only the white-box-chosen boundary 3 separates the implementations.

**Expected output.** rows ending with a disagreement exactly at x = 3

**Edge cases.** Negative x and non-integers are legitimate inputs unless the spec forbids them - another reason the spec's domain statement matters. Equivalence-class sampling is efficient but blind at boundaries; combine both styles.

**Complexity.** Suite size stays small (4-8 rows) because white-box targeting hits the seams instead of sampling blindly.

---

**Python companion.** The triangle classifier under today's test table - every row's expectation is asserted by the output:

```python
def classify(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return "invalid"
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"

print(classify(3, 4, 5), classify(5, 5, 5), classify(4, 4, 7), classify(1, 2, 8))
# expect: scalene equilateral isosceles invalid
```
