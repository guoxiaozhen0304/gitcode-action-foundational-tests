# USE-UNKN-01-004  - **标题**: 未文档化字段 select/manual_override/code-update/顶层 inputs 的文档集合 diff   - **维度**: usability   - **评级**: 断言一致

## 想测什么

平台实际支持的每个字段都应在语法参考中有条目；样本独有且文档未提的 key 数量应为 0

## 做了什么

- 1. 抽取样本中全部 YAML key 集合
- 2. 与文档语法参考列出的合法 key 集合做 diff
- 3. 对样本独有且文档未提的 key 逐条登记

- - [负向] 样本独有且文档未提的 key 每多 1 个即一条缺陷
- - [非功能] 文档应对顶层 inputs 与 on.workflow_dispatch.inputs 的关系给出说明

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 样本key与文档key集合diff确定性检查 |
