# Worked Examples — Lecture 24

Each example below follows the same arc: problem, analysis, algorithm, pseudocode,
then Python where the lecture has introduced it. Python blocks are machine-verified;
the comment lines `# expect:` match the actual output. Edge cases and complexity close
each example - they are part of the answer, not decoration.

| Example | Case | Python? |
| --- | --- | --- |
| [1. The Friend Circle: adjacency list and BFS](#1) | cs-093 | yes |
| [2. The Prerequisite Chain: topological order by peeling](#2) | cs-095 | yes |
| [3. The Epidemic Alarm: BFS measures time, not just reach](#3) | cs-096 | yes |

---

## 1. The Friend Circle: adjacency list and BFS (case cs-093)

**Problem.** Students 1..6; friendships (1,2), (1,3), (4,5). How many separate friend circles, and how big is each?

**Analysis.** Model: people are vertices, friendships edges; a circle is a connected component. BFS from any unvisited person floods their whole circle; counting floods counts circles. The adjacency list is the data structure that makes flooding cheap.

**Algorithm.**
1. build adjacency list from the friendship pairs
2. for each unvisited vertex: BFS, marking all reachable
3. each BFS flood = one circle; record its size

**Pseudocode.**

```
    adj <- empty map
    FOR each (u, v): adj[u].add(v); adj[v].add(u)
    circles <- 0
    FOR each person p
        IF not visited[p]
            circles++ ; BFS from p marking visited
    WRITE circles and sizes
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
from collections import deque

pairs = [(1, 2), (1, 3), (4, 5)]
adj = {}
for u, v in pairs:
    adj.setdefault(u, []).append(v)
    adj.setdefault(v, []).append(u)

visited = set()
sizes = []
for start in range(1, 7):
    if start in visited:
        continue
    frontier = deque([start])
    visited.add(start)
    size = 0
    while frontier:
        u = frontier.popleft()
        size += 1
        for w in adj.get(u, []):
            if w not in visited:
                visited.add(w)
                frontier.append(w)
    sizes.append(size)
print(len(sizes), sorted(sizes))
# expect: 3 [1, 2, 3]
```

**Trace (dry run).** Start 1: flood reaches 2, 3 -> circle size 3. Start 4: reaches 5 -> size 2. Start 6: no friends (adj.get returns []) -> size 1. Three circles: sizes 3, 2, 1. Vertex 6 shows why 'unvisited start' drives the outer loop, not the edge list.

**Expected output.** 3 circles of sizes 3, 2, 1

**Edge cases.** No friendships -> n circles of size 1. Self-friendships and duplicate pairs should be deduped or tolerated. BFS vs DFS changes the visit order, never the component count - any flood works.

**Complexity.** O(V + E) - each vertex enqueued once, each edge scanned twice (undirected).

## 2. The Prerequisite Chain: topological order by peeling (case cs-095)

**Problem.** Courses a..e; prerequisites b<a, c<a, d<b, e<c. Order the courses so every prerequisite comes first.

**Analysis.** The graph is directed; a valid schedule is a topological order. Kahn's peeling: repeatedly take a course whose prerequisites are all taken. If a cycle ever blocks the peel, the requirements are contradictory - the algorithm doubles as a cycle detector.

**Algorithm.**
1. compute in-degree (prerequisite count) for each course
2. take all zero in-degree courses
3. when taking a course, decrement the in-degree of its dependants
4. new zeros join the queue; if the queue empties before all are taken -> cycle

**Pseudocode.**

```
    indeg <- count of prerequisites per course
    queue <- all courses with indeg 0
    order <- empty
    WHILE queue not empty
        c <- pop queue; append c to order
        FOR each dependant d of c: indeg[d]--; IF indeg[d] = 0 THEN push d
    IF length(order) < number of courses THEN 'cycle'
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
deps = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": [], "e": []}
indeg = {k: len(v) for k, v in deps.items()}
queue = [k for k, v in indeg.items() if v == 0]
order = []
while queue:
    c = queue.pop()
    order.append(c)
    for k, v in deps.items():
        if c in v:
            indeg[k] -= 1
            if indeg[k] == 0:
                queue.append(k)
print(sorted(order))
# expect: ['a', 'b', 'c', 'd', 'e']
```

**Trace (dry run).** indeg: a=2, b=1, c=1, d=0, e=0 -> queue [d, e]. Pop e -> c's count 0 -> queue [d, c]. Pop c -> a's count 1. Pop d -> b's count 0 -> queue [b]. Pop b -> a's count 0 -> queue [a]. Pop a. Order {a,b,c,d,e} - all five taken, no cycle.

**Expected output.** a valid order exists: a, b, c, d, e (e.g. d, e, c, b, a)

**Edge cases.** Cycle example: b<a, a<b -> neither ever reaches in-degree 0 -> order shorter than 5 -> report 'contradictory requirements', not an infinite loop. Multiple zeros -> any order among them is valid (tie policy free). This 'peel zeros' pattern returns for job scheduling and build systems.

**Complexity.** O(V + E) with a real reverse-adjacency map (the demo re-scans deps for teaching clarity - worth flagging as the O(V*E) version).

## 3. The Epidemic Alarm: BFS measures time, not just reach (case cs-096)

**Problem.** Contacts spread infection per day: edges (1,2), (2,3), (2,4), (4,5). Infection starts at 1. On which day does each person fall ill?

**Analysis.** BFS from the source processes the graph in layers: layer k is exactly 'infected on day k'. Distances fall out of BFS for free - the queue's FIFO order is what makes the day assignment correct.

**Algorithm.**
1. distance[start] = 0; queue holds (person, day)
2. each contact of an infected person at day d falls ill at day d+1
3. first infection time wins (later rediscoveries are ignored)

**Pseudocode.**

```
    dist <- map start->0
    queue <- [(start, 0)]
    WHILE queue not empty
        (u, d) <- pop
        FOR each neighbour w of u
            IF w not in dist
                dist[w] <- d + 1; push (w, d+1)
    WRITE dist
```

**Python** (this block runs; its output is verified by `scripts/validate.py`):

```python
from collections import deque

edges = [(1, 2), (2, 3), (2, 4), (4, 5)]
adj = {}
for u, v in edges:
    adj.setdefault(u, []).append(v)
    adj.setdefault(v, []).append(u)

dist = {1: 0}
q = deque([1])
while q:
    u = q.popleft()
    for w in adj.get(u, []):
        if w not in dist:
            dist[w] = dist[u] + 1
            q.append(w)
print([dist.get(p) for p in range(1, 6)])
# expect: [0, 1, 2, 2, 3]
```

**Trace (dry run).** Start 1 (day 0) infects 2 (day 1). 2 infects 3 and 4 (day 2). 4 infects 5 (day 3). Person 5's day is decided by the first path to reach them - 1-2-4-5, length 3. Layers: {1}, {2}, {3,4}, {5}.

**Expected output.** infection days: person 1:0, 2:1, 3:2, 4:2, 5:3

**Edge cases.** Disconnected person -> no entry (dict.get gives None - print it as 'never'). Multiple sources (two outbreak points) -> seed all of them at day 0, BFS handles it unchanged. Weighted edges (hours not days) break BFS - that needs Dijkstra, the natural extension.

**Complexity.** O(V + E); the day count equals the BFS layer, computed with no extra work.
