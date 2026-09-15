---
name: skill-router
description: Use when the user supplies this skill library, asks to use their skills, or gives a mixed task without a clear specialist (使用技能库、启动项目、开发功能、设计或审查 UI、学习代码、写技术文章). Identify the target, choose the smallest available route, and load one skill at a time. Do not implement, interview unnecessarily, or claim automatic installation.
---

# Skill Router

Choose the next capability, not a mandatory end-to-end ceremony.

## Resolve the two roots

`LIBRARY_ROOT` is the source of the skills. `PROJECT_ROOT` is the actual work
target. Reuse known values; never assume the library is the application. When
the user asks to maintain the library itself, they may be the same.

Repository mode: locate the root `AGENTS.md` and `skills/INDEX.md` from the
supplied checkout/URL. Keep relative paths on that repository and ref. Use the
index as the sole name-to-path catalog. Resolve symlinks to their source when
available. Do not search the user's filesystem indiscriminately.

Installed mode: use the host's advertised skill names and file paths. If this
installer provided `references/library-index.md`, it is a generated snapshot
of the source index and a routing aid, not evidence that every listed skill
is installed. Load a dependency only if its actual location is readable. A
copied skill need not have access to the original repository. If neither an
index nor host metadata is available, explain the missing access and request
the entry/index or an accessible checkout; do not invent a catalog.

## Route

1. Classify the current request: learning, discovery/planning, UI direction,
   system design, implementation, review, writing or library maintenance.
   Respect explicit scope and previously confirmed decisions.
2. Inspect the target's applicable instructions and enough context to avoid
   unnecessary questions. For development, read relevant code/tests directly;
   do not make the user sit through a code-learning exercise.
3. Select the smallest available capability from the index/host metadata.
   A new project or material feature with critical unknowns starts with
   `development-discovery`. Interface-flow gaps use `product-ui-discovery`.
   Clear UI work may go directly to `ui-implementer` subject to its gate.
4. State the immediate route in one sentence, then read the selected skill.
   Mention later stages only as conditional steps; do not preload their text.
5. Preserve the handoff below. Re-route when a specific blocker or changed
   intent requires it. Do not recurse into this router or bounce between
   discovery skills without naming the exact unresolved decision.

## Guardrails

Before implementation, critical behavior/scope/state/permission/failure and
acceptance decisions must be resolved and the current scope must be authorized.
A recommendation is not a decision. A spec draft is not implementation approval.
An earlier explicit instruction to execute a fully defined plan can satisfy
approval; do not request duplicate confirmation. Tiny clear fixes need only a
compact behavior/change/check note, not a full document set.

Learning and review-only requests remain read-only unless the user authorizes
an exercise or fix. If the user asks only to plan, stop at the plan. If tools,
rendering, network access or a named skill are missing, report the limitation.
A skill does not create tools, spawn agents, or enforce a runtime security gate.
For backend-only execution without a matching library skill, hand off to the
host's normal coding workflow after approval and say that no specialist exists.

## Handoff

Preserve target/ref, intent, scope/non-goals, confirmed requirements and their
sources, proposed defaults, critical open decisions, spec/plan version,
approval source and permitted actions, acceptance criteria, evidence/untested
areas, next step. Store project artifacts only in the target project's agreed
location. On resume, restore this record before asking or editing.
