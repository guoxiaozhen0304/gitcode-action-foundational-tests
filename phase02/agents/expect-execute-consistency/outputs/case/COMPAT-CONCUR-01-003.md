# COMPAT-CONCUR-01-003
- **标题**: concurrency preemption enable 行为差异   - **维度**: 兼容性   - **评级**: 部分不符
## 想测什么
验证 concurrency.preemption.enable 配置被系统明确接受或拒绝，不应静默忽略。
## 做了什么
workflow_dispatch 触发，concurrency cancel-in-progress:true，step sleep 30 + echo `done`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
| 2 | run_status | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
说明：文本专注于 preemption.enable 字段，但 YAML workflow 中并未声明 preemption 字段（仅有 cancel-in-progress:true）。文本与 YAML 错位：文本要求测试 preemption 配置，YAML 只测了 cancel-in-progress。preemption 验证点为 MISSING 于步骤层面。 |
