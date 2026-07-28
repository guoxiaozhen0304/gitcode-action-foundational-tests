# REL-CLUSTER-01-001
- **标题**: 集群断连恢复后断连窗口任务日志同步
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
K8s 集群断连 ≥1 个日志采集周期后恢复连接，验证断连窗口任务日志能正常返回（完整或明确标注缺口），不应静默丢失。
## 做了什么
YAML workflow=null，trigger=manual，fault_injection=network_partition mid_job。断言均 eval=llm_assisted。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | log_sync_after_reconnect | positive | 断连恢复后日志完整返回或明确标注缺口 | LLM_DEPENDENT | YAML eval=llm_assisted，需结合实测环境判定日志完整性 |
| 2 | log_sync_after_reconnect | negative | 不应静默丢失且无提示 | LLM_DEPENDENT | YAML eval=llm_assisted，需 LLM 辅助判定是否静默丢失 |
