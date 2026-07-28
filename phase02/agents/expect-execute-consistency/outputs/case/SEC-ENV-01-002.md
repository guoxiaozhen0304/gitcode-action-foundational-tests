# SEC-ENV-01-002
- **标题**: 环境级 secret 审批前 workflow 不可读取
- **维度**: security
- **评级**: 断言一致

## 想测什么
审批前 workflow job 无法读取环境 secret 值，job 应挂起或失败。

## 做了什么
workflow 引用 environment: production 的 PROD_TOKEN；脚本检查 $PROD_TOKEN 是否为空。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "secret accessible unexpectedly" | COVERED | 对应"审批前 job 绝不应读取到环境 secret 的值"；脚本判 $PROD_TOKEN 为空→GENUINE |
| 2 | run_status | positive | equals "pending_or_failed" | COVERED | 对应"job 状态为挂起或权限拒绝" |
