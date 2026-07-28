# SEC-CACHE-01-002
- **标题**: 主仓 cache restore 对 fork cache miss
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
补真实验证步骤：restore 后 grep 检查 poison.txt 是否含 FORK_POISON_MARKER——泄漏则 FORK_CACHE_LEAKED + exit 1，否则 FORK_CACHE_NOT_RESTORED_OK；run_logs equals cache_miss（整日志精确匹配，形式错误）替换为标记断言。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cache_restore | negative | must_not_hit fork_cache_key | ✅ COVERED | cache action 恢复行为 |
| 2 | run_logs | positive | must_contain FORK_CACHE_NOT_RESTORED_OK | ✅ GENUINE | 真实 grep 校验后输出 |
| 3 | run_logs | negative | must_not_contain FORK_CACHE_LEAKED | ✅ GENUINE | 泄漏时输出并 exit 1 |
