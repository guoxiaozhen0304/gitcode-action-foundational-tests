# SEC-BASE-01-002
- **标题**: fork PR 改 workflow 不被 pull_request_target 采用
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
断言 2 原 STATUS_GUARANTEED（裸 echo + 非法状态值 success_with_base_workflow）。步骤改为 checkout + 真实校验（工作区非空，失败 exit 1）；run_status 断言值改回合法 success；补 base_branch_workflow_executed 标记断言。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain fork_injected_step | ✅ GENUINE | fork 注入若被执行则出现 |
| 2 | run_status | positive | equals success | ✅ GENUINE | checkout + 校验有真实失败路径 |
| 3 | run_logs | positive | must_contain base_branch_workflow_executed | ✅ GENUINE | 真实校验后输出 |
