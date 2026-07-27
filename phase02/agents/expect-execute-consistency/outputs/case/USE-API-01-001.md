# USE-API-01-001

- **标题**: API 字段值与事件类型命名同一概念分裂的对照检查
- **维度**: 易用性
- **优先级**: P2
- **评级**: 断言一致

---

## 1. 想测什么

本用例验证：**API 字段值与事件类型命名同一概念分裂的对照检查**

- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-USE-048

通过标准：
1. type=negative, target=api_response, eval=deterministic

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

## 3. 触发与运行环境

| 触发事件 | `workflow_dispatch` |
| 触发身份 | `maintainer` |
| Repo 环境 | `with-pr` |
| Secrets | `[]` |
| 故障注入 | 无 |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | api_response | negative | eval=deterministic | ✅ GENUINE | 通用断言匹配 |

---