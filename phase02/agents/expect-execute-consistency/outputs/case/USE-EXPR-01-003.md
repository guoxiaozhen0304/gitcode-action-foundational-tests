# USE-EXPR-01-003
- **标题**: expressions 函数表语法标记可解析性与状态关键字术语区分
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
检查 expressions.md 函数表中语法列是否存在无法通过表达式 parser 的字符串（如多余括号），以及文档是否把无括号状态关键字与真正函数混称而不加区分。

## 做了什么
纯文档检查用例（workflow: null）。对 expressions.md 函数表语法列做括号配平与词法检查，扫描关键词确认 success/failed/always/cancelled 是否被混入函数一节。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | 函数表语法列含多余括号等不可解析字符串即不合格 | COVERED | eval: deterministic，可程序化做括号配平与词法检查 |
| 2 | documentation | negative | 状态关键字被列为函数且无说明即不合格 | COVERED | eval: deterministic，字符串扫描可判定 |
