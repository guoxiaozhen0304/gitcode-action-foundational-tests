# REL-PROJLIMIT-01-068
- **标题**: 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排队
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排队**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-068
通过标准：
1. completed_count = 201
2. failed_count = 0
3. queued_count ≥ 1
4. 总耗时 ≤60 min（非功能）
5. lost_count = 0（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | quick step | `echo "run_id=${{ atomgit.run_id }}"; sleep 5` | — | 输出 run_id 并持有 runner 5 秒 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_count = 201 | positive | — | ✅ GENUINE | 同 REL-PROJLIMIT-01-067，`${{ atomgit.run_id }}` 使用上下文表达式 + `sleep 5` 真实命令，201 次并发触发测试超限排队 |
| 2 | failed_count = 0 | positive | — | ✅ GENUINE | 所有 job 均 echo+exit 0 |
| 3 | queued_count ≥ 1 | positive | — | ✅ GENUINE | 超出 200 上限的 1 条应排队，由 harness 观测 |
| 4 | total_duration_seconds ≤ 3600 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
| 5 | lost_count = 0 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
