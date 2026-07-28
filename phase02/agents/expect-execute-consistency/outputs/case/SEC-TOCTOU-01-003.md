# SEC-TOCTOU-01-003
- **标题**: 评论触发后被编辑的内容绝不应改变已排队/运行中 workflow 读取的事件负载
- **维度**: security
- **评级**: 部分不符

## 想测什么
created 触发读取到触发时刻内容；触发后编辑评论不应改变已排队/运行中 workflow 的事件负载。

## 做了什么
step1 echo "COMMENT_SNAPSHOT..."，step2 sleep 60 后 echo "POST_EDIT_READ..."。均未输出断言期望的具体字符串。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | equals:trigger_time_snapshot_consistent | VACUOUS | step 不输出该字符串，仅输出 COMMENT_SNAPSHOT / POST_EDIT_READ 标记 |
| 2 | run_logs | negative | must_not_contain:edited_content_adopted | VACUOUS | step 从不输出该字符串 |
| 3 | trigger_audit | nonfunctional | equals:audit_comment_matches_trigger_time | LLM_DEPENDENT | nonfunctional 类型 + 审计目标，需 LLM 辅助判定 |
