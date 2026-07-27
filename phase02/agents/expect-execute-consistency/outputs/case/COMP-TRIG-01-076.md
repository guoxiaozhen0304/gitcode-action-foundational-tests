# COMP-TRIG-01-076
- **标题**: issue_comment 事件关键字段与 types 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**issue_comment 事件关键字段与 types 验证**
- 触发事件: `issue_comment`
- 规格引用: INTENT-COMP-076
通过标准：
1. issue 评论创建时触发（正向）
2. event.comment.id 非空（正向）
3. event.issue.number 非空（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print comment fields | `${{ atomgit.event.comment.id }}`, `${{ atomgit.event.issue.number }}`, `echo "issue_comment_ok"` | - | 平台事件上下文 + issue_comment_ok |
## 3. 触发与运行环境
| 触发事件 | issue_comment |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: COMMENT_ID= | ✅ GENUINE | `${{ atomgit.event.comment.id }}` 为平台事件上下文求值 |
| 2 | run_logs | positive | must_contain: issue_comment_ok | ✅ GENUINE | 步骤整体含 `${{ }}` 表达式，issue_comment_ok 为同一步骤内的辅助标记 |
---
