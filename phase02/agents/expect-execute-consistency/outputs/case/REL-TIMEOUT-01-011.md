# REL-TIMEOUT-01-011
- **标题**: 自定义 timeout 超默认值——timeout-minutes=720 的接受/拒绝语义探测   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
探测 timeout-minutes=720（超默认 360 分钟）的语义：接受则验证可超 360 运行，拒绝则错误信息含上限值，不得静默截断为 360。
## 做了什么
提交 job 级 timeout-minutes=720 的 workflow，探针 step echo 标记，观察平台解析/保存/执行行为。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | config_outcome | positive | equals "accepted_or_explicitly_rejected" | COVERED | harness 判断平台行为：接受按 720 执行或明确拒绝 |
| 2 | silent_truncation_to_360_detected | negative | equals "true" | COVERED | harness 检测静默截断为 360 的情况 |
| 3 | rejection_error_contains_limit | nonfunctional | equals "true_if_rejected" | COVERED | harness 检查拒绝时的错误信息是否含实际上限值 |
