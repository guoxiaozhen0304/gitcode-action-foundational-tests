# COMP-STAGES-01-003
- **标题**: post.run_always true 时 workflow 失败仍执行 post
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**post.run_always true 时 workflow 失败仍执行 post**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-007
通过标准：
1. post 阶段步骤日志存在（正向）
2. post 阶段步骤输出出现在运行详情页（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Force failure (main) | `exit 1` | - | (job 失败) |
| 2 | Post cleanup (post) | `echo "post executed"` | run_always: true | post executed |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: failure | ✅ GENUINE | exit 1 故意失败，run 应标记为 failure |
| 2 | post_logs | positive | contains: post executed | ✅ GENUINE | post 块含 run_always: true，主 job 失败后仍应执行 post 步骤，验证了 run_always 机制 |
---
