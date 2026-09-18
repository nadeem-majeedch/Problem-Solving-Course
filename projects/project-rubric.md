# Rubric — Projects A and B (30 marks each)

Shared criteria; apply to either project. Half-bands where genuinely
between. The two "problem solving" criteria are where this course earns
its name — do not let correct code alone reach the top bands.

## 1. Programs work as specified (8)

| Band | Descriptor |
| --- | --- |
| 8 | All specified behaviour present and correct, including seeds and edge handling; validator (B) checks every rule independently. |
| 6 | Core behaviour correct; one specified feature missing or subtly wrong (e.g. a cleaning rule silently applied). |
| 4 | Runs and produces plausible output, but 2–3 specified behaviours are wrong or missing. |
| 2 | Runs with effort; behaviour deviates from the brief in most parts. |
| 0 | Does not run. |

## 2. Problem-solving process shown (8)

| Band | Descriptor |
| --- | --- |
| 8 | Choices are argued from the data/brief (priority rule, cleaning rules, seed policy); alternatives considered and rejected with reasons. |
| 6 | Choices stated and mostly justified; one significant alternative missing. |
| 4 | Choices stated but justified only by assertion ("this is simpler"). |
| 2 | Choices invisible; the code reads like the brief was guessed. |
| 0 | No evidence of decision-making. |

## 3. Analysis (8)

| Band | Descriptor |
| --- | --- |
| 8 | Complexity arithmetic correct with growth terms named; the trade-off/constraint part is specific and honest (includes what the method cannot do). |
| 6 | Complexity correct at Big-O level but the trade-off discussion is thin. |
| 4 | Complexity attempted with minor slips; trade-off is generic. |
| 2 | Complexity present but wrong; trade-off missing. |
| 0 | No analysis. |

## 4. Data integrity and reproducibility (6)

| Band | Descriptor |
| --- | --- |
| 6 | Generator documented and seeded; every cleaning/fixing rule reported with counts; nothing silent anywhere. |
| 4 | Seeds present; one rule undisclosed or discovered only by re-running. |
| 2 | Data hard-coded or partly undocumented; fixes not reported. |
| 0 | No reproducibility. |

**Marking shortcut:** re-run the generator with the submitted seed —
outputs must match byte-for-byte (A: sales.csv; B: requests.json).
