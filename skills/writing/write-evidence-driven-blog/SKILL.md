---
name: write-evidence-driven-blog
description: Draft or revise evidence-driven Chinese technical blogs from learning notes, discussions, debugging sessions, architecture decisions, and completed engineering work. Use when the user asks to turn a process into a blog, technical article, learning retrospective, project write-up, or less AI-sounding prose. Do not use for fiction, marketing copy, or publishing without explicit authorization.
---

# Evidence-Driven Blog Writing

Turn raw experience into original prose that explains what happened, why the
decisions changed, what the evidence supports, and where the conclusion stops.
Borrow editorial methods, never another author's phrases, persona, cadence, or
signature structure.

Before drafting or substantially revising a post, read
[references/editorial-method.md](references/editorial-method.md).

## Establish The Contract

Record these privately before outlining:

- **Author:** who owns the experience and what first-person `I` means. When the
  user is the author, do not attribute the agent's actions or opinions to them.
- **Reader:** the narrowest plausible reader and what they already understand.
- **Contract:** what the reader will be able to understand, decide, reproduce,
  or challenge after reading.
- **Evidence floor:** the facts, commands, code, measurements, failures, and
  sources that can support the promised conclusion.

Ask only for missing information that would materially change authorship,
scope, or the central claim. Otherwise draft from the available evidence and
mark genuine unknowns.

## Shape The Article

Choose a form and a structural spine independently:

| Choice | Use when |
| --- | --- |
| Note / TIL | One bounded fact or failure mode is enough. |
| Guide | The reader must build a mental model or reproduce a task. |
| Project record | A real system's change, reasons, and verified result matter. |
| Argument | The reader must compare alternatives under shared criteria. |
| Pattern spine | Transferable judgments matter more than chronology. |
| Process spine | The investigation sequence changed the next decisions. |
| System spine | Design intent, components, and operational consequences matter. |

Default to a pattern spine when a judgment transfers to another project. Keep
chronology only when an observation changed the working hypothesis or next
action. Do not turn a chat transcript into sections.

Outline as a ladder of reader questions. Add a section only when the active
question, evidence type, or abstraction level changes. Headings should carry a
specific question or claim, not labels such as `背景`, `实现细节`, or `总结`.

## Draft From Evidence

- Open on an observed consequence, constraint, action, or result. Do not begin
  with ceremonial phrases announcing what the article will discuss.
- Explain one load-bearing concept at a time. Reuse a concrete example to move
  from observation, to mechanism, to harder cases.
- Put alternatives under the same criteria. Give the strongest live
  alternative a fair explanation before choosing.
- Distinguish fact, inference, preference, and unknown. Scope conclusions by
  version, workload, ownership boundary, or failure model.
- Keep exact commands, error fragments, paths, versions, measurements, and
  before/after results only when they support a claim or make it reproducible.
- Use code, tables, and diagrams to answer a concrete reader question. Do not
  add them as decoration.
- Let `I` refer consistently to the chosen author. Describe agent work as an
  agent run, assistant action, or tool-assisted investigation when ownership
  matters.

## Edit Without A Machine Fingerprint

Delete a sentence unless it contributes an observed fact, evidence, causal
reasoning, constraint, trade-off, decision, reproducible action, or concrete
consequence. Remove rhetorical wrappers instead of replacing them with
synonyms.

Reject generic AI-writing habits: topic announcements, manufactured surprise,
vague authority, repeated mini-summaries, mechanical paragraph lengths,
decorative bolding, emoji headings, universal lessons, and a closing recap that
adds no retrieval value.

Vary section and paragraph shape according to the material. Do not force every
post into `问题 → 原因 → 方案 → 总结`, numbered patterns, or a fixed number of
headings.

## Deliver And Verify

Provide the complete draft when the user asks to review it. A useful delivery
normally contains the selected title and body; include alternative titles,
slug, abstract, tags, or publication metadata only when requested or relevant.

Before presenting the draft, verify:

- The title preserves the defining technology or system and promises no more
  than the evidence proves.
- Every major section changes the reader's question or advances the argument.
- Each recommendation names the constraint that makes it appropriate.
- First-person attribution matches what the user and agent actually did.
- Code and factual claims are checked; external claims have direct sources.
- No unresolved placeholder, invented metric, fake quote, or hidden uncertainty
  remains.
- The ending stops on the final useful decision, boundary, or retrieval aid.

Drafting is not publishing. Show a preview and respect the destination's
confirmation workflow before writing to a note system, CMS, repository, or
other external destination.
