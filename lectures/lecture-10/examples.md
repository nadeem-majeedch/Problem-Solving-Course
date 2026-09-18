# Worked Examples — Lecture 10

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. Username auditor: classifier with one character of memory](#1) | cs-037 | no |
| [2. The reversal family: three problems, one idea](#2) | cs-038 | no |
| [3. Template mail-merge: parse, fill, report](#3) | cs-039 | no |
| [4. The anagram detector: the normalisation ladder](#4) | cs-040 | no |

---

## 1. Username auditor: classifier with one character of memory (case cs-037)

**Problem.** Usernames valid when: 5-16 chars, letters/digits/underscores only, not starting with a digit, no two consecutive underscores. Audit the batch.

**Analysis.** Rules run in order (length → charset → first-char → adjacency) with early exit. Adjacency needs one variable of history: prev. If current and prev are both '_', fail.

**Algorithm.**
1. check length 5-16
2. scan chars: class? first-char? prev/cur both '_'?
3. fail names the first broken rule

**Pseudocode.**

```
    IF length < 5 OR length > 16 THEN fail "length"
    prev <- none
    FOR i, ch IN username
        IF ch not allowed THEN fail "charset"
        IF i = 0 AND ch is digit THEN fail "first char"
        IF ch = "_" AND prev = "_" THEN fail "double underscore"
        prev <- ch
    pass
```

**Trace (dry run).** ada_2019 → pass. ada__love → fail (positions 3-4 both '_'). 9lives → fail (first char digit). ok → fail (short).

**Expected output.** pass | fail: consecutive underscores | fail: starts with letter check | fail: too short

**Edge cases.** Exactly 5 and exactly 16 chars; '_' at the very end (prev survives - fine); empty string (fails length before indexing); unicode letters (name the alphabet).

**Complexity.** O(length) with early exits; the design content is the rule ORDER.

## 2. The reversal family: three problems, one idea (case cs-038)

**Problem.** Reverse 'stressed' → 'desserts'; reverse words of 'the quick brown fox'; decide whether 'Never odd or even' is a palindrome.

**Analysis.** Three positional questions, three slices: s[::-1]; split → reverse → join; palindrome = normalise then compare with reversal. The reference prints exactly these.

**Algorithm.**
1. reverse chars: s[::-1]
2. reverse words: join(reversed(split(s)))
3. palindrome: norm = lowercase letters only; norm == norm[::-1]

**Pseudocode.**

```
    WRITE reverse(s)
    WRITE join(reverse(split(s, " ")), " ")
    norm <- lowercase(letters-only(s))
    WRITE (norm = reverse(norm))
```

**Trace (dry run).** 'stressed' → 'desserts'. Words → fox brown quick the. 'neveroddoreven' is symmetric → True; 'hello' → False.

**Expected output.** desserts | fox brown quick the | True False

**Edge cases.** Empty string (palindrome True - define it); punctuation (the ladder strips it); multiple spaces (split handles); case (rung one).

**Complexity.** O(n) per operation; lecture 19 replaces slicing with two pointers for the palindrome.

## 3. Template mail-merge: parse, fill, report (case cs-039)

**Problem.** Template 'Dear {name}, your {item} is due {deadline}.' When 'item' is missing, print '[item]' visibly rather than crashing.

**Analysis.** Scan for '{', read the key to '}', look it up; absent keys substitute visibly - a *reporting* decision, stated. The reference shows both behaviours.

**Algorithm.**
1. scan for '{'
2. read key until '}'
3. present → value; absent → '[key]'
4. continue after '}'

**Pseudocode.**

```
    result <- ""
    WHILE template not consumed
        IF next char is "{" THEN
            key <- text until "}"
            result +:= record.get(key, "[" + key + "]")
        ELSE result +:= next char
    WRITE result
```

**Trace (dry run).** name=Ada, item missing, deadline=Friday → 'Dear Ada, your [item] is due Friday.'

**Expected output.** Dear Ada, your [item] is due Friday. | Dear Bo, your book is due Monday.

**Edge cases.** Unclosed '{' (treat literally - state it); empty key; values containing '{' (out of scope - say so); visible-missing vs crash is a design debate.

**Complexity.** O(template + record); accumulate-then-join, not repeated concatenation.

## 4. The anagram detector: the normalisation ladder (case cs-040)

**Problem.** 'Dormitory' / 'dirty room!'; 'astronomer' / 'moon starer'; 'hello' / 'world'. Reference: True, True, False.

**Analysis.** Ladder: lowercase → keep letters only → sort characters → compare. Two strings are anagrams exactly when their normal forms are equal.

**Algorithm.**
1. norm(s) = sorted(lowercase letters of s)
2. anagram iff norm(a) = norm(b)

**Pseudocode.**

```
    FUNCTION norm(s)
        t <- ""
        FOR ch IN s
            IF ch is letter THEN t +:= lowercase(ch)
        RETURN sort(t)
    WRITE norm(a) = norm(b)
```

**Trace (dry run).** dormitory ↔ dirtyroom! same multiset → True. hello vs world → False.

**Expected output.** True | True | False

**Edge cases.** Empty vs empty (True - define it); length mismatch (fast reject); the O(n) counting version waits for lecture 13's dictionaries.

**Complexity.** O(n log n) via sorting; counting is O(n) - both honest, the ladder is the transferable part.

---

**Python companion.** The username rule (starts with a letter, ends with a digit) with one character of memory:

```python
for name in ("ab1", "abc"):
    print(name, name[0].isalpha() and name[-1].isdigit())
# expect: ab1 True
# expect: abc False
```
