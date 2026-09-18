# Lab 4 — Checkpoint Notes (instructor only)

Not for publication.

- **A1.** 8 nodes (gate, library, canteen, cs-dept, gym, labs, hall,
  theatre), 10 undirected edges. Verified by running BFS on the given
  edge list.
- **A2.** Fewest-hop gate → labs: distance 3, with **three** minimal
  routes: gate–canteen–cs-dept–labs, gate–canteen–gym–labs,
  gate–library–cs-dept–labs. (gate–library–hall–theatre–labs is 4, not
  minimal.) Award for the count with the routes listed.
- **B1.** Levels from gate: 0 {gate}; 1 {library, canteen}; 2 {cs-dept,
  gym, hall}; 3 {labs, theatre}; done. Verified against the code. Note
  theatre lands at 3 via hall, and labs at 3 via theatre as well — the
  first time a node is reached fixes its level; later discoveries do not
  update it.
- **B2.** Build the adjacency list with both directions — the classic
  defect is one-directional edges, which surfaces as "unreachable" nodes
  that are obviously reachable. Convention for unreachable: either omit or
  ∞; the report must state which. Encourage the dict built during BFS.
- **B3.** Agreement check: the hand-run predicts, the code verifies.
  Disagreements almost always trace to (a) one-directional adjacency,
  (b) a visited-set set too late (a node enqueued twice, distance
  overwritten), or (c) marking visited when *dequeued* instead of when
  *enqueued* — in BFS the enqueued-time marking is the safe order at this
  scale.
- **C1.** With `("annex", "theatre")`: from `gate` every node is reachable
  (annex at distance 4, via gate–library–hall–theatre–annex). From `annex`:
  theatre 1, labs 2, hall 2, gym 3, cs-dept 3, library 3, canteen 4,
  gate 4. All reachable now. Before the new edge, from `gate` annex was
  unreachable — the two runs must be recorded *in order* to show the change.
- **C2.** Bus edges among {gate, hall, gym}: gate–hall, gate–gym, hall–gym.
  From gate: gym drops to 1, theatre to 2 (gate–hall–theatre), labs to 2
  (gate–gym–labs). Eccentricity of gate goes 3 → 2. The number and its
  before/after comparison are the checkpoint.
- **D1.** Room-level questions: which specific room is busiest / how
  doorway width or corridor congestion changes routes; anything below
  building granularity. The model must answer *at its granularity*.
- **D2.** "Which route is fastest to walk?" — hop-count is wrong when edge
  costs differ; fix by weighting edges (Dijkstra-shaped thinking, next
  course; naming it is optional enrichment, not required).
- **Checkpoint 6.** Honest answers: how long a *queue* is at the canteen at
  1 pm (needs live data, not structure); whether a route is *pleasant*;
  anything requiring weights, time, or traffic. Reject "nothing".
- Completion bar: hand-run + code agreement, C1/C2 numbers, and a defended
  position in D. Early finishers: multi-source BFS — put all three bus
  stops in the queue at distance 0 and recompute everyone's distance to
  the nearest stop.
