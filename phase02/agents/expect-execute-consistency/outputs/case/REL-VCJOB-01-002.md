# REL-VCJOB-01-002
- **标题**: 大规模 vcjob 并发提交（≥50）无丢失、无级联失败   - **维度**: 可靠性   - **评级**: 部分不符
## 想测什么
验证大规模(50个)vcjob并发提交时无静默丢失、无级联失败，提交数=记录数=终态数。
## 做了什么
YAML中workflow:null，trigger为manual事件，参数指定platform_op=vcjob_batch_submit、concurrency=50。无实际workflow步骤，依赖harness/平台侧编排批量提交和对账。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | vcjob_terminal_reconciliation | positive | submitted==recorded==terminal==50 | COVERED | 平台操作可观测，等于断言目标明确 |
| 2 | vcjob_records | negative | 不应出现静默丢失 | UNVERIFIABLE | eval:llm_assisted，rubric明确需要"oracle仅有xlsx预期结果列"，依赖LLM判定 |
| 3 | cascading_failure | nonfunctional | 不应出现级联失败 | UNVERIFIABLE | eval:llm_assisted，级联失败的归因判定需要LLM辅助 |
