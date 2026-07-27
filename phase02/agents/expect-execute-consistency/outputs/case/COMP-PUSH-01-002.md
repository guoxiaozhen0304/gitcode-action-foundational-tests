# COMP-PUSH-01-002
- **标题**: 不匹配 branches 的 push 不触发 workflow
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**不匹配 branches 的 push 不触发 workflow**
- 触发事件: `push`
- 规格引用: INTENT-COMP-003
通过标准：
1. 运行列表中不存在该 push 触发的运行（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo triggered | `echo "should not run"` | - | should not run |
## 3. 触发与运行环境
| 触发事件 | push |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_created | negative | equals: no_run_for_non_matching_branch | ✅ GENUINE | 平台 branches 过滤行为由 harness 验证——push 到 non-matching 分支不应创建 run |
---
