# USE-EXPR-01-002
- **标题**: 调用未知函数时报错应提示函数名错误与修正方向
- **维度**: 易用性/兼容性
- **评级**: 部分不符

## 想测什么
验证在 if 条件中使用 `${{ unknownFunc() }}` 时平台应报错指出未知函数而非静默通过。

## 做了什么
workflow 在 step 的 if 条件中调用不存在的函数 `unknownFunc()`。期望平台在解析/求值阶段报错。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | 表达式含未知函数应导致校验失败 → GENUINE |
| 2 | error_message | nonfunctional | 报错含 unknownFunc 或未知函数字样 | UNVERIFIABLE | eval: llm_assisted，需 LLM 主观判断 → LLM_DEPENDENT |
