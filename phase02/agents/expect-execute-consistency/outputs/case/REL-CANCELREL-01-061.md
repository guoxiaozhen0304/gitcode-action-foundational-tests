# REL-CANCELREL-01-061
- **标题**: 取消操作可靠性——queued/running/post 各阶段取消状态正确过渡
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
queued/running/post 三阶段取消状态正确，收敛≤60s。

## 做了什么
sleep 60s + if:always() cleanup step；由 harness 在不同阶段发起取消。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cancel_queued_status | positive | equals "canceled" | COVERED | harness 在 queued 阶段取消，平台状态可观测 |
| 2 | cancel_queued_status | negative | equals "success" | COVERED | queued 取消不应为 success |
| 3 | cancel_queued_status | negative | equals "failure" | COVERED | queued 取消不应为 failure |
| 4 | cancel_running_status | positive | equals "canceled" | COVERED | running 阶段取消终态可观测 |
| 5 | cancel_post_main_status | positive | equals "success" | COVERED | post 阶段主 step 已完成，主结论应保持 success |
| 6 | cancel_stabilization_seconds | nonfunctional | le 60 | LLM_DEPENDENT | 非功能性能指标 |
