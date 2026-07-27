# COMP-CALL-01-002

- **标题**: 3 层 workflow_call 嵌套应被拒绝
- **维度**: completeness
- **优先级**: P1
- **评级**: 完全不符

---

## 1. 想测什么

本用例验证：**3 层 workflow_call 嵌套应被拒绝**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-006

通过标准：
1. [负向] 运行不应成功完成 —— 断言 run_status != success
2. [非功能] 报错信息应清晰说明最多 2 层限制 —— 🔶 LLM_DEPENDENT（跳过）

## 2. 做了什么

| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo before call | `echo "attempting 3 layer call"` | - | 字面量字符串 |

## 3. 触发与运行环境

| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | reusable-workflow-3layer |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success | ❌ IMPOSSIBLE | workflow 仅含一条 echo 步骤，无任何 workflow_call，永远不可能失败。断言期望「不等于 success」但实际必然 success |
| 2 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 跳过 |

### 问题

**断言 1 — IMPOSSIBLE**: 标题声称测试「3 层 workflow_call 嵌套应被拒绝」，但 YAML 中完全没有嵌套调用。workflow 仅包含一个 `echo "attempting 3 layer call"`。断言期望 run_status != success（即平台应拒绝），但 workflow 只有一条 echo 必然 success。即使 fixture 有 3 层结构，此 workflow 也未实际触发它。

