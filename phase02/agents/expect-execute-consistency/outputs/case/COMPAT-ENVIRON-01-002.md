# COMPAT-ENVIRON-01-002
- **标题**: environment 字段绑定 secrets 的行为差异   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 environment: prod + secrets 引用时系统明确报错/警告，不应静默忽略。
## 做了什么
workflow_dispatch 触发，environment: prod，step echo `env_secret=${{ secrets.ENV_SECRET }}`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；environment 字段不应被静默忽略 |
| 2 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；系统应给出明确报错或警告 |
