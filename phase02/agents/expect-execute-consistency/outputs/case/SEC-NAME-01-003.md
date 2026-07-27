# SEC-NAME-01-003

- **标题**: 可遮蔽系统变量的 secret 命名（ATOMGIT_ 前缀/非法字符/数字开头）创建时必须被拒
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**可遮蔽系统变量的 secret 命名（ATOMGIT_ 前缀/非法字符/数字开头）创建时必须被拒**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-041

通过标准：
1. type=positive, target=secret_mgmt_api, equals=valid_name_created
2. type=negative, target=secret_mgmt_api
3. type=nonfunctional, target=error_message, eval=llm_assisted

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
| 1 | secret_mgmt_api | positive | equals=valid_name_created | ✅ GENUINE | 断言有条件可被步骤验证 |
| 2 | secret_mgmt_api | negative |  | ✅ GENUINE | 通用断言匹配 |
| 3 | error_message | nonfunctional | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 3 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---