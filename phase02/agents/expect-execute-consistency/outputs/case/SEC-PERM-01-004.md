# SEC-PERM-01-004
- **标题**: 默认状态下写操作被 403 拒绝   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
未声明permissions时push操作被权限拒绝。
## 做了什么
YAML workflow无permissions声明，step执行git clone + git push，失败时输出"push denied as expected"。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "main -> main" | COVERED | push成功的ref更新记录不应出现 |
| 2 | run_logs | positive | contains "push denied as expected" | COVERED | 失败回退字符串可观测 |
