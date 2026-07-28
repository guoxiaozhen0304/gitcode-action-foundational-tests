# COMP-PR-01-003

- **标题**: fork PR 的 pull_request workflow ATOMGIT_TOKEN 仅 read 权限
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 fork PR 的 `pull_request` workflow 中 ATOMGIT_TOKEN 仅有 read 权限，写操作（创建评论）应失败。

## 做了什么
`on: pull_request` + `as: untrusted_contributor`；step 使用 `curl` 以 `$ATOMGIT_TOKEN` 认证调用 API 创建 issue 评论。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_step_result | negative | equals: write_succeeded | COVERED | 写操作预期因权限不足失败 |
| 2 | run_status | positive | equals: success_or_failure | COVERED | 运行成功或因 curl 失败均为可接受结果 |
