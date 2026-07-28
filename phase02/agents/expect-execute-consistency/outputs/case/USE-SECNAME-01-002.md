# USE-SECNAME-01-002  - **标题**: Secret 名称以数字开头时应给出命名规则错误   - **维度**: usability/security   - **评级**: 断言一致

## 想测什么

系统给出命名规则提示，说明允许字符与格式

## 做了什么

- 1. 在 workflow 中引用 ${{ secrets.1SECRET }}

- - [负向] 不应仅报 Secret not found
- - [非功能] 报错中是否包含命名格式说明

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: ${{ secrets.1SECRET }}表达式求值→真实平台行为 |
| 2 | error_message | positive | must_contain=`1SECRET` | COVERED | error_message+must_contain: 错误信息可验证 |
| 3 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 命名格式说明质量需LLM评估 |
