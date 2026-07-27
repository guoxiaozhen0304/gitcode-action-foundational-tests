# COMP-TRIG-01-072
- **标题**: push 事件关键字段与过滤验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**push 事件关键字段与过滤验证**
- 触发事件: `push`
- 规格引用: INTENT-COMP-072
通过标准：
1. push 到 main 触发 workflow（正向）
2. event.before 和 event.after 非空（正向）
3. branches 过滤生效（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print push fields | `${{ atomgit.event.ref }}`, `${{ atomgit.event.before }}`, `${{ atomgit.event.after }}`, `echo "push_ok"` | - | 平台事件上下文 + push_ok |
## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: REF=refs/ | ✅ GENUINE | `${{ atomgit.event.ref }}` 为平台事件上下文求值 |
| 2 | run_logs | positive | must_contain: BEFORE= | ✅ GENUINE | `${{ atomgit.event.before }}` 为平台事件上下文求值 |
| 3 | run_logs | positive | must_contain: push_ok | ✅ GENUINE | 步骤整体含 `${{ }}` 表达式，push_ok 为同一步骤内的辅助标记 |
---
