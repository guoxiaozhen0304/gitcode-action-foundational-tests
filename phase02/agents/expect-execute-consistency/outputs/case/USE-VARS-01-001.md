# USE-VARS-01-001
- **标题**: vars 上下文在文档与样本中的声明必须一致
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
检查 context.md 与 workflow-samples 对 vars 上下文的支持声明是否一致——要么均支持，要么均不支持。

## 做了什么
纯文档检查用例（workflow: null）。LLM 辅助对比文档与样本注释对 vars 的支持声明。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | nonfunctional | 文档与样本对 vars 上下文的声明必须一致 | UNVERIFIABLE | eval: llm_assisted，全 LLM_DEPENDENT；Rule 9 → 断言一致 |
