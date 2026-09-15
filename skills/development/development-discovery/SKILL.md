---
name: development-discovery
description: Use before starting a new software project or materially new feature when goals, behavior, scope, state ownership, permissions, failure semantics or acceptance are unclear (启动项目、开发新功能、需求没说清、先讨论方案). Inspect existing context, guide the developer with options and recommendations, then produce a spec, plan and explicit readiness handoff. Do not silently decide critical requirements in code or turn clear small fixes into an interview.
---

# Development Discovery

Turn incomplete intent into an agreed, implementable change. Help the developer
make decisions; do not merely request a complete PRD or ask a long questionnaire.

## Before asking

Read the current conversation, target repository instructions, relevant docs,
existing flows, contracts, tests and nearby implementation. Reuse established
stack, branding, data ownership and decisions unless the request changes them.
If the target is inaccessible, distinguish repository unknowns from product
unknowns. Never claim an architecture was inspected when it was not.

Classify the task:

- **New project:** establish user outcome, primary loop, platforms, system and
  trust boundaries, persistence, deployment constraints and the smallest MVP.
- **New feature:** identify entry points, unchanged invariants, affected
  contracts, lifecycle, compatibility and rollout/rollback needs.
- **Clear small fix:** state expected behavior, bounded change and checks in a
  compact note. Reuse existing authorization. Skip unnecessary interviews.
- **Planning only:** produce the requested proposal and stop; do not code.

## Guided conversation

Use [references/question-framework.md](references/question-framework.md) to
identify missing decisions, not as a questionnaire to send wholesale.

For each turn:

1. Briefly state what is already understood. Label repository evidence, user
   confirmation, inference and proposed defaults separately.
2. Choose the one unknown with the highest impact on behavior or architecture;
   ask at most three only when tightly related. Explain its consequence.
3. Give two or three meaningful options when alternatives exist, their user
   behavior and trade-offs, and a recommendation tied to the user's goal.
   Include an alternative/custom answer; do not force a false binary choice.
4. Ask the developer which behavior they want. Wait for the answer before
   treating a critical choice as settled. Do not append implementation to the
   same turn while calling it a clarification.
5. Update the decision record, then resolve the next meaningful gap.

When the answer is '不知道', explain with a concrete user scenario and suggest
an MVP default. Do not ask the same jargon question again. When the user says
'你决定', record the delegated decision scope and rationale; delegation does
not expand permission for destructive actions, external writes or new scope.
Low-risk, reversible details may use stated defaults. Unknown permission,
data-loss, billing or public-exposure behavior is never a hidden default.

## Gate and artifacts

Apply [references/readiness-gate.md](references/readiness-gate.md). Read-only
inspection and draft proposals are allowed during discovery. Do not scaffold
a project, add dependencies or modify production code while critical choices
for that scope remain unresolved. A POC requires authorization for a bounded,
isolated experiment; it is not permission to ship production behavior.

For substantial work, draft a [feature spec](templates/feature-spec.md) and a
separate [implementation plan](templates/implementation-plan.md). Reuse the
target project's existing docs layout; otherwise propose `docs/specs/` and
`docs/plans/`. Use project-local durable documents only within authorized
writes; in a read-only session, provide equivalent content in chat and mark it
unsaved. Do not write private project artifacts into the skill library.

The spec states what and why: goal, actors, scope/non-goals, flows, state/data
ownership, permission boundaries, failure/recovery semantics and observable
acceptance. The plan states how: inspected paths, dependency order, tasks,
verification, risks, rollback and any authorized spike. Unknown file paths or
APIs are marked proposed, not invented as existing facts.

Present a concise behavior summary and the current spec/plan version. Ask for
implementation authorization only if not already explicitly granted for this
scope. Selecting a visual option or saying '继续讨论' is not approval to code.

## Handoff and resume

Output the current gate status, confirmed decisions, proposed defaults,
critical blockers, spec/plan location and version, approval evidence, allowed
next actions and acceptance checks. Do not implement inside this skill; hand
off when ready. UI work may need interface discovery/direction/system stages;
backend work may use the host's normal coding workflow. No skill is presumed
installed merely because its name is mentioned.

On resume, restore the record and inspect relevant repository changes before
repeating questions. A changed requirement invalidates only affected decisions
and approval; explain the delta and request a decision, not a full restart.
During implementation, a newly discovered blocker returns here before the
agent chooses new product behavior. After verification, record deviations and
propose only stable cross-feature rules for the target project's AGENTS.md;
never silently change its instructions or claim tests/visual checks not run.
