# SEC-PERM-01-002
- **标题**: permissions 声明 read 时写操作被平台拒绝
- **维度**: security
- **评级**: 断言一致

## 想测什么
声明 repository: read 时 push 返回 403，不出现 ref 更新记录。

## 做了什么
workflow job 级 permissions: repository: read；git clone 后 git push，失败时 echo "push denied as expected"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "main -> main" | COVERED | 对应"日志中绝不应出现 push 成功的 ref 更新记录"；real git→GENUINE |
| 2 | run_logs | positive | contains "push denied as expected" | COVERED | 对应"返回明确的权限拒绝错误"；real git→GENUINE |
