# COMPAT-ENVIRON-01-001
- **标题**: 含 environment 字段的 job 应被报错或警告   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 job 下 environment: production 字段不被静默接受，应产生解析错误或警告。
## 做了什么
workflow_dispatch 触发，job 声明 environment: production，step echo `hello`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应静默接受并正常运行 |
| 2 | error_message | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；应对 environment 字段给出明确报错/警告 |
