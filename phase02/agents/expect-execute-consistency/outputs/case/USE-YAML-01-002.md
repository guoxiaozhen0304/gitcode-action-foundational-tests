# USE-YAML-01-002  - **标题**: YAML 缩进错误时报错应指出具体行号与列号   - **维度**: usability   - **评级**: 断言一致

## 想测什么

报错包含具体的行号、列号，指出缩进错误位置

## 做了什么

- 1. 提交一个 steps 缩进错误的 workflow

- - [负向] 不应仅报泛化 YAML parse error
- - [非功能] 报错中是否包含行号与列号

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: YAML缩进错误→平台应拒绝; batch_validate可验证 |
| 2 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 报错行号列号准确性需LLM评估 |
