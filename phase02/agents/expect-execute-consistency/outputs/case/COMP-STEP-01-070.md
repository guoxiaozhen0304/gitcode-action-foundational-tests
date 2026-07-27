# COMP-STEP-01-070
- **标题**: step 可选字段 id env if with 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**step 可选字段 id env if with 验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-069
通过标准：
1. id 定义的步骤可被后续引用 outputs（正向）
2. env 仅在该 step 内生效（正向）
3. if 条件正确控制步骤执行（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Step with id (id: mystep) | `echo "result=hello" >> "$ATOMGIT_OUTPUT"` | - | 写入 step output |
| 2 | Use output | `echo "OUT=${{ steps.mystep.outputs.result }}"` | - | OUT=hello |
| 3 | Conditional step | `if: ${{ true }}`, env: STEP_VAR=step_value, `echo "STEP_VAR=$STEP_VAR"` | if: ${{ true }} | STEP_VAR=step_value |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: OUT=hello | ✅ GENUINE | $ATOMGIT_OUTPUT 写入 + `${{ steps.mystep.outputs.result }}` 上下文求值，测试了 id 引用 outputs 的完整链路 |
| 2 | run_logs | positive | must_contain: STEP_VAR=step_value | ✅ GENUINE | `if: ${{ true }}` 条件 + env 变量注入为实质平台行为 |
---
