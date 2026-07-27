# SEC-PERM-01-004
- **标题**: 默认状态下写操作被 403 拒绝
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**默认无 permissions 时 push 返回权限拒绝**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-017
通过标准：
1. 不含 push_successful
2. push 被拒或 403
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt push without permissions | `git clone ... ; cd repo; git add/commit/push origin main \|\| echo push denied as expected` | — | push 结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 push_successful | negative | run_logs must_not_contain | ✅ GENUINE | git clone + push 使用 ${{ atomgit.token }} → NEVER VACUOUS |
| 2 | push_denied_or_403 | positive | run_logs equals | ❌ VACUOUS | git push 失败时输出 "push denied as expected"，非 "push_denied_or_403" 标签 |
### 问题
断言 2 VACUOUS：步骤输出自然语言字符串，断言期望下划线标签。
---
