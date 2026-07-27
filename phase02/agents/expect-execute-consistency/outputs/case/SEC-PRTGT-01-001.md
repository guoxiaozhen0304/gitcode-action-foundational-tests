# SEC-PRTGT-01-001
- **标题**: pull_request_target 下显式 checkout 不可信 PR 时 secrets 仍应受控
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**pull_request_target 中 checkout fork PR head 后 secret 不可被脚本直接读取**
- 触发事件: `pull_request_target` (as maintainer)
- 规格引用: INTENT-SEC-002
通过标准：
1. 日志不含 DEPLOY_TOKEN 明文
2. run_status 为 blocked_or_pending
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Checkout PR head | `uses: checkout` with ref: ${{ atomgit.event.pull_request.head.sha }} | — | fork 代码 checkout |
| 2 | Attempt secret access | `echo "secret is ${{ secrets.DEPLOY_TOKEN }}"` | — | secret 值或脱敏 |

## 3. 触发与运行环境
| 触发事件 | pull_request_target |
| 触发身份 | maintainer |
| Repo 环境 | with-secrets |
| Secrets | DEPLOY_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 DEPLOY_TOKEN 明文 | negative | run_logs must_not_contain_secret | ✅ GENUINE | uses: checkout + ${{ secrets.DEPLOY_TOKEN }} + ${{ atomgit.event... }} → NEVER VACUOUS |
| 2 | blocked_or_pending | positive | run_status equals | ⚠️ STATUS_GUARANTEED | 步骤无非 0 退出路径，step 不会主动使 job 挂起；审批状态由平台控制 |
### 问题
断言 2 STATUS_GUARANTEED：echo 成功执行后必然 success，除非平台审批机制在 job 级拦截。
---
