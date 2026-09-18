# Lab 7 — Checkpoint Notes (instructor only)

Not for publication; discuss after the lab.

- **Expected outputs (derive before running; verified by execution on
  2026-09-18):** marks [72, 85, 90, 60, 55, 91]; true average = 453/6 =
  75.5; true passes (≥ 60) = 5 (72, 85, 90, 60, 91 — 60 included, 55 not);
  true top = fay with 91.
- **Patient A.** Defect: `range(1, len(marks))` skips marks[0] = 72.
  Prints 381/6 = 63.5. Hypothesis confirmation: print `i` and `marks[i]`
  for the first two iterations — 72 never appears. Fix: `range(len(marks))`.
  Watch for symptom-patches (adding 12 to the result) — reject them.
- **Patient B.** Defect: two overlapping ifs — every mark > 60 is counted
  twice (by both ifs), and marks = 60 exactly once (only the first if).
  Prints 9 on the given data (72, 85, 90, 91 counted twice = 8, plus 60
  once). Hypothesis confirmation: print `m` and `passes` each iteration;
  the jump of 2 at 72 is the tell. Fix: delete the second if. Deep version
  (for discussion): the boundary 60 vs > 60 — "pass" must be defined once,
  in one place.
- **Patient C — the visible defect.** `marks[k] >= best` with `best = 0`
  accepts equal marks and overwrites `best_name`, so *the last* student
  with the top mark wins. On the given data fay (91) is last so the output
  looks right! The symptom is silent — which is why A1's hand-derived
  expectation ("fay") matches. Hmm — so what fails? Change the list to
  [91, 85, 90, 60, 55, 91]: top should be *ann or fay depending on the
  tie rule*, and the program says fay without ever justifying the rule.
  That is D1's tie defect: the program encodes "last wins" silently.
  **Fix for teaching:** prepare Patient C with the top mark NOT last —
  e.g. marks [91, 85, 90, 60, 55, 72] where the naive read still looks
  fine but `>=` vs `>` decides between ann and nobody-else; the clean
  exposing input is two students tied at the top with the first one
  expected under a "first wins" rule: [91, 91] → the program reports the
  second. State the tie rule in the fix, not just the operator.
- **B2.** Regression discipline: after fixing A, re-run [10, 20] (fine
  before and after) — the point is the *habit*; nothing dramatic happens,
  and say so.
- **C1.** The strongest review question is "would your observation also
  fit hypothesis X?" — e.g. Patient A's low average also fits "summing
  wrong" rather than "starting late". A confirming observation must
  discriminate.
- **C2.** Expected honest answer: Patients A and B are found faster by
  reading (`range(1, …)` is visible); the method pays when the code is
  long, the state is large, or the defect is interactional (Patient C's
  silent tie rule is invisible to both reading *and* single runs — only
  a targeted input exposes it).
- **D2.** Exceptions localise themselves (they point at a line); silent
  wrong answers leave you to construct the localisation — which is exactly
  what the log formalises. Connect to cs-045 ("The Median That Lies") and
  cs-046 ("The Phantom Zero"), same lecture.
- Preparation note: wrap each snippet in a file that prints exactly as
  shown (no crashing). Keep a fourth "healthy" patient on hand for pairs
  who finish early — a program with *no* defect, to test whether their
  method concludes "no defect found" honestly rather than inventing one.
- Completion bar as in Lab 1. Fast finishers: hand them cs-047's
  really_broken (the swap that wasn't) as a fourth patient with the same
  log format.
