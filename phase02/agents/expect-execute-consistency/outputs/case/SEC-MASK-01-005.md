# SEC-MASK-01-005
- **标题**: Secret 日志脱敏不可通过多行值输出绕过   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
多行secret的每一行在日志中均被脱敏，换行符不成为脱敏边界。
## 做了什么
YAML workflow中step直接echo ${{ secrets.MULTI_LINE_SECRET }}。断言含must_not_contain_secret和contains ***。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain_secret "MULTI_LINE_SECRET" | COVERED | 全文搜索secret原值 |
| 2 | run_logs | positive | contains "***" | COVERED | 脱敏标记可观测 |
