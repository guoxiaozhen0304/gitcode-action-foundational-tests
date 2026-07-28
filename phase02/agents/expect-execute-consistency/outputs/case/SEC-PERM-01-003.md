# SEC-PERM-01-003
- **标题**: 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）
- **维度**: security
- **评级**: 断言一致

## 想测什么
默认无 permissions 声明时写操作被拒，返回 403。

## 做了什么
workflow 无 permissions 声明；curl POST 写操作并输出 HTTP 码。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "201" | COVERED | 对应"日志中绝不应出现写操作成功的 201"；real curl→GENUINE |
| 2 | run_logs | positive | contains "403" | COVERED | 对应"写操作返回 HTTP 403"；real curl→GENUINE |
