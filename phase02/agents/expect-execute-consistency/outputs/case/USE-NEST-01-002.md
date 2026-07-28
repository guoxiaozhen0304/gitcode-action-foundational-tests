# USE-NEST-01-002
- **标题**: workflow_call 嵌套 2 层时应正常执行
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
验证合法二层嵌套（主 workflow → reusable-level1 → reusable-level2）可正常执行，日志包含最内层步骤输出。

## 做了什么
主 workflow 以 job 级 uses 调用 reusable-level1.yml，level1 再以 job 级 uses 调用 reusable-level2.yml（含实际执行步骤 echo "level2 executed"）。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | 运行成功完成 | COVERED | 合法嵌套应调度成功 → GENUINE |
| 2 | run_logs | positive | 日志含 "level2 executed" | COVERED | 嵌套链路执行到最内层的日志输出 → GENUINE |
