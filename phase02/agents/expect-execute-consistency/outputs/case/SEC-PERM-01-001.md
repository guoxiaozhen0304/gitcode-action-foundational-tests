# SEC-PERM-01-001
- **标题**: 显式声明的 permissions 必须在 job 级实际生效并限制 ATOMGIT_TOKEN
- **维度**: security
- **评级**: 断言一致

## 想测什么
声明 repository: read 时读操作成功，写操作返回 403。

## 做了什么
workflow job 级 permissions: repository: read + pr/issue/note/project/hook: none；curl POST 写操作并输出 HTTP 码。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains "403" | COVERED | 对应"声明 read 时写操作返回 HTTP 403"；real curl→GENUINE |
| 2 | run_logs | negative | must_not_contain "201" | COVERED | 对应"日志中绝不应出现写操作成功的 201 响应码"；real curl→GENUINE |
