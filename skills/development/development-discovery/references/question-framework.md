# Guided decision framework

Inspect first. Use this checklist privately; surface only the next high-impact
unknown. Do not ask the user to restate known facts or choose arbitrary tools.

| Dimension | Look for | Example consequence |
| --- | --- | --- |
| Outcome | User problem and observable success | A monitoring app is not a full remote IDE |
| Actor and trigger | Who initiates, executes and approves | Phone user and desktop executor have different permissions |
| Core flow | Entry, primary action and completion | Sending a message might create a task or steer an existing one |
| Scope | MVP, non-goals and unchanged behavior | Adding attachments need not introduce a new storage platform |
| State and data | Owner, persistence, lifetime, synchronization | A disconnected phone must not accidentally cancel a desktop task |
| Safety | Trust, roles, consent, destructive or paid actions | Tool approval cannot be inferred from viewing a message |
| Failure | Offline, timeout, retry, cancellation, duplicates, conflicts | An uncertain ACK must not trigger duplicate side effects |
| Acceptance | Observable examples and regression boundaries | A spinner disappearing is not proof a task completed |
| UI when relevant | Entry points, hierarchy, content, states, input and platform | An interrupt action needs explicit semantics before a button |

## Turn shape

Use the developer's language. One useful format is:

```text
我理解本次要实现 X，已有的 A/B 决定会保留。
还缺一个会影响实现的决定：在 Y 情况下，用户应该看到什么行为？
方案 A：...；代价是 ...。
方案 B：...；代价是 ...。
基于你强调的 Z，我建议 B。
你希望采用哪一种，还是有其他行为？
```

Do not fabricate options for a requirement with only one viable implementation.
Explain the constraint and ask about the relevant product trade-off instead.

## Example: a message arrives while an agent is running

First inspect whether the existing runtime supports queueing, cancellation or
steering. Then explain these as user-visible choices, not API names:

- Queue: finish the current task, then handle the next message.
- Interrupt: attempt to stop the current task, then start the next one. Decide
  what happens when a tool cannot be cancelled or has already had side effects.
- Steer: incorporate the message into the current task, only if supported by
  the runtime. Do not promise steering through a new UI alone.

A possible recommendation is queue-by-default plus explicit interrupt, but it
is not a universal requirement. Tie it to the actual workflow and supported
protocol. Follow up with persistence/offline behavior only after this decision.

## Unknown versus optional

Critical: changing the answer changes public behavior, core architecture,
ownership, trust, destructive effects, interface contract or acceptance.
Reversible: internal naming, a token already prescribed by the design system,
or an implementation detail that preserves agreed behavior.

Record reversible defaults and continue after authorized scope is ready. Do
not seek approval for every pixel or internal function name. Keep incompatible
choices open rather than silently choosing the easiest one to implement.
