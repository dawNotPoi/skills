---
name: ui-implementer
description: Implement an approved and sufficiently specified interface in a target codebase (实现页面、修改 UI、按设计开发), preserving responsive behavior, accessibility and agreed states. Check readiness before editing; stop for critical missing product decisions and guide clarification instead of guessing in code. Do not redesign, deploy or publish without authorization.
---

# UI Implementer

Build the specified experience and provide evidence that important behavior
works. This gate applies even when this skill is invoked directly.

## Before editing

Resolve the target project, read its instructions, current conversation,
existing architecture/design system/assets, relevant paths/tests and approved
specification. Preserve the library/project boundary and existing user edits.

Verify that scope, core behavior, relevant state/data ownership, permissions,
failure semantics, UI direction and observable acceptance are sufficiently
specified. Identify a bounded plan and authorization for the current scope.
A supplied mockup does not settle unspecified interactions or data contracts.
Reuse approval already given; a precise low-risk change needs only a compact
inline behavior/change/check note, not another full discovery cycle.

**If a critical requirement is missing, do not modify the affected code.**
State known facts, the exact missing decision, alternatives and a recommendation.
Use an available `development-discovery` for product/system choices or
`product-ui-discovery` for interface flows. If unavailable, guide the choice
locally and disclose that no skill was loaded. Do not leave a critical product
decision as a TODO after implementing an assumed behavior.

## Workflow

1. Trace relevant routes, components, styles, data boundaries and tests.
2. Plan the smallest coherent change. Reuse existing patterns and semantic
   tokens; introduce abstractions only when repetition or ownership warrants it.
3. Implement the agreed structure, content, responsive layout, interaction,
   keyboard/focus behavior, validation and in-scope states.
4. Use verified assets and contracts. Do not disguise missing behavior with
   decorative controls or fabricated production data. Label fixture-only POCs.
5. If a new constraint changes behavior, record its evidence and pause affected
   work for a decision. Do not quietly redefine the approved spec.
6. Run relevant checks and inspect rendered output across representative states
   and viewports when tools permit. Temporal behavior requires interaction
   evidence or recording; screenshots alone do not prove it.

Dependencies, architecture changes and shared-system edits require a concrete
need within authorized scope. An approved isolated POC is not production
approval. Do not treat a successful build as a visual pass.

## Output and write-back

Map acceptance criteria to changes and checks. Include checks/results actually
observed, screenshots or previews when available, untested states, limitations,
and approved deviations. Preserve spec/plan version and evidence so another
session can resume. Record feature-specific deviations in target-project docs;
propose stable general rules separately rather than silently editing AGENTS.md.

Use `visual-qa-critic` for a separate review when appropriate and available.
If no renderer exists, mark visual verification incomplete. Implementation
permission does not authorize deployment, publishing or unrelated repository
changes. Do not claim 'done' while critical acceptance remains unresolved.
