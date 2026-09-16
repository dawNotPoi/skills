---
name: interactive-learning
description: Teach a topic interactively without losing the original learning path by maintaining an explicit roadmap, current node, question branches, return points, parking lot, and periodic understanding checks. Use when the user wants to learn through dialogue, asks follow-up questions mid-lesson, or needs a long topic taught incrementally instead of receiving a one-shot tutorial.
---

# Interactive Learning

Teach for durable understanding while preserving the learner's place in the curriculum.

The central problem this skill solves is conversational drift:

```text
roadmap: A -> B -> C -> D
           |
           +-> question -> deeper question -> another branch
```

A useful teaching session must answer the branch without forgetting that the learner was originally at `A` and should later return to `B`.

The unit of progress is therefore:

`learning goal -> roadmap -> current node -> branch -> return point -> verified understanding -> next node`

Do not replace this with a long tutorial dump.

## When To Use

Use this skill when the user:

- says "teach me", "带我学", "一步一步学", or asks for interactive learning;
- is learning a topic through repeated questions and corrections;
- wants a large subject broken into a stable sequence;
- often interrupts a lesson with questions about the current point;
- wants to resume a prior learning thread without restarting from the beginning.

Do not force this mode when the user only wants:

- a direct factual answer;
- a complete reference document or report;
- a one-shot summary;
- a finished artifact rather than a learning process.

If another specialist skill owns the subject matter, combine them rather than replacing it. For example, `learn-codebase` owns repository-specific investigation and evidence rules; this skill can own pacing, branch handling, return points, and progress state.

## Core Learning State

Maintain this state conceptually throughout the session:

```text
Goal:
Roadmap:
Current node:
Current question branch:
Return point:
Branch stack:
Parking lot:
What the learner has demonstrated:
Open misconceptions or gaps:
Next checkpoint:
```

The state may live only in conversation. Do not create files unless the user asks for a persistent artifact or the host workflow already requires one.

Do not print the full state on every turn. Surface only the parts that help orientation, especially when entering or leaving a branch, completing a node, resuming after a long detour, or when the learner asks to see the map.

Use `templates/learning-state.md` when a persistent or visible state card is useful.

## Workflow

### 1. Establish the learning goal

Infer the goal and current level from the conversation before asking questions the user has already answered.

Determine:

- what the learner ultimately wants to be able to explain, predict, build, debug, or decide;
- what they already understand;
- what prerequisite gaps materially block the next step;
- whether they prefer explanation, active recall, exercises, source reading, or a mix.

Do not begin with a generic questionnaire when the current conversation already provides enough evidence.

### 2. Build a compact roadmap before deep explanation

Create a small map of the subject before teaching it in detail.

Prefer roughly 4-8 major nodes. A node should represent a meaningful concept or capability, not every subtopic that might ever arise.

Example:

```text
Goal: understand how an Agent executes work

1. Message and instruction roles
2. Context construction
3. Agent loop
4. Tool calling
5. State and memory
6. Multi-agent delegation

Current: 1. Message and instruction roles
```

The roadmap is a navigation structure, not a promise to teach every node exhaustively. Revise it when genuine new evidence changes the learning dependency graph.

### 3. Teach one node at a time

For the current node:

1. explain the minimum model needed to reason about it;
2. use a concrete example when useful;
3. invite the learner's question or ask one meaningful check;
4. respond to the answer precisely;
5. deepen only where the learner's uncertainty requires it;
6. mark the node complete only after there is evidence of adequate understanding.

Do not automatically continue through several major nodes in one response just because they are already on the roadmap.

### 4. Treat follow-up questions as branches, not a new curriculum

A learner's follow-up question normally belongs to the current node.

Before answering a branch, preserve its return point conceptually:

```text
Main path: 3. Agent loop > Planner vs Executor
Branch: Why can Planner not execute tools directly?
Return point: 3. Agent loop > Planner vs Executor
```

Answer the branch fully enough to resolve the actual confusion.

A question can create another nested question. Maintain this like a call stack:

```text
Main node
  -> branch A
       -> branch A1
       <- return to A
  <- return to main node
```

When the branch is resolved, explicitly restore orientation if the detour was non-trivial:

```text
这个问题已经解决。回到刚才的主线：3. Agent loop > Planner vs Executor。
```

Then continue from the saved return point rather than generating a new lesson outline.

### 5. Use a parking lot for valuable but non-blocking detours

Some questions are useful but would substantially expand the current node.

If the question is not required to understand the present node, place it in the parking lot and keep moving unless the learner explicitly wants to explore it now.

Example:

```text
Parking lot:
- MCP vs CLI
- How sandbox permissions affect tool execution
```

Do not use the parking lot to evade a question that actually blocks understanding.

If the learner says "先把这个搞懂", promote the parked item into a branch and save the current return point.

### 6. Make navigation commands cheap

Interpret short steering phrases naturally:

- `继续` / `继续主线`: resume from the current return point or next roadmap node;
- `先解决这个`: enter or deepen the current branch;
- `放停车场`: defer the issue without losing it;
- `回到上一层`: pop one branch level;
- `跳过`: mark the node intentionally skipped, not understood;
- `复盘`: test recent understanding rather than repeating the same explanation;
- `显示地图`: show the current roadmap, branch, progress, and parking lot.

Do not require the learner to use exact commands. Infer equivalent intent from natural language.

### 7. Verify understanding with active recall

A learner saying "懂了" is useful but weak evidence. Periodically ask for a prediction, explanation, comparison, or application.

Prefer questions such as:

- "用你自己的话说，Planner 和 Executor 的边界是什么？"
- "如果 tool call 失败两次，你觉得 retry 应该属于哪一层？为什么？"
- "如果删除这层状态，哪个行为会先出错？"
- "给你一个新例子，你会把它归到哪个概念？"

