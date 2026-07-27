# COMP-TIMEOUT-01-001
- **标题**: 未声明 timeout-minutes 的 job 在 360 分钟内正常完成
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**未声明 timeout-minutes 的 job 在 360 分钟内正常完成**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-008
通过标准：
1. 运行状态为 success（正向）
2. 运行耗时远小于 360 分钟（非功能）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Quick step | `echo "done"` | - | done |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 步骤仅 echo 字面量，无条件失败路径 |
| 2 | run_duration | nonfunctional | less_than_minutes: 360 | 🔶 LLM_DEPENDENT | 依赖 LLM 评估运行耗时是否远小于 360 分钟 |
### 问题
**断言 1 — STATUS_GUARANTEED**: 步骤仅 echo 字面量，测试的是"未声明 timeout-minutes 时 job 能否完成"，但 step 内容不涉及长时间运行，无法验证 timeout 机制。
---
