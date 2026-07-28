# USE-MASK-01-002
- **标题**: 直接 echo secrets 值时文档描述的绕过风险与实际一致
- **维度**: 易用性/安全性
- **评级**: 断言一致

## 想测什么
验证直接在 run 中 `echo ${{ secrets.TEST_SECRET }}` 时文档声明的脱敏绕过风险与实际行为是否一致，以及文档是否给出缓解建议。

## 做了什么
workflow 在 run 中直接 echo secrets 值（未通过 env 中转）。断言依赖 LLM 分析日志和文档一致性。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | nonfunctional | 文档风险声明与实际行为一致且给出缓解建议 | UNVERIFIABLE | eval: llm_assisted，全 LLM_DEPENDENT；Rule 9: 仅含 LLM_DEPENDENT → 断言一致 |
