# REL-SCHED-01-058
- **标题**: schedule 触发准点性与丢失率——cron 最短 5 分钟间隔下 2 小时窗口的触发可靠性
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
2小时内触发≥23/24、每次sha=默认分支HEAD、非默认分支不产生run、重复触发=0、丢失率≤5%、P95≤300s。

## 做了什么
schedule cron */5 * * * *，harness观察2小时(24次理论触发)。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | runs_on_default_branch_head | positive | equals=true | COVERED | 文本"每次run的sha=默认分支HEAD"对应 |
| 2 | duplicate_trigger_count | positive | equals=0 | COVERED | 文本"同一计划时刻不应触发2次(重复触发=0)"精确对应 |
| 3 | non_default_branch_triggered | negative | equals=true | COVERED | 文本"非默认分支的schedule配置不应产生任何run"精确对应 |
| 4 | trigger_loss_rate_pct | nonfunctional | le=5 | COVERED | 文本"丢失率≤5%"精确对应 |
| 5 | trigger_delay_p95_seconds | nonfunctional | le=300 | COVERED | 文本"触发延迟P95≤300秒"精确对应 |
