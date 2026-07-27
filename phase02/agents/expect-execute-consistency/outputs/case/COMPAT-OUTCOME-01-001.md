# COMPAT-OUTCOME-01-001
- **标题**: continue-on-error false 时 outcome 与 conclusion 应均为 failure
- **维度**: 兼容性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**continue-on-error false 时 outcome 与 conclusion 应均为 failure**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMPAT-035
通过标准：
1. 失败 step 的 outcome 为 failure
2. 失败 step 的 conclusion 为 failure
3. job 整体状态为 failure
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | checkout source | uses: checkout | — | — |
| 2 | failing step | `exit 1` (continue-on-error: false) | — | 非零退出码 |
| 3 | check status | `echo "Check step outcome and conclusion"` | `${{ always() }}` | 检查信息 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | 无 |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status equals failure (eval=llm) | positive | llm_assisted | 🔶 LLM_DEPENDENT | step outcome 由 LLM 判定 |
| 2 | step_conclusion equals failure (eval=llm) | positive | llm_assisted | 🔶 LLM_DEPENDENT | step conclusion 由 LLM 判定 |
| 3 | run_status equals failure (eval=llm) | positive | llm_assisted | 🔶 LLM_DEPENDENT | job 失败状态由 LLM 判定 |
### 问题
全部断言均为 LLM_DEPENDENT
---
