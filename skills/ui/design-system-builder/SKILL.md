---
name: design-system-builder
description: Create or evolve reusable semantic tokens, theme mappings, component contracts, states and accessibility rules from approved direction and demonstrated needs (主题色、设计系统、组件规范). Use for consistency and reuse, not speculative catalogs. Code-producing work requires a clear contract and implementation authorization; do not redefine product behavior.
---

# Design System Builder

Turn repeated UI decisions into a maintainable system without abstracting
beyond demonstrated needs.

## Inputs and implementation gate

Read target instructions, the selected direction, existing tokens/components,
framework, supported platforms, accessibility target and affected screens.
Preserve compatible conventions; do not re-interview the user about decisions
already established upstream.

Specifying tokens is not the same as permission to modify shared code. Before
code-producing work, resolve material behavior/direction/compatibility gaps,
identify acceptance and a bounded plan, and verify authorization for this scope.
Existing explicit approval counts. If a critical choice is missing, stop the
affected coding and return the named decision to discovery/direction with
options and a recommendation. Do not silently pick a breaking component API.

## Workflow

1. Audit primitives, components, duplication and exceptions in actual screens.
2. Define semantic color, typography, spacing, size, radius, border, elevation,
   motion and responsive roles. Separate raw values and semantic mappings where
   useful. Keep product colors in the token layer; document justified exceptions
   such as user content, external brand artwork or data-driven visualization.
3. Prioritize components proven by the current scope. Define anatomy, variants,
   states, behavior, content constraints, accessibility and composition.
4. Specify theming and extension points without arbitrary styling knobs that
   defeat consistency. Validate theme/state combinations as applicable.
5. Plan migration, compatibility, ownership and validation proportionally.
   Do not force unrelated interactions into one abstraction.

## Output: Design-System Contract

Provide token taxonomy/mappings, prioritized components, their state/behavior
contracts, theme/responsive/content rules, target-screen coverage, migration,
known exceptions and unresolved decisions. Preserve target/ref, selected
version, implementation authorization and acceptance checks at handoff.

When authorized to code, implement primitives and examples, not unrelated
product flows. Report checks actually run and rendering limitations. Leave
screen assembly to `ui-implementer`; use `visual-qa-critic` for conformance
review when appropriate. A passing token test is not a visual acceptance pass.
