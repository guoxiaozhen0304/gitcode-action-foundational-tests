# REL-LOGPERF-01-052
- **标题**: 日志实时性——运行中 job 的日志流式可见延迟应有界且与完成后日志一致
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
验证运行中 job 日志的流式可见性：首行延迟≤30s，运行中日志与完成后日志内容一致（前缀关系），P95 追平延迟≤60s。

## 做了什么
workflow 每5秒输出带时间戳日志共120行（10分钟）；harness 每10秒拉取日志并比对。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | streaming_log_is_prefix_of_final | positive | equals=true | COVERED | 文本"运行中可见日志为完成后日志的前缀"直接对应 |
| 2 | first_line_visibility_seconds | nonfunctional | le=30 | COVERED | 文本"首行可见延迟≤30秒"精确匹配 |
| 3 | p95_catchup_latency_seconds | nonfunctional | le=60 | COVERED | 文本"P95追平延迟≤60秒"精确匹配 |
