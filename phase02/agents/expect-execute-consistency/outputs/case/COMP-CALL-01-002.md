# COMP-CALL-01-002
- **标题**: 3 层 workflow_call 嵌套应被拒绝
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
第 3 层嵌套调用应被平台拒绝，运行不应成功完成。

## 做了什么
1. caller job：`uses: ./.gitcode/workflows/reusable-level1.yml`（level1 调用 level2，level2 调用 level3，共 3 层）

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success | COVERED | 期望运行不应成功，3 层嵌套有真实拒绝路径 |
| 2 | error_message | nonfunctional | llm_assisted | LLM_DEPENDENT | eval=llm_assisted，报错信息评估 |
