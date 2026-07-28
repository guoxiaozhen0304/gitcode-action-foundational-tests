# REL-RERUN-01-011
- **标题**: rerun 边界值——单条运行连续重新运行 3 次应全部成功   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证单条运行可连续重新运行（rerun all jobs）3 次，每次均创建新运行且状态为 success。
## 做了什么
对一次失败的 workflow 运行依次执行 Re-run all jobs 共 3 次。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_count | positive | equals "3" | COVERED | harness 统计实际创建的 rerun 次数 |
| 2 | run_status | positive | equals "completed(success)" | COVERED | 平台 API 查询每次 rerun 的终态 |
