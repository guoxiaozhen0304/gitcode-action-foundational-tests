# COMPAT-OUTCOME-01-003
- **标题**: outcome 与 conclusion 在 job 条件判断中不应互换语义
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**outcome 与 conclusion 在 job 条件判断中不应互换语义**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-035
通过标准：
1. job A 的 conclusion 为 success
2. job B 的 needs 条件应基于 conclusion 判断
3. 不应出现 outcome 与 conclusion 互换的误判
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | job-a: checkout source | uses: checkout | — | — |
| 2 | job-a: failing step tolerated | `exit 1` (continue-on-error: true) | — | 非零退出码 |
| 3 | job-b: verify job a conclusion | `echo "Job A conclusion should be success"` | — | success 消息 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status equals success (eval=llm) | positive | llm_assisted | 🔶 LLM_DEPENDENT | job 状态由 LLM 判定 |
| 2 | step_status equals failure (eval=llm) | positive | llm_assisted | 🔶 LLM_DEPENDENT | step outcome 由 LLM 判定 |
| 3 | semantic_swap eval=llm_assisted | negative | llm_assisted | 🔶 LLM_DEPENDENT | 语义互换由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
