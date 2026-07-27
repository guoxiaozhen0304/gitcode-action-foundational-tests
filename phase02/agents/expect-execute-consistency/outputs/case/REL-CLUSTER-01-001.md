# REL-CLUSTER-01-001

- **标题**: 集群断连恢复后断连窗口任务日志同步
- **维度**: 可靠性
- **优先级**: P1
- **评级**: 部分不符

---

## 1. 想测什么

本用例验证：**集群断连恢复后断连窗口任务日志同步**

- 触发事件: `manual`
- 规格引用: INTENT-REL-091

通过标准：
1. type=positive, target=log_sync_after_reconnect, eval=llm_assisted
2. type=negative, target=log_sync_after_reconnect, eval=llm_assisted

## 2. 做了什么

workflow 中每个步骤的实际行为：

| # | 步骤名 | 命令/uses | 条件 (if) | 实质 |
|---|--------|-----------|------|------|

## 3. 触发与运行环境

| 触发事件 | `manual` |
| 触发身份 | `maintainer` |
| Repo 环境 | `default` |
| Secrets | `[]` |
| 故障注入 | `{'at': 'mid_job', 'action': 'network_partition', 'params': {'disconnect_duration': '>=1 个日志采集周期'}, 'recovery_expectation': '恢复连接后断连窗口日志同步追平，或日志明确标注缺失区间'}` |

## 4. 能否达成目标

逐条断言对比步骤实际输出：

| # | 目标 | 类型 | 条件 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_sync_after_reconnect | positive | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |
| 2 | log_sync_after_reconnect | negative | eval=llm_assisted | 🔶 LLM_DEPENDENT | 非功能性/LLM 辅助断言，跳过步骤追溯分析 |

### 问题

**断言 1 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

**断言 2 — LLM_DEPENDENT**⚠️: 非功能性/LLM 辅助断言，跳过步骤追溯分析

---