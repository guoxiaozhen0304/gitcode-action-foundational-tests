# Abnormal 总结 · 2026-07-24-valid297-final2

## COMPILE_ERROR（63 条）

| 原因 | 数量 | 说明 |
|---|---|---|
| intent_ref 格式不合规 | 54 | 新增用例使用 KEEP-TC-* 等格式 |
| runs-on 格式不合规 | 6 | 非数组格式（字符串/NoneType） |
| fault_injection 声明错误 | 2 | teardown.reset 不兼容 |
| step name 非法字符 | 1 | 含 `+` 号 |

**倾向**: 用例问题——54/63 需 Phase 01 修复 intent_ref 使其匹配 schema 规范。

## TIMEOUT（16 条）

| 维度 | 数量 | 原因 |
|---|---|---|
| reliability | 10 | 长时测试（350min）被 harness 300s 截断 + dispatch 排队 |
| security | 3 | fork PR / comment 触发超时 |
| compatibility | 2 | push 队列 |
| completeness | 1 | push 队列 |

**倾向**: 环境问题——harness 全局 300s 超时是主要原因。长时测试需要 per-case 超时白名单。

## ENV_ERROR（4 条）

全为 dispatch_workflow HTTP 400——workflow YAML 含 token 操作/invalid input 被 dispatch API 拒绝。

## INCONCLUSIVE（1 条）

fork_pr 需要第二个 GitCode 账号/Token 模拟 fork PR 场景。
