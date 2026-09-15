---
name: development-discovery
description: Guide new projects and materially new features from incomplete requirements to decisions, a spec, and an implementation plan. Use for 新项目、新功能、先讨论需求 and unresolved workflow, scope, state, API, permission, failure, or acceptance decisions. Do not write product code while critical gaps remain or turn clear small edits into an interview.
---

# Development Discovery

Help the developer decide what to build, not merely answer a questionnaire.
The default output is an implementable proposal, not production code.

## Read first

Identify the target project separately from the skill library. Read the current
conversation, project instructions, relevant documentation, nearby code, API
contracts, and tests before asking. Reuse decisions already made and cite the
artifact or symbol that establishes them. Do not invent repository facts or
repeat questions whose answers are available.

For a new project, establish the user, outcome, core workflow, platform, system
boundaries, and MVP. For an existing feature, inspect the narrow affected path,
existing behavior, integration contracts, and compatibility requirements first.
Do not ask the developer which framework is in a readable manifest.

## Triage missing information

Use [the decision framework](references/decision-framework.md) as an internal
checklist, not a form to send wholesale.

- **Critical decision:** changes the user's outcome, observable behavior,
  scope, state/data ownership, public contract, privacy, permissions, destructive
  actions, cost-bearing side effects, or acceptance. Do not silently guess it.
- **Evidence gap:** a fact discoverable from code/docs/tests. Investigate it.
  If inaccessible, state the limitation and whether it blocks the decision.
- **Reversible detail:** naming, token reuse, or a local implementation choice
  that does not change the above. Follow project conventions and record a
  material default; do not ask about every pixel or variable.

While blocked, reading, analysis, and drafting a proposal are allowed. Do not
scaffold the application, add dependencies, change production code or schemas,
or call write-capable services to commit an unresolved product decision.
A technical spike requires a separately agreed question, scope, and isolated
location. A successful spike is evidence, not permission to ship the feature.

## Guided conversation

Each turn should do the following, proportionally:

1. State the current understanding and reuse confirmed requirements.
2. Identify the highest-impact unresolved decision and why it affects behavior.
3. Offer two or three meaningful options, including trade-offs and a recommended
   default when evidence supports one. Ask in user-visible scenarios, not only
   infrastructure jargon.
4. Ask one primary question; use at most three tightly related questions when
   they are genuinely coupled. Wait for the developer's answer before resolving
   critical choices. Never treat silence as approval.
5. Update confirmed decisions, proposed defaults, open questions, and the next
   step. If the developer does not know, explain through an example or recommend
   a bounded experiment; do not repeat "please confirm" without helping.

For example, "运行中的 Agent 收到新消息" needs a behavior decision: queue it,
interrupt the run, steer the current run, or start a parallel session. Explain
what the user will observe and what the existing protocol supports before
recommending a default. Do not encode a guessed answer in an event handler.

## Readiness gate

This is an instruction-level protocol, not a tool-enforced security barrier.
No numeric readiness score is needed.

| Stage | Allowed next work | Exit condition |
| --- | --- | --- |
| BLOCKED | Investigate evidence and guide decisions | No critical unresolved product decisions |
| READY_FOR_SPEC | Draft requirements and technical alternatives | Behavior, scope, boundaries, failure semantics and acceptance are concrete |
| READY_FOR_PLAN | Inspect implementation impact and decompose work | Spec is accepted or explicitly delegated; technical blockers are resolved |
| READY_TO_IMPLEMENT | Hand off approved scope to an implementer | Current spec/plan, no critical blockers, and traceable implementation authorization |

The stage is descriptive. Inspect code and draft partial specs at any stage;
never fabricate completeness to advance the label. "Implementation authorized"
and "requirements understood" are separate facts. Acceptance of a design alone
is not permission to edit files.

For substantial work, show the spec and bounded plan and ask for implementation
approval if it is not already provided. Record the actual conversation/review
source and scope. "Looks good" confirms a design unless the surrounding request
clearly authorizes implementation; "continue" preserves the current mode.

## Fast path and delegation

When a small task has clear behavior, scope, acceptance, and explicit permission
to implement, summarize those in a few lines and hand off immediately. Do not
require separate documents or another approval for an already authorized edit.
A detailed approved spec may be reused; do not recreate it to satisfy a template.

"You decide" may delegate ordinary product or technical choices. Make the
chosen defaults and consequences explicit and record the delegation. It does
not authorize data deletion, secret access, deployment, spending, or relaxed
permissions outside the user's scope. "Don't ask questions" is not evidence of
missing requirements; make safe progress on analysis/proposals and disclose
unresolved critical decisions rather than concealing them in code.

## Produce durable artifacts

Use existing project paths and formats. For substantial work without an existing
convention, propose `docs/specs/<feature>.md` and `docs/plans/<feature>.md` inside
the target project. Write them only when file changes are authorized; otherwise
present the content in the conversation. A filename is not proof of approval.

Read the relevant template when needed:

- [Feature specification](templates/feature-spec.md): what, for whom, behavior,
  non-goals, contracts, risk, decisions, and observable acceptance.
- [Implementation plan](templates/implementation-plan.md): repository evidence,
  change boundaries, ordered tasks, tests, rollback, and verification limits.

Keep requirements separate from execution steps. A technical plan must use
verified paths, not invented filenames presented as existing files. Label new
paths explicitly. Each task maps back to an acceptance criterion.

## Handoff and feedback

For UI work, hand confirmed product behavior to `product-ui-discovery`, then
use only necessary direction/system/implementation/review skills. For non-UI
work, hand off to the host's actual engineering capabilities; this library does
not supply a generic backend executor. Peer skills are optional, not assumed.

If implementation reveals a critical gap or contradiction, pause the affected
work, preserve completed changes, return to the decision, and revise the spec.
Do not invent a server capability, silently alter scope, or restart discovery
from scratch. Reopen approval only for materially changed scope or risk.

After verification, record actual deviations and unverified behavior. Propose
only stable, general project invariants for the project's `AGENTS.md`; keep
feature details in its spec/plan. Obtain authorization before changing project
instructions. Never write project-specific details into this skill library.
