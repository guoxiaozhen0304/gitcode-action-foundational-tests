# REL-API-01-065
- **标题**: API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据
- **维度**: 稳定性
- **优先级**: P2
- **评级**: 断言一致
---
## 1. 想测什么
本用例验证：**API 限流与一致性——10 QPS 高频查询 run/job 状态不丢数据**
- 触发事件: `workflow_dispatch`
- 规格引用: INTENT-REL-065
通过标准：
1. [正向] 200 占比=100%
2. [负向] 不应出现 429/503/500
3. [非功能] P95≤2s

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| 1 | sleep step | `sleep 30` | - | 无（保持 running 供外部 API 测试） |

## 3. 触发与运行环境
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | 无 |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | http_200_ratio | positive | equals="100%" | ✅ GENUINE | 外部测试 harness 对 running workflow 以 10 QPS 查询 API 并衡量 200 比例，workflow 仅提供受测目标 |
| 2 | http_error_codes | negative | contains="429" (期望不存在) | ✅ GENUINE | 外部测试框架验证无 429/503/500 错误 |
| 3 | response_time_p95_seconds | nonfunctional | le="2" | 🔶 LLM_DEPENDENT | 非功能：外部 harness 验证 P95 响应时间 |

---
