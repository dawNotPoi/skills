---
name: skill-router
description: Route a task to the smallest useful set of skills in this repository. Use when the user gives the whole skills repository to an Agent, asks which skill to use, or the task spans multiple domains or stages. Produce a short execution route and load only the selected skills. Do not perform the specialist work itself and do not preload the entire library.
---

# Skill Router

Choose capabilities before doing specialist work.

## Inputs

Read `skills/INDEX.md` and the user's request. Inspect repository context only enough to determine the task stage and domain.

## Routing workflow

1. Classify the request by stage: discovery, repository understanding, design, systemization, implementation, verification, or writing.
2. Identify the primary domain: development, UI, writing, or mixed.
3. Check whether implementation is blocked by unresolved critical decisions.
4. Select one primary skill and the smallest plausible downstream set.
5. Read only those selected `SKILL.md` files.
6. Re-route if the task changes stage or a selected skill reaches a stop condition.

## Development default

For a new software project or materially new feature, default to `development/development-discovery` when product behavior or system semantics are not sufficiently defined.

If the existing codebase must be understood to resolve the decision, add `development/learn-codebase` but constrain it to the relevant subsystem.

Do not use implementation as a way to discover what the product should do.

## Output

Return a compact internal or user-visible route when useful:

```text
Primary skill: development-discovery
Then: learn-codebase -> ui/product-ui-discovery -> ui/ui-implementer
Reason: feature behavior is unresolved and the existing session model must be understood first.
```

Avoid ceremonial routing output when the next skill can simply be invoked. The purpose of this skill is context control and correct sequencing, not extra process.
