# COMP-SCRIPT-01-081
- **标题**: 仓库内脚本执行与路径验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么 / ## 做了什么 / ## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain: REPO_SCRIPT_RAN_OK | COVERED | step if 分支 echo REPO_SCRIPT_RAN_OK |
| 2 | run_logs | negative | must_not_contain: REPO_SCRIPT_MISSING | COVERED | step else 分支写此值但预期不匹配 |
