# REL-DEBOUNCE-01-002
- **标题**: 触发幂等——10 秒内推送 10 个 tag 的 run 记录应与 tag 事件 100% 可解释
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
10 秒内连续 push 10 个不同 tag，验证每个 tag 事件有对应 run（10/10 或文档化去抖）、同 tag 不重复触发、不出现无解释丢失。
## 做了什么
YAML 定义 on:push tags:["v*"]，step 使用 `${{ atomgit.ref }}` 记录 ref。harness 在 10s 窗口批量推送 10 个 tag。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | tag_event_run_reconciliation | positive | 10/10_or_documented_debounce | COVERED | YAML `${{ atomgit.ref }}` 表达式为 GENUINE，harness 对账 tag 事件与 run 记录 |
| 2 | same_tag_duplicate_runs_count | positive | equals 0 | COVERED | YAML assert 同 tag 重复触发数=0，对应文本"同一 tag 不应触发 2 次" |
| 3 | unexplained_run_loss_detected | negative | equals true | COVERED | YAML 负向检测无解释丢失，对应文本"不应出现 tag 事件无对应 run 且无文档说明" |
