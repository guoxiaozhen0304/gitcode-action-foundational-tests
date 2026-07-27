# COMP-TIMEOUT-01-002
- **标题**: 超时的 job 被强制终止并标记为 failure
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**超时的 job 被强制终止并标记为 failure**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-008
通过标准：
1. 运行状态为 failure（负向：不应 success）（正向：应为 failure）
2. 超时前已完成的 step 日志完整保留（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo before sleep | `echo "starting"` | - | starting |
| 2 | Sleep beyond timeout | `sleep 120` | timeout-minutes: 1 | (超时被 kill) |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals: success | ✅ GENUINE | sleep 120 + timeout-minutes: 1 构成真实超时场景，run 不应 success |
| 2 | run_status | positive | equals: failure | ✅ GENUINE | timeout 机制触发后 run 应标记为 failure |
| 3 | run_logs | positive | contains: starting | ❌ VACUOUS | 步骤仅 echo 字面量 "starting"，未执行与 timeout 日志保留相关的实质验证 |
### 问题
**断言 3 — VACUOUS**: 步骤仅 echo 了字面量 "starting"，该标记空洞。但超时场景本身（sleep 120 + timeout-minutes: 1）是真实的，只是日志保留断言依赖空洞标记。
---
