# REL-CONC-01-001
- **标题**: concurrency.max=5 时同时触发 5 个运行应全部进入执行态
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
配置 concurrency.max=5 的 workflow，同时触发 5 次，验证 5 个运行均为 completed(success)，queued→running 延迟 ≤60s。
## 做了什么
YAML 定义 concurrency max:5 exceed-action:QUEUE，sleep 10 真实命令，harness 同时触发 5 次 dispatch。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals completed(success) | COVERED | YAML 使用 sleep 真实命令 + concurrency 配置，platform/action 日志确认并发执行状态 |
| 2 | queued_to_running_latency | nonfunctional | le 60s | COVERED | YAML assert 调度延迟 ≤60s，对应文本"queued→in_progress 调度时延 ≤60 秒" |
