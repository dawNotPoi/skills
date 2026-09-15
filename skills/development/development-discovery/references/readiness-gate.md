# Readiness gate

This is an agent workflow contract, not a runtime permission system. Host and
project restrictions still apply. Do not claim a Markdown file can technically
prevent tool execution.

| Status | Meaning | Allowed next work |
| --- | --- | --- |
| DISCOVERY | Critical decisions are unresolved or evidence is insufficient | Read, compare options, ask focused questions, draft proposals |
| PROPOSAL | The behavior is specified and a plan can be reviewed; authorization may still be absent | Refine spec/plan and request only missing approval |
| READY_TO_IMPLEMENT | The current scope meets every check below and is authorized | Hand off to implementation within that scope |
| BLOCKED | Access, capability, dependency or a contradictory constraint prevents progress | Explain the blocker and provide the smallest decision/unblock action |

`READY_TO_IMPLEMENT` requires:

- The goal, actor, core behavior, scope and non-goals are known.
- Relevant state/data ownership, permission boundaries, failure/retry/offline
  and compatibility behavior are resolved or explicitly out of scope.
- Acceptance is observable; the relevant verification method is identified.
- The plan is grounded in the repository or explicitly identifies a new
  project's proposed structure. No critical decisions are hidden in tasks.
- The user has authorized implementation of this version/scope, or explicitly
  delegated those decisions and authorized execution. Record the message or
  referenced artifact; never generate a fictitious 'approved' status yourself.

## Approval is scoped

A brief '按这个方案实现' can be sufficient after a specific proposal. A previous
request to implement an already complete specification also counts. Do not
require a magic phrase or another confirmation for the same approved scope.
A choice of color, a draft document, '继续讨论', silence, or an agent's preferred
option alone does not authorize production work. '继续' resumes the current
stage unless the preceding context clearly authorizes the named next action.

If the user asks for no questions, provide a best-effort proposal with explicit
defaults. Keep material unresolved decisions visible and do not disguise a
prototype as approved production behavior. Explicitly delegated, reversible
choices can be settled by the agent; separate action permissions still apply.

## Proportionality and change control

A clear, low-risk correction can use a short inline spec/plan and existing
approval. Do not create three documents to change one known label. A new
project or material feature gets a reviewable spec and plan.

A newly discovered constraint pauses only affected work. Record the old
assumption, evidence, proposed behavior change, acceptance impact and approval
needed. Other independent, already authorized work may proceed. An isolated
POC needs a goal, boundary, permitted changes, success criterion and disposal
or integration decision; POC approval is not production approval.

On context loss, restore spec/plan version, decisions, approval source,
open issues and evidence before acting. If no reliable record exists, state
what is missing rather than reconstructing approval from memory.
