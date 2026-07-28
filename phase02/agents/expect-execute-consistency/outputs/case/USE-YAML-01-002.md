# USE-YAML-01-002
- **标题**: YAML 缩进错误时报错应指出具体行号与列号
- **维度**: 易用性
- **评级**: 部分不符

## 想测什么
验证提交 steps 缩进不一致的 workflow 时平台应报错并指出具体行号与列号，不应仅报泛化 YAML parse error。

## 做了什么
workflow 中第二个 step 缩进不一致（少了一个空格）故意制造 YAML 缩进错误。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | YAML 缩进错误应导致解析失败 → GENUINE |
| 2 | error_message | nonfunctional | 报错含行号与列号 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
