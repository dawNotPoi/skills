---
name: learn-codebase
description: Rapidly build a reliable mental model of an unfamiliar open-source or internal codebase using repository mapping, execution-path tracing, core-abstraction analysis, Git history, runtime verification, active recall, and a small change exercise. Use when the user wants to understand, onboard to, study, explain, or become productive in a repository. Do not read files linearly or dump a repository-wide summary without evidence.
---

# Learn Codebase

Build a usable mental model of a repository, not a pile of file summaries.

The unit of learning is:

`user scenario -> execution path -> core abstractions -> dependencies -> design decisions -> verified behavior`

Prefer evidence from code, tests, runtime behavior, commits, and pull requests over guesses based on names or directory structure.

## Default Teaching Style

Use guided learning rather than one-shot explanation.

- Explain only enough to establish the next concept.
- Ask one meaningful question at a time when the user is actively learning.
- Let the user's answer determine what to explain next.
- Correct misconceptions precisely and preserve what the user already understands.
- Periodically ask the user to predict behavior before revealing the answer.
- Do not flood the user with the whole repository at once.

If the user asks only for a map or report, skip the interactive questioning and produce the requested artifact directly.

## Evidence Rules

Every important architectural claim should point to concrete evidence such as:

- repository path;
- class, function, type, interface, or symbol;
- call site or reference;
- test;
- configuration;
- commit or pull request;
- runtime output.

Do not infer responsibilities from filenames alone. Mark uncertain claims explicitly and verify them before treating them as facts.

Ignore generated output, vendored dependencies, lockfiles, snapshots, build artifacts, and large data files unless they materially affect the behavior being studied.

## Workflow

### 1. Establish the product and repository boundary

Before reading implementation details, determine:

- what problem the project solves;
- who or what invokes it;
- the primary runtime environment;
- major languages, frameworks, packages, and processes;
- likely entry points;
- build, test, and run commands;
- whether the repository is a monolith, monorepo, library, service, CLI, frontend, agent, framework, or mixed system.

Read high-signal files first: README, package or build manifests, workspace definitions, top-level configuration, executable entry points, and representative tests.

### 2. Build a repository map

Produce a compact map of the important modules and their responsibilities.

Classify directories and files into categories such as:

- entry points;
- domain/core logic;
- orchestration/runtime;
- API or transport;
- persistence/state;
- tools/integrations;
- UI/presentation;
- infrastructure/configuration;
- tests;
- generated or low-priority code.

Then identify the smallest reading set that gives the highest information gain. Prefer roughly 5-15 files over exhaustive reading.

### 3. Choose one anchor scenario

Pick one concrete user-visible or system-visible behavior and trace it end to end.

Examples:

- a chat message entering an Agent system and producing a tool result;
- an HTTP request becoming a database write;
- a CLI command reaching a compiler pass;
- a button click becoming a state update and network request;
- a queue message becoming a background job.

Do not choose a vague scenario such as "how the backend works".

### 4. Trace the execution path

Follow the anchor scenario through real call sites.

For each important step record:

- file path;
- symbol;
- input;
- output;
- state read or written;
- next call or dispatch target;
- important branch conditions;
- async, queue, event, RPC, IPC, or tool boundaries.

Represent the path compactly, for example:

```text
User action
  -> API route: src/api/chat.ts#handleChat
  -> runtime: src/agent/runtime.ts#run
  -> planner: src/agent/planner.ts#plan
  -> tool registry: src/tools/registry.ts#execute
  -> response stream
```

When a dynamic call, dependency injection container, plugin registry, reflection layer, event bus, or framework hides the next step, search references and registrations instead of guessing.

### 5. Identify the core abstractions

Find the small set of concepts that control most behavior.

For each abstraction answer:

1. What responsibility does it own?
2. What invariant does it maintain?
3. What inputs and outputs define its boundary?
4. Who creates it?
5. Who calls it?
6. What would break or become duplicated if it disappeared?
7. Which neighboring abstraction could easily be confused with it?

Examples include `Agent`, `Planner`, `Executor`, `Message`, `Context`, `Fiber`, `Scheduler`, `Route`, `Dependency`, `Store`, `Task`, or project-specific equivalents.

Do not confuse frequently referenced utility code with a true architectural control point.

