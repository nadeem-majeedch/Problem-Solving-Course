# Lab 2 — Checkpoint Notes (instructor only)

Not for publication.

- **A1.** Reject tables written after code was peeked at — walk the room
  during Part A. Strong own-choice rows: 8 characters, letter first, digit
  last, but a space inside (is the space "a character"? yes — valid);
  `"CS101000"`-style rows where rules 2 and 3 both fail (order matters:
  verdict must name *first* failure, so "first character"); unicode
  letters; trailing newline from file reads (why live data is hostile).
  Boundary rows: 7 and 9 characters, plus the 8-character pass.
- **B1.** The ordering trap: teams write all three checks then join
  messages; the spec demands first-failure. Test case "7 characters,
  starting with a digit" separates ordered `elif` chains from
  collect-all-then-join designs. The driver pattern to encourage:

  ```python
  table = [("CS101", "length"), ...]
  for sid, expected in table:
      observed = verdict(sid)
      print(sid, expected, observed, "PASS" if observed == expected else "FAIL")
  ```

- **B2.** The integrity moment of the lab: students tempted to edit the
  expected column should instead argue the row. Usually the row was right
  and the code had the rule order wrong.
- **C2.** The spec ambiguity most pairs hit: is a 9-character ID with all
  other rules fine a "length" failure — or should extra-long IDs be
  truncated first? There is no right answer; the deliverable is a *written*
  resolution, which is checkpoint 4's point.
- **C3.** Adding the best two of their rows: watch for silent addition
  without re-running; insist on the full-table re-run print.
- **D1.** Normalisation changes verdicts when case or whitespace was the
  failing feature: `" cs101 "` is 7 characters (length fail) before
  stripping, valid after. The discussion target: normalisation is a *spec
  change*, not a courtesy — decide it explicitly.
- **Checkpoint 6.** The honest answer is usually "one circled row caught
  the ordering bug; the other never failed". Draw the lesson: a test that never fails is not wasted — it is a regression guard — but at design time it felt more powerful than it proved to be.
- Completion bar: ≥ 10 deliberate rows, driver output printed, exchange
  analysis present. Pairs finishing early: have them write the *one-row*
  table that would have caught each defect found in the room, then compare.
