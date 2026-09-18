# Glossary

Terms are defined as used in this course. First-taught lecture noted where a
term anchors to a specific case sequence.

**Abstraction** — Deliberately ignoring details that do not matter for the
current problem (e.g., treating "a student record" as just two numbers).
First taught in Lecture 01.

**Algorithm** — A finite sequence of unambiguous steps that transforms an
input into an output.

**Assignment** — Storing a value in a named variable (`x = 3`).

**Assumption** — A condition you are allowed to rely on (stated in each case's
metadata) that you need not check in code.

**Big-O category** — The growth class of a running time as input grows, e.g.
constant, logarithmic, linear, linearithmic, quadratic, exponential. Taught
from Lecture 17.

**Binary search** — Search on sorted data that halves the search range each
step. Lecture 21.

**Boolean expression** — An expression that is true or false; drives `if` and
`while` decisions.

**Boundary case** — An input at the edge of the constraints (smallest,
largest, first, last, empty). Central to Lecture 08.

**Brute force** — Trying all possibilities without cleverness; the baseline
every other strategy must beat. Lecture 20.

**Case study** — A short, self-contained problem used in the five-minute
cycle. This course contains 144 of them (cs-001 … cs-144).

**Complexity class** — See *Big-O category*.

**Constraint** — A limit on inputs or resources that any valid solution must
respect.

**Contradiction (proof by)** — Assuming the opposite of what you want and
deriving an impossibility; used in Lecture 26 and later.

**Decomposition** — Splitting a problem into smaller sub-problems you can
solve separately. Lecture 01.

**Dictionary** — Python's key→value map (`counts[key]`); used for frequency
counting. Lecture 13.

**Dynamic programming** — Solving a problem by combining stored solutions of
smaller sub-problems in a defined order. Lecture 23.

**Edge case** — An input outside the typical pattern where naive solutions
break (empty, single element, duplicates, extremes).

**Enrichment** — Optional material (tagged in lecture plans) beyond the
mandatory core sequence.

**Flowchart** — A diagram of an algorithm using standard shapes for
processes, decisions, and input/output. Lecture 03.

**Frequency counting** — Tallying how often each value occurs, usually with a
dictionary. Lecture 13.

**Function** — A named, reusable block of code with inputs (parameters) and
an output (`return`). Lecture 14.

**Greedy strategy** — Making the locally best choice at each step and keeping
it; requires an argument that local choices are safe. Lecture 22.

**Heuristic** — A rule of thumb that is fast and often good, without a
guarantee; distinguished from an exact method in Lecture 31.

**Invariant** — A statement that stays true at every step of a loop; the
standard way to argue a loop is correct. Lecture 19.

**Linear scan** — Checking items one by one; the default search when data is
unsorted. Lecture 17.

**Loop** — Repeating steps: `for` over a sequence, `while` under a
condition.

**Loop invariant** — See *Invariant*.

**Model (mathematical)** — A translation of a word problem into numbers,
symbols, and relations. Lecture 05 onward.

**Modulo (`%`)** — Remainder after division; the workhorse of cycles,
grouping, and parity checks. Lecture 05.

**Monotonic** — Only ever increasing or only ever decreasing; the property
binary search needs. Lecture 21.

**Off-by-one error** — A boundary mistake in a loop or index (one too few or
one too many steps). Lecture 06.

**Pseudocode** — Structured plain language that describes an algorithm
precisely without syntax of a real language. Lecture 02.

**Recursion** — A function calling itself on a smaller input, with a base
case. Lecture 22.

**Running total** — A variable that accumulates a result across loop
iterations. Lecture 09.

**Set** — A collection of distinct items; used for membership and duplicate
questions. Lecture 13.

**Simulation** — Answering a question by mimicking the process step by step
under a model. Lecture 30.

**Slicing** — Extracting a part of a sequence, e.g. `s[1:4]`. Lecture 11.

**State (program state)** — The complete snapshot of all variables at one
moment; what a trace table records. Lecture 06.

**Strategy** — A general plan for attacking unfamiliar problems (decompose,
invariants, greedy, DP, simulation, heuristics). Lectures 31–32.

**String** — A sequence of characters; supports indexing and slicing.
Lecture 10.

**Test case** — A named input with its expected output and the reason it was
chosen. Lecture 08.

**Trace table** — A table of variable values after each step/iteration, used
to predict and verify behaviour. Lecture 06.

**Type** — The kind of a value (int, float, string, bool, list, dict, set).
Type mismatches are a top-three bug source in this course.

**Walking pointer** — An index that moves through data (e.g. two pointers
moving toward each other). Lecture 18.
