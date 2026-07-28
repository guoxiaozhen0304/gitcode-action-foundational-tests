# SEC-CACHE-01-002
- **标题**: 主仓 cache restore 对 fork cache miss
- **维度**: security
- **评级**: 断言一致

## 想测什么
主仓用相同 key restore cache 时应 miss，不读到 fork 的毒数据。

## 做了什么
主仓 workflow 用 cache action restore、检查 poison.txt；脚本判干净/泄漏。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_restore | negative | must_not_hit "fork_cache_key" | COVERED | 对应"主仓绝不应命中 fork PR 的缓存"；harness 检查 |
| 2 | run_logs | positive | must_contain "FORK_CACHE_NOT_RESTORED_OK" | COVERED | 对应"cache restore 返回 miss"；real script→GENUINE |
| 3 | run_logs | negative | must_not_contain "FORK_CACHE_LEAKED" | COVERED | 脚本在中毒时输出→non-trivial |
