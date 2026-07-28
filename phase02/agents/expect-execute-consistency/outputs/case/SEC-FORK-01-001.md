# SEC-FORK-01-001
- **标题**: fork PR 触发 pull_request 时不可读取项目 secrets   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
fork PR场景下系统阻止访问DEPLOY_TOKEN，日志中不出现secret明文。
## 做了什么
YAML workflow由pull_request触发(untrusted_contributor)，step中echo ${{ secrets.DEPLOY_TOKEN }}和env检查。断言含must_not_contain_secret和completed_or_blocked。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 日志全文搜索secret原值 |
| 2 | run_status | positive | equals "completed_or_blocked" | COVERED | 运行状态为平台可观测值 |
