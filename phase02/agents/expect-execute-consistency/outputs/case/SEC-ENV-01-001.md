# SEC-ENV-01-001
- **标题**: 环境级 secret 必须经审批后才能被 workflow 访问   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
审批后secret可被正常引用job成功执行，审批前不应读取到secret值。
## 做了什么
YAML workflow使用environment:production，step中使用$PROD_TOKEN输出其长度。trigger为workflow_dispatch，断言含must_not_contain_secret。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals "success_after_approval" | COVERED | 审批后运行状态可观测 |
| 2 | run_logs | negative | must_not_contain_secret "PROD_TOKEN" | COVERED | 日志全文搜索secret原值需命中0 |
