# REL-FLOOD-01-037
- **标题**: 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
50 个 push 全部创建，API 无 5xx，无重复触发，总时长合理。

## 做了什么
workflow on push + workflow_dispatch；step echo RUN_ID/RUN_NUMBER + sleep 5s。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | created_runs_count | positive | equals "50" | MISSING | workflow 自身不统计；需 harness 侧 |
| 2 | api_status | positive | equals "200" | MISSING | 平台 API 状态非 workflow 步骤输出；需 harness 侧监控 |
| 3 | api_status | negative | equals "500" | MISSING | 同上 |
| 4 | duplicate_trigger_count | negative | equals "0" | MISSING | 需 harness 侧去重统计 |
| 5 | total_duration_seconds | nonfunctional | le 1800 | LLM_DEPENDENT | 非功能指标 |
