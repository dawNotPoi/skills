---
name: design-system-builder
description: Create or evolve semantic tokens, component contracts, states, accessibility rules, and governance from an accepted UI direction. Use for 主题、设计系统、组件规范 and demonstrated consistency needs. Do not redefine product behavior or implement system code without authorization.
---

# Design System Builder

Turn repeated UI decisions into a maintainable system without abstracting
beyond demonstrated product needs.

## Inputs and gate

Read the accepted direction, relevant project rules, existing tokens/components,
target framework/platforms, accessibility needs, and target screens. Preserve
compatible conventions unless the requested change justifies migration.

Missing branding direction or product behavior is not permission to invent it.
Return to the relevant discovery/direction skill when available; otherwise
explain the gap, offer options and ask the decision owner. Drafting a contract
is allowed; editing shared primitives requires clear scope and implementation
authorization. Existing explicit authorization need not be requested again.

## Workflow

1. Audit existing primitives, repeated patterns and exceptions.
2. Define semantic color, typography, spacing, size, radius, border, elevation,
   motion and responsive roles. Separate raw values and semantic mappings where
   theming or change benefits. Prefer native semantic colors when appropriate.
3. Prioritize components proven by real target screens. Specify anatomy,
   variants, states, behavior, content, accessibility and composition.
4. Define theme/extension boundaries without arbitrary style knobs that defeat
   consistency. Product components should consume semantic tokens; exceptional
   raw values need a documented reason, not an indiscriminate ban on asset data.
5. Plan proportional migration, compatibility, deprecation and verification.
   Check affected consumers before changing a shared contract.

Avoid speculative component catalogs and do not force unlike interactions into
one abstraction. A new screen does not automatically need a new design system.

## Output: Design-System Contract

Include semantic mappings, proven component inventory/contracts, theme and
responsive behavior, content/composition rules, screen coverage, migration,
exceptions and validation. Preserve accepted scope and decision sources.

When code is authorized, implement only system primitives and examples in
scope. Leave application flows to `ui-implementer`. Run available contract,
contrast and consumer checks; rendered review belongs to `visual-qa-critic`
when available. Report anything not actually verified.
