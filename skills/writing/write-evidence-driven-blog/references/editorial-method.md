# Editorial Method

Use this reference to plan and edit evidence-driven technical posts. It
generalizes methods observed in Innei's public technical writing and published
writing workflow. It is not a style-cloning specification.

## Reader Contract

Write two planning lines before the outline:

```text
Reader: [specific reader] who already knows [prerequisites] and needs to [decision/task].
Contract: after reading, they can [understand/decide/reproduce/challenge] [bounded outcome].
```

A real engineering session does not automatically imply a chronological
project record. Choose the form by the reader's outcome:

| Form | Promise | Minimal shape |
| --- | --- | --- |
| Note / TIL | Learn one bounded fact | Finding, sufficient example, scope, stop |
| Project record | Understand a real change | Consequence, evidence, decisions, result |
| Guide | Build a predictive model | Prerequisite, example, trace, principle, harder case |
| Argument | Evaluate a position | Criteria, alternatives, evidence, trade-off, scoped claim |

## Structural Spines

### Pattern

Use when the session yields a judgment that transfers to another codebase.
Organize sections around those judgments; use the session's failures, commands,
and measurements as evidence. Do not label sections `Pattern 1`, `Pattern 2`,
or repeat the same internal block shape.

### Process

Use when the investigation rhythm teaches the reader something. Retain an
event only when it changed the hypothesis or next action:

```text
observation → available evidence → decision → intervention → verification
```

Remove status updates, conversational turn-taking, and failed attempts that
did not change the method.

### System

Use when the author owns a tool or workflow and its present shape is the point.
Open with purpose and constraint. Explain each major design decision as intent,
mechanism, then operational consequence.

## Narrative Movements

Choose the shortest sound path from the reader's current model to the target
model:

- **Consequence first:** begin with a failure, changed behavior, measurement,
  or constraint; backfill only necessary context.
- **Model ladder:** reuse one example, predict behavior, trace actual behavior,
  state the principle, then vary one condition.
- **Competing models:** define common criteria, make both options credible,
  expose where each stops fitting, then state the scoped choice.
- **Decision chronology:** preserve sequence only when one finding changed the
  next decision.

Do not manufacture mystery, conflict, or a hero arc around routine work.

## Evidence Selection

Classify raw session material before drafting:

| Keep in the article | Compress or remove |
| --- | --- |
| A failed assumption that changed the solution | Repeated attempts with the same lesson |
| Error output that identifies a mechanism | Complete logs with no additional evidence |
| A command needed to reproduce or verify | Setup commands unrelated to the claim |
| Before/after measurement under named conditions | Unsourced performance adjectives |
| A design constraint and its consequence | Chat chronology and status narration |
| A limitation that changes applicability | Defensive caveats that change nothing |

Ask of every artifact: which claim does it support, and what would become less
credible or less reproducible if it were removed?

## Technical Viewpoints

Build recommendations in this order:

1. State the properties and constraints of a good outcome.
2. Present the strongest live alternatives under the same criteria.
3. Show decisive evidence or operational consequences.
4. Separate fact, inference, preference, and unknown.
5. Bound the conclusion by version, workload, environment, and ownership.

Replace `X is better` with `under constraints A and B, X removes cost C while
accepting trade-off D`. A local result does not become a universal rule merely
because it worked.

## Titles

A useful title combines semantic roles without forcing one syntax:

- **Identity anchor:** product, protocol, framework, library, or system.
- **Action or scenario:** migration, failure, comparison, or operating condition.
- **Earned claim:** mechanism, consequence, or boundary proved by the body.

Audit the title:

- Would the intended reader recognize the defining technology?
- Does it reveal the article's actual contract?
- Does the body prove every number and consequence?
- Is the claim no broader than the tested environment?
- Could the same title fit a hundred unrelated posts?
- Does it preserve terms a future reader would search for?

Avoid generic wrappers such as `一些思考`, `踩坑记录`, `最佳实践`, `一文搞懂`,
and `终极指南` unless they are literally accurate and necessary.

## Sections And Headings

Use a question ladder during planning:

```text
What observable mismatch starts the problem?
What model is required to explain it?
What evidence can test that model?
Which alternatives remain live under the constraints?
What decision or reproducible action follows?
Where does the claim stop applying?
```

A new heading earns its place only when one of those questions changes. A
section may provide context or verification without carrying its own grand
lesson. Merge consecutive sections that repeat the same movement.

## First-Person Ownership

When the user is the author, `I` may describe their motivation, decisions,
observations, and conclusions only when supported by the conversation or
provided evidence. Do not quietly rewrite an agent's implementation as the
user's manual action.

Prefer accurate attribution:

```text
I chose the remote HTTP architecture after comparing the deployment boundary.
An agent run then verified initialize, tools/list, and a real tools/call request.
```

Use neutral narration when ownership would distract from the transferable
model.

## Anti-Slop Pass

Search Chinese drafts for phrases such as `本文将`, `值得注意的是`, `简单来说`,
`众所周知`, `真正关键的是`, `这不仅是`, `赋能`, `闭环`, `彰显`, `标志着`,
and `最后总结一下`.

For each match:

- Delete it when it carries no factual proposition.
- Replace the wrapper with the evidence, cause, constraint, or consequence.
- Keep a contrast only when two live alternatives genuinely need separation.
- Name the source behind vague authority.

Also inspect structural fingerprints: identical paragraph lengths, every
section ending in a slogan, random bold phrases, emoji headings, and repeated
`问题 → 原因 → 方案 → 小结` blocks.

## Endings

Stop when the final technical point lands. A long guide may end with a compact
decision table or verification checklist when it helps future retrieval. Do
not append a generic recap, call to action, metaphor, proverb, or universal
lesson.

## Source Basis

These public sources informed the generalized method:

- Innei homepage: https://innei.in/
- CSS to StyleX migration: https://innei.in/posts/tech/css-to-stylex-migration
- AI-era development workflow: https://innei.in/posts/tinkering/ai-era-dev-workflow-review-and-verify
- Session to assets article: https://innei.in/posts/tech/skill-first-blog-second-my-session-to-asset-pipeline
- Published writing-style reference: https://github.com/Innei/SKILL/blob/main/skills/automation/session-to-skill-and-blog/references/writing-style.md

Treat these as editorial evidence, not permission to imitate wording or copy
article structure.
