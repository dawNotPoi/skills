---
name: ui-implementer
description: Implement an approved UI direction or specification in an existing or new codebase, including responsive behavior, interaction states, accessibility, and verification. Use when the user asks to build or modify an interface and the relevant product/UI decisions are sufficiently resolved. Do not silently change product requirements, substitute a new visual direction, or resolve critical product decisions in code.
---

# UI Implementer

Build the specified experience faithfully in the target environment and prove that its important behavior works.

## Inputs

Inspect the repository instructions, existing architecture, design system, assets, UI specification, supported viewports, and acceptance criteria. Reuse the project's components and conventions when they satisfy the specification.

Before editing, check whether any unresolved choice would materially change:

- user-visible behavior;
- state or system ownership;
- API/protocol/data shape;
- permissions or security;
- failure, retry, interruption, or concurrency semantics;
- acceptance criteria;
- the approved visual direction.

If such a critical gap exists, stop implementation and return to `development/development-discovery` (or `ui/product-ui-discovery` when the unknown is purely UI workflow). Never resolve a product decision implicitly in code.

Non-critical implementation details may be handled as explicit assumptions when they can be changed locally without altering the product contract.

## Workflow

1. Trace the relevant routes, components, styles, data boundaries, and tests before editing.
2. Confirm the task is implementation-ready; if a critical decision is missing, route back to discovery instead of guessing.
3. Plan the smallest coherent change. Separate reusable primitives only when actual repetition or ownership boundaries justify it.
4. Implement semantic structure, content hierarchy, responsive layout, interactions, keyboard behavior, focus, validation, and loading, empty, error, disabled, and success states in scope.
5. Use real assets and data contracts when available. Do not disguise missing behavior with decorative mock controls or fabricate production data.
6. Verify the changed UI at representative viewport sizes and interaction states. Run relevant automated checks and inspect rendered output when the environment supports it.
7. Compare the implementation with the approved specification and record material deviations instead of silently rewriting the requirement.

Follow established framework and styling choices. Adding a dependency, rewriting architecture, or changing a shared system requires a concrete need within the requested scope.

## Output

Provide:

- the working implementation;
- a concise mapping from specification or acceptance criteria to changed behavior;
- checks performed and their results;
- screenshots or preview references when useful;
- material implementation deviations and their reasons;
- remaining non-critical assumptions and any follow-up that needs a product or design decision.

Implementation does not authorize deployment, publishing, or unrelated repository changes. Use `visual-qa-critic` for a separate visual review when fidelity is central to acceptance.
