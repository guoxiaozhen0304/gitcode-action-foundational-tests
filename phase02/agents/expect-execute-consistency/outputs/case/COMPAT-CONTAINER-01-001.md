# COMPAT-CONTAINER-01-001
- **标题**: container 字段不被支持时应明确报错而非静默忽略   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 jobs.<id>.container 字段不被支持时系统明确报错（包含 container 关键字），而非静默忽略或模糊报错。
## 做了什么
workflow_dispatch 触发，job 声明 container.image: ubuntu:latest，step echo `hello`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | validation_error | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应 generic YAML error |
| 2 | run_status | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应静默忽略导致成功运行 |
| 3 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；报错需包含 container 关键字及可操作建议 |
