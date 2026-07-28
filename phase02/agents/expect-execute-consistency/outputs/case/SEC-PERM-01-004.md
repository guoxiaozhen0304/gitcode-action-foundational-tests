# SEC-PERM-01-004
- **标题**: 默认状态下写操作被 403 拒绝
- **维度**: security
- **评级**: 断言一致

## 想测什么
默认无 permissions 声明时 git push 被拒绝。

## 做了什么
workflow 无 permissions 声明；git clone 后 git push，失败时 echo "push denied as expected"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "main -> main" | COVERED | 对应"日志中绝不应出现 push 成功的 ref 更新记录"；real git→GENUINE |
| 2 | run_logs | positive | contains "push denied as expected" | COVERED | 对应"权限拒绝信息明确"；real git→GENUINE |
