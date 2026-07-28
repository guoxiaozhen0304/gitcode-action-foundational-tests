# USE-CONT-01-001
- **标题**: container.image 文档声明可用与实际可用性的一致性
- **维度**: usability
- **评级**: 断言一致

## 想测什么
文档出现的 container.image 字段应与平台实际可用字段一致；未 GA 能力应显式标注。

## 做了什么
workflow 配置 `container: image: "ubuntu:22.04"`，step `echo "in-container"`。断言检查 validation_result 和 documentation。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result | positive | eval:deterministic | COVERED | 平台对 container.image 的处理行为可观察记录 |
| 2 | documentation | negative | eval:deterministic | COVERED | 文档字段集合与实际可用字段 diff 检查 |
