# Lecture Notes — Lecture 28: Summaries That Don't Mislead

Companion to the lecture plan and the worked examples. Read the *Definitions* before
class, the *Explanation* after it; the practice questions and the lecture quiz close the loop.

## Definitions

- **Mean** — the total divided by the count; sensitive to every value, especially extremes
- **Median** — the middle value of the sorted data; robust to extremes
- **Skew** — asymmetry in the data's shape; the mean-median gap is its alarm
- **Percentage points** — the arithmetic difference of two percentages
- **Relative change** — the difference divided by the starting value
- **Honest summary** — a claim plus its denominator, its n, and the summary choice it depends on

## Explanation

A summary is an argument, and it can mislead without one false digit. Mean versus median: the mean answers 'total cost per person', the median answers 'the middle experience' - and in skewed data (salaries, waiting times) they diverge enormously. The gap itself is the skew alarm; report both or report the median. Percentages carry two units that get swapped in the wild: percentage points (10% to 8% is -2 points) versus relative change (which is -20%). Compounded changes multiply on shifting bases: up 20% then down 20% lands at 96, not 100. The honest summary bundles the number with its denominator, its n, and the alternative summary that would tell a different story. The discipline: before trusting any chart, ask what would make this look better - then look for that choice in the fine print.

## Examples

The lecture's worked examples live in [examples.md](examples.md); the case studies this
lecture builds on are worked in class from the projector. The case sequence with difficulties:
- [cs-109](../../case-studies/student/cs-109.md) (Beginner)
- [cs-110](../../case-studies/student/cs-110.md) (Foundational)
- [cs-111](../../case-studies/student/cs-111.md) (Intermediate)
- [cs-112](../../case-studies/student/cs-112.md) (Advanced)

## Common misconceptions

- Quoting the mean of skewed data as 'the average' without the median beside it.
- Swapping percentage points and percent - churn 'down 2 points' is 'down 20 percent', not the same claim.
- Adding percentage changes across shifting bases - up 20% then down 20% is a net 4% loss.
- Believing a chart cannot lie if the numbers are true - truncated axes and chosen baselines mislead.
- Reporting an n alongside a percentage is optional - without n, the reader cannot judge stability.

## Summary and key takeaways

1. Mean answers 'total per person'; median answers 'the middle experience' - report both under skew.
2. The mean-median gap is the skew alarm; the tail fraction is the experience of the unlucky.
3. Percentage points and percent are different units; name the base every time.
4. Compounding multiplies on shifting bases - +20% then -20% is a 4% loss.
5. An honest summary names its denominator, its n, and the choice it depends on.

## Practice questions

- Compute mean and median for 5 salaries with one extreme; write the one-sentence honest summary.
- Restate 'churn fell from 10% to 8%' in both units; which makes the team look better, and to whom?
- Compound: price +15% then -15%; then -15% then +15%. Explain why order does not matter here.
- Enrichment: find a real-feeling dataset where median and mean tell opposite stories; write both headlines.
- Enrichment: critique a truncated-axis bar chart (drawn by hand) and redraw it honestly.

## Where this leads

Next lecture: **Simulation as a Way of Knowing**. The quiz below checks this lecture's essentials before we build on them.
