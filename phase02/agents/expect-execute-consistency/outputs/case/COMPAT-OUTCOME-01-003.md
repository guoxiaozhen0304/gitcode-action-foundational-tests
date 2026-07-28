# COMPAT-OUTCOME-01-003
- **标题**: outcome 与 conclusion 在 job 条件判断中不应互换语义
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
测试 outcome（真实执行结果）与 conclusion（最终判定）不被互换使用——needs 条件应基于 conclusion 判断。

## 做了什么
job A 含 continue-on-error: true 且失败的 step；job B 通过 needs 依赖 job A，验证 job B 仍可执行（因 conclusion=success）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | job_status | positive | llm_assisted rubric | LLM_DEPENDENT | job conclusion 语义需 LLM 辅助判断 |
| 2 | step_status | positive | llm_assisted rubric | LLM_DEPENDENT | step outcome 保持 failure 需 LLM 辅助判断 |
| 3 | semantic_swap | negative | llm_assisted rubric | LLM_DEPENDENT | outcome/conclusion 互换误判需 LLM 辅助判断 |
