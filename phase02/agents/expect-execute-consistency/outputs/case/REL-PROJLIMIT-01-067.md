# REL-PROJLIMIT-01-067
- **标题**: 项目级 workflow 并发上限——200 条同时触发时全部完成无丢失
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**项目级 workflow 并发上限——200 条同时触发时全部完成无丢失**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-067
通过标准：
1. completed_count = 200
2. failed_count = 0
3. queued_count = 0
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
| 1 | completed_count = 200 | positive | — | ✅ GENUINE | `echo "run_id=${{ atomgit.run_id }}"` 使用 `${{ }}` 输出唯一标识，`sleep 5` 持有资源。200 次并发触发真实测试项目级并发上限 |
| 2 | failed_count = 0 | positive | — | ✅ GENUINE | 200 次全部 echo + sleep 5，无失败路径，由 harness 统计 |
| 3 | queued_count = 0 | positive | — | ✅ GENUINE | 平台应支持 200 条同时 running，由 harness 观察 |
| 4 | total_duration_seconds ≤ 3600 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
| 5 | lost_count = 0 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
