# SEC-MASK-01-001
- **标题**: Secret 值在运行日志中必须被自动脱敏为 ***   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
echo secret时日志中secret原值被替换为***，全文搜索原值命中数为0。
## 做了什么
YAML workflow中step直接echo ${{ secrets.DEPLOY_TOKEN }}。trigger为workflow_dispatch。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "DEPLOY_TOKEN" | COVERED | 日志全文搜索secret原值 |
| 2 | run_logs | positive | contains "***" | COVERED | 脱敏标记可观测 |
