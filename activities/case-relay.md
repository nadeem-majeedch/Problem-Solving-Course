# Activity — Case Relay

**Format for algorithmic lectures 09–20 · 12 minutes · one case, four teams.**

1. Project one intermediate-or-harder case and split the board into four
   columns: **Model · Plan · Code · Test**.
2. Team 1 writes the model (inputs, outputs, constraints) in 2 minutes
   and passes the pen. Team 2 writes pseudocode from that model, and so
   on. Teams may not change earlier work — they inherit it, bugs included.
3. The final team also writes one test that the *inherited* plan would
   fail if it were wrong.
4. Debrief: run the pseudocode by hand on the final team's test. Where
   did the relay break? Almost always: an unclear model forced a guess
   downstream.

**Why it works.** It makes specification debt visible in 12 minutes —
students feel their own ambiguity being inherited.

**Pitfall.** Choose a case with a genuinely small model (two-pointer or
brute-force family). Sorting-family cases stall at the code step.
