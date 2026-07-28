# USE-CONT-01-001
- **标题**: container.image 文档声明可用与实际可用性的一致性
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
文档出现的 container.image 字段与实际平台可用性一致；未 GA 能力应显式标注。

## 做了什么
workflow 配置 `container: image: "ubuntu:22.04"`，提交后观测平台行为。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result | positive | 记录平台对 container.image 的实际处理行为 | COVERED | 真实 workflow 提交，平台接受/忽略/报错均在 validation_result 中可观测 |
| 2 | documentation | negative | 文档字段集合与实际可用字段集合一致 | COVERED | harness 对文档与平台实际行为做 diff |

