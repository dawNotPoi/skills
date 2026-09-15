# Codebase Learning Map

Use this note to preserve the current mental model while exploring a repository.
Keep it compact and update it as evidence changes.

## Goal

What do I want to be able to explain, debug, extend, or modify?

## Project Purpose

- Problem solved:
- Primary users/callers:
- Runtime environment:
- Main technologies:

## Repository Map

| Area | Responsibility | High-signal files/symbols | Confidence |
| --- | --- | --- | --- |
| | | | |

## Anchor Scenario

Describe one concrete behavior to trace end to end.

## Execution Path

```text
Trigger
  ->
  ->
  ->
Result
```

For each important step:

| Step | Path / Symbol | Input | Output | State / Side Effect | Evidence |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Core Abstractions

| Abstraction | Owns | Invariant | Called by | Calls / depends on | Why it exists |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## State Model

- Important state:
- Owner:
- Mutation points:
- Persistence boundary:
- Cache / derived state:

## External Boundaries

- Database:
- Network / RPC:
- Queue / event bus:
- Tool / plugin / MCP boundary:
- OS / filesystem:
- Third-party services:

## Verified Facts

Record only claims backed by code, tests, runtime output, commits, or PRs.

- 

## Hypotheses / Open Questions

- 

## Design History

| Decision / abstraction | Commit / PR | Previous design | Motivation | Result |
| --- | --- | --- | --- | --- |
| | | | | |

## Active Recall

Questions I should be able to answer without looking:

1. Where does execution begin for the anchor scenario?
2. Which abstraction owns the central decision?
3. Where does important state live?
4. Why are the two most similar abstractions separate?
5. Where would I add a small new behavior, and why?

## Change Exercise

- Proposed change:
- Expected owning layer:
- Symbols expected to change:
- Symbols expected not to change:
- Tests to add/update:
- Regression risks:
- Actual result:
- What my prediction got wrong:

## Next Highest-Value Investigation

What single search, file, test, runtime experiment, commit, or PR would reduce uncertainty the most?
