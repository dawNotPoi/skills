---
name: visual-qa-critic
description: Review rendered UI against requirements and record reproducible visual, responsive, accessibility, content, and interaction defects. Use for 视觉验收、检查界面 and pre-release UI review. Do not redesign by taste, claim unavailable runtime evidence, or edit code without explicit authorization.
---

# Visual QA / Critic

Evaluate observable UI quality against stated intent and produce actionable
findings. Review only by default.

## Inputs

Use the rendered UI and strongest available baseline: accepted specification,
screens, design-system contract, acceptance criteria or established conventions.
Record target project/ref, viewport, platform, theme, content and state.

If the baseline has an unresolved behavior decision, report that ambiguity;
do not invent an expected result to make a test pass. Route the decision to the
appropriate discovery capability. Missing peers do not prevent reporting the
gap. Missing render tools permit only a clearly labeled static review, not a
claim that visual acceptance passed.

## Workflow

1. Distinguish requirement violations from optional improvements.
2. Exercise relevant viewports, interactions, content, loading, empty, error,
   validation, disabled, focus, hover and success states.
3. Inspect hierarchy, spacing, typography, color, contrast, imagery, clipping,
   density, responsive behavior, affordances, feedback and keyboard paths.
4. Capture reproducible evidence. Screenshots cover visual states; animation,
   streaming or transitions require interaction/recording evidence when tested.
5. Prioritize user impact and confidence. Separate blockers, polish, subjective
   preferences and untested areas.

Do not report pixel differences without explaining their consequence. Visual
inspection alone does not prove accessibility conformance. State the exact
checks performed. Do not call the review independent merely because the same
agent changed roles.

## Output: QA Report

Give confidence scoped to the evidence and a test matrix. Each finding includes
severity, location/state, reproduction, observed versus expected behavior,
impact, evidence, a bounded recommendation and confidence.

End with passed checks, not-verified checks and outstanding decisions. Preserve
spec revision and authorization in handoff. When fixes are also authorized,
hand confirmed issues to `ui-implementer`, which still runs its readiness gate,
and retest changed states. Review alone never authorizes fixes or release.
