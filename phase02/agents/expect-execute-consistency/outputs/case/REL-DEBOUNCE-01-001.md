# REL-DEBOUNCE-01-001
- **标题**: 触发幂等——同分支 10 秒内连续 5 次 push 的 run 记录应与事件一一对账
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
同一分支 10s 内连续 push 5 次（不同 commit），验证 run 与 push sha 对账一致（5/5 或文档化去抖）、同一 sha 不重复触发、不出现无解释丢失。
## 做了什么
YAML 定义 on:push branches:[main]，step 使用 `${{ atomgit.sha }}` echo 记录 sha。harness 在 10s 窗口推送 5 个不同 commit。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | push_sha_run_mapping | positive | 1:1_or_documented_debounce | COVERED | YAML `${{ atomgit.sha }}` 表达式为 GENUINE，harness 对账 push SHA 与 run 记录 |
| 2 | same_sha_duplicate_runs_count | positive | equals 0 | COVERED | YAML assert 同 sha 重复触发数=0，对应文本"同一 sha 不被重复触发" |
| 3 | unexplained_run_loss_detected | negative | equals true | COVERED | YAML 负向检测无解释丢失，对应文本"不应出现 run 数小于 push 数且无文档化去抖说明" |
