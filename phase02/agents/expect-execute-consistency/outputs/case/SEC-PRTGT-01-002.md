# SEC-PRTGT-01-002
- **标题**: pull_request_target 无审批不执行 fork PR 代码
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**pull_request_target 未审批状态下 job 挂起或拒绝，不直接执行 fork PR 的构建脚本**
- 触发事件: `pull_request_target` (as maintainer)
- 规格引用: INTENT-SEC-002
通过标准：
1. run_status 不为 success_without_approval
2. run_status 为 pending_or_blocked
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Checkout PR head | `uses: checkout` with ref: ${{ atomgit.event.pull_request.head.sha }} | — | fork 代码 checkout |
| 2 | Run build | `echo "Building PR code"` | — | 构建标记 |

## 3. 触发与运行环境
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | DEPLOY_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | != success_without_approval | negative | run_status must_not_equal | ✅ GENUINE | uses: checkout + ${{ ... }} → NEVER VACUOUS；审批状态由平台控制，可能 job 级拦截 |
| 2 | pending_or_blocked | positive | run_status equals | ⚠️ STATUS_GUARANTEED | 步骤无 exit 1 路径；echo 必然成功；若平台不拦截则必然 success |
### 问题
断言 2 STATUS_GUARANTEED：步骤无失败路径，若平台无审批拦截则必然 success。
---
