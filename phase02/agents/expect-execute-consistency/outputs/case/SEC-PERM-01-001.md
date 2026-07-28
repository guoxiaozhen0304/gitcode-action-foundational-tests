# SEC-PERM-01-001
- **标题**: 显式声明的 permissions 必须在 job 级实际生效并限制 ATOMGIT_TOKEN   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
job级声明repository:read后读操作成功，写操作返回403。
## 做了什么
YAML workflow中job级permissions设repository:read等为none，step执行curl POST写操作并输出HTTP状态码。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | contains "403" | COVERED | curl输出%{http_code}到日志 |
| 2 | run_logs | negative | must_not_contain "201" | COVERED | 写操作成功响应码不应出现 |
