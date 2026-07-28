# COMP-PERMS-01-003
- **标题**: fork PR 的 pull_request 下声明 write 仍仅 read
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
fork PR 的 pull_request workflow 中声明 repository: write 后，ATOMGIT_TOKEN 写操作仍因权限不足失败。

## 做了什么
1. permissions: repository: write, trigger: pull_request, as: untrusted_contributor
2. step `Attempt write`：curl POST 创建 issue comment 使用 ATOGIT_TOKEN，失败时输出 "write failed as expected"

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success_with_write | COVERED | 期望写操作失败，step 失败不一定导致 workflow 失败（|| echo 处理） |
| 2 | run_logs | positive | contains: write failed as expected | COVERED | curl 失败时 `|| echo` 输出 |
