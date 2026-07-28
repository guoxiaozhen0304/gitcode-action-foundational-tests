# COMPAT-INPUTS-01-002
- **标题**: workflow_dispatch inputs 类型限制 - string 正常通过
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
STRING_INPUT_OK 原为空洞 echo（STATUS_GUARANTEED）。改为真实校验：`if [ "${{ inputs.environment }}" = "production" ]` 条件成立才输出标记，否则 exit 1。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | ✅ GENUINE | 存在真实失败路径 |
| 2 | run_logs | positive | must_contain STRING_INPUT_OK | ✅ GENUINE | 条件校验通过后输出 |
| 3 | run_logs | positive | must_contain ENV=production | ✅ GENUINE | 依赖 inputs 正确传递 |
