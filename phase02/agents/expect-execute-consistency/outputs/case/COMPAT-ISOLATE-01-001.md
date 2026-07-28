# COMPAT-ISOLATE-01-001
- **标题**: Runner 环境隔离——跨 job 文件隔离
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
原 4 条断言均为 llm_assisted。workflow 步骤本为真实命令（写标记文件 + ls 条件判断），仅将断言转为确定性：must_contain WORKSPACE_ISOLATED_OK / TMP_ISOLATED_OK，must_not_contain ISOLATION_BROKEN_WORKSPACE / ISOLATION_BROKEN_TMP。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain WORKSPACE_ISOLATED_OK | ✅ GENUINE | job-verify 真实 ls 检查后输出 |
| 2 | run_logs | positive | must_contain TMP_ISOLATED_OK | ✅ GENUINE | 同上 |
| 3 | run_logs | negative | must_not_contain ISOLATION_BROKEN_WORKSPACE | ✅ GENUINE | 隔离失效时步骤输出该串并 exit 1 |
| 4 | run_logs | negative | must_not_contain ISOLATION_BROKEN_TMP | ✅ GENUINE | 同上 |
