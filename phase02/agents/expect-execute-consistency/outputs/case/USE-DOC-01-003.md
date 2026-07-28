# USE-DOC-01-003
- **标题**: trigger-events 每分钟 cron 示例与最短间隔 5 分钟声明自相矛盾
- **维度**: usability
- **评级**: 断言一致

## 想测什么
文档不应在最短间隔 5 分钟提示下方仍给出每分钟 cron 示例。

## 做了什么
workflow 配置 `cron: "* * * * *"`（每分钟），step `echo "scheduled"`。断言检查 documentation 和 validation_result。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | eval:deterministic | COVERED | 文档自相矛盾检查，确定性比对 |
| 2 | validation_result | positive | eval:deterministic | COVERED | 平台对每分钟 cron 的接受/拒绝行为记录，与文档声明比对 |
