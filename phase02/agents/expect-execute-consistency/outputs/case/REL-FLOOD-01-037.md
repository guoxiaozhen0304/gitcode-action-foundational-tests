# REL-FLOOD-01-037
- **标题**: 并发洪泛——同一仓库 50 个 push 同时触发应正确排队/限流不崩溃
- **维度**: reliability
- **评级**: 部分不符
## 想测什么
30s 内 push 50 次触发 50 个 workflow 运行，验证 50 个 run 均创建、API/UI 无 5xx、总时长合理、不应丢失或重复触发。
## 做了什么
YAML 定义 on:push + workflow_dispatch，sleep 5，harness 在 30s 内 push 50 次。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | created_runs_count | positive | equals 50 | COVERED | YAML sleep 5 + push 触发，platform 日志确认 run 创建数=50 |
| 2 | api_status | positive | equals 200 | COVERED | YAML assert API 状态=200，对应文本"API/UI 响应正常" |
| 3 | api_status | negative | equals 500 | COVERED | YAML 负向断言 API 无 5xx，对应文本"API/UI 无 5xx" |
| 4 | total_duration_reasonable | nonfunctional | 全部完成总时长合理 | MISSING | 文本有非功能断言"全部完成总时长合理"，YAML 无对应 assertion |
| 5 | no_loss_or_duplicate | negative | 不应丢失或重复触发 | MISSING | 文本有负向断言"不应出现运行丢失或重复触发"，YAML 无对应 assertion |
