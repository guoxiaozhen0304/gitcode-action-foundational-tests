# COMP-RUNNER-01-080
- **标题**: runner 上下文属性可访问性验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: NAME= | COVERED | step echo NAME=\${{ runner.name }} |
| 2 | run_logs | positive | must_contain: TEMP= | COVERED | step echo TEMP=\${{ runner.temp }} |
| 3 | run_logs | positive | must_contain: TOOL_CACHE= | COVERED | step echo TOOL_CACHE=\${{ runner.tool_cache }} |
| 4 | run_logs | positive | must_contain: runner_ok | COVERED | step echo runner_ok |
