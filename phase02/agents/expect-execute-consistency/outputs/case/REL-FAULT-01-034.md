# REL-FAULT-01-034
- **标题**: 故障注入——cache 服务 503 不可用时 job 应优雅降级为 cache miss
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
cache restore 期间注入 503，job=success，日志含 "cache miss"。

## 做了什么
cache restore step + subsequent echo step；fault_injection 在 step 1 注入 cache 503。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | equals "success" | COVERED | cache 不可用时降级为 miss，后续 step 正常执行 |
| 2 | run_logs | positive | contains "cache miss" | COVERED | 平台 cache 插件在 miss 时输出，真实可观测 |
