# COMP-CALL-01-001
- **标题**: 2 层 workflow_call 嵌套正常执行
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
2 层嵌套 workflow_call 成功执行，子 workflow 的步骤日志 marker 可见。

## 做了什么
1. caller job：`uses: ./.gitcode/workflows/reusable-sub.yml`（job 级 `uses:` 调用可复用 workflow）

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | job 级 `uses:` 调用可复用 workflow 是真实调用，可能失败 |
| 2 | run_logs | positive | must_contain: sub_workflow_marker | COVERED | 子 workflow 内部步骤输出此 marker，日志由平台汇总 |
