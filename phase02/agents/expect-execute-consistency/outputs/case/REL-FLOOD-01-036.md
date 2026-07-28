# REL-FLOOD-01-036
- **标题**: 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
步骤由裸 sleep 改为输出 RUN_ID/RUN_NUMBER（${{ }} 表达式）作为唯一性核验材料；补缺失的 unique_run_ids 断言。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | created_runs_count | positive | equals 10 | ✅ COVERED | harness 计数 |
| 2 | run_status | positive | equals completed(success) | ✅ COVERED | 全部完成 |
| 3 | unique_run_ids | positive | equals true | ✅ COVERED | 各 run 日志含 RUN_ID 供对账 |
