# REL-NEST-01-023
- **标题**: workflow_call 嵌套边界——2 层嵌套调用应成功执行   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证 2 层 workflow_call 嵌套调用（主→level1→level2）能成功执行，最外层运行状态为 success。
## 做了什么
触发主 workflow，该 workflow 通过 `uses: ./.gitcode/workflows/level1.yml` 调用 level1，level1 再调用 level2。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals "completed(success)" | COVERED | 平台 API 查询最外层运行状态 |
