# Decision discovery

Inspect evidence first. Select the next question by its impact on the design,
not by this table's order. Never send the entire checklist as an interview.

| Area | Find or elicit | Example decision impact |
| --- | --- | --- |
| Outcome | User, situation, success and non-goals | Read progress versus remotely control execution |
| Workflow | Trigger, successful path, alternatives | A new message queues, interrupts, or starts another run |
| Boundaries | MVP, excluded work, target platforms | Mobile is a controller, not an execution host |
| State/data | Owner, durability, lifecycle, source of truth | Reconnection must restore a run, not replay its writes |
| Contracts | Existing APIs, validation, events, compatibility | A design cannot assume an unsupported server operation |
| Authority | Authentication, approvals, private data, destructive acts | Tool approval and ordinary chat must be distinguishable |
| Failure | Offline, timeouts, cancellation, duplicates, partial success | Retry a read differs from replaying a tool execution |
| Acceptance | Observable behavior and verification environment | An ACK proves delivery, not task completion |

## Question pattern

Use the developer's language and present a concrete scenario:

> 我理解这次是给现有聊天页增加附件，继续沿用现有主题和登录。
> 目前没有确认附件只在当前设备可见，还是另一台设备也要读取；
> 这会决定是否需要上传和跨端授权。A 是仅本地预览，B 是上传后同步。
> 如果目标是跨端继续同一会话，我建议 B。首版需要跨端读取附件吗？

Do not ask them to choose a database before deciding whether persistence is
needed. Do not invent knowledge of their repository to make a recommendation.

## When the developer says "I don't know"

Translate the choice into observed behavior, compare cost/complexity/risk under
their constraints, and recommend a default. If uncertainty is technical, name
a cheap test that can resolve it and ask for a bounded spike only when needed.
An unsure answer is not consent to your preferred option.

## Decision ledger

Track only useful entries:

| Decision | Status | Source / rationale | Consequence / next action |
| --- | --- | --- | --- |
| Example new-message behavior | proposed, not approved | Existing protocol lacks steering | Recommend queue; ask developer |

Statuses: observed, confirmed, proposed, delegated, unresolved, superseded.
Keep fact, preference, inference, and authorization distinct. On a requirement
change, supersede the old decision and identify affected acceptance criteria.

## Proportionality

A typo fix may need one line of scope and a test. A cross-device execution flow
needs explicit ownership, failure and authorization semantics. A new design
system is not a prerequisite for every new button. Unavailable screenshots mean
visual acceptance is not verified, even when static checks succeed.
