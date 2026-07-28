# REL-CONC-01-001
- **标题**: concurrency.max=5 时同时触发 5 个运行应全部进入执行态
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
concurrency max=5 时 5 个并发运行全进入 in_progress、排队延迟≤60s。

## 做了什么
workflow 配置 concurrency max=5 exceed-action=QUEUE；job sleep 10s；由 harness 并发触发 5 次。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals "completed(success)" | COVERED | 5 个运行均应在 max=5 内并发执行完成 |
| 2 | queued_to_running_latency | nonfunctional | le "60s" | LLM_DEPENDENT | 非功能延迟指标，需 harness 测量 |
