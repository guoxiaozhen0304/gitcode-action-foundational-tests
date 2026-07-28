# COMP-PERMS-01-001
- **标题**: permissions 空对象时 ATOMGIT_TOKEN 仅 repository read
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
permissions: {} 时 ATOMGIT_TOKEN 写操作因权限不足失败。

## 做了什么
1. permissions: {}
2. step `Attempt write`：git config → echo "change" >> README.md → git add → git commit → git push 使用 ATOMGIT_TOKEN

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success | COVERED | git push 因权限不足应失败（非零退出导致 step 失败） |
| 2 | run_logs | positive | contains: 403 | COVERED | git push 失败时输出 HTTP 403 |
