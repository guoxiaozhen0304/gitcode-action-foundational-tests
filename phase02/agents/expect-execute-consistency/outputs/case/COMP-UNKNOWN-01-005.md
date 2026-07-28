# COMP-UNKNOWN-01-005
- **标题**: 顶层 inputs 与 manual_override 字段的实际处理记录   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么
记录顶层 inputs（含 manual_override）是否被平台识别、default 是否注入上下文。
## 做了什么
workflow_dispatch 触发，声明顶层 inputs.branch_name（default: main, manual_override: true），echo `TOP_INPUT=${{ inputs.branch_name }}`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | must_contain: TOP_INPUT= | GENUINE→COVERED | `${{ inputs.branch_name }}` 为表达式引用，按 R6 视为 GENUINE |
| 2 | top_inputs_handling | nonfunctional | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
| 3 | silent_ignore | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9 |
