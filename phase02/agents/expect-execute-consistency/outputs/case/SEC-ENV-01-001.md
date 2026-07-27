# SEC-ENV-01-001
- **标题**: 环境级 secret 必须经审批后才能被 workflow 访问
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**审批后环境 secret 可读，审批前不可读，日志不含 secret 明文**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-027
通过标准：
1. 审批后成功
2. 日志不含 secret 明文
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Use env secret | `echo "secret length is ${#PROD_TOKEN}"` | environment: production | secret 长度 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | with-env-secrets |
| Secrets | PROD_TOKEN |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | success_after_approval | positive | run_status equals | ⚠️ STATUS_GUARANTEED | 步骤仅 echo 长度，无 exit 1/if 条件；必然成功；无法区分审批前/后 |
| 2 | 不含 PROD_TOKEN 明文 | negative | run_logs must_not_contain_secret | ✅ GENUINE | 步骤使用 secrets.PROD_TOKEN（环境 secret），${{ }} 表达式 → NEVER VACUOUS；平台脱敏机制决定 |
### 问题
断言 1 STATUS_GUARANTEED：echo 必然成功，无法区分审批前后行为差异。
---
