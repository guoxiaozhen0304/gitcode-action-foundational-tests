# REL-SCHED-01-058
- **标题**: schedule 触发准点性与丢失率——cron 最短 5 分钟间隔下 2 小时窗口的触发可靠性   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 schedule 触发可靠性：cron */5 * * * * 下 2 小时窗口内触发 ≥23/24 次（丢失率 ≤5%），每次 run 的 sha=默认分支 HEAD，非默认分支不触发，无重复触发。
## 做了什么
在默认分支启用 */5 cron 的 schedule workflow，连续观察 2 小时；对照组为非默认分支相同配置。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | runs_on_default_branch_head | positive | equals "true" | COVERED | harness 检查每次 run 的 sha 是否等于默认分支 HEAD |
| 2 | duplicate_trigger_count | positive | equals "0" | COVERED | harness 统计重复触发次数 |
| 3 | non_default_branch_triggered | negative | equals "true" | COVERED | harness 检测非默认分支是否产生 run |
| 4 | trigger_loss_rate_pct | nonfunctional | le "5" | COVERED | harness 计算丢失率（≥23/24 → ≤5%） |
| 5 | trigger_delay_p95_seconds | nonfunctional | le "300" | COVERED | harness 统计触发延迟 P95 |
