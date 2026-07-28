# COMP-PRTARGET-01-002
- **标题**: 显式 checkout head.sha 后执行不可信代码的风险可控
- **维度**: 完备性
- **优先级**: P0
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
断言 2 原 VACUOUS（裸 echo 标记）。步骤改为 git rev-parse HEAD 真实比对 head.sha（不一致 exit 1），输出 HEAD_SHA_CHECKOUT_OK + BASE_VERSION_MARKER；新增 HEAD_SHA_CHECKOUT_OK 断言。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | ✅ GENUINE | git 比对有真实失败路径 |
| 2 | run_logs | positive | contains BASE_VERSION_MARKER | ✅ GENUINE | 真实校验后输出 |
| 3 | run_logs | positive | contains HEAD_SHA_CHECKOUT_OK | ✅ GENUINE | git rev-parse 真实比对通过 |
