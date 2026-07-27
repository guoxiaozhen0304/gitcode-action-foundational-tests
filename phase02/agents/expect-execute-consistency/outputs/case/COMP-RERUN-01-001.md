# COMP-RERUN-01-001
- **标题**: rerun 后 atomgit.sha 保持原始值 run_number 递增
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**rerun 后 atomgit.sha 保持原始值 run_number 递增**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-009
通过标准：
1. rerun 后 sha 与原始运行一致（正向）
2. rerun 后 run_number 大于原始值（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Dump context | `echo "sha=$ATOMGIT_SHA"` / `echo "ref=$ATOMGIT_REF"` / `echo "run_number=$ATOMGIT_RUN_NUMBER"` | - | 平台环境变量值 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_context | positive | sha_unchanged: True | ✅ GENUINE | $ATOMGIT_SHA 为平台注入变量，harness 对比原始/rerun 运行的 sha 值 |
| 2 | rerun_context | positive | run_number_increased: True | ✅ GENUINE | $ATOMGIT_RUN_NUMBER 为平台上下文，harness 对比两次运行的 run_number |
---
