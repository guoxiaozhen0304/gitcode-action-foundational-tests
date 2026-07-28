# SEC-PERM-01-003
- **标题**: 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）   - **维度**: 安全性   - **评级**: 断言一致
## 想测什么
未声明permissions时ATOMGIT_TOKEN默认仅read权限，写操作返回403。
## 做了什么
YAML workflow无permissions声明，step执行curl POST写操作输出%{http_code}。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | negative | must_not_contain "201" | COVERED | 写操作成功码不应出现 |
| 2 | run_logs | positive | contains "403" | COVERED | 权限拒绝码可观测 |
