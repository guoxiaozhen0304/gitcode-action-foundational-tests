# SEC-PERM-01-002
- **标题**: permissions 声明 read 时写操作被平台拒绝
- **维度**: 安全性
- **优先级**: P0
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**permissions: repository:read 下 push 操作返回 403**
- 触发事件: `workflow_dispatch` (as maintainer)
- 规格引用: INTENT-SEC-016
通过标准：
1. 不含 push_successful
2. push 被拒或 403
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Clone repo | `git clone https://x-access-token:${{ atomgit.token }}@atomgit.com/${{ atomgit.repository }}.git repo` | permissions: repository:read | clone 结果 |
| 2 | Attempt push | `cd repo; echo test > test.txt; git add/commit/push origin main \|\| echo push denied as expected` | — | push 结果 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | 不含 push_successful | negative | run_logs must_not_contain | ✅ GENUINE | git clone + push 使用 ${{ atomgit.token }} → NEVER VACUOUS；依赖平台权限控制 |
| 2 | push_denied_or_403 | positive | run_logs equals | ❌ VACUOUS | git push 失败时 echo "push denied as expected"，不输出 "push_denied_or_403" 字面量 |
### 问题
断言 2 VACUOUS：步骤输出 "push denied as expected"（有空格），断言期望 "push_denied_or_403"（下划线标签）。
---
