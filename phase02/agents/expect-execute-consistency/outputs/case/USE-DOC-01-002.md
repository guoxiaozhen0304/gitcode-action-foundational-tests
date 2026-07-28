# USE-DOC-01-002
- **标题**: stages 与 stages 内 jobs 字段语法跨文档四种形态互相矛盾的扫描
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
文档应给出 stages 与 jobs 的唯一权威形态定义，同页不应自相矛盾。

## 做了什么
workflow 为 null，纯文档扫描。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | 形态组合数大于 1 且无等价说明即不合格 | COVERED | grep 扫描 stages: 和 jobs 形态，确定性判定 |
| 2 | documentation | nonfunctional | workflow-file-location-structure.md 应给出单一权威形态定义 | COVERED | 文档扫描，确定性判定 |

