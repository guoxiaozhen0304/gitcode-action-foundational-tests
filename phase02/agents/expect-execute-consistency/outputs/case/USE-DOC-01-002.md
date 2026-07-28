# USE-DOC-01-002
- **标题**: stages 与 stages 内 jobs 字段语法跨文档四种形态互相矛盾的扫描
- **维度**: usability
- **评级**: 断言一致

## 想测什么
文档应给出 stages 与 jobs 的唯一权威形态定义；同页不应自相矛盾。

## 做了什么
workflow: null。纯文档验证用例，断言指向 documentation 确定性 grep/diff。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | eval:deterministic | COVERED | 文档 grep stages/jobs 形态组合数检查，确定性比对 |
| 2 | documentation | nonfunctional | eval:deterministic | COVERED | 单一权威形态定义检查 |
