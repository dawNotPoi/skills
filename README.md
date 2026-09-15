# Skills

Reusable Codex skills for writing and engineering workflows.

## Available Skills

### learn-codebase

Rapidly build a reliable mental model of an unfamiliar open-source or internal
repository. The skill avoids linear file-by-file reading and instead combines
repository mapping, one concrete execution path, core-abstraction analysis,
state and dependency modeling, runtime/test verification, Git history, active
recall, and a small change exercise.

It supports quick orientation, guided interactive learning, and deep subsystem
analysis. Important claims are expected to be backed by code, tests, runtime
behavior, commits, or pull requests rather than inferred from filenames.

[View the skill](skills/learn-codebase/SKILL.md)

### write-evidence-driven-blog

Turn learning notes, technical discussions, debugging sessions, architecture
decisions, and completed engineering work into original, evidence-driven
Chinese technical blogs.

The skill emphasizes reader contracts, evidence selection, scoped technical
claims, accurate first-person attribution, and editing that removes generic AI
prose without imitating another author's voice.

[View the skill](skills/write-evidence-driven-blog/SKILL.md)

### UI skills

A composable workflow for discovering product UI requirements, choosing a
visual direction, building a design system, implementing interfaces, and
running visual QA. Each stage is an independent skill with explicit handoff
artifacts, so teams can use only the capability the task needs.

[View the UI skills overview](skills/ui/README.md)

## Install

Clone the repository and copy the selected skill into your Codex skills
directory:

```bash
git clone https://github.com/dawNotPoi/skills.git
cp -R skills/skills/learn-codebase ~/.codex/skills/
```

Restart Codex or open a new task, then invoke it explicitly:

```text
$learn-codebase Help me understand this repository through one real execution path.
```

For the writing workflow, copy and invoke `write-evidence-driven-blog` in the
same way. Skills can also be discovered automatically when the request matches
their frontmatter descriptions.
