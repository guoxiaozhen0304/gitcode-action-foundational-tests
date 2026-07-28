# USE-YAML-01-001  - **标题**: 缺少必填字段 on 时报错应指出具体字段名与位置   - **维度**: usability   - **评级**: 断言一致

## 想测什么

报错包含文件名、出错行号、缺少字段名，最好给出正确写法示例

## 做了什么

- 1. 提交一个缺少 on 字段的 workflow

- - [负向] 不应仅报泛化 YAML parse error
- - [非功能] 报错中是否同时包含字段名与所在行号

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: workflow缺失on字段→畸形YAML→平台应拒绝; batch_validate可验证 |
| 2 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 报错信息完整度需LLM评估 |
