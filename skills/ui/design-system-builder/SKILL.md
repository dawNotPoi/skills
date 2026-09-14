---
name: design-system-builder
description: Create or evolve a reusable UI system of tokens, component contracts, states, accessibility rules, and governance from an approved direction and real product needs. Use when multiple screens or teams need consistency and reuse. Do not redefine product requirements, invent an unrelated visual direction, or implement whole product screens.
---

# Design System Builder

Turn repeated UI decisions into a maintainable system without abstracting
beyond demonstrated product needs.

## Inputs

Inspect the approved direction, existing tokens and components, target
framework, supported platforms, browser matrix, accessibility target, and the
screens or flows the system must serve. Preserve compatible conventions unless
there is evidence that migration is worth its cost.

## Workflow

1. Audit existing primitives, components, duplicated patterns, and exceptions.
2. Define semantic foundations: color, typography, spacing, size, radius,
   border, elevation, motion, and responsive rules. Separate raw values from
   semantic roles where that distinction enables themes or change.
3. Prioritize components proven by target screens. For each, define anatomy,
   variants, states, behavior, content constraints, accessibility semantics,
   and composition rules.
4. Specify theming and extension points without exposing arbitrary styling
   knobs that undermine consistency.
5. Provide migration and governance guidance proportional to the system's
   scale, including ownership, compatibility, deprecation, and validation.

Avoid speculative component catalogs. Prefer composition over near-duplicate
variants, but do not force unlike interactions into one abstraction.

## Output: Design-System Contract

Deliver the artifacts appropriate to the request:

- token taxonomy and semantic mappings;
- prioritized component inventory;
- component contracts with variants, states, behavior, and accessibility;
- responsive, theme, content, and composition rules;
- mapping from target screens to system coverage;
- migration plan, known exceptions, and governance decisions.

When code is requested, implement system primitives and component examples,
not unrelated application flows. Leave product-screen assembly to
`ui-implementer` and independent conformance review to `visual-qa-critic`.
