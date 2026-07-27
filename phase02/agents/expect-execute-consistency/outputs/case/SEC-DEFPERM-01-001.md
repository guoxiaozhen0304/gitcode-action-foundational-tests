# SEC-DEFPERM-01-001
- **标题**: ATOMGIT_TOKEN 默认权限范围与 job 级覆盖必须正确生效
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**顶层 permissions: repository: read 继承到 job，写操作返回 403**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-036
通过标准：
1. 写操作不成功
2. 返回 403 或权限拒绝
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Attempt write | `curl ... POST ... issues ... -H "Authorization: token ${{ atomgit.token }}"` | — | HTTP 状态码 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 write_successful | negative | run_logs must_not_contain | ✅ GENUINE | 步骤使用 ${{ }} 表达式 + curl 真实 API 调用，依赖平台权限控制行为 |
| 2 | 403 或权限拒绝 | positive | run_logs equals "403_or_permission_denied" | ❌ VACUOUS | curl 输出 HTTP 状态码数字（如 "403"），步骤从未输出字面量 "403_or_permission_denied"；该字符串仅存在于断言期望中 |
### 问题
断言 2 VACUOUS：步骤输出数字状态码，断言期望的是语义标签字符串。
---
