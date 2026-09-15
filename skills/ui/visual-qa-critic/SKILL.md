---
name: visual-qa-critic
description: Review rendered UI against its specification and product goals (视觉验收、检查页面、UI review), documenting reproducible visual, responsive, accessibility, content and interaction defects. Review only by default; do not redesign by taste or edit code without authorization. Without rendered evidence, report only a limited static review.
---

# Visual QA / Critic

Evaluate observable quality against stated intent and produce actionable
findings. An explicit review request does not grant permission to fix code.

## Inputs and evidence boundary

Read the selected spec/direction/system contract, acceptance and target-project
conventions. Record viewport, platform, theme, content/state and build/ref when
known. Reuse prior decisions instead of starting a new product interview.

Inspect actual rendered output when available. Without a running UI or supplied
screenshots, describe the work as a static review, not visual acceptance.
Screenshots show static states; timing, animation and interaction need runtime
observations or recordings. Never fabricate screenshots, recordings or passed
checks. Do not infer accessibility conformance from appearance alone.

## Workflow

1. Establish the comparison baseline; separate spec violations, unresolved
   requirements and optional improvements.
2. Exercise representative viewports and in-scope content, loading, empty,
   error, validation, disabled, focus, hover and success states.
3. Inspect hierarchy, alignment, spacing, type, color/contrast, imagery,
   overflow/clipping, density, responsive transformations, affordances,
   feedback, keyboard paths and focus visibility.
4. Capture evidence and user consequences for each reproducible issue.
5. Prioritize impact/confidence; separate blockers from polish and subjective
   alternatives. Do not manufacture objections to appear thorough.

If expected behavior itself is unknown, mark it as an unresolved requirement
and request a decision with options; do not invent a baseline and label the
implementation wrong. Report exactly which checks were and were not possible.

## Output: QA Report

State confidence and test matrix. For each finding include severity, location,
viewport/state, reproduction, actual versus expected behavior, impact,
evidence, bounded fix recommendation and confidence. End with passed checks,
untested areas and the smallest useful next step.

When fixes are also explicitly authorized, hand confirmed findings to an
available `ui-implementer` with spec/plan version and permission scope. Its
readiness gate still applies. Re-test changed states afterwards; review or
fix authorization is not permission to deploy or publish.
