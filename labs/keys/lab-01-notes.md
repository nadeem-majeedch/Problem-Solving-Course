# Lab 1 — Checkpoint Notes (instructor only)

Not for publication; discuss after the lab.

- **A1.** Assumptions we expect: first input may be 0 (empty session —
  count 0, sum 0, and largest must not be printed or must be defined);
  inputs are one per line vs space-separated; non-numeric input is not
  tested (parsing out of scope). Watch for teams that skip stating
  assumptions entirely — that is the lab's first teaching point.
- **B1.** Common pseudocode faults: initialising `largest` to 0 (fails for
  negative sessions); updating `largest` outside the loop; counting the
  sentinel. The translation sticking point is usually the
  initialisation-before-loop discipline.
- **B2.** Expected output on `[7, 3, 15, 2, 9, 3]`: count 6, sum 39,
  largest 15.
- **B3.** Empty list: a correct program prints count 0, sum 0, and either
  no largest line or a defined message. `[4]`: count 1, sum 4, largest 4.
  A `ValueError` from `max([])` is the classic discoverable defect.
- **C1/C2.** Good hostile lists: `[-5, -2]` (largest must be −2, catches the
  0-initialisation), `[0]` (is 0 data or terminator?), `[5, 5, 5]`
  (identical elements), huge lists (no defect, but teaches that not
  everything needs to be hostile).
- **C3.** Look for mechanism-level fixes vs symptom patches: e.g. changing
  `largest = 0` to `largest = session[0]` with an empty-guard, rather than
  special-casing the hostile input that exposed it.
- **D1.** Legitimate style differences: sentinel handling, one-pass vs
  three-pass, output wording. Genuine defects to hope for: counting the
  terminator, wrong divisor for the average if they extended it.
- Completion bar: all six checkpoints attempted with honest notes. Pairs
  that "finished early" should be sent to extend their exchange list to a
  five-row test table, not told they are done.
