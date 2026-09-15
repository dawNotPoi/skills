---
name: ui-implementer
description: Implement clear, authorized UI changes in new or existing codebases with responsive behavior, states, accessibility, and verification. Use for 实现页面 and approved interface changes. Check readiness even on direct invocation; stop on critical missing product decisions rather than resolving them in code.
---

# UI Implementer

Build the specified experience faithfully and prove its important behavior.

## Readiness before writes

Read the conversation, target-project instructions, relevant routes/components,
contracts, tests, design direction and acceptance criteria before editing.
Keep the skill-library root separate from the target project.

Implementation requires clear outcome, scope, important behavior and failure
semantics, constraints, observable acceptance and explicit authorization. Reuse
an existing approved spec/plan; for a clear small fix an inline summary suffices.
Do not require paperwork or another approval for an already authorized edit.

If a critical requirement is missing, pause the affected implementation. Do not
scaffold files, add dependencies or encode a guess. Use `development-discovery`
for product/system decisions or `product-ui-discovery` for UI-flow decisions.
If unavailable, identify the unknown, explain its impact, offer alternatives
and a recommendation, ask one focused question, and wait. Do not present a
proposed default or agent-written approval field as user confirmation.

Reversible details may follow the existing system. New persistence, permission,
API, destructive or cost-bearing behavior is not a reversible styling detail.
A proposal/review request is not implementation permission.

## Workflow

1. Trace related code, data boundaries and tests; plan the smallest coherent
   change. Mark proposed-new paths separately from verified existing files.
2. Implement semantic structure, hierarchy, responsive layout, keyboard/focus,
   validation and relevant loading/empty/error/disabled/success states.
3. Reuse actual components and semantic tokens. Do not silently introduce a
   new brand, arbitrary color system, or near-duplicate component catalog.
4. Use real data contracts and assets. Explicitly label mocks and prototypes;
   never disguise unsupported behavior behind decorative controls.
5. Run relevant checks and inspect rendered output when tools allow. Temporal
   behavior needs interaction/recording evidence, not only a screenshot.
6. Compare results to acceptance criteria. A passing build is not UI acceptance.

Adding a dependency, replacing shared architecture or migrating a public
contract must be justified within scope. If new evidence invalidates a critical
decision, stop affected work and reopen only that decision; preserve user edits.

## Output and handoff

Report changed behavior and acceptance mapping, checks actually run, visual or
interaction evidence, spec deviations, and unverified areas. Do not describe
an unavailable simulator/browser as having passed acceptance.

Use `visual-qa-critic` for a separate review when requested or when fidelity is
central. If unavailable, report the limitation. A separate review pass is not
proof of an independent agent or a guarantee against shared errors.

Implementation does not authorize deployment, publication, unrelated changes,
or overwriting project instructions. Propose durable rule updates separately.
