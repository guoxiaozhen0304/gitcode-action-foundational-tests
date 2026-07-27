# COMP-TRIG-01-077
- **标题**: pull_request_comment 事件关键字段与过滤验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**pull_request_comment 事件关键字段与过滤验证**
- 触发事件: `pull_request_comment`
- 规格引用: INTENT-COMP-077
通过标准：
1. PR 评论创建时触发（正向）
2. event.comment.body 非空（正向）
3. event.pull_request.number 非空（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print PR comment fields | `${{ atomgit.event.pull_request.number }}`, `${{ atomgit.event.comment.body }}`, `echo "pr_comment_ok"` | - | 平台事件上下文 + pr_comment_ok |
## 3. 触发与运行环境
| 触发事件 | pull_request_comment |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: PR_NUM= | ✅ GENUINE | `${{ atomgit.event.pull_request.number }}` 为平台事件上下文求值 |
| 2 | run_logs | positive | must_contain: pr_comment_ok | ✅ GENUINE | 步骤整体含 `${{ }}` 表达式，pr_comment_ok 为同一步骤内的辅助标记 |
---
