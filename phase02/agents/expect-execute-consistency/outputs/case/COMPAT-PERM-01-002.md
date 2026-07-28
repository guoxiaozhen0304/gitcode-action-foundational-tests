# COMPAT-PERM-01-002
- **标题**: 未声明 permissions 时 fork PR 写操作隔离
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 fork PR 场景下未声明 permissions 时，默认 TOKEN 的写操作被隔离——写操作应被拒绝或失败。

## 做了什么
fork PR 触发下，step 执行 git config + commit + `git push origin HEAD` 尝试写操作。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals success | COVERED | 写操作被隔离失败时 run 不应成功 |
| 2 | run_logs | negative | must_not_contain_secret: "" | VACUOUS | 空字符串 secret 名无意义，不产生有效检查 |
