# COMP-PRTARGET-01-001
- **标题**: pull_request_target 默认使用 base 分支 workflow 版本
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
步骤由裸 echo（TRIVIAL）改为增输 WORKFLOW_REF=${{ atomgit.ref }} 表达式（规则 6：含 ${{ }} 即 GENUINE）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains BASE_VERSION_MARKER | ✅ GENUINE | 步骤含 ${{ }} 表达式 |
| 2 | run_logs | negative | must_not_contain FORK_VERSION_MARKER | ✅ GENUINE | fork 版本若被执行则出现 |
