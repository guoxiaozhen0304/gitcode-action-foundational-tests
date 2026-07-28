# REL-CANCEL-01-029
- **标题**: 多并发 run 中取消指定 run——取消应按 run_id 寻址而非栈序误杀最新一条
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
3 条并发 run 中取消 RUN-2，RUN-1/3 不受干扰，取消收敛≤60s。

## 做了什么
单 job sleep 300s；由 harness 管理并发触发(3 条)、按 run_id 取消中间一条。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | target_run_status | positive | equals "canceled" | COVERED | harness 按 run_id 取消，平台状态可观测 |
| 2 | sibling_run_status | positive | equals "success" | COVERED | 未被取消的 run 应正常完成 |
| 3 | sibling_run_status | negative | equals "canceled" | COVERED | 未被取消的 run 不应被错杀 |
| 4 | cancel_convergence_seconds | nonfunctional | le 60 | LLM_DEPENDENT | 非功能性能指标 |
