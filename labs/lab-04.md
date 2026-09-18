# Lab 4 — Modelling with Graphs (Lecture 24 follow-up)

**Machine lab · 2 hours · Work in pairs.** You will model a campus situation
as a graph, implement breadth-first search, and defend the modelling choices
in writing. Submit: a report answering the checkpoints.

## Setup

- Python 3 as `python`; files in `lab4/`.
- The campus map (paste into `lab4/map.py`):

```python
edges = [
    ("gate", "library"), ("gate", "canteen"), ("library", "cs-dept"),
    ("canteen", "cs-dept"), ("canteen", "gym"), ("cs-dept", "labs"),
    ("gym", "labs"), ("library", "hall"), ("hall", "theatre"),
    ("theatre", "labs"),
]
```

Edges are undirected: a path works in both directions. All edges cost one
"hop" regardless of physical distance.

## Part A — Model first (20 min)

A1. Draw (on paper) the graph from `edges`. Count nodes and edges.
A2. Answer before coding: what is the fewest-hop route gate → labs?
    How many such minimal routes exist? Write your answers down — Part B
    will check them.

## Part B — BFS by hand and in code (35 min)

B1. Run BFS *by hand* from `gate`: write each BFS level (0, 1, 2, 3, …) and
    its nodes. The level of a node *is* its fewest-hop distance.
B2. Implement `lab4/bfs.py`: adjacency list from `edges` (build it with a
    loop — both directions!), BFS from a start node returning
    `{node: distance}`, unreachable nodes either absent or marked ∞ — your
    choice, but state it.
B3. Run from `gate`. Compare with your hand-run and your A2 answers.
    Resolve any disagreement — the hand-run and the code must agree.

## Part C — The unreachable case (20 min)

C1. Add edge `("annex", "theatre")` and run BFS from `annex` and from
    `gate`. Record both outputs. Which nodes are unreachable from where?
C2. Suppose the college adds a bus service: any two of
    {`gate`, `hall`, `gym`} become one hop apart. Add those edges. Does the
    eccentricity of `gate` (its maximum distance to any node) shrink? Show
    the numbers.

## Part D — Defend the model (20 min)

D1. A colleague proposes a different model: nodes are *rooms*, not
    buildings, with edges for doorways. Name one question the room-level
    model answers that your building-level model cannot.
D2. The physical distances between buildings are known. Name one question
    for which hop-count is the *wrong* cost — and what model change fixes it.

## Checkpoints (submit these as your report)

1. Your drawing's node and edge counts from A1, and your A2 predictions.
2. The BFS levels from B1 and the program output from B3, side by side.
3. Your stated convention for unreachable nodes (B2), and the C1 outputs
   for both starts.
4. The C2 eccentricity answer with the before/after numbers.
5. D1 and D2, one or two sentences each — the modelling defence is the
   heart of this lab.
6. One thing the graph model *cannot* answer about the campus, however
   modelled.

## What completion looks like

Completion-graded: hand-run and code must both appear and must agree;
modelling answers must take a position and defend it, not hedge. "Both
models are equally good" without an argument earns no checkpoint credit.
