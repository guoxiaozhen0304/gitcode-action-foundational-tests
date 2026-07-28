# COMPAT-DEPR-01-001
- **标题**: ::set-env:: 废弃命令应被拒绝或给出迁移指引   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证废弃命令 `::set-env name=MY_VAR::hello` 被拒绝或警告，不应静默忽略导致用户误以为生效。
## 做了什么
workflow_dispatch 触发，step echo `::set-env name=MY_VAR::hello`，然后 echo `MY_VAR=$MY_VAR`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应静默忽略导致 MY_VAR 未被设置 |
| 2 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；系统应给出明确响应 |
| 3 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；警告应包含 ATOMGIT_ENV 替代示例 |
