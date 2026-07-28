# USE-RUN-01-002  - **标题**: 使用单标签 ubuntu-latest 时报错应给出三段式格式指引   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

系统在校验或调度阶段报错，给出三段式标签格式示例或可用标签列表

## 做了什么

- 1. 在 job 中写 runs-on: [ubuntu-latest]

- - [负向] 不应无限 queued 且无提示
- - [非功能] 报错中应包含三段式或 default 等关键词

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: runs-on:[ubuntu-latest]格式不完整→平台应拒绝 |
| 2 | error_message | positive | must_contain=`runs-on` | COVERED | error_message+must_contain: 报错信息可验证 |
| 3 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 报错指引质量需LLM评估 |
