# USE-SECNAME-01-002
- **标题**: Secret 名称以数字开头时应给出命名规则错误
- **维度**: 易用性/安全性
- **评级**: 部分不符

## 想测什么
验证引用以数字开头的 secret 名称时平台应报错并给出命名格式说明，不应仅报 Secret not found。

## 做了什么
workflow 引用 `${{ secrets.1SECRET }}`（数字开头不合法）。期望平台在校验或运行时给出命名规则错误。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | 非法 secret 名称应触发错误 → GENUINE |
| 2 | error_message | nonfunctional | 报错含命名格式说明 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
