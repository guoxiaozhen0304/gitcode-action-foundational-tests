# SEC-BASE-01-001
- **标题**: pull_request_target 使用 base 分支的 workflow 版本
- **维度**: security
- **评级**: 断言一致

## 想测什么
pull_request_target 触发时加载 base 分支 workflow，fork PR 分支对 workflow 的修改不被采用。

## 做了什么
workflow 在 pull_request_target 下执行，echo base_branch_workflow_executed；断言 fork 注入步骤不应出现。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain "base_branch_workflow_executed" | COVERED | 对应"base 分支 workflow 按其定义执行"；echo→GENUINE |
| 2 | run_logs | negative | must_not_contain "fork_injected_step" | COVERED | 对应"fork PR 分支内对 workflow 文件的改动不得被采用"；step 不写该串→non-trivial observable（如果隔离失效会出现） |
