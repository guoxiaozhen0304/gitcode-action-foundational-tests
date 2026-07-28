# SEC-FORK-01-002
- **标题**: fork PR 中 secrets 引用返回空值且 job 不崩溃   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
fork PR中secrets.API_KEY返回空字符串，环境变量未设置，job正常完成。
## 做了什么
YAML workflow将secrets.API_KEY注入API_KEY环境变量，step检查为空则输出expected否则exit 1。trigger为pull_request(untrusted_contributor)。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "API_KEY" | COVERED | 日志全文搜索secret原值应命中0 |
| 2 | run_status | positive | equals "success" | COVERED | job状态为平台可观测值 |
