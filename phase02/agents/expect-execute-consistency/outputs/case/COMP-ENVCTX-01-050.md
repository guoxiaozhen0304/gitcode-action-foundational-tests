# COMP-ENVCTX-01-050
- **标题**: env 优先级链 step 大于 job 大于 workflow
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
step 级 env 覆盖 job 级，job 级覆盖 workflow 级；无 job 级 env 时继承 workflow 级。

## 做了什么
1. workflow 级 env: MY_VAR=workflow_value
2. verify job 级 env: MY_VAR=job_value
   - step `Step override`（step 级 env: MY_VAR=step_value）：`echo "MY_VAR=$MY_VAR"`
   - step `Job inherit`（无 step 级）：`echo "JOB_VAR=$MY_VAR"`
3. verify-inherit job（无 job 级 env）：`echo "WF_VAR=$MY_VAR"`

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: MY_VAR=step_value | COVERED | step 级 env 覆盖 job 级，echo $MY_VAR 输出 |
| 2 | run_logs | positive | must_contain: JOB_VAR=job_value | COVERED | 无 step 级覆盖，取 job 级 env |
| 3 | run_logs | positive | must_contain: WF_VAR=workflow_value | COVERED | 无 job 级覆盖，取 workflow 级 env |
