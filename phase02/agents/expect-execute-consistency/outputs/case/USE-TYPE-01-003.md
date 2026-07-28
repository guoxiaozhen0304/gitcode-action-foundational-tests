# USE-TYPE-01-003
- **标题**: pull_request_comment 与 pr_comment 事件名双轨的文档说明
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
验证平台对 `pr_comment` 别名事件名的接受情况，检查文档 trigger-events.md 是否说明 pr_comment 与 pull_request_comment 的关系。

## 做了什么
workflow 使用 `on: pr_comment` 别名事件名。记录平台是否接受此写法，文档侧检查是否提及别名。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_result | positive | 记录平台对 pr_comment 别名的接受情况 | COVERED | eval: deterministic，校验结果可记录 |
| 2 | documentation | negative | 文档未提及 pr_comment 别名而样本在用即不合格 | COVERED | eval: deterministic，文档搜索可程序化 |
