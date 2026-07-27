# COMP-STATUS-01-001
- **标题**: 运行状态机 queued 到 completed 转换正确
- **维度**: 完备性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**运行状态机 queued 到 completed 转换正确**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-017
通过标准：
1. 状态转换序列符合预期（正向）
2. 最终状态为 completed/success（正向）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo | `echo "running"` | - | running |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status_sequence | positive | equals: queued_in_progress_completed | ✅ GENUINE | harness 通过 API 轮询验证状态机转换序列 |
| 2 | run_status | positive | equals: success | ⚠️ STATUS_GUARANTEED | 所有步骤仅 echo 字面量，无条件失败路径 |
### 问题
**断言 2 — STATUS_GUARANTEED**: 步骤仅 echo 字面量，无条件失败路径，run_status=success 为必然结果。
---
