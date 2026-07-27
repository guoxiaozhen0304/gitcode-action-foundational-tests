# COMP-SYSENV-01-059
- **标题**: ATOMGIT 系统环境变量关键变量存在性
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**ATOMGIT 系统环境变量关键变量存在性**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-059
通过标准：
1. 关键 ATOMGIT_* 变量在日志中显示非空（正向）
2. 无关键变量缺失（负向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Check critical vars | `[ -n "$ATOMGIT_SHA" ] && echo yes || echo no` 等 shell 条件检查 | - | SHA_SET=yes / REF_SET=yes ... |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: SHA_SET=yes | ✅ GENUINE | `[ -n "$ATOMGIT_SHA" ]` 为实质 shell 命令 + 平台环境变量 |
| 2 | run_logs | positive | must_contain: REF_SET=yes | ✅ GENUINE | `[ -n "$ATOMGIT_REF" ]` 实质 shell 命令 |
| 3 | run_logs | positive | must_contain: EVENT_NAME_SET=yes | ✅ GENUINE | `[ -n "$ATOMGIT_EVENT_NAME" ]` 实质 shell 命令 |
| 4 | run_logs | positive | must_contain: WORKSPACE_SET=yes | ✅ GENUINE | `[ -n "$ATOMGIT_WORKSPACE" ]` 实质 shell 命令 |
| 5 | run_logs | positive | must_contain: REPO_SET=yes | ✅ GENUINE | `[ -n "$ATOMGIT_REPOSITORY" ]` 实质 shell 命令 |
| 6 | run_logs | positive | must_contain: RUN_ID_SET=yes | ✅ GENUINE | `[ -n "$ATOMGIT_RUN_ID" ]` 实质 shell 命令 |
---
