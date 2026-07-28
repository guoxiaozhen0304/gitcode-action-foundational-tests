# REL-RERUN-01-013
- **标题**: rerun 6 小时年龄限制——超期运行不可重新运行   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证完成时间超过 6 小时的运行 rerun 请求应被拒绝，不应创建新运行。
## 做了什么
存在一条完成时间超过 6 小时的运行记录，6 小时 1 分钟后尝试 rerun。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_request | positive | equals "rejected" | COVERED | harness 检查 rerun 请求返回状态 |
| 2 | new_run_created | negative | equals "true" | COVERED | harness 检测不应出现新运行被创建的情况 |
