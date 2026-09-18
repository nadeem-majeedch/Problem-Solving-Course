# Activity — Complexity Duel

**Format for lectures 17–24 · 6 minutes · needs the counting rule first.**

1. Project three snippets that solve the *same* task (linear scan,
   nested scan, early-exit scan) on inputs of size n.
2. Students individually rank them by how the running time *grows*, not
   which is faster on small inputs — then estimate counts for n = 1,000
   using the course's counting rules.
3. Vote by show of hands on the ranking; let the minority argue first.
4. Reveal: run all three on n = 1,000 and n = 10,000 live if a machine
   is available; otherwise compare the arithmetic (≈ one million
   operations vs ten million for the nested one).

**The trap to engineer.** Make the linear snippet do slightly more work
per iteration (e.g. build a string). Some students will rank it slower;
use that to separate constant factors from growth — the course's
repeated Big-O lesson.

**Pitfall.** Never include recursion in the snippets here; the call-tree
cost is its own lecture and muddies the vote.
