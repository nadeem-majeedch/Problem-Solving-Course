# Teaching Notes — Lecture 12

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the repro->hypothesise->isolate->fix protocol, now executed by STUDENTS.
- Middle: the three seeded defects listed as patients; symptoms only, no names.
- Right: 'what each defect taught us' - filled during the debrief.

## Questions to ask students

- Which symptom alone already suggests the median-of-even bug?
- What is the minimal input for the phantom zero - can you make it 3 lines?
- Why did the swap defect survive the first test suite?

## Alternative explanations

- Struggling pairs: hand out the defect NAMES after 10 minutes; the hunt becomes confirmation + fix.
- Fast pairs: a fourth seeded defect (off-by-one in a window sum) hidden in the same file.

## Expected student difficulties

- Editing three places at once - enforce one-fix-one-test cycles.
- Blaming the language - redirect to the hypothesis table; the defect is always in a stated line.

## Connections to neighbouring lectures

The lab operationalises L7-L8; next: dictionaries give the tally pattern its natural home (L13).

## Quiz answer key

**A1.** Why one fix per test cycle?
- *Expected:* So cause and effect stay attributable; shotgun edits hide which change worked.

**A2.** What is the minimal repro discipline?
- *Expected:* Shrink the input while the bug persists; smallest reproducer reveals the mechanism.

**A3.** Name a defect class a happy-path suite misses.
- *Expected:* Boundary/even-length handling (the median-of-even bug).

**A4.** What does the regression suite protect after the lab?
- *Expected:* Every fix stays fixed; reruns catch reintroduction.

**B1.** Write the minimal input that exposes a phantom-zero (empty string scored as 0).
- *What earns marks:* Input: one line, empty score ('bo,DS1,'). Expected: flagged/missing, not 0.

**B2.** A swap defect (a, b = b, a miswritten) survives normal tests - what test finds it?
- *What earns marks:* A test where order matters with distinct values (x=1, y=2 -> expect 2, 1); symmetric tests hide swaps.

## Exit ticket - expected answers

1. Why must the reproduction step precede any hypothesis?
   - *Expected:* an unreproduced defect cannot be falsified; you would be guessing

2. What does 'fix without breaking green tests' require?
   - *Expected:* a regression suite run before and after every change

3. Name the isolation technique used on cs-048.
   - *Expected:* history bisect: halve the commit range each experiment
