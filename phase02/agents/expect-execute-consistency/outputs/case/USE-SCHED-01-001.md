# USE-SCHED-01-001
- **标题**: schedule 不触发时的可观测提示（判定方式：llm_assisted）
- **维度**: 易用性/可靠性
- **评级**: 断言一致

## 想测什么
验证 schedule 未触发时平台不应完全静默——workflow 列表应显示下次预计触发时间，跳过的触发应留记录并附原因。

## 做了什么
workflow 配置 cron schedule，触发方式为 schedule 事件。断言依赖 LLM 判断 UI 可观测性。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | ui | negative | schedule 未触发时平台不应完全静默 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
| 2 | ui | nonfunctional | UI 信息可区分 cron 写错与平台故障，显示预计触发时间 | UNVERIFIABLE | eval: llm_assisted，全 LLM_DEPENDENT；Rule 9 → 断言一致 |
