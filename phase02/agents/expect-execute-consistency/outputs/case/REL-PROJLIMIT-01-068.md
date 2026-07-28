# REL-PROJLIMIT-01-068
- **标题**: 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排队
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
触发201次，全部进入终态无丢失、failed=0、queued≥1、不应429/500。

## 做了什么
harness在60s内API触发201次，每次带唯一序号对账。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_count | positive | equals=201 | COVERED | 文本"completed_count=201"精确对应 |
| 2 | failed_count | positive | equals=0 | COVERED | 文本"failed_count=0"精确对应 |
| 3 | queued_count | positive | ge=1 | COVERED | 文本"queued_count≥1"精确对应 |
| 4 | total_duration_seconds | nonfunctional | le=3600 | COVERED | 文本"总耗时≤60min"对应 |
| 5 | lost_count | nonfunctional | equals=0 | COVERED | 文本"lost_count=0"对应 |
| 6 | (文本负向) 不应429/500导致触发失败 | — | — | MISSING | 文本"不应因并发超限而直接返回429/500"在YAML中无独立断言 |
