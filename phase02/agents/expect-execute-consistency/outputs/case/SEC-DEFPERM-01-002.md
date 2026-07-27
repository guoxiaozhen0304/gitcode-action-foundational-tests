# SEC-DEFPERM-01-002
- **标题**: job 级覆盖后权限正确收窄
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**job 级 permissions: repository: read 覆盖顶层 write，写操作被拒**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-036
通过标准：
1. 写操作不成功
2. 返回 403 或权限拒绝
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt write after override | `curl ... POST ... issues ... -H "Authorization: token ${{ atomgit.token }}"` | — | HTTP 状态码 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 write_successful | negative | run_logs must_not_contain | ✅ GENUINE | 步骤使用 ${{ }} + curl 真实 API 调用，依赖平台权限控制 |
| 2 | 403 或权限拒绝 | positive | run_logs equals "403_or_permission_denied" | ❌ VACUOUS | curl 输出数字状态码，步骤不输出语义标签字符串 |
### 问题
断言 2 VACUOUS：同上，curl 输出数字状态码而非 "403_or_permission_denied" 字面量。
---
