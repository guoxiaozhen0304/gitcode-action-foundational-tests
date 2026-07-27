# REL-LOGPERF-01-052
- **标题**: 日志实时性——运行中 job 的日志流式可见延迟应有界且与完成后日志一致
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**日志实时性——运行中 job 的日志流式可见延迟应有界且与完成后日志一致**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-084
通过标准：
1. 运行中可见日志是完成后日志的前缀（内容一致）
2. 首行可见延迟 ≤30 秒（非功能）
3. 10 分钟窗口内日志追平延迟 P95 ≤60 秒（非功能）

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | emit timestamped lines step | `for i in $(seq 1 120); do echo "TS_$(date +%s)_LINE_$i"; sleep 5; done` | — | 120 行带真实时间戳的日志 |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | (无) |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | streaming_log_is_prefix_of_final = true | positive | — | ✅ GENUINE | step 使用 `$(date +%s)` 生成真实时间戳日志，通过真实命令产生可对比的日志内容，由 harness 外部对核准实时与最终日志 |
| 2 | first_line_visibility_seconds ≤ 30 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
| 3 | p95_catchup_latency_seconds ≤ 60 | nonfunctional | — | 🔶 LLM_DEPENDENT | 非功能断言 |
---
