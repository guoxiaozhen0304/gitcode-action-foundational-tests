# COMP-PERMS-01-003

- **标题**: fork PR 的 pull_request 下声明 write 仍仅 read
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 fork PR 场景下即使声明 `permissions: { repository: write }`，TOKEN 写入仍被平台强制降级为 read-only。

## 做了什么
`on: pull_request` + `permissions: { repository: write }`，触发方为 `untrusted_contributor`（fork PR）；step 使用 `curl` 向 API 发 POST 创建评论，输出 HTTP 状态码。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success_with_write | COVERED | 写操作预期受限，不应达到 success_with_write 状态 |
| 2 | run_logs | positive | contains: write failed as expected | COVERED | curl 失败时 `|| echo "write failed as expected"` 产生该输出 |
