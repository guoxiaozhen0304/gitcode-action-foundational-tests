# COMP-PR-01-003
- **标题**: fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限
- **维度**: completeness
- **评级**: 部分不符

## 想测什么
fork PR 的 pull_request workflow 中 ATOMGIT_TOKEN 写操作失败，仅 read 权限。

## 做了什么
1. trigger: pull_request, as: untrusted_contributor
2. step `Attempt write with token`：curl POST 创建 issue comment 使用 ATOMGIT_TOKEN，失败时 `|| echo "write failed as expected"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_step_result | negative | equals: write_succeeded | UNVERIFIABLE | 目标不是 run_logs/run_status，step 级结果需外部判断 |
| 2 | run_status | positive | equals: success_or_failure | COVERED | curl 失败通过 `|| echo` 处理不导致 step 失败 |
