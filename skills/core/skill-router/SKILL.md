---
name: skill-router
description: Select and sequence skills when the user supplies this library or asks to use their skills without naming a capability. Use for 使用我的技能库 and cross-domain workflows. Read only the next relevant skill and preserve decision state. Do not implement products or override a clearly selected specialist.
---

# Skill Router

Route the task, not every possible stage of software development.

## Locate the library and target

Infer the target project from explicit context or the active workspace. Do not
confuse the skill-library checkout with the product repository. If the target
is missing, work on a proposal and resolve the target before making file changes.

There are two supported modes:

- **Repository mode:** when this file is under `skills/core/skill-router/`, read
  `skills/INDEX.md` from that library root. With remote access, use the same
  branch or commit for the index and selected files. Prefer a pinned commit for
  reproducible runs. A URL does not imply local installation.
- **Installed mode:** use the host's skill registry. If unavailable but local
  file reads are available, inspect sibling skill metadata only. Do not require
  `../../INDEX.md` or any other file outside this installed skill folder.
  Installing only the router does not install specialists. Name missing skills
  and the resulting limitation; do not claim to load or execute them.

## Choose the next step

1. Classify intent: learning, discovery, design, implementation, review, or
   writing. Preserve explicit read-only/proposal-only constraints.
2. Inspect available requirements and target-project rules. For new projects
   and materially new behavior, route critical gaps to `development-discovery`.
   Clear, authorized edits take a short path; do not add a questionnaire.
3. Select the smallest sufficient skill. Read its instructions before acting.
   Briefly explain the route when useful, without a ceremonial routing report.
4. Load only that stage and needed local references. Select downstream skills
   after their prerequisites are actually met, not all at once.
5. Preserve the existing specification and approval scope. Use the optional
   [handoff note](references/handoff.md) for multi-stage or resumed work.
6. When a task spans domains, separate product decisions from UI decisions.
   A design choice cannot silently change persistence, permission, or execution
   behavior. Return to the decision owner when implementation uncovers a gap.

Do not force every task through development discovery. Review-only, learning,
and writing can start with their specialists. Do not convert a feature request
into an interactive codebase lesson unless the user asked to learn.

## Handoff and stop conditions

A handoff records the target, mode, confirmed decisions and sources, assumptions,
blocking questions, current spec/plan revision, authorization, verification,
and next action. Distinguish a proposed route from work actually performed.

If a selected skill is absent, use only capabilities the host really has and
state the fallback. If no safe fallback exists, report the missing capability.
A skill is an instruction package, not a subprocess or an automatic tool grant.

Stop at a requested proposal/review boundary. "Continue" continues the current
phase; it is not implicit authorization to implement an unapproved design.
