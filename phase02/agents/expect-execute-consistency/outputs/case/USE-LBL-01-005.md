# USE-LBL-01-005
- **标题**: runs-on 含资源池名写法的文档资源池清单 diff
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
检查真实样本中出现的资源池名（如 dedicate-hosted、codearts-hosted 等）是否全部被 selecting-runner-labels.md 文档列出。

## 做了什么
纯文档检查用例（workflow: null）。从样本抽取资源池名集合，与文档清单做包含检查。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | 样本资源池名不在文档清单内即缺陷 | COVERED | eval: deterministic，集合包含检查可程序化 |
