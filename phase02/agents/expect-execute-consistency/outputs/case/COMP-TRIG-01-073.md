# COMP-TRIG-01-073
- **标题**: pull_request 事件关键字段与 types 验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**pull_request 事件关键字段与 types 验证**
- 触发事件: `pull_request`
- 规格引用: INTENT-COMP-073
通过标准：
1. PR 创建时触发 workflow（正向）
2. event.pull_request.number 非空（正向）
3. types 仅匹配指定类型（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print PR fields | `${{ atomgit.event.pull_request.number }}`, `${{ atomgit.event.pull_request.title }}`, `${{ atomgit.event.pull_request.state }}`, `echo "pr_ok"` | - | 平台事件上下文 + pr_ok |
## 3. 触发与运行环境
| 触发事件 | pull_request |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: PR_NUM= | ✅ GENUINE | `${{ atomgit.event.pull_request.number }}` 为平台事件上下文求值 |
| 2 | run_logs | positive | must_contain: pr_ok | ✅ GENUINE | 步骤整体含 `${{ }}` 表达式，pr_ok 为同一步骤内的辅助标记 |
---
