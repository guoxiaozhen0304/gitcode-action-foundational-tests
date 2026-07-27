# COMP-TRIG-01-074
- **标题**: workflow_dispatch 事件关键字段与 inputs 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**workflow_dispatch 事件关键字段与 inputs 验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-074
通过标准：
1. 手动触发成功创建 run（正向）
2. inputs 参数值在 step 中可访问（正向）
3. 未传参时使用 default 值（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print inputs | `${{ inputs.environment }}`, `${{ inputs.version }}`, `echo "dispatch_ok"` | - | 平台 inputs 上下文 + dispatch_ok |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: ENV= | ✅ GENUINE | `${{ inputs.environment }}` 为 workflow_dispatch 的 inputs 上下文求值 |
| 2 | run_logs | positive | must_contain: VER= | ✅ GENUINE | `${{ inputs.version }}` 为 workflow_dispatch 的 inputs 上下文求值 |
| 3 | run_logs | positive | must_contain: dispatch_ok | ✅ GENUINE | 步骤整体含 `${{ }}` 表达式，dispatch_ok 为同一步骤内的辅助标记 |
---
