# USE-DOC-01-003
- **标题**: trigger-events 每分钟 cron 示例与最短间隔 5 分钟声明自相矛盾
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
文档不应在最短间隔 5 分钟提示下方仍给出每分钟 cron 示例。

## 做了什么
workflow 提交每分钟 cron `schedule: - cron: "* * * * *"`，观测平台接受/拒绝行为。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | 文档不应在最短间隔 5 分钟声明下仍给每分钟 cron 示例 | COVERED | 文档扫描 + 平台行为观测，确定性比对 |
| 2 | validation_result | positive | 记录平台对 cron 的接受/拒绝行为 | COVERED | 提交 schedule workflow，平台 validation 可观测 |

