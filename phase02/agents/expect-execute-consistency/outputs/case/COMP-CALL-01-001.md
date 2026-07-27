# COMP-CALL-01-001

- **标题**: 2 层 workflow_call 嵌套正常执行
- **维度**: completeness
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**2 层 workflow_call 嵌套正常执行**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-006

通过标准：
1. [正向] 运行状态成功 —— 断言 run_status=success
2. [正向] 子 workflow 的 step 日志可见 —— 未对应断言

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo before call | `echo "calling reusable workflow"` | - | 字面量字符串 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | reusable-workflow |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 唯一步骤仅为 echo "calling reusable workflow"，无条件失败路径，无 workflow_call 调用 |

### 问题

**断言 1 — STATUS_GUARANTEED**: 标题声称测试「2 层 workflow_call 嵌套正常执行」，但 YAML 中没有任何 `uses:` 调用可重用 workflow 的步骤。workflow 仅包含一个 `echo "calling reusable workflow"`，完全不涉及被测功能。workflow 永远成功，断言空洞为真。

文本规格的第二个验证点「子 workflow 的 step 日志可见」在 YAML 断言中完全缺失，进一步证实 YAML 未实现嵌套调用。

