# SEC-AUDIT-01-001
- **标题**: 敏感操作（secret/权限/rerun/审批/评论触发）必须全部留有不可擦除的审计记录
- **维度**: security
- **评级**: 断言一致

## 想测什么
各类敏感操作审计记录覆盖率100%，操作者本人不可删除/篡改审计记录。

## 做了什么
workflow=null（平台操作型），harness 通过 API 执行 ops 列表中的敏感操作并对账审计记录。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | audit_log | positive | equals "records_present_all_op_classes" | COVERED | 对应"各类敏感操作审计记录覆盖率100%"；harness 审计接口对账 |
| 2 | sensitive_op_without_trace_detected | negative | equals "true" | COVERED | 对应"敏感操作绝不应无痕发生"；negative + equals true 语义="不应出现" |
| 3 | operator_audit_delete_accepted | negative | equals "true" | COVERED | 对应"审计记录绝不应可被操作者本人删除或篡改"；harness 判定 |
| 4 | audit_log | nonfunctional | equals "retention_and_export_determinable" | COVERED | 对应"保留期与导出能力可判定" |
