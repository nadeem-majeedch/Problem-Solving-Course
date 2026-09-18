# Quiz 3 — Answer Key (instructor only)

Not for publication.

## Q1. Aggregation (5)

(a) *(1 per accumulator, up to 2)* For waits `W`: `longest ← W[0]` (or a
sentinel like −1 if the empty case is discussed), `total ← 0`, `over10 ← 0`.
*Accept `longest ← 0` only if the student notes the empty-input caveat —
the point of the question is deliberate initialisation.*

(b) *(3)* Model (Python shown; pseudocode equally acceptable):

```python
longest = waits[0]
total = 0
over10 = 0
for w in waits:
    if w > longest:
        longest = w
    total = total + w
    if w > 10:
        over10 = over10 + 1
print(longest, total / len(waits), over10)
```

Award: single pass with all updates inside (2), correct comparisons (1).
*Two-pass solutions (separate loops) lose 1: the question demands one pass.*

## Q2. The zero bug (4)

Input: any list where the true shortest is longer than 0 characters,
e.g. `["hi", "hello"]` → returns `""` (1 mark for input, 1 for the wrong
answer shown). Mechanism (1): `len("") = 0` beats every real word, so the
comparison never fires. Fix (1): initialise from the data,
`shortest = words[0]` (with an empty-list guard), not from a constant.

## Q3. String reasoning (5)

(a) *(3)* Model:

```python
if len(sid) != 8:
    verdict = "length"
elif not sid[0].isalpha():
    verdict = "first character"
elif not sid[-1].isdigit():
    verdict = "last character"
else:
    verdict = "valid"
```

Award: all three rules (2), distinct verdict per failed rule (1).

(b) *(2)* Length boundaries: 7 characters (just short) and 9 characters
(just long); 8 itself is the valid boundary value. Any two of {7, 8, 9}.

## Q4. Trace (6)

(a) *(1 each)* `""` → `"a"` → `"ab"` → `"abc"` (unchanged at the 4th
iteration since `a` is already in `seen`) → final `"abc"`.

(b) *(1)* Output: `abc 1`

(c) *(1)* The number of characters dropped as duplicates (count of
characters that were already seen).

Grade boundaries suggestion: 16–20 excellent · 11–15 good · 7–10 satisfactory.
