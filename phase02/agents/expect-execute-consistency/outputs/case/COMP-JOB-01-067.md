# COMP-JOB-01-067
- **标题**: job 可选字段 env if timeout-minutes needs 验证
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
job 级 env 对该 job 所有 step 可见，needs 正确建立依赖。

## 做了什么
1. prepare job：`echo "prepare_done"`
2. verify job（needs: prepare, if: ${{ true }}, timeout-minutes: 30, env: JOB_VAR=job_value）：
   - step `Check fields`：`echo "JOB_VAR=$JOB_VAR"` 和 `echo "optional_ok"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: prepare_done | COVERED | prepare job echo 输出（依赖 needs 建立执行顺序） |
| 2 | run_logs | positive | must_contain: JOB_VAR=job_value | COVERED | echo $JOB_VAR 输出 job 级 env 值 |
| 3 | run_logs | positive | must_contain: optional_ok | COVERED | echo 固定标记 |
