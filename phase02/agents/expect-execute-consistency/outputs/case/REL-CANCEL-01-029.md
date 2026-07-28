# REL-CANCEL-01-029
- **标题**: 多并发 run 中取消指定 run——取消应按 run_id 寻址而非栈序误杀最新一条
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
同一 workflow 触发 3 条并发 run（RUN-1/2/3），API 按 run_id 取消中间 RUN-2，验证 RUN-2 取消、RUN-1/RUN-3 不受干扰，取消不应作用于最新一条。
## 做了什么
YAML 定义 sleep 300 单 job，harness 并发 3 次 dispatch，30 秒后按 run_id 取消第 2 条。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | target_run_status | positive | equals canceled | COVERED | YAML sleep 300 真实命令，harness API 取消，platform 日志记录状态变更 |
| 2 | sibling_run_status | positive | equals success | COVERED | YAML assert RUN-1/RUN-3 状态=success，对应文本"RUN-1/RUN-3 不受干扰" |
| 3 | sibling_run_status | negative | equals canceled | COVERED | YAML 负向断言 RUN-1/RUN-3 不应为 canceled，对应文本"RUN-1/RUN-3 不应被取消或中断" |
| 4 | cancel_convergence_seconds | nonfunctional | le 60 | COVERED | YAML assert 取消收敛 ≤60s，对应文本"取消请求到 RUN-2 终态稳定 ≤60 秒" |
