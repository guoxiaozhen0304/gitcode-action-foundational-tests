# REL-CANCEL-01-028
- **标题**: 手动取消 workflow——运行中取消时 always() cleanup step 仍应执行
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
运行中取消时非 always step 终止、cleanup step 执行、终态 cancelled。

## 做了什么
sleep 60s main step + if:always() cleanup step echo "cleanup executed"；触发后由 harness 取消。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | cleanup_step_status | positive | equals "success" | COVERED | if:always() 确保取消时 cleanup 仍执行；step 状态可观测 |
| 2 | run_status | positive | equals "canceled" | COVERED | 平台最终状态可观测 |
