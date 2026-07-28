# USE-UNKN-01-004
- **标题**: 未文档化字段 select/manual_override/code-update/顶层 inputs 的文档集合 diff
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
抽取真实样本中全部 YAML key，与文档语法参考列出的合法 key 集合做 diff，检查 select、manual_override、code-update、顶层 inputs 等样本独有 key 是否被文档遗漏。

## 做了什么
纯文档检查用例（workflow: null）。对样本 YAML key 集合与文档合法 key 集合做 diff。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | 样本独有且文档未提的 key 数量应为 0 | COVERED | eval: deterministic，集合 diff 可程序化 |
