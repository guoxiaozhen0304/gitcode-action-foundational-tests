# USE-DOC-01-007
- **标题**: environment 字段能力描述存在而语法参考缺失及平台报错指引
- **维度**: usability
- **评级**: 断言一致

## 想测什么
文档能力描述与语法参考应对应；平台对未识别字段的报错应给出是否未来支持的指引。

## 做了什么
workflow 配置 `environment: production`，step `echo "deploy"`。断言检查 error_message 和 documentation。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | positive | eval:deterministic | COVERED | 平台应拒绝 environment 字段并报错；记录报错文本供指引质量判定 |
| 2 | documentation | negative | eval:deterministic | COVERED | 文档能力描述与语法参考一致性检查 |
