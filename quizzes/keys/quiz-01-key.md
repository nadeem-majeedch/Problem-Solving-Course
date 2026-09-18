# Quiz 1 — Answer Key (instructor only)

Not for publication. Marking notes in *italics*.

## Q1. Decomposition (4)

(a) Expected subproblems *(any four, 2 marks; award generously for sensible
splits — the exact names do not matter)*:

1. Compute the cost of pages 1–10 at rate 2.
2. Compute the cost of pages 11–50 at rate 1.5.
3. Compute the cost of pages beyond 50 at rate 1.
4. Decide whether the 20-page surcharge applies.
5. Sum the parts; report the total.

(b) Valid assumptions *(2 marks; accept any clearly stated one)*: tiers are
cumulative not alternative; the surcharge is flat (not per page); prices are
per single-sided page; a 0-page document costs 0.

*Common error:* treating tiers as exclusive ("first 10 pages only applies if
total ≤ 10"). The worked arithmetic: 10×2 + 40×1.5 + 23×1 + 5 = 20 + 60 + 23
+ 5 = 108.

## Q2. Pseudocode (5)

Model answer:

```
count TO 0; total TO 0
READ x
WHILE x ≠ 0 DO
    count TO count + 1
    total TO total + x
    READ x
END WHILE
IF count = 0 THEN
    OUTPUT "no numbers"
ELSE
    OUTPUT count, total / count
END IF
```

Marks: sentinel loop correct (2); count and total updated inside the loop,
not after (1); empty-list case handled explicitly (1); output statement
present and correct type (1). *Deduct 1 if the first READ is missing — the
loop then never sees the first value.*

## Q3. Flowchart (4)

(a) *(2)* If `temperature > 30` is false, the first condition fails and the
second condition — which requires the same `temperature > 30` — must also be
false. So the ELSE-IF branch is unreachable.

(b) *(2)* Any sensible restructuring, e.g.: "IF temperature > 30 THEN start
sprinkler; ELSE IF soil is dry THEN sound alarm." Also acceptable: split on
soil moisture first. Award marks for both outcomes being reachable and the
logic stated precisely.

## Q4. Trace (7)

(a) *(1 per correct row)*

| n | total | count |
| --- | --- | --- |
| 4 | 4 | 0 |
| 2 | 6 | 0 |
| 9 | 6 | 1 |
| 2 | 8 | 1 |
| 7 | 8 | 2 |

(b) *(1)* Output: `8 2`

(c) *(2)* It sums the even numbers and counts the odd numbers in the list.
*Accept equivalent phrasings; the key insight is the two accumulators track
different subsets.*

Grade boundaries suggestion: 17–20 excellent · 12–16 good · 8–11 satisfactory
· below 8 revisit lectures 01–04.
