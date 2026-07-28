# REL-FLOOD-01-036
- **标题**: 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
10 个 push 创建 10 个 run，各有独立 RUN_ID，全部 completed。

## 做了什么
workflow on push + workflow_dispatch；step echo RUN_ID/RUN_NUMBER。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | created_runs_count | positive | equals "10" | MISSING | workflow 自身不统计创建数；需 harness 侧对账 |
| 2 | run_status | positive | equals "completed(success)" | COVERED | job sleep 5s 后 exit 0，状态可观测 |
| 3 | unique_run_ids | positive | equals "true" | MISSING | 需 harness 侧对比所有 run_id 去重 |
