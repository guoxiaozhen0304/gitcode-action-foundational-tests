# USE-CONC-01-002
- **标题**: concurrency.max 配置 -1 时报错应提示有效范围
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
concurrency.max 配置负值时 YAML 校验报错，明确说明有效范围。

## 做了什么
workflow 配置 `concurrency: max: -1`，触发时应被平台拒绝。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: COMPLETED | COVERED | 不应以 COMPLETED 状态成功（应被拒绝），平台状态可观测 |
| 2 | error_message | nonfunctional | llm_assisted | LLM_DEPENDENT | LLM 辅助判定报错是否包含有效范围说明 |

