# SEC-PERM-01-003
- **标题**: 未声明 permissions 时 ATOMGIT_TOKEN 默认权限必须最小化（read-only）
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**默认无 permissions 声明时 ATOMGIT_TOKEN 仅 read 权限，写操作被拒**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-017
通过标准：
1. 不含 write_permission_granted
2. run_status 为 completed
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt write without permissions | `curl ... POST ... issues ... -H "Authorization: token ${{ atomgit.token }}"` | — | HTTP 状态码 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 write_permission_granted | negative | run_logs must_not_contain | ✅ GENUINE | curl 使用 ${{ atomgit.token }} → NEVER VACUOUS；默认权限由平台决定 |
| 2 | completed | positive | run_status equals "completed" | ⚠️ STATUS_GUARANTEED | curl 失败不 exit 1，步骤始终完成；无区分读写行为的能力 |
### 问题
断言 2 STATUS_GUARANTEED：curl 失败不会触发 exit 1，步骤必然 completed。
---
