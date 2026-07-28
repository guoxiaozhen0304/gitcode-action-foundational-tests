# SEC-PRTGT-01-001
- **标题**: pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
pull_request_target中显式checkout fork PR代码时，secrets不应被不可信代码读取。
## 做了什么
YAML workflow使用pull_request_target触发，uses:checkout action checkout PR head sha，再echo secret。断言含must_not_contain_secret和blocked_or_pending状态。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 日志搜索secret原值 |
| 2 | run_status | positive | equals "blocked_or_pending" | COVERED | 安全限制下运行状态可观测 |
