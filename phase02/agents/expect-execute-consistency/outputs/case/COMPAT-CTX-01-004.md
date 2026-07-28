# COMPAT-CTX-01-004
- **标题**: atomgit.actor 规格自相矛盾的实测仲裁   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 atomgit.actor 是否有确定值（触发者用户名或明确不支持），消除文档自相矛盾。
## 做了什么
workflow_dispatch 触发，step echo `ACTOR_VALUE=${{ atomgit.actor }}` 和 `PROBE_DONE`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | must_contain: PROBE_DONE | GENUINE→COVERED | `${{ atomgit.actor }}` 为表达式引用，按 R6 GENUINE |
| 2 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；ACTOR_VALUE 需 LLM 判定 |
| 3 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应三方不一致无记录 |
