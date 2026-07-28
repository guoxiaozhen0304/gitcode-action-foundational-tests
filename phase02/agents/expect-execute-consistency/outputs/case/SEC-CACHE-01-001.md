# SEC-CACHE-01-001
- **标题**: fork PR 写入的 cache 必须不可被主仓后续 workflow 读取
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
补真实投毒写入步骤（node_modules/poison.txt 含 FORK_POISON_MARKER + FORK_CACHE_WRITE_ATTEMPTED 标记），使主仓 restore 检查有实质核对对象；cache_restore 断言归属 harness（主仓后续 workflow 恢复检查，YAML 已注释）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain FORK_CACHE_WRITE_ATTEMPTED | ✅ GENUINE | 真实写文件后输出 |
| 2 | cache_restore | negative | must_not_hit test-cache-key | ✅ COVERED | harness 主仓恢复检查 |
| 3 | run_status | positive | equals completed | ✅ GENUINE | 真实写+cache action 有失败路径 |
