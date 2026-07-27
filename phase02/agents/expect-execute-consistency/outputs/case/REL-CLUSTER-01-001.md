# REL-CLUSTER-01-001
- **标题**: 集群断连恢复后断连窗口任务日志同步
- **维度**: 稳定性
- **优先级**: P1
- **评级**: 部分不符
---
## 1. 想测什么
本用例验证：**集群断连恢复后日志同步完整性**
- 触发事件: `manual`
- 规格引用: INTENT-REL-091
通过标准：
1. 断连恢复后日志可正常返回
2. 不应静默丢失

## 2. 做了什么
| # | 步骤名 | 命令 | 条件 (if) | 输出 |
|---|--------|------|------|------|
| — | 无 workflow 步骤 | workflow: null | — | 手工运维操作测试 |

## 3. 触发与运行环境
| 触发事件 | manual |
| 触发身份 | maintainer |
| Repo 环境 | default |
| Secrets | [] |
| 故障注入 | network_partition（集群断连） |

## 4. 能否达成目标
| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_sync_after_reconnect | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | LLM 辅助评估日志完整性 |
| 2 | log_sync_after_reconnect | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | LLM 辅助评估静默丢失 |
---
