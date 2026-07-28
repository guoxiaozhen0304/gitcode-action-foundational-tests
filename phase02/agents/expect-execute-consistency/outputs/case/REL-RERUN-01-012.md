# REL-RERUN-01-012
- **标题**: rerun 越界值——尝试第 4 次重新运行应被系统拒绝   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证第 4 次 rerun 请求应被系统明确拒绝（rerun 上限为 3 次）。
## 做了什么
已完成 3 次 rerun 后尝试第 4 次 rerun。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_request | positive | equals "rejected" | COVERED | harness 检查第 4 次 rerun 请求的返回状态 |
