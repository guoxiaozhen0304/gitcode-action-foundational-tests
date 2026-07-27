# SEC-FORK-01-001
- **标题**: fork PR 触发 pull_request 时不可读取项目 secrets
- **维度**: 安全性
- **优先级**: P0
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**fork PR 下 secrets 不可访问，日志不含 secret 明文**
- 触发事件: `pull_request` (as untrusted_contributor)
- 规格引用: INTENT-SEC-001
通过标准：
1. 日志不含 DEPLOY_TOKEN 明文
2. run_status 为 completed_or_blocked
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Try access secret | `echo "secret value is ${{ secrets.DEPLOY_TOKEN }}"` | — | secret 值或空/*** |
| 2 | Print env | `env \| grep DEPLOY_TOKEN \|\| echo "not found"` | — | DEPLOY_TOKEN env 状态 |

## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | untrusted_contributor |
| Repo 环境 | with-secrets |
| Secrets | DEPLOY_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 DEPLOY_TOKEN 明文 | negative | run_logs must_not_contain_secret | ✅ GENUINE | 步骤使用 ${{ secrets.DEPLOY_TOKEN }} → NEVER VACUOUS；fork PR 下平台脱敏/隔离机制决定 |
| 2 | completed_or_blocked | positive | run_status equals | ✅ GENUINE | fork PR 下 secret 隔离 → job 可能被阻止或完成（secret 为空继续执行） |
### 问题
(无)
---
