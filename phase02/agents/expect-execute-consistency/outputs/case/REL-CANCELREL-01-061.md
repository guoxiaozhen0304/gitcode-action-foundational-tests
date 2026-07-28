# REL-CANCELREL-01-061
- **标题**: 取消操作可靠性——queued/running/post 各阶段取消状态正确过渡
- **维度**: reliability
- **评级**: 部分不符
## 想测什么
在 queued/running/post 三个阶段分别取消 workflow，验证各阶段终态稳定、取消到终态 ≤60s、queued 取消后不应错标 success/failure。
## 做了什么
YAML 定义 sleep 60 主 step + `if: ${{ always() }}` cleanup step，harness 在三个时机点分别取消。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cancel_queued_status | positive | equals canceled | COVERED | YAML 使用 sleep 真实命令 + platform 日志，harness 在 queued 阶段取消观测状态 |
| 2 | cancel_running_status | positive | equals canceled | COVERED | YAML 使用 sleep 真实命令，harness 在 running 阶段取消观测 |
| 3 | cancel_post_main_status | positive | equals success | COVERED | YAML 定义 cleanup step（`if: always()`），post 阶段取消时主 job 已完成=success |
| 4 | cancel_stabilization_seconds | nonfunctional | le 60 | COVERED | YAML assert 取消稳定时间 ≤60s，对应文本"取消到终态稳定时间≤60s" |
| 5 | queued_cancel_no_false_success | negative | queued 取消后不应错标 success/failure | MISSING | 文本有负向断言"queued 取消后不应错标 success/failure"，YAML 无对应 assertion |
