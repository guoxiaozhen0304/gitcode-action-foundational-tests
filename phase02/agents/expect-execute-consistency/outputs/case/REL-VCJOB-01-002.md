# REL-VCJOB-01-002
- **标题**: 大规模 vcjob 并发提交（≥50）无丢失、无级联失败
- **维度**: reliability
- **评级**: 断言一致

## 想测什么
并发提交50个vcjob，确保全部有任务记录、全部进入终态、无静默丢失、无级联失败。

## 做了什么
workflow=null（平台操作型，harness 编排 vcjob 批量提交与对账），断言 vcjob_terminal_reconciliation、lost_count、cascading_failure。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | vcjob_terminal_reconciliation | positive | submitted==recorded==terminal==50 | COVERED | 与文本"提交数=任务记录数=终态数=50"精确对应；GENUINE（harness 对账） |
| 2 | lost_count | negative | equals 0 | COVERED | 对应"无静默丢失"；harness 负向断言确定性覆盖 |
| 3 | cascading_failure | nonfunctional | llm_assisted | COVERED | 对应"不出现级联失败"；LLM 辅助 = 断言一致 |
