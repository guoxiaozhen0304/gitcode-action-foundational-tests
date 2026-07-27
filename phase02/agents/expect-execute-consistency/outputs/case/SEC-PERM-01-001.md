# SEC-PERM-01-001
- **标题**: 显式声明的 permissions 必须在 job 级实际生效并限制 ATOMGIT_TOKEN
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**job 级 permissions: repository:read 时写操作返回 403，读操作正常**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-016
通过标准：
1. 读操作成功
2. 不含 write_permission_granted
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt write | `curl ... POST ... issues ... -H "Authorization: token ${{ atomgit.token }}"` | permissions: repository:read, pr:none, issue:none, note:none, project:none, hook:none | HTTP 状态码 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 读操作成功 | positive | run_logs equals "read_operations_successful" | ❌ VACUOUS | curl 输出 HTTP 状态码，不输出语义标签；无实际读操作步骤 |
| 2 | 不含 write_permission_granted | negative | run_logs must_not_contain | ✅ GENUINE | curl 使用 ${{ atomgit.token }} 尝试 POST → NEVER VACUOUS；依赖平台权限控制 |
### 问题
断言 1 VACUOUS：无 git clone/API 读取步骤验证"读操作成功"，且 curl 输出状态码而非标签字符串。
---
