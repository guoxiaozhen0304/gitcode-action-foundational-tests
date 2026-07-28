# COMPAT-DEPR-01-002
- **标题**: ::add-path:: 废弃命令应被拒绝或给出迁移指引   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证废弃命令 `::add-path::/custom/path` 被拒绝或警告，不应静默忽略。
## 做了什么
workflow_dispatch 触发，step echo `::add-path::/custom/path`，然后 echo `PATH=$PATH`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应静默忽略导致 PATH 未修改 |
| 2 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
| 3 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
