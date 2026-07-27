# SEC-ORG-01-001
- **标题**: 可见范围外仓库的 workflow 绝不应读到组织级 secret 原值
- **维度**: 安全性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**范围外仓库引用组织级 secret 返回空/报错，日志不含原值**
- 触发事件: `workflow_dispatch` (as maintainer, repo_scope: outside_visibility)
- 规格引用: INTENT-SEC-039
通过标准：
1. 日志不含 ORG_SHARED_KEY 原值
2. 日志显示空或错误
3. 可见性变更即时生效
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo org secret value | `echo "ORG_SECRET_VALUE: ${{ secrets.ORG_SHARED_KEY }}"` | — | secret 值或空 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch (repo_scope: outside_visibility) |
| 触发身份 | maintainer |
| Repo 环境 | org-scoped-secret |
| Secrets | ORG_SHARED_KEY |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 ORG_SHARED_KEY 原值 | negative | run_logs must_not_contain_secret | ✅ GENUINE | ${{ secrets.ORG_SHARED_KEY }} → NEVER VACUOUS；范围外仓库隔离由平台决定 |
| 2 | empty_or_error_outside_scope | positive | run_logs equals | ❌ VACUOUS | echo 输出 "ORG_SECRET_VALUE: " + 值或空；不输出 "empty_or_error_outside_scope" 字面量 |
| 3 | 可见性变更即时生效 | nonfunctional | visibility_change equals | 🔶 LLM_DEPENDENT | nonfunctional + external target |
### 问题
断言 2 VACUOUS：步骤输出的是前缀+值，非语义标签字符串。
---
