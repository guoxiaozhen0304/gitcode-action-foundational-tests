# REL-FAIR-01-044
- **标题**: 并发资源公平性——2 个 workflow 各 3 个 jobs 应被公平调度
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
2 个 workflow 各 3 jobs，启动时延差≤60s，无串行执行。

## 做了什么
单 YAML 内含 6 个独立 job（wx_job1..3, wy_job1..3），各 sleep 30s；由 harness 拆分为两个 workflow 并发触发。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | startup_time_diff_seconds | nonfunctional | le 60 | LLM_DEPENDENT | 非功能指标，需 harness 测量两个 workflow 间 job 启动时差 |
| 2 | serial_execution_detected | negative | equals "true" | MISSING | workflow 自身不产出串行检测标记；需 harness 侧对比时序判定 |
