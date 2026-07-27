# SEC-INJ-01-002
- **标题**: 不可信分支名不可直接插进 run 脚本导致命令注入
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**分支名中的 shell 元字符不被解释为命令**
- 触发事件: `pull_request` (as untrusted_contributor)
- 规格引用: INTENT-SEC-010
通过标准：
1. 日志不含 injected_command_executed
2. run_status 为 success
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Inline branch name | `echo "Branch is ${{ atomgit.head_ref }}"` | — | 分支名 |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 injected_command_executed | negative | run_logs must_not_contain | ✅ GENUINE | ${{ atomgit.head_ref }} → NEVER VACUOUS |
| 2 | run_status success | positive | run_status equals "success" | ✅ GENUINE | 分支名含 shell 元字符 → 平台转义行为决定 |
### 问题
(无)
---
