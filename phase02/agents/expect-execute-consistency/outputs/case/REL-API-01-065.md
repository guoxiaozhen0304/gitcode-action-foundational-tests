# REL-API-01-065
- **标题**: API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据
- **维度**: 稳定性
- **评级**: 断言一致
## 想测什么
验证以 10 QPS 连续查询 running 状态 run 的 API 时，全部返回 200、无矛盾、P95≤2s。
## 做了什么
以 10 QPS 连续查询 running run 的详情 API 持续 60s，检查状态码和响应时间。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | http_200_ratio | positive | equals=100% | COVERED | 测试脚本直接计算 200 占比，Harness 可度量 |
| 2 | http_error_codes | negative | contains=429 | COVERED | 测试脚本检测错误码，Harness 可判断是否包含 429 |
| 3 | response_time_p95_seconds | nonfunctional | le=2 | LLM_DEPENDENT | type=nonfunctional，性能指标需人工解读结果 |
