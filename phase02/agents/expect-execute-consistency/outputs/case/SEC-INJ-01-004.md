# SEC-INJ-01-004
- **标题**: 不可信 commit message 不可直接插进 run 脚本导致命令注入
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**commit message 中的反问号/分号不被解释为 shell 命令**
- 触发事件: `push` (as untrusted_contributor)
- 规格引用: INTENT-SEC-012
通过标准：
1. 日志不含 injected_command_executed
2. run_status 为 success
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Inline commit message | `echo "Message is ${{ atomgit.event.commits[0].message }}"` | — | commit message |

## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | untrusted_contributor |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 injected_command_executed | negative | run_logs must_not_contain | ✅ GENUINE | ${{ atomgit.event.commits[0].message }} → NEVER VACUOUS |
| 2 | run_status success | positive | run_status equals "success" | ✅ GENUINE | commit message 含 shell 元字符 → 平台转义决定 |
### 问题
(无)
---
