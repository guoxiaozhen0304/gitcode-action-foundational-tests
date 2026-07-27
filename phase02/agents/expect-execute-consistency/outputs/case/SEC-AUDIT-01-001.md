# SEC-AUDIT-01-001

- **标题**: 敏感操作（secret/权限/rerun/审批/评论触发）必须全部留有不可擦除的审计记录
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**敏感操作（secret/权限/rerun/审批/评论触发）必须全部留有不可擦除的审计记录**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-046

通过标准：
1. type=positive, target=audit_log, equals=records_present_all_op_classes
2. type=negative, target=audit_log
3. type=negative, target=audit_log
4. type=nonfunctional, target=audit_log, equals=retention_and_export_determinable

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | audit_log | positive | equals=records_present_all_op_classes | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | audit_log | negative |  | ✅ GENUINE | 通用断言匹配 |
| 3 | audit_log | negative |  | ✅ GENUINE | 通用断言匹配 |
| 4 | audit_log | nonfunctional | equals=retention_and_export_determinable | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 4 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---