# COMPAT-OUTCOME-01-001
- **标题**: continue-on-error false 时 outcome 与 conclusion 应均为 failure
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 continue-on-error: false（默认）时失败的 step，其 outcome 和 conclusion 均为 failure。

## 做了什么
step 设置 `continue-on-error: false` 并 `exit 1`，后续 step 以 `always()` 条件执行 check。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status | positive | llm_assisted rubric "equals failure" | LLM_DEPENDENT | outcome 值需 LLM 辅助判断 |
| 2 | step_conclusion | positive | llm_assisted rubric "equals failure" | LLM_DEPENDENT | conclusion 值需 LLM 辅助判断 |
| 3 | run_status | positive | llm_assisted rubric "equals failure" | LLM_DEPENDENT | job 整体状态需 LLM 辅助判断 |
