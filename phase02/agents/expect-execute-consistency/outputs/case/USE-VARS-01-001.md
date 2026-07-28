# USE-VARS-01-001  - **标题**: vars 上下文在文档与样本中的声明必须一致   - **维度**: usability   - **评级**: 断言一致

## 想测什么

两者声明一致：要么均支持，要么均不支持

## 做了什么

- 1. 比对 syntax-reference/context.md 与 workflow-samples 注释对 vars 的支持声明

- - [正向] 若支持，文档示例可运行且样本注释已移除已知不支持
- - [负向] 若不支持，文档中不应出现 vars 使用示例

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | documentation | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | documentation+llm_assisted: 文档与样本vars声明一致性需LLM评估 |
