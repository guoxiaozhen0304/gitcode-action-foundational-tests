# USE-LBL-01-003

- **标题**: runs-on 标签写法跨文档形态扫描（同一字段不应出现三种以上互斥形态）
- **维度**: 易用性
- **优先级**: P0
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**runs-on 标签写法跨文档形态扫描（同一字段不应出现三种以上互斥形态）**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-031

通过标准：
1. type=negative, target=documentation, eval=deterministic
2. type=nonfunctional, target=documentation, eval=deterministic

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
| 1 | documentation | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |
| 2 | documentation | nonfunctional | eval=deterministic | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---