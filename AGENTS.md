# Agent Entry

This repository is a reusable skill library. Treat it as a capability index, not as a prompt bundle to preload.

## Bootstrap

When this repository is provided for a task:

1. Read `skills/INDEX.md` first.
2. Select the smallest set of skills that covers the request.
3. Read only the selected `SKILL.md` files and their required references/templates.
4. Preserve outputs that downstream skills depend on.
5. Respect each skill's explicit scope, stop conditions, and handoff rules.

## Development gate

For a new project or materially new feature, use `skills/development/development-discovery/SKILL.md` when important product or system decisions remain unresolved.

Do not silently choose product behavior, ownership boundaries, permission semantics, failure semantics, or acceptance criteria inside implementation code.

If a critical decision is missing, return to discovery before implementation. Non-critical assumptions may be made only when they are stated and do not materially change user-visible or system behavior.

## Routing rules

- Do not load every skill in the repository.
- Use `skills/core/skill-router/SKILL.md` when the correct skill set is unclear.
- Use `skills/development/learn-codebase/SKILL.md` when understanding an existing repository is necessary before planning or changing it.
- Use the UI family only for interface-specific discovery, direction, system, implementation, or visual QA.
- Use writing skills only when the requested output is a writing artifact.

## Handoffs

A handoff should preserve:

- user goal and scope;
- decisions already made and their rationale;
- unresolved questions;
- constraints and authoritative evidence;
- acceptance criteria;
- artifacts already produced, such as a feature spec, design direction, or implementation plan.

Do not quietly replace an approved upstream decision in a downstream skill.
