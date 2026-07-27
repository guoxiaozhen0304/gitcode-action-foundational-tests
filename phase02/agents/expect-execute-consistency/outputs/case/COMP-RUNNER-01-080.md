# COMP-RUNNER-01-080
- **标题**: runner 上下文属性可访问性验证
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**runner 上下文属性可访问性验证**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-080
通过标准：
1. runner.name / temp / tool_cache 非空（正向）
2. runner.os 为预定义值之一（正向）
3. runner.arch 为预定义值之一（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Print runner props | `${{ runner.name }}`, `${{ runner.temp }}`, `${{ runner.tool_cache }}`, `${{ runner.os }}`, `${{ runner.arch }}`, `echo "runner_ok"` | - | 平台上下文变量值 + runner_ok |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: NAME= | ✅ GENUINE | `${{ runner.name }}` 为平台上下文表达式求值 |
| 2 | run_logs | positive | must_contain: TEMP= | ✅ GENUINE | `${{ runner.temp }}` 为平台上下文表达式求值 |
| 3 | run_logs | positive | must_contain: TOOL_CACHE= | ✅ GENUINE | `${{ runner.tool_cache }}` 为平台上下文表达式求值 |
| 4 | run_logs | positive | must_contain: runner_ok | ✅ GENUINE | 步骤整体含 `${{ }}` 表达式，runner_ok 为同一步骤内的辅助标记 |
---
