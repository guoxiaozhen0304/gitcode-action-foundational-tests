# USE-STAT-01-002
- **标题**: 使用 success() 带括号时报错应提示 GitCode 括号差异
- **维度**: 易用性/兼容性
- **评级**: 部分不符

## 想测什么
验证在 step 中使用 `if: ${{ success() }}`（GitCode 状态函数不应带括号）时平台应报错并提示 GitCode 状态函数不带括号。

## 做了什么
workflow 在 step 中使用 `if: ${{ success() }}`。期望平台在解析/校验阶段报错。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | 错误的状态函数写法应导致校验失败 → GENUINE |
| 2 | error_message | nonfunctional | 报错提示 GitCode 状态函数不带括号 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
