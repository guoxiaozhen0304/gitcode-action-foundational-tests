# USE-EXPR-01-001  - **标题**: 引用不存在的上下文属性时报错应包含原始表达式与错误类型   - **维度**: usability/compatibility   - **评级**: 断言一致

## 想测什么

报错包含原始表达式字符串和错误类型说明（undefined property / unknown context）

## 做了什么

- 1. 在 run 步骤中使用 ${{ atomgit.nonexistent_property }}

- - [负向] 不应静默求值为空字符串
- - [非功能] 报错中是否包含原始表达式和错误位置

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: ${{ atomgit.nonexistent_property }}表达式真实求值→应失败; 平台状态可观察 |
| 2 | error_message | positive | must_contain=`nonexistent_property` | COVERED | error_message+must_contain: 错误信息从平台运行日志获取 |
| 3 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 报错文案质量需LLM辅助评估 |
