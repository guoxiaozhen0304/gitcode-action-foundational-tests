# SEC-CACHE-01-001
- **标题**: fork PR 写入的 cache 必须不可被主仓后续 workflow 读取
- **维度**: security
- **评级**: 断言一致

## 想测什么
fork PR 写入 cache 后，主仓 workflow 不应命中该缓存。

## 做了什么
fork PR workflow 写入含毒标记的 cache；harness 在主仓侧对 test-cache-key 执行 cache_restore 检查。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "FORK_CACHE_WRITE_ATTEMPTED" | COVERED | 确定性锚点；echo→GENUINE |
| 2 | cache_restore | negative | must_not_hit "test-cache-key" | COVERED | 对应"主仓不应命中 fork PR 写入的缓存"；harness 两段执行检查 |
| 3 | run_status | positive | equals "completed" | COVERED | 确保 fork 侧 workflow 正常完成 |
