# SEC-AUDIT-01-001
- **标题**: 敏感操作（secret/权限/rerun/审批/评论触发）必须全部留有不可擦除的审计记录
- **维度**: 安全性
- **优先级**: P1
- **评级**: 完全不符
---
## 1. 想测什么
本用例验证：**各类敏感操作均留有不可擦除审计记录，操作者无法删除或篡改**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-046
通过标准：
1. 所有操作类别审计记录可查
2. 敏感操作无痕发生次数为 0
3. 操作者删除审计记录被拒
4. 保留期与导出能力可判定
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | (workflow: null) | — | — | — |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch (ops: [secret_create, secret_update, permission_change, rerun, env_approval, comment_trigger]) |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 审计记录可查 | positive | audit_log equals | ❌ MISSING_SOURCE | target=audit_log 为平台审计接口，workflow 为 null，无步骤生成审计记录 |
| 2 | 敏感操作无痕发生 | negative | audit_log must_not_equal | ❌ MISSING_SOURCE | 同上 |
| 3 | 操作者删除被拒 | negative | audit_log must_not_equal | ❌ MISSING_SOURCE | 同上 |
| 4 | 保留期与导出可判定 | nonfunctional | audit_log equals | 🔶 LLM_DEPENDENT | nonfunctional + external target |
### 问题
workflow 为 null，所有断言 target=audit_log 均为外部平台接口，YAML 无法驱动任何验证。
---
