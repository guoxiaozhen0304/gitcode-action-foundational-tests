# COMP-PUSH-01-001
- **标题**: 匹配 branches 的 push 正确触发 workflow
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
run_status 原 STATUS_GUARANTEED（裸 echo）。步骤改为真实校验触发分支：atomgit.ref == refs/heads/main 则 TRIGGERED_ON_MAIN_OK，否则 exit 1；补 head_branch=main 验证点对应断言。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | ✅ GENUINE | 分支校验有真实失败路径 |
| 2 | run_event | positive | equals push | ✅ GENUINE | trigger.event 一致 |
| 3 | run_logs | positive | must_contain TRIGGERED_ON_MAIN_OK | ✅ GENUINE | 真实分支比对后输出 |
