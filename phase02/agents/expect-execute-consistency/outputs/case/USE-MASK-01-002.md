# USE-MASK-01-002  - **标题**: 直接 echo secrets 值时文档描述的绕过风险与实际一致   - **维度**: usability/security   - **评级**: 断言一致

## 想测什么

实际行为与文档声明一致；若确实可绕过，文档已给出缓解建议

## 做了什么

- 1. 在 workflow 中直接执行 echo ${{ secrets.TEST_SECRET }}

- - [负向] 若绕过确实发生，日志中可能出现明文
- - [非功能] 文档是否给出不要在 run 中直接 echo secrets 的缓解建议

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: secret绕过行为与文档一致性需LLM评估 |
