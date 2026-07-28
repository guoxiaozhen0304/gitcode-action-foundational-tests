# SEC-ORG-01-002
- **标题**: fork PR 触发的运行绝不应读取组织级 secret（与项目级同等隔离）   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
fork PR路径下组织级secret与项目级secret同等隔离，workflow拿不到该值。
## 做了什么
YAML workflow由pull_request触发(untrusted_contributor)，step中echo ${{ secrets.ORG_SHARED_KEY }}。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "ORG_SHARED_KEY" | COVERED | 日志全文搜索secret原值 |
| 2 | run_logs | positive | equals "fork_pr_org_secret_isolated" | COVERED | 隔离结果可通过日志输出判定 |
