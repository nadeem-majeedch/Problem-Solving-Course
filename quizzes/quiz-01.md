# Quiz 1 — Foundations (Lectures 01–04)

**Time: 20 minutes · Closed book · Answer all questions.**
Write pseudocode or Python as instructed; a clear method earns marks even
when the final answer is imperfect. Show assumptions.

## Q1. Decomposition (4 marks)

A campus print shop charges: first 10 pages 2 per page, pages 11–50 at 1.5
per page, pages beyond 50 at 1 per page, with a flat 5 surcharge only when
printing more than 20 pages. A student brings a 73-page document.

(a) List the subproblems you would decompose this task into. *(2)*
(b) State one assumption you must make before any code can be written. *(2)*

## Q2. Pseudocode (5 marks)

Write pseudocode that reads numbers until the value 0 appears (0 is not
data), then outputs how many numbers were read and their average. The list
may be empty apart from the terminator — say what your pseudocode outputs
in that case.

## Q3. Flowchart reasoning (4 marks)

A flowchart branch reads: *"IF temperature > 30 THEN start sprinkler;
ELSE IF temperature > 30 AND soil is dry THEN sound alarm."*

(a) Explain why the second branch can never run. *(2)*
(b) Redraw (in words) a branch structure that makes both outcomes reachable
    and sensible. *(2)*

## Q4. Trace the code (7 marks)

```python
total = 0
count = 0
for n in [4, 2, 9, 2, 7]:
    if n % 2 == 0:
        total = total + n
    else:
        count = count + 1
print(total, count)
```

(a) Fill the trace table (one row per iteration): `n`, `total`, `count`. *(4)*
(b) State the final printed output. *(1)*
(c) In one sentence: what does this program compute? *(2)*
