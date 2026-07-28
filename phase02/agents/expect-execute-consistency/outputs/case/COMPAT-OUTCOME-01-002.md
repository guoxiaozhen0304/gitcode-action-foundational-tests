# COMPAT-OUTCOME-01-002
- **标题**: continue-on-error true 时 outcome 应为 failure 而 conclusion 应为 success
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 continue-on-error: true 时失败的 step，outcome 为 failure 但 conclusion 被覆盖为 success。

## 做了什么
step 设置 `continue-on-error: true` 并 `exit 1`，后续 step echo "This step should run"。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | step_status | positive | llm_assisted rubric "equals failure" | LLM_DEPENDENT | outcome 值需 LLM 辅助判断 |
| 2 | step_conclusion | positive | llm_assisted rubric "equals success" | LLM_DEPENDENT | conclusion 值需 LLM 辅助判断 |
| 3 | run_status | positive | llm_assisted rubric "equals success" | LLM_DEPENDENT | job 整体状态需 LLM 辅助判断 |
