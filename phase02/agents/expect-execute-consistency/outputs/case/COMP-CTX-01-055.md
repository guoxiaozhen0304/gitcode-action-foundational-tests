# COMP-CTX-01-055

- **标题**: workflow_dispatch 触发下 inputs 正常求值（回归保护）
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**workflow_dispatch 触发下 inputs 正常求值（回归保护）**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-020

通过标准：
1. [正向] inputs.pr_id 求值为声明默认值 default-pr —— 断言 DISPATCH_INPUT=default-pr
2. [正向] 运行成功 —— 断言 run_status=success

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo dispatch input | `echo "DISPATCH_INPUT=${{ inputs.pr_id }}"` | - | 平台对 workflow_dispatch inputs 默认值的求值结果 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | 步骤包含 `${{ inputs.pr_id }}` 表达式，平台上下文求值是真实行为 |
| 2 | run_logs | positive | must_contain: DISPATCH_INPUT=default-pr | ✅ GENUINE | `${{ inputs.pr_id }}` 求值为 workflow_dispatch inputs 声明的默认值，非硬编码字面量 |

