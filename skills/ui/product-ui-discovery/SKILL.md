---
name: product-ui-discovery
description: Turn known product intent into evidence-backed UI flows, content, states and acceptance criteria (界面需求、交互流程、页面状态没说清). Use before visual design when the interface workflow is unclear. Guide unresolved choices with options and a recommendation. Route system or permission decisions upstream; do not implement or select a visual style.
---

# Product UI Discovery

Define what the interface must enable before deciding how it should look.

## Inputs and boundary

Read the existing conversation, target project instructions, product notes,
flows, screenshots, design system and prior decisions first. Reuse confirmed
requirements; do not restart the developer interview at every handoff. Separate
observed evidence from assumptions and proposed defaults.

If state ownership, permissions, offline/retry semantics or the meaning of an
action are unresolved, name the specific blocker and use an available
`development-discovery` skill. Do not loop between discovery skills without a
new decision. If that skill is unavailable, explain the blocker and guide the
same decision locally; never pretend it was loaded.

## Workflow

1. State outcome, users, trigger, primary task and explicit non-goals.
2. Read existing behavior before ranking primary and secondary user jobs.
3. Map the shortest successful flow and meaningful alternate paths.
4. Inventory content, actions, permissions, validation, loading, empty, error,
   partial, offline and success states relevant to this scope.
5. Identify platform, responsive, accessibility, localization, privacy and
   technical constraints. Avoid adding requirements merely to fill a checklist.
6. For a material UI choice, ask one focused question, offer meaningful
   alternatives, explain their consequences and recommend one. At most three
   related questions per turn. If the developer does not know, explain with a
   user scenario rather than asking the same question again.
7. Record decisions and convert them into observable acceptance criteria.

Do not invent user research. Label hypotheses and propose the cheapest useful
validation. This skill is non-implementing: unresolved flow/acceptance decisions
must not be silently completed in code.

## Output: UI Discovery Brief

Include outcome/users/context, ranked tasks, scope/non-goals, primary and
failure flows, content/state inventory, existing constraints and references,
acceptance, confirmed decisions, assumptions and critical open questions.
Preserve target/ref, upstream spec/plan version and approval source when known.

A UI brief does not authorize coding. Hand off to direction design only when
needed, or to implementation after the current behavior/design and coding scope
are authorized. Persist artifacts in the target project only within authorized
writes; otherwise provide the brief in chat and mark it unsaved.
