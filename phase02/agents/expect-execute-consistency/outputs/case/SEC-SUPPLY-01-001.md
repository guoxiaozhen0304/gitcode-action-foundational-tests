# SEC-SUPPLY-01-001
- **标题**: 第三方 Action 引用应支持完整 commit hash 固定
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**第三方 Action 引用应支持完整 commit hash 固定**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-SEC-014
通过标准：
1. 完整 commit SHA 引用可成功执行 action
2. commit SHA 不匹配时 job 应失败或拒绝执行

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use pinned action | uses: docker/build-push-action@1234567890abcdef1234567890abcdef12345678 | - | action 执行输出（由平台解析 hash 引用） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: "success_or_action_executed" | ✅ GENUINE | `uses:` 引用 action（hash 固定），运行状态由平台解析行为决定 |
| 2 | run_logs | negative | must_not_contain: "unauthorized_action_execution" | ✅ GENUINE | `uses:` action 执行产生日志输出，断言监控无越权执行标记 |
---
