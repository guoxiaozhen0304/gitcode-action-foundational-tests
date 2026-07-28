# SEC-BASE-01-001
- **标题**: pull_request_target 使用 base 分支的 workflow 版本
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
断言 1 原 VACUOUS（步骤 echo 与断言字面值不匹配）。步骤改为输出 ${{ atomgit.ref }}/${{ atomgit.sha }} 表达式 + base_branch_workflow_executed 标记；断言改 must_contain 与步骤输出对齐。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain base_branch_workflow_executed | ✅ GENUINE | 步骤含 ${{ }} 表达式，真实输出版本信息 |
| 2 | run_logs | negative | must_not_contain fork_injected_step | ✅ GENUINE | fork 注入步骤若被执行则出现 |
