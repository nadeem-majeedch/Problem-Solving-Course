# Quiz 2 — Answer Key (instructor only)

Not for publication.

## Q1. Remainders (4)

(a) *(2)* 41 mod 7 = 6 → day 6 of the cycle → **Sunday** (day 0 Monday).
*Accept the named day only if the modulo is shown or clearly implied.*

(b) *(2)* Last day is day 140. 140 mod 7 = 0 → **Monday**. *Watch for the
off-by-one: "starts day 41 and lasts 100 days" ends on day 140 inclusive
(days 41…140 is 100 days). Award 1 mark for 139 with the interpretation
"100 days after the start" if stated — the boundary is the point being
tested, so a stated interpretation with correct arithmetic earns both marks
for the stated reading.*

## Q2. Predict the output (5)

Trace: 5 → 16 → 8 → 4 → 2 → 1. Output: **1** (2 marks for output, 3 for a
correct trace or equivalent one-line explanation: even halves, odd maps to
3n+1, loop ends when x reaches 1). *No trace/explanation: cap at 2.*

## Q3. Debugging (5)

(a) *(2)* Examples: `[2, 2]` or a single-element list like `[7]`, chosen so
the wrong output (larger than every element) still appears. Minimal = fewest
elements that still show the defect; if a one-element list reproduces it,
that is the minimal case.

(b) *(2)* Ordered hypotheses, e.g.: (1) the divisor is wrong — dividing by
`len(list) - 1` or by 0-handling inflates the result; (2) the sum is
accumulated twice inside a loop. Any two plausible, testable hypotheses
count; they must be *competing* (mutually distinguishable).

(c) *(1)* E.g. printing `len(scores)` and `total` once at the boundary — the
observed values eliminate one hypothesis. Any single discriminating
observation.

## Q4. Test design (6)

(a) *(1 per row, 4 needed)*

| years | expected | reason |
| --- | --- | --- |
| 0 | 0 | smallest valid input |
| 4 | 0 | just below the boundary |
| 5 | 100 | the boundary itself |
| 6 | 100 | just above the boundary |

*Also accept 1 as smallest-below-boundary alternative; the four rows must
bracket the boundary and include the smallest valid input.*

(b) *(2)* One passing test (e.g. `bonus(10)`) only shows one input behaves;
the boundary (5 vs 4) is where this requirement actually fails, and testing
from the code rather than the requirement proves nothing.

Grade boundaries suggestion: 17–20 excellent · 12–16 good · 8–11 satisfactory.
