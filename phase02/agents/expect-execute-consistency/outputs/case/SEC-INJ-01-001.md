# SEC-INJ-01-001
- **标题**: 不可信 PR 标题不可直接插进 run 脚本导致命令注入
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**PR 标题中的 shell 元字符不被解释为命令执行**
- 触发事件: `pull_request` (as untrusted_contributor)
- 规格引用: INTENT-SEC-009
通过标准：
1. 日志不含 injected_command_executed
2. run_status 为 success
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Inline PR title | `echo "PR title is ${{ atomgit.event.pull_request.title }}"` | — | PR 标题值 |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 injected_command_executed | negative | run_logs must_not_contain | ✅ GENUINE | 步骤使用 ${{ atomgit.event.pull_request.title }} → NEVER VACUOUS；不可信输入的 shell 转义由平台决定 |
| 2 | run_status success | positive | run_status equals "success" | ✅ GENUINE | 不可信 PR 标题含 shell 元字符 → 若平台正确转义则成功，否则可能导致命令注入错误 |
### 问题
(无)
---
