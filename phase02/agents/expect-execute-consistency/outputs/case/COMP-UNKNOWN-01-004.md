# COMP-UNKNOWN-01-004
- **标题**: select 与 selected_by_default 声明时的实际行为记录
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**select: selected_by_default 的实际行为（与未声明是否等价）及 select 与 if 并存时的求值顺序**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-021
通过标准：
1. 逐字记录 select 字段的处理方式
2. 不应出现字段看似声明实则被静默忽略且无提示
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Mark beta | `echo "SELECT_JOB_RAN"` | — | SELECT_JOB_RAN |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | select_handling 行为记录 | nonfunctional | llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 逐字分析 select 字段处理结果 |
| 2 | run_logs 静默忽略检测 | negative | llm_assisted | 🔶 LLM_DEPENDENT | 需 LLM 判断 select 是否被静默忽略 |
### 问题
(无 — 所有断言均为 LLM 辅助评估，自动化判定不适用)
---
