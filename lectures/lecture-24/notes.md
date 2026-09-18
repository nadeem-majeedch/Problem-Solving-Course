# Lecture Notes — Lecture 24: Graphs as Models

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Graph** — a set of entities (vertices) plus relationships (edges) between them
- **Adjacency list** — for each vertex, the list of its neighbours - the standard graph representation
- **Breadth-first search** — explore in rings: all distance-1 neighbours, then distance-2, and so on
- **Connected component** — a maximal group of vertices reachable from each other
- **In-degree** — the number of incoming edges - for prerequisites, how many requirements remain
- **Topological order** — an ordering where every edge points forward; a valid schedule of dependencies

## Explanation

Graphs are the modelling lecture: the algorithm is only as good as the vertex-edge choice. Students are vertices with friendship edges; courses are vertices with prerequisite arrows. Adjacency lists make exploration cheap. Breadth-first search floods outward in rings, which makes it simultaneously a reachability test, a distance measurer (unweighted), and a multi-source propagator when several starting vertices are seeded at day zero. Connected components (friend circles) fall out of repeated floods. Directed graphs add Kahn's peeling: repeatedly take a vertex with no remaining prerequisites; if you get stuck before finishing, the requirements contain a cycle - the algorithm doubles as a contradiction detector. The design questions repeat every time: what is a vertex, what is an edge, directed or not, and what does 'distance' mean here. Answer those and the traversal usually writes itself.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-093](../../case-studies/student/cs-093.md) (Beginner)
- [cs-094](../../case-studies/student/cs-094.md) (Foundational)
- [cs-095](../../case-studies/student/cs-095.md) (Intermediate)
- [cs-096](../../case-studies/student/cs-096.md) (Advanced)

## Common misconceptions

- Modelling one-way prerequisites as undirected edges - direction is the content.
- Believing BFS and DFS give different components or distances - the flood differs, the answers do not (unweighted).
- Forgetting that disconnected vertices exist - the outer loop must visit every start, not walk edges only.
- Treating a topological-order failure as a bug - a cycle is a legitimate answer: 'requirements are contradictory'.
- Adding weights to BFS distance - unweighted BFS layers are not Dijkstra distances.

## Summary and key takeaways

1. Choose vertices and edges first; the traversal follows from the model.
2. BFS = rings = unweighted distances; seed several sources for propagation problems.
3. Repeated floods count components; every vertex must get a start chance.
4. Kahn's peeling schedules prerequisites and detects contradictory cycles.
5. Directed or not is a modelling decision with algorithmic consequences.

## Practice questions

- Model 4 courses with prerequisites as a directed graph; produce one valid order by peeling.
- BFS by hand on a 6-vertex friendship graph: write the ring (layer) of every vertex.
- Count connected components for a graph with an isolated vertex; explain the outer loop's role.
- Enrichment: multi-source BFS - two sensors report a fault; compute first-fault-day for every node.
- Enrichment: convert Kahn's peeling to detect and report the exact cycle when the peel stalls.

## Where this leads

Next lecture: **Thinking with Data**. The quiz below checks this lecture's essentials before we build on them.
