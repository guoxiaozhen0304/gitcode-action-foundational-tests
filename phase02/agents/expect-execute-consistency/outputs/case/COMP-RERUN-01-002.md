# COMP-RERUN-01-002
- **标题**: 第 4 次 rerun 应被系统拒绝
- **维度**: 完备性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**第 4 次 rerun 应被系统拒绝**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-COMP-009
通过标准：
1. 第 4 次 rerun 不应创建新运行（负向）
2. 报错信息应说明最多 3 次限制（非功能）
## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | Echo | `echo "run"` | - | run |
## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |
## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_result | negative | equals: 4th_rerun_created | ✅ GENUINE | 平台 rerun 次数限制由 harness 验证——连续 4 次 rerun 尝试中最后 1 次不应创建新 run |
| 2 | error_message | nonfunctional | eval: llm_assisted | 🔶 LLM_DEPENDENT | 依赖 LLM 评估报错信息是否说明了 3 次上限 |
---
