# Teaching Notes — Lecture 10

*Instructor only - not rendered on the public site.*

## Board plan

- Left: string as an indexed sequence - boxes with positions and negatives drawn.
- Middle: the username classifier's state: 'last character' memory, nothing else.
- Right: normalisation ladder: trim -> case -> punctuation -> compare.

## Questions to ask students

- How much memory does the classifier need to test 'ends with digit'?
- Which two normalisation steps commute, and which do not?
- What does slicing s[1:-1] mean for a two-character string?

## Alternative explanations

- Regex-free policy: every task solvable with loops and slices this week.
- Students with regex exposure: let them show it AFTER the loop version, as comparison.

## Expected student difficulties

- Immutability surprise: s[0] = 'X' fails - show the rebuild pattern.
- Case-sensitivity bugs in comparisons - mandate the normalisation step explicitly.

## Connections to neighbouring lectures

Strings are lists wearing costumes; next lecture: real lists, real mutation (L11).

## Quiz answer key

**A1.** What is s[-1] in Python?
- *Expected:* The last character.

**A2.** Why can't you assign s[0] = 'X'?
- *Expected:* Strings are immutable - build a new string instead.

**A3.** Name the normalisation steps before comparing user text.
- *Expected:* Trim, lowercase, strip punctuation (and collapse spaces).

**A4.** How much memory does an 'ends with digit' check need?
- *Expected:* O(1) - only the last character.

**B1.** Classify 'ab1', 'abc', 'a1c' under: must start with a letter, must end with a digit.
- *What earns marks:* 'ab1' valid; 'abc' fails last-char; 'a1c' fails last-char (ends with c).

**B2.** Fill the template 'Dear {name}, your {item} is ready.' for name=Bo, item=parcel - what does the code split on?
- *What earns marks:* Split on '{' and '}' pairs; replace each placeholder with its value -> 'Dear Bo, your parcel is ready.'

## Exit ticket - expected answers

1. Why normalise before comparing strings?
   - *Expected:* so equal-meaning strings compare equal (case, spaces, order)

2. What does immutability of strings imply for building output?
   - *Expected:* each change builds a new string; accumulate in a list and join

3. When is slicing clearer than a loop?
   - *Expected:* when the operation is positional (reverse, prefix, step) rather than conditional
