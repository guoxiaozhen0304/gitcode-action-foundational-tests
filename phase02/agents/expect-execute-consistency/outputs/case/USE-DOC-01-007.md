# USE-DOC-01-007
- **标题**: environment 字段能力描述存在而语法参考缺失及平台报错指引
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
文档能力描述与语法参考应一一对应；平台对未识别字段的报错应给出指引。

## 做了什么
workflow 中 job 定义 `environment: production` 字段，观测平台行为。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | positive | 平台应拒绝 environment 字段并报 unknown property | COVERED | 提交含 environment 字段的 workflow，平台 validation 可观测 |
| 2 | documentation | negative | using-secrets.md 描述环境级 Secret 而语法参考无 environment 条目即不合格 | COVERED | 文档扫描确定性判定 |

