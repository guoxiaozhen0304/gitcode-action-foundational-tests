# SEC-TOCTOU-01-003
- **标题**: 评论触发后被编辑的内容绝不应改变已排队/运行中 workflow 读取的事件负载
- **维度**: 安全性
- **评级**: 断言一致

## 想测什么
触发后编辑评论绝不应改变运行中 workflow 的事件负载，edited 事件作为新事件独立重新评估。

## 做了什么
workflow 使用 pull_request_comment 触发（types: created, edited），step 中 sleep 60s 留编辑竞态窗口。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | trigger_time_snapshot_consistent | COVERED | 真实命令 sleep + echo，harness 验证触发时刻快照一致性 |
| 2 | run_logs | negative | must_not_contain: edited_content_adopted | COVERED | 平台日志验证，编辑后内容不应被本次执行采纳 |
| 3 | trigger_audit | nonfunctional | audit_comment_matches_trigger_time | UNVERIFIABLE | 平台审计面验证，workflow 无对应产生物 |

