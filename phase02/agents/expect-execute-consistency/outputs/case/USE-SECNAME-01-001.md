# USE-SECNAME-01-001  - **标题**: Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误   - **维度**: usability/security   - **评级**: 断言一致

## 想测什么

系统在校验或运行时给出明确的命名规则提示，区分名称违规与未配置

## 做了什么

- 1. 在 workflow 中引用 ${{ secrets.ATOMGIT_TOKEN }}

- - [负向] 不应仅报 Secret not found
- - [非功能] 报错中是否包含 Secret 名称规则、大写字母/数字/下划线、不得以 ATOMGIT_ 开头等提示

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | negative | equals=`COMPLETED` | COVERED | negative+run_status: ${{ secrets.ATOMGIT_TOKEN }}表达式求值→真实平台行为; 应拒绝保留前缀名 |
| 2 | error_message | positive | must_contain=`ATOMGIT_TOKEN` | COVERED | error_message+must_contain: 错误信息可验证 |
| 3 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | nonfunctional+llm_assisted: 命名规则提示质量需LLM评估 |
