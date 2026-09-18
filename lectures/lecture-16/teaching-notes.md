# Teaching Notes — Lecture 16

*Instructor only - not rendered on the public site.*

## Board plan

- Left: the review map: 15 lectures as a metro line, stations = techniques.
- Middle: the two challenge cases with their assumption lists growing.
- Right: 'open questions' parking lot - anything the room cannot yet settle.

## Questions to ask students

- Which technique from Block I did today's case silently use?
- Where would your solution break first if the input doubled in size?
- Which assumption in the challenge case would you negotiate with the client first?

## Alternative explanations

- Exam-anxious students: run the exit quiz as a team relay instead of solo.
- Advanced: ask for a second solution path and a complexity comparison.

## Expected student difficulties

- Retrieval discomfort - students want notes open; mandate closed-notes first pass, open after.
- Assumption-hunting feels pedantic - show the money one flipped assumption moved in cs-001.

## Connections to neighbouring lectures

Mid-course consolidation; next block opens the algorithmics arc with searching (L17).

## Quiz answer key

**A1.** List the method's five phases.
- *Expected:* Specify (frame + assumptions), plan, execute, verify, present.

**A2.** Why does an assumption deserve a written line?
- *Expected:* It is the visible handle for later disagreement - and it moves answers.

**A3.** What is one-pass and why does it matter here?
- *Expected:* All aggregates in one loop - halves the reading cost and forces clean accumulator design.

**A4.** What makes a verification plan 'chosen, not felt'?
- *Expected:* Named edge cases with expected values, written before running.

**B1.** Plan (no code) the gradebook audit: parse, flag missing, flag anomalies, average - name each stage's output.
- *What earns marks:* Stage outputs: records; missing-list; anomaly-list; per-student averages with n.

**B2.** Estimate (method only) the digit sum of 2^15 and the longest heads-run in 100 flips.
- *What earns marks:* 2^15 = 32768 -> 26; streak via simulation, typical maximum 6-7 (report trials).

## Exit ticket - expected answers

1. Name the three stations and why you chose yours.
   - *Expected:* tracing / data structures / plan-first; chosen by personal weak spot

2. What must an integration plan name before code?
   - *Expected:* the techniques, their order, and the data each stage hands on

3. What does exam pacing change about case attempts?
   - *Expected:* time-boxing: a complete partial plan beats an unfinished perfect one
