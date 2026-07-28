# USE-NEST-01-001  - **标题**: workflow_call 嵌套 3 层时报错应明确提示上限为 2 层   - **维度**: usability   - **评级**: 断言一致

## 想测什么

系统在校验或调度阶段报错，明确说明 workflow_call 嵌套层数超过 GitCode 上限 2 层

## 做了什么

- 1. 主 workflow 调用 A，A 调用 B，B 调用 C

- - [负向] 不应静默失败或卡死
- - [非功能] 报错中是否包含 workflow_call、嵌套、2 层、上限等关键词

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: uses:嵌套3层→平台应拒绝; 状态可观察 |
| 2 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 报错关键词完整度需LLM评估 |
