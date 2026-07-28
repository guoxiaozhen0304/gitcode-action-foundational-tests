# USE-EXPR-01-004  - **标题**: 未文档化函数 default() 的文档缺失 diff（与平台行为断言合并证据链）   - **维度**: usability   - **评级**: 断言一致

## 想测什么

平台支持的函数应在函数表有完整条目；函数表函数名集合应包含样本实际出现的函数名集合

## 做了什么

- 1. 抽取样本中实际出现的表达式函数名集合
- 2. 与 expressions.md 函数表函数名集合做包含检查
- 3. 提交含 default() 条件表达式的探针 workflow 记录求值行为

- - [负向] 函数表缺少样本实际使用的函数每 1 个即一条缺陷
- - [正向] 记录 default() 的实际求值结果
- - [非功能] 若为内部函数，文档应说明不建议使用

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | eval=deterministic | COVERED | run_logs+deterministic: if: ${{ default() }}表达式求值→GENUINE; 记录求值结果 |
| 2 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 函数表集合diff确定性检查 |
