# USE-TYPE-01-003  - **标题**: pull_request_comment 与 pr_comment 事件名双轨的文档说明   - **维度**: usability   - **评级**: 断言一致

## 想测什么

平台若接受别名，文档应显式声明等价关系；若不接受，应明确报错而非静默忽略

## 做了什么

- 1. 用样本中的别名事件名提交 workflow
- 2. 记录平台是否识别该别名及触发行为
- 3. 检查文档是否说明两个事件名的关系

- - [正向] 记录平台对别名事件名的识别情况
- - [负向] 文档只提一个事件名而样本用另一个且无任何说明即不合格

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | validation_result | positive | eval=deterministic | COVERED | validation_result+deterministic: 记录平台对pr_comment别名接受情况→可确定性验证 |
| 2 | documentation | negative | eval=deterministic | COVERED | documentation+deterministic: 事件名文档覆盖度确定性检查 |
