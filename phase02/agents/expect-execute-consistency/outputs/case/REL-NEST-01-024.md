# REL-NEST-01-024
- **标题**: workflow_call 嵌套越界——3 层嵌套调用应被拒绝   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 3 层 workflow_call 嵌套调用（A→B→C→D）应被平台拒绝，运行状态为 failure，日志明确提示嵌套超限。
## 做了什么
触发主 workflow 调用 level1_deep.yml，经过 3 层嵌套；fixture 使用 reusable-workflow-3layer。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals "completed(failure)" | COVERED | 平台 API 查询运行状态 |
| 2 | run_logs | positive | contains "嵌套" | COVERED | harness 解析日志查找嵌套超限提示 |
