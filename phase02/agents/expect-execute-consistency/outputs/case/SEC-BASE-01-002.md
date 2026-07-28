# SEC-BASE-01-002
- **标题**: fork PR 改 workflow 不被 pull_request_target 采用
- **维度**: security
- **评级**: 断言一致

## 想测什么
pull_request_target 不执行 fork PR 注入的步骤，运行采用的 workflow 与 base 分支一致。

## 做了什么
workflow 在 pull_request_target 下 checkout base 源码并验证；断言 fork_injected_step 不出现、base_branch_workflow_executed 出现。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain "fork_injected_step" | COVERED | 对应"fork PR 注入的步骤未出现在执行记录中" |
| 2 | run_status | positive | equals "success" | COVERED | 对应"运行采用的 workflow 与 base 一致"→job 成功 = COVERED |
| 3 | run_logs | positive | must_contain "base_branch_workflow_executed" | COVERED | echo→GENUINE |
