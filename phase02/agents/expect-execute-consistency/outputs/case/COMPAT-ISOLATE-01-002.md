# COMPAT-ISOLATE-01-002
- **标题**: Runner 环境隔离——跨 job 环境变量隔离
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
原 3 条断言均为 llm_assisted。步骤本为真实命令（写 $ATOMGIT_ENV + bash 条件判断泄漏），仅将断言转为确定性 must_contain/must_not_contain。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain ENV_ISOLATED_OK | ✅ GENUINE | job-verify-env 真实条件判断输出 |
| 2 | run_logs | negative | must_not_contain ENV_ISOLATION_BROKEN | ✅ GENUINE | 泄漏时输出该串并 exit 1 |
| 3 | run_logs | positive | must_contain ENV_SET_IN_JOB_A | ✅ GENUINE | job-set-env 真实写 $ATOMGIT_ENV 后输出 |