### 6. Build the dependency and state model

Explain the repository in terms of relationships, not folders.

Capture:

- control flow;
- data flow;
- state ownership;
- dependency direction;
- process or service boundaries;
- synchronous versus asynchronous edges;
- extension points;
- external systems.

Explicitly identify where important state lives and who is allowed to mutate it.

### 7. Verify with runtime behavior and tests

Whenever feasible:

- run the project or a narrow test;
- reproduce the anchor scenario;
- add temporary logging or use existing traces when useful;
- inspect test cases that encode expected behavior;
- compare observed behavior with the current mental model.

If execution is impossible, say so and increase reliance on tests and static evidence.

Do not claim runtime behavior was verified when it was only inferred statically.

### 8. Use Git history to recover design intent

For confusing or important abstractions, inspect history.

Use `git log`, `git blame`, relevant commits, and pull requests to answer:

- when the abstraction was introduced;
- what existed before it;
- what problem motivated the change;
- what alternative was rejected or replaced;
- how the design evolved afterward.

Current code explains what exists. History often explains why it exists.

Do not inspect history mechanically for every file; use it where design intent is unclear or surprising.

### 9. Switch to active recall

After a meaningful chunk of learning, stop explaining and test the mental model.

Ask one question at a time. Prefer questions that require causal reasoning, such as:

- "Why is planning separated from execution here?"
- "Where would you add retry logic, and why?"
- "What state would become inconsistent if this function were bypassed?"
- "If this event handler were removed, which user-visible behavior would fail?"
- "Predict the next function called after this branch."

Avoid trivia about names or syntax unless syntax itself is the learning objective.

After the answer:

1. state what is correct;
2. identify the exact misconception or gap;
3. point back to code evidence;
4. ask the next question at the appropriate difficulty.

### 10. Validate understanding with a small change

The strongest proof of understanding is a correct prediction about a modification.

Choose a narrow change such as:

- add a retry policy;
- add one tool or command;
- add a validation rule;
- add a new event;
- expose one new field;
- change a timeout;
- add one testable behavior.

Before editing code, ask the learner to predict:

- which layer should own the change;
- which symbols should change;
- which symbols should not change;
- what tests should be added or updated;
- what regressions are possible.

Then implement or inspect the change and compare the result with the prediction.

## Search Strategy

Prefer targeted repository exploration over reading files sequentially.

Useful techniques include:

- `rg` / repository search for symbols, routes, event names, config keys, and error strings;
- reference and call-site search;
- test-name search;
- `git log -- <path>` and commit-message search;
- `git blame` for surprising lines;
- language-aware symbol navigation or LSP tools when available;
- running a narrow test before a full suite.

When the repository is large, repeatedly ask: "Which next file would reduce uncertainty the most?"

## Learning State

Maintain a compact working model during the session:

```text
Goal:
Anchor scenario:
Known entry point:
Execution path:
Core abstractions:
State ownership:
External boundaries:
Verified facts:
Open questions:
Current misconception/gap:
Next highest-value investigation:
```

Use `templates/learning-map.md` when a persistent artifact is useful.

## Output Modes

### Quick Map

Use when the user wants fast orientation.

Return:

- project purpose;
- architecture map;
- top 5-15 files to read;
- one representative execution path;
- core abstractions;
- major unknowns.

### Guided Learning

Use by default when the user's goal is to learn.

Work iteratively:

`map -> explain one concept -> ask -> correct -> deepen -> verify -> repeat`

Do not continue to the next major concept until the current one is sufficiently understood.

### Deep Dive

Use when the user asks how a subsystem really works.

Include:

- detailed execution path;
- state and dependency model;
- concurrency or lifecycle behavior;
- tests and runtime verification;
- relevant history and design intent;
- failure modes and extension points.

## Completion Criteria

A learning session is complete when the learner can, with reasonable accuracy:

1. explain what the system does and where execution begins;
2. trace one important behavior end to end;
3. explain the responsibility of the core abstractions;
4. identify where important state lives;
5. predict where a small feature or fix belongs;
6. name the main uncertainty or trade-off in the design;
7. verify or falsify a claim using code, tests, runtime behavior, or history.

Do not equate "all files were summarized" with understanding.
