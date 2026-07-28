# SEC-PRTGT-01-002
- **标题**: pull_request_target 无审批不执行 fork PR 代码
- **维度**: security
- **评级**: 断言一致

## 想测什么
无审批状态下 pull_request_target 的 job 不应直接执行 fork PR 代码。

## 做了什么
workflow pull_request_target 下 checkout ref: head.sha，在无审批状态触发。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | must_not_equal "success_without_approval" | COVERED | 对应"绝不应在无审批情况下直接执行 fork PR 构建脚本"；platform→GENUINE |
| 2 | run_status | positive | equals "pending_or_blocked" | COVERED | 对应"未审批状态下 job 应处于挂起或拒绝态"；platform→GENUINE |
