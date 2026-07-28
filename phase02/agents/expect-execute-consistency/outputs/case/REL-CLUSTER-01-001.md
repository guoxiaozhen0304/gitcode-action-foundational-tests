# REL-CLUSTER-01-001
- **标题**: 集群断连恢复后断连窗口任务日志同步
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
K8s 集群断连恢复后断连窗口内日志完整追平或明确标注缺口。

## 做了什么
workflow: null, trigger: manual(platform_op: cluster_disconnect_reconnect)，依赖 fault_injection 网络分区 + harness 管理。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_sync_after_reconnect | positive | eval llm_assisted | LLM_DEPENDENT | LLM 判读日志同步完整性；workflow 为 null 无步骤执行 |
| 2 | log_sync_after_reconnect | negative | eval llm_assisted | LLM_DEPENDENT | LLM 判读是否静默丢失 |
