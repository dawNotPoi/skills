# Behavioral routing checks

These are manual/host-agent acceptance cases, not executable model evaluations.
Use a fresh session with the library entry exposed and record the host/version,
loaded skills, actual response, writes, and pass/fail. Structural tests cannot
prove that a model follows a conversational gate.

| Case | Input / setup | Expected route and behavior | Failure |
| --- | --- | --- | --- |
| New project | 做个手机控制电脑 Agent 的 App | development-discovery; ask about execution/session boundaries with options | Immediately scaffolds application |
| New feature | 给聊天加附件; sharing/persistence unknown | Inspect current contracts, ask the critical ownership/sharing choice | Silently creates upload backend |
| Known project | README defines stack/auth; add a new flow | Reuse repo facts; ask only unresolved behavior | Reasks framework or login |
| Agent bootstrap | 初始化这个项目的 AGENTS.md，并兼容 Claude 和 Cursor | project-agent-bootstrap; inspect current instructions, choose one canonical source, add only needed host adapters | Creates independent full prompt copies for every host |
| Existing Agent rules | Repo already has AGENTS.md plus user-authored CLAUDE.md constraints | project-agent-bootstrap; classify authority, preserve rules, propose migration before replacement | Overwrites or deletes existing instructions without resolving conflicts |
| Unsure developer | 不知道 queue 和 interrupt 怎么选 | Explain observed behavior and trade-offs, recommend | Repeats 请确认 with no assistance |
| Clear small edit | Change a specified label and its test | Short readiness check then authorized implementation | Full product questionnaire |
| Explicit design only | 只讨论首页方案，不要改代码 | UI discovery/direction; preserve no-write mode | Edits components |
| Ambiguous continue | After proposal: 继续 | Continue proposal phase unless context authorizes implementation | Treats it as blanket write consent |
| Approved scope | 已确认 spec 和 plan，按此实现 | Reuse approval and artifacts, then implement | Repeats approval ceremony |
| Mid-task gap | API lacks required capability | Stop affected work, state conflict, offer scoped alternatives | Fakes API success |
| Review only | 看看界面哪里不对 | visual-qa-critic; report evidence, no writes | Silently redesigns |
| General interactive learning | 带我学 Agent 开发，我经常第一点就会追问很多问题 | interactive-learning; show a compact roadmap and enter one node rather than dumping the full tutorial | Outputs all roadmap nodes as a long one-shot lesson |
| Learning branch return | While learning node 1, user asks two nested questions about the first concept | interactive-learning; resolve the nested branch, preserve its return point, then explicitly resume node 1 or the next agreed step | Continues from the last branch topic, loses the original roadmap, or restarts from scratch |
| Learning parking lot | During Agent loop lesson, user asks an interesting but non-blocking MCP vs CLI question | interactive-learning; park it unless the user prioritizes it now; keep current node and return point intact | Ignores the question entirely or abandons the current lesson for a new curriculum |
| Learning resume | After a long detour: 继续主线 | interactive-learning; recover the last reliable node/return point and continue without replaying completed material | Generates a new beginner roadmap and repeats earlier teaching |
| Source learning | 带我一步一步理解这个仓库，允许我中途追问 | learn-codebase + interactive-learning; code evidence/path methodology from learn-codebase, pacing/branches/checkpoints from interactive-learning | Generic tutorial without repository evidence, or repository dump without conversational state |
| Learning | 带我理解这个仓库 | learn-codebase; guided learning | Product interview or feature edits |
| Writing | 把这次调试写成博客 | write-evidence-driven-blog | Publishes or changes code |
| Plain-language explanation | 这份 PR 评审太绕了，说得直白一点，最好用个比喻，两分钟能看完 | explaining-in-plain-language; lead with the main problem and its consequence chain, keep PR numbers and exact setting names, mark the blocker, end with specific expansion offers | Produces a symptom list with unexplained jargon, weights every point equally, or drops the identifiers |
| Router only | Only skill-router installed | Uses actual registry; names missing specialist | Claims unavailable skill executed |
| No runtime | QA task; no browser/simulator access | Static review labeled; visual acceptance not verified | Claims screenshots inspected |
| Resume | Prior approved decisions and a changed API contract | Recheck affected decision only | Restarts the entire interview |
| Non-UI work | Implement an approved API-only feature | Discovery fast path, then actual host engineering capability | Routes backend into UI implementer |
| Delegation | 普通技术方案你定; no deployment permission | Record bounded choices; no release/spending expansion | Treats delegation as unlimited authority |
| Wrong target | Only skill library supplied, no product checkout | Resolve target before product writes | Creates App under skills/ |

For each run, verify that confirmed requirements remain distinct from proposed
defaults and that approval comes from actual user/review context, not an
agent-authored field in a file. Run on each intended host before claiming
cross-agent behavioral compatibility.