After the answer:

1. preserve what is correct;
2. identify the exact gap;
3. explain only the missing causal link;
4. ask the next question at an appropriate difficulty.

Do not turn every turn into a quiz. Use checks at meaningful boundaries.

### 8. Create checkpoints after meaningful progress

After roughly 2-4 major nodes, after a long branch, or before switching to a new conceptual layer, create a compact checkpoint.

A checkpoint should contain only what helps resume:

```text
Completed:
- 1. Roles
- 2. Context

Current:
- 3. Agent loop > Planner

Learner can already explain:
- why Developer and User instructions differ
- how context reaches the model

Still open:
- Planner vs Executor boundary

Parking lot:
- MCP vs CLI

Next:
- finish Planner, then Tool Calling
```

Do not restate the entire lesson.

### 9. Recover from conversational drift

If the dialogue has wandered far from the roadmap:

1. identify the last reliable current node from conversation evidence;
2. summarize what the branch resolved;
3. restore the most likely return point;
4. show the compact roadmap if orientation is no longer obvious;
5. continue from there.

Do not silently invent completed nodes.

If the exact previous state cannot be recovered, state the uncertainty briefly and rebuild the smallest reliable map from available context instead of restarting the whole subject.

### 10. Adapt the roadmap when understanding changes

The initial roadmap is not sacred.

Split a node when it hides an important dependency. Merge or skip nodes that the learner already understands. Add a prerequisite only when it genuinely blocks progress.

When changing the roadmap, explain the structural reason briefly:

```text
我把原来的 Tool Calling 拆成“协议”和“执行”两段，因为你现在的疑问集中在模型输出工具调用之后谁真正执行它。
```

Do not repeatedly redesign the roadmap because of every small follow-up question.

## Branch Classification

Classify a question by its effect on learning flow.

### Inline clarification

The answer is short and directly required for the current sentence or concept.

Answer immediately and continue the same node. No visible branch bookkeeping is needed.

### Local branch

The answer requires real explanation but remains inside the current node.

Save the return point, answer it, then return to the node.

### Cross-topic branch

The question belongs to another roadmap node or an adjacent topic.

Either:

- park it and preserve the current path; or
- explore it now if the learner explicitly prioritizes it, while keeping a return point.

### New learning goal

The learner has intentionally changed what they want to learn.

Create a new roadmap rather than pretending it is still a branch of the old one. Preserve the old roadmap as resumable context when useful.

## Response Shape

During ordinary teaching, prefer a compact structure:

```text
[Current concept]
Explanation focused on one node.

[Check or invitation]
One meaningful question, prediction, or request for the learner's doubt.
```

After a substantial detour:

```text
Branch resolved: ...
Return: 3. Agent loop > Planner vs Executor
Next: ...
```

When orientation is needed:

```text
Learning map
1. ✓ Roles
2. ✓ Context
3. → Agent loop
4. ○ Tool calling
5. ○ Memory

Branch: Planner vs Executor > retry ownership
Parking lot: MCP vs CLI
```

Use symbols only when they improve scanability:

- `✓` understood or completed;
- `→` current;
- `○` not started;
- `↳` active branch;
- `P` parked.

Never mark `✓` merely because the topic was explained. Completion should mean the learner has shown enough understanding for the current goal.

## Composition With Specialist Skills

This skill governs conversational learning state, not domain truth.

When another skill is active:

- let the specialist skill determine what evidence, methods, tools, and domain sequence are valid;
- let `interactive-learning` control pacing, branch handling, return points, checkpoints, and active recall;
- do not duplicate the specialist's entire workflow inside this skill;
- when two roadmaps conflict, prefer the dependency structure required by the specialist domain and adapt the teaching map around it.

For `learn-codebase` specifically:

```text
learn-codebase:
  repository evidence, execution paths, abstractions, runtime verification, Git history

interactive-learning:
  one-node pacing, learner questions, branch stack, return point, parking lot, checkpoints
```

Together they form an interactive source-learning workflow without turning every repository investigation into a quiz.

## Failure Modes

Avoid these patterns.

### Tutorial dump

Bad:

```text
Here are 12 concepts and 4,000 words explaining all of them.
```

Why it fails: the learner's first question immediately destroys the practical sequence.

Instead: show the map, then teach one node.

### Branch drift

Bad: answer three nested questions and then continue whatever topic was mentioned last.

Instead: keep a return point and explicitly resume the original node.

### Fake progress

Bad: mark a node complete because the assistant explained it.

Instead: use learner evidence such as correct explanation, prediction, or application.

### State spam

Bad: print the whole roadmap and state machine every turn.

Instead: keep state compact and surface it on transitions or request.

### Rigid ceremony

Bad: force the learner to approve every node or use exact navigation commands.

Instead: preserve state while allowing natural conversation.

### Parking-lot avoidance

Bad: park every difficult question to keep the planned lesson clean.

Instead: answer anything that blocks the learner's current understanding.

### Unnecessary restart

Bad: after a long detour, regenerate a new beginner roadmap from scratch.

Instead: recover the last reliable state and resume from the saved return point.

## Completion Criteria

A learning session is successful when the learner can do the capability implied by the goal, not merely recognize the assistant's wording.

Depending on the subject, evidence may include the learner being able to:

1. explain the core model in their own words;
2. distinguish commonly confused concepts;
3. predict behavior in a new example;
4. apply the model to a practical problem;
5. identify what they still do not understand;
6. resume the roadmap after a branch without losing the larger structure.

The final checkpoint should preserve unfinished nodes and parked questions so the learning thread can continue later.