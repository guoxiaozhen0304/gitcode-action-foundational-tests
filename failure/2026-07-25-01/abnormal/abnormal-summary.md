# Abnormal 总结 · 2026-07-25-01

## COMPILE_ERROR（7 条）

| 原因 | 数量 | 用例 |
|---|---|---|
| cron 表达式不合法 | 3 | COMP-SCHEDULE-01-001/002/003 |
| fault_injection 冲突 | 2 | REL-FAULT-01-034/035 |
| 缺 jobs | 1 | COMP-WFLOW-01-064 |
| step name 非法字符 | 1 | REL-OUTPUT-01-017 |

**倾向**: 用例问题——YAML 自身缺陷，需 Phase 01 修复。

## ENV_ERROR（11 条）

全为 dispatch_workflow HTTP 400——workflow YAML 含 token 操作/嵌套调用等被 dispatch API 拒绝。

## TIMEOUT（27 条）

18 条为 push/PR/dispatch 触发后在队列中长时间等待（301-424s），9 条为 harness 300s 超时截断。

## INCONCLUSIVE（1 条）

COMPAT-PERM-01-002: fork_pr 需第二 GitCode 账号。
