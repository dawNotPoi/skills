---
name: product-ui-discovery
description: Turn known product goals into UI requirements, task flows, content, states, and acceptance criteria. Use for 界面需求、页面流程 and unclear navigation or interactions. Reuse confirmed product decisions and guide missing UI choices before design. Do not implement interfaces or silently decide system behavior.
---

# Product UI Discovery

Define what the interface must enable before deciding how it should look.

## Inputs and decision boundary

Read the current conversation, existing spec, project rules, screens and
contracts first. Reuse confirmed product decisions instead of repeating the
whole interview. Distinguish evidence, proposals and assumptions.

For missing state ownership, execution semantics, permissions, persistence or
API scope, use `development-discovery` when available. If it is not installed,
state the critical gap, offer options and a recommendation, ask a focused
question, and stop before implementation. Do not invent a missing peer skill.

For UI-specific gaps, ask one primary question per turn (at most three related
questions), explain why the choice matters, and offer concrete alternatives.
Help a developer who does not know choose through examples; do not send a
checklist wholesale or treat silence as a choice. Reversible details can follow
existing conventions with a recorded default.

## Workflow

1. State the product outcome, target users, and the situation triggering the UI.
2. Rank primary and secondary user jobs.
3. Map the shortest successful flow and meaningful alternate paths.
4. Inventory required information, actions, permissions, validation, loading,
   empty, error, partial, offline, and success states relevant to the task.
5. Capture platform, responsive, accessibility, localization, privacy, and
   technical constraints that affect the UI.
6. Convert findings into observable acceptance criteria. Separate critical
   unanswered questions from reversible presentation details.

Do not invent research findings. Label unverified claims as hypotheses and
propose the cheapest useful validation. Do not write product code in this stage.

## Output: UI Discovery Brief

Include outcome/users/jobs, scope and non-goals, primary and failure flows,
content/state inventory, constraints and sources, acceptance criteria, and
unresolved choices. Preserve the current spec revision and authorization mode.

A brief may be a few conversation lines for a small task. Persist it in the
target project's established documentation only when file writing is authorized.
Stop before selecting a visual direction or component API. Acceptance of the
brief alone is not permission to implement.
