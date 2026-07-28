# COMPAT-NEST-01-002
- **标题**: workflow_call 嵌套层数 - 3 层越界应报错
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 3 层 workflow_call 嵌套时平台应给出明确错误（最多支持 2 层）。

## 做了什么
顶层调用第 2 层，第 2 层继续调用第 3 层；3 层嵌套结构。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals success | COVERED | 3 层嵌套被拒绝时 status 不应为 success |
| 2 | error_message | nonfunctional | llm_assisted rubric | LLM_DEPENDENT | 错误信息质量需 LLM 辅助判断 |
