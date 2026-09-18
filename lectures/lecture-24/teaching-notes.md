# Teaching Notes — Lecture 24

*Instructor only - not rendered on the public site.*

## Board plan

- Left: two models of the same class: friendship (undirected) vs prerequisites (directed).
- Middle: BFS rings around the source, labelled with distances.
- Right: Kahn's peel: the zero-in-degree frontier advancing; the stall marked 'cycle here'.

## Questions to ask students

- What is a vertex in each model - and what would the WRONG choice blur?
- Why does the outer loop over all vertices still give O(V + E) overall?
- In the peel, what does a stalled queue tell us - and is that a bug or an answer?

## Alternative explanations

- Physical-graph demo: students hold string edges; BFS as a wave through the room.
- Advanced: multi-source BFS seeding - two outbreak points at day zero.

## Expected student difficulties

- Forgetting the isolated vertex - the all-vertices outer loop is the fix.
- Treating a cycle as failure - it is a legitimate, reportable answer.

## Connections to neighbouring lectures

Graph models complete the algorithmics arc; Block IV opens with data thinking (L25).

## Quiz answer key

**A1.** What two choices define a graph model?
- *Expected:* What is a vertex; what is an edge (and directed or not).

**A2.** What does BFS give in an unweighted graph?
- *Expected:* Shortest distances (rings/layers).

**A3.** How do you count connected components?
- *Expected:* Flood from every unvisited vertex; count the floods.

**A4.** What does a stalled topological peel mean?
- *Expected:* A cycle - contradictory requirements, a legitimate answer.

**B1.** Friendships (1,2),(1,3),(4,5), vertex 6 alone: components and sizes.
- *What earns marks:* Three: {1,2,3}, {4,5}, {6} - sizes 3, 2, 1.

**B2.** Prereqs b<a, c<a, d<b, e<c: give one valid order.
- *What earns marks:* d, e, c, b, a (any topological order).

## Exit ticket - expected answers

1. What is a node in the campus model, and why?
   - *Expected:* junctions/rooms — decisions and meetings happen there

2. What does BFS level number mean?
   - *Expected:* minimum number of steps from the source

3. When is there no valid ordering in cs-095?
   - *Expected:* exactly when the prerequisite graph has a cycle
