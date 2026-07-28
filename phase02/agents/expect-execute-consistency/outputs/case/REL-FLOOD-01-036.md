# REL-FLOOD-01-036
- **标题**: 并发洪泛——同一仓库 10 个 push 同时触发 10 个 workflow 运行应无丢失
- **维度**: reliability
- **评级**: 部分不符
## 想测什么
10s 内 push 10 次触发 10 个 workflow 运行，验证 10 个 run 均被创建、每个有独立 RUN_ID、不应丢失或状态混乱。
## 做了什么
YAML 定义 on:push + workflow_dispatch，sleep 5，harness 在 10s 内 push 10 次。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | created_runs_count | positive | equals 10 | COVERED | YAML sleep 5 真实命令 + push 触发，platform 日志确认 run 创建数=10 |
| 2 | run_status | positive | equals completed(success) | COVERED | YAML assert 所有 run 状态=completed(success)，对应文本"10 个运行最终全部 completed" |
| 3 | unique_run_ids | positive | 每个运行有独立 RUN_ID | MISSING | 文本有正向断言"每个运行有独立的 RUN_ID"，YAML 无对应 assertion（仅 count=10 未验证唯一性） |
| 4 | no_loss_or_chaos | negative | 不应丢失或状态混乱 | COVERED | created_runs_count=10 + run_status=success 组合覆盖此负向 |
