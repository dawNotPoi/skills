---
name: explaining-in-plain-language
description: Explain a complex technical situation in plain everyday words and metaphors so the reader grasps it in about two minutes, without losing factual precision. Use when the user asks 说得直白一点, 用个比喻, 两分钟能看完, 给我捋一下, 通俗解释, or asks for a short plain-language read of an issue, PR review, design decision, or debugging result — including when turning it into learning notes or a question to ask someone. Do not use for teaching a topic through dialogue, for long-form articles, or for a technical report that must stay in full detail.
---

# Explaining In Plain Language

Make a tangled technical situation understandable in about two minutes, without
flattening the facts.

The text you produce is an explanation, not a work order. It helps the reader
understand and decide; it does not authorize anyone's next steps.

Violating the letter of these rules is violating the spirit of them. A short
explanation that buries the main problem, hedges every cause into vagueness, or
drops the details the reader needs to look things up has failed, however readable
it is.

## When To Use

Use it when the reader must quickly get:

- what is actually wrong, in one breath;
- why the situation became this way;
- which parts block progress and which are cosmetic;
- what the realistic fix or next move looks like, and what is still undecided.

Typical triggers: `说得直白一点`, `用个比喻`, `两分钟能看完`, `给我捋一下`,
`通俗讲讲`, `我该怎么跟别人说这件事`, or writing up an issue / PR review /
debugging result as a note to self.

Do not use it for:

- teaching a topic across a conversation — `interactive-learning` owns that;
- a long evidence-backed article — `write-evidence-driven-blog` owns that;
- an audience that explicitly needs full API-level detail;
- pure code changes with no explanation requested.

## Extract Before Writing

Read the actual source material (the diff, the review comments, the failing test,
the issue thread). Never explain from the title alone.

Pull out five things privately:

1. **The one-line situation.** If you cannot say it in one sentence with a
   concrete image, you have not understood it yet.
2. **What must be true for the reader to follow.** Usually two or three facts
   about how the system works or how the outside world works.
3. **The specific artifacts.** Numbers, field names, settings, platform names,
   error text, and who said what.
4. **What is broken versus what is merely untidy**, and which item blocks
   progress.
5. **What has still not been decided**, and the candidate options.

## Output Skeleton

Fill these slots; drop a slot only when it has nothing real in it. Keep the whole
thing readable in about two minutes — when in doubt, cut.

**1. One blunt line.** Lead with the sharpest true sentence, and a metaphor or
image if one fits naturally. No preamble, no "本文将分析".

**2. Background, two or three sentences.** Only what the reader needs to follow
the problem. Say what the thing is supposed to do and which outside rule it runs
into.

**3. The main problem, with its consequence chain.** Name the single thing that
hurts most, walk the chain of events step by step, and land on the bad outcome in
plain words ("the work gets rejected at the last step and is wasted"). Do not
label the problem — show the chain that produces it.

**4. The remaining points, one short block each.** Each block says what happens,
what the reader would observe, and why it matters. Keep the speaker's own labels
(`Blocking`, `nit`, severity) next to your retelling so they stay findable.

**5. What was verified, listed briefly.** State it as fact, without re-arguing it.

**6. Solutions, one line per point.** Plain language, and name the recommended
option while keeping the alternatives visible. When something is deliberately out
of scope, say what the system should do instead of half-doing it.

**7. What happens next, as recommendations.** Mark them as recommendations. If
one option is clearly best, say so and give the one reason that decides it.

**8. One or two expansion hooks.** End by offering specific deeper dives ("want me
to expand how the cross-repo PR is opened, or why that setting override kills the
global instructions?"). Offer at least one; a narrow offer beats a vague "any
questions?".

## Accuracy Rules

Simplification may not change the facts.

- **Keep the identifiers.** Issue and PR numbers, exact setting or field names,
  command flags, platform names, error strings, file paths, and who holds which
  permission stay exactly as they are. They are the reader's search keys and
  their evidence in an argument. Drop a detail only when it changes nothing for
  this reader.
- **Separate confirmed from recommended from undecided.** Never let a suggestion
  read as a requirement, or an open question read as settled.
- **Attribute correctly.** Do not put the agent's conclusions or wording into a
  maintainer's or teammate's mouth, and do not soften a real blocker into a
  preference.
- **Explain jargon the first time it appears** (fork, remote, override, PR
  target) in one clause, or replace it. Never leave a term that only insiders
  decode.
- **Keep genuine uncertainty visible.** If something is unverified, say
  "may / probably / not yet confirmed" rather than asserting it.
- **Say when it is a guess.** Distinguish "the code does X" from "I think this is
  why it was written that way".

## Match The Reader

Pick the register from who will read it.

| Reader | Include |
| --- | --- |
| Note to self | Your own judgment, open doubts, what you would check next |
| Telling a teammate / maintainer | Facts, impact, options, honest unknowns; no personal judgment about people, no defensiveness, no arguing the review |
| Asking someone for help | The blocking fact, what you already tried, the specific question |

When writing notes to self, write the explanation the way you would say it out
loud, not the way a report reads.

## Common Mistakes

| Mistake | Why it fails | Fix |
| --- | --- | --- |
| Structured report as the first version | Buries the point under sections and terminology; the reader has to work | Lead with the blunt line and the consequence chain |
| Metaphor as decoration | Comparisons that do not carry the causal structure teach nothing | Use a metaphor whose parts map onto the real steps; drop it if it does not |
| "It's complicated / there are some risks" | Vague hedging tells the reader nothing | Name the exact step that fails and what the user sees |
| Four points weighted equally | The reader cannot tell what blocks progress | Mark the blocker explicitly, keep the rest short |
| "Should / must / need to" everywhere | An explanation starts to read as an approved task list | Use "recommended / if we choose A / still open" |
| List of the original wording | Restating the source is not explaining it | Retell each point in the reader's vocabulary first |
| Trimming the numbers and names | The reader can no longer verify or quote you | Keep them, cut adjectives instead |

## Self-Check Before Sending

- Does the first line alone convey the main thing?
- Can one cause be traced from symptom to bad outcome without gaps?
- Is it clear which item blocks progress, and which are small?
- Does every recommendation name the one constraint that makes it right?
- Are all identifiers, permissions, and platform limits still exact?
- Is there an offer to go deeper on something specific?

Fix the draft against this list before delivering it. Do not deliver a first
draft and promise a cleaner version.
