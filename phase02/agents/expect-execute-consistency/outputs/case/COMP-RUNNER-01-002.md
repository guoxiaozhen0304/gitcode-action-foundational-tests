# COMP-RUNNER-01-002
- **标题**: runs-on default 等效 ubuntu-latest x64 small
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**runs-on default 等效 ubuntu-latest x64 small**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-010
通过标准：
1. 运行状态为 success（正向）
2. Runner 规格与 small（2核8G）一致（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo runner info | `echo "os=$RUNNER_OS"` / `echo "arch=$RUNNER_ARCH"` | - | 平台环境变量值 |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ✅ GENUINE | runs-on 标签触发平台调度，$RUNNER_OS/$RUNNER_ARCH 为平台注入变量 |
| 2 | runner_spec | positive | equals: small | ✅ GENUINE | harness 验证 Runner 规格与 small 一致 |
---
