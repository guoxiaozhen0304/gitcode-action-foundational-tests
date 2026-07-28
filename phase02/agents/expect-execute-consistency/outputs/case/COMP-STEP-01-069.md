# COMP-STEP-01-069
- **标题**: step 必填与核心字段 name run uses 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
run_ok 原裸 echo（TRIVIAL）。调整步骤顺序（checkout 在前），run 步骤改为真实校验工作区非空才输出 run_ok（为空 exit 1）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain run_ok | ✅ GENUINE | 真实校验后输出 |
| 2 | run_status | positive | equals success | ✅ GENUINE | checkout + 校验有真实失败路径 |
