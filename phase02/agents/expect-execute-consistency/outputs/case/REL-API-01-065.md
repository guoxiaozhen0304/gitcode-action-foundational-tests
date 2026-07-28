# REL-API-01-065
- **标题**: API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
以10 QPS连续60s查询running状态run详情API，验证全部返回200、无429/503/500、P95响应时间≤2s。

## 做了什么
workflow仅包含 `sleep 30` 作为持续运行的简单job。实际API查询由外部测试脚本执行，workflow仅为被测目标。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | http_200_ratio | positive equals "100%" | 全部200 | COVERED | API响应码由外部harness采集(GENUINE R1 real cmd) |
| 2 | http_error_codes | negative contains "429" | "不应出现429" | COVERED | API响应码外部采集(GENUINE)；负向校验 |
| 3 | response_time_p95_seconds | nonfunctional le "2" | "P95≤2s" | COVERED | 响应时间由外部harness测量(GENUINE R1) |

注：本用例的步骤/断言不在workflow内部，而是对API端点的外部压力测试。workflow仅提供持续运行的job实例作为查询目标。断言中的http_200_ratio、http_error_codes、response_time均为外部负载测试工具观测指标，与YAML中定义的target一致。
