# REL-PREEMPT-01-005
- **标题**: preemption events 边界值——配置 10 个应正常解析   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 concurrency.preemption.events 配置 10 个事件时 YAML 校验通过且运行正常。
## 做了什么
创建 concurrency.preemption.events 含 10 个事件的 workflow（push, pull_request, workflow_dispatch, schedule, tag, issue_comment, pull_request_comment, merge_requests, fork_pr, manual）并触发。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals "completed(success)" | COVERED | 平台 API 查询运行状态 |
