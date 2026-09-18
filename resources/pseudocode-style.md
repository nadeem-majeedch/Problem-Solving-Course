# Pseudocode Style Sheet

One consistent pseudocode is used in every lecture, solution, and rubric, so
that what you write matches what you read. It is deliberately close to Python
so translating later is mechanical — but it is **language-free**: no syntax
marks beyond structure.

## Keywords

```
SET x TO value          assignment
READ x                  input
OUTPUT x                output (print / return-to-user)
IF condition THEN ... ELSE IF ... ELSE ... END IF
REPEAT ... UNTIL condition          do-while
WHILE condition DO ... END WHILE
FOR EACH item IN collection DO ... END FOR
FOR i FROM a TO b DO ... END FOR     inclusive both ends
FUNCTION name(params) ... RETURN value END FUNCTION
```

## Conventions

1. **One statement per line.** Indentation shows nesting (4 spaces or a tab);
   closing keywords (`END IF`, `END WHILE`) may be omitted in hand-drawn
   flowchart work but are required in written answers.
2. **Names are descriptive**: `total`, `attempt_count`, not `t`, `x2`.
3. **Conditions are plain Boolean sentences**: `IF age >= 18 AND has_id THEN`.
4. **Arrays/sequences are 1-indexed in pseudocode** (`item[1]` is the first),
   and we say so when translating to Python (0-indexed). Off-by-one insight
   is part of Lecture 06.
5. **No language tricks.** No list comprehensions, no `+=`, no ternaries. Say
   what you mean in plain steps.
6. **Comments** start with `//`.

## Worked example

Task: read numbers until a sentinel 0, output the maximum.

```
FUNCTION find_maximum()
    SET maximum TO 0            // assumes at least one positive number
    SET done TO FALSE
    WHILE done = FALSE DO
        READ value
        IF value = 0 THEN
            SET done TO TRUE
        ELSE IF value > maximum THEN
            SET maximum TO value
        END IF
    END WHILE
    OUTPUT maximum
END FUNCTION
```

## Relation to flowcharts

| Pseudocode construct | Flowchart shape |
| --- | --- |
| START / END | rounded box |
| SET, OUTPUT | rectangle / parallelogram |
| IF, WHILE | diamond with two exits |
| FOR EACH | rectangle (counter) + diamond (more?) |
| arrows between steps | arrows |

## Relation to Python

| Pseudocode | Python |
| --- | --- |
| `SET x TO 3` | `x = 3` |
| `READ x` | `x = int(input())` |
| `OUTPUT x` | `print(x)` |
| `FOR i FROM 1 TO n` | `for i in range(1, n + 1):` |
| `FOR EACH item IN items` | `for item in items:` |
| `item[1]` (first) | `item[0]` |

## Grading notes

Assignment 1 and Quiz 2 grade pseudocode with this rubric: **completeness**
(all cases handled), **precision** (a different reader could implement it),
**structure** (loops/conditionals chosen well), **style** (conventions above).
A correct algorithm in wrong style loses the style point only — reasoning
first, formatting second.
