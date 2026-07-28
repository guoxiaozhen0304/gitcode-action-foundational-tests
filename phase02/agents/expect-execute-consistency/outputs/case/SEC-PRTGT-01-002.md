# SEC-PRTGT-01-002
- **标题**: pull_request_target 无审批不执行 fork PR 代码   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
未审批状态下pull_request_target不应直接执行fork PR代码，job应挂起或拒绝。
## 做了什么
YAML workflow使用pull_request_target触发，uses:checkout action checkout PR head sha，再echo "Building PR code"。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | must_not_equal "success_without_approval" | COVERED | 无审批成功为非法状态 |
| 2 | run_status | positive | equals "pending_or_blocked" | COVERED | 挂起或阻塞为预期合法状态 |
