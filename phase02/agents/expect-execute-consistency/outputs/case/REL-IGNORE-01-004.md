# REL-IGNORE-01-004
- **标题**: concurrency IGNORE 策略——超上限运行应直接执行
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
concurrency max=2 IGNORE 时 4 个并发运行全部 in_progress，无 queued。

## 做了什么
workflow concurrency max=2 exceed-action=IGNORE；job sleep 30s；harness 并发触发 4 次。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals "completed(success)" | COVERED | IGNORE 策略下 4 个运行均应完成 |
| 2 | run_status | negative | equals "queued" | COVERED | IGNORE 策略不排队，不应有 queued 状态 |
