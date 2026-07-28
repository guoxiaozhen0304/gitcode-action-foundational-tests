# COMPAT-CONCUR-01-002
- **标题**: concurrency 配置越界或不支持时应给出清晰报错   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 concurrency group 为数组等非法配置时系统拒绝，报错包含 concurrency 关键字并指向具体字段。
## 做了什么
workflow_dispatch 触发，concurrency group 配置为 `[invalid, array]`（非法值），step echo `hello`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | validation_error | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应只报 generic YAML error |
| 2 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；需 LLM 判定报错包含 concurrency 关键字 |
说明：越界配置由 YAML 语法本身触发平台校验，步骤逻辑作为探针嵌入。断言均依赖 LLM 分析平台实际校验结果。 |
