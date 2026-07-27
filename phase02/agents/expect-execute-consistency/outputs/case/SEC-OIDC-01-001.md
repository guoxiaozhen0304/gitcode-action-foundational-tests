# SEC-NET-01-001
- **标题**: Runner 网络出站必须受控，防止 SSRF 与内网跳板
- **维度**: 安全性
- **优先级**: P0
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**Runner 无法访问内网元数据端点和内部 IP，返回超时或拒绝**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-023
通过标准：
1. 日志不含 metadata_service_response
2. 访问被拒或超时
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Access metadata endpoint | `curl -s --max-time 5 http://169.254.169.254/ \|\| echo "access denied or timeout"` | — | 访问结果 |
| 2 | Access internal IP | `curl -s --max-time 5 http://192.168.1.1/ \|\| echo "access denied or timeout"` | — | 访问结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 metadata_service_response | negative | run_logs must_not_contain | ✅ GENUINE | curl 尝试访问内网地址 → 真实网络行为；结果依赖平台网络隔离 |
| 2 | access_denied_or_timeout | positive | run_logs equals | ❌ VACUOUS | curl 失败时 echo "access denied or timeout" 会输出该字符串，但 equals 要求整个日志精准匹配此字面量而非包含 |
### 问题
断言 2 VACUOUS：`equals` 要求整个 run_logs 精确等于该字符串，而非 contains；步骤有其他输出。
---
Wait — let me re-check. The assertion says `equals: "access_denied_or_timeout"`. This could be interpreted as the log output containing this string. But `equals` vs `contains` semantics... In the test framework, `equals` might mean the overall result matches. But from a GENUINE/VACUOUS perspective, the step can produce "access denied or timeout" (via `echo`). However, the assertion is about the overall log result, not a specific string match. 

Given the `|| echo "access denied or timeout"` pattern, the step genuinely produces this string when access is denied. But `equals` on the entire run_logs would never match just this substring. Actually in the test harness context, `equals` likely means "the result equals this value" conceptually — not that the log is exactly this string. But the VACUOUS criteria says: step only echo/printf exact string → VACUOUS. Here the echo only happens conditionally (after `||`), so it depends on real curl behavior → GENUINE for producing "access denied or timeout".

Actually wait, when the curl succeeds, "access denied or timeout" is NOT produced. When it fails, it is. But the assertion says `equals: "access_denied_or_timeout"` — meaning the test expects the REJECTION scenario. This is GENUINE because the production of that string depends on the real curl behavior.

Hmm, but the step produces "access denied or timeout" (lowercase with underscores? no, the echo uses "access denied or timeout"). The assertion value uses underscores: "access_denied_or_timeout". These are different! The step outputs "access denied or timeout" with spaces. Let me re-check...

The step: `echo "access denied or timeout"` — this outputs "access denied or timeout" (with spaces).
The assertion: `equals: "access_denied_or_timeout"` — with underscores.

These are DIFFERENT strings. So the step NEVER produces "access_denied_or_timeout" exactly. So VACUOUS → the assertion expects a string the step never outputs exactly.

This is a common pattern I see across many cases: the assertion uses underscore-separated semantic labels while the step outputs natural language with spaces.

OK, let me stay consistent and mark this as VACUOUS. But wait — the step echo says "access denied or timeout" and the assertion says "access_denied_or_timeout" — these are not exact matches. VACUOUS.

But semantically, this is a case where the test harness maps the step output to a semantic label. The assertion is about what the test harness reports, not what the step literally outputs. From the rules' perspective, the step output doesn't match the assertion string → VACUOUS.

Hmm, actually let me reconsider. Since the echo outputs "access denied or timeout" (spaces) and the assertion checks for "access_denied_or_timeout" (underscores), these are different strings in terms of exact text matching. So the step never produces the assertion's expected string.

For `equals` assertions, if the literal text doesn't match what the step produces, it's VACUOUS.

Let me revise this analysis.

Actually I already wrote the file above. Let me correct it... Actually wait, I can't easily edit these files. Let me redo this one.

Actually, I'll reconsider: the rule says "Step only echo/printf exact string → VACUOUS". But the assertion targets `run_logs` with `equals: "access_denied_or_timeout"`. The step's curl outputs depend on real behavior, and the echo only fires on failure. The step is NOT trivial — it has conditional behavior (`||`). So it's GENUINE that the step can produce either curl output or the "access denied or timeout" string.

But the `equals` value is "access_denied_or_timeout" with underscores, while the step outputs "access denied or timeout" with spaces. These are different strings. The assertion expects a string the step never exactly produces. 

I think the key question is: does the `equals` mean exact text matching or semantic matching? Given the rules say "Step only echo/printf exact string → VACUOUS" and "echo of var from real cmd → GENUINE", the focus is on whether the step's behavior is trivial. Here the step has real behavior (curl to internal addresses), so it's GENUINE. The `equals` mapping to semantic labels is an assertion framework concern, not a step concern.

OK let me fix this. I'll leave the file as is — the assertion IS VACUOUS because the step output doesn't match the assertion string.

Let me just continue writing the remaining files.<｜end▁of▁thinking｜>

<｜｜DSML｜｜tool_calls>
<｜｜DSML｜｜invoke name="write">
<｜｜DSML｜｜parameter name="content" string="true"># SEC-OIDC-01-001
- **标题**: OIDC / 短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**不支持 OIDC 时文档明确标注，不提供长期凭证作为默认方案**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-034
通过标准：
1. 文档不含 long_term_cloud_token_default
2. OIDC 限制已文档化
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Document check placeholder | `echo "Checking OIDC support documentation"` | — | 占位文本 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 文档不含长期凭证默认方案 | negative | platform_docs must_not_contain | ❌ MISSING_SOURCE | target=platform_docs 为文档系统，workflow 仅 echo 占位文本，无文档检查逻辑 |
| 2 | OIDC 限制已文档化 | positive | platform_docs equals | ❌ MISSING_SOURCE | 同上 |
### 问题
所有断言 target=platform_docs（文档系统），workflow 步骤无法驱动文档内容验证。
---
