# COMP-ENVCTX-01-050

- **标题**: env 优先级链 step 大于 job 大于 workflow
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 env 变量优先级：step 级 > job 级 > workflow 级；无 job 级定义时继承 workflow 级。

## 做了什么
workflow 级 `MY_VAR=workflow_value`，job 级覆盖为 `job_value`，step 级覆盖为 `step_value`。第一个 step 输出 `$MY_VAR`（期望 step_value），同一个 job 的第二个 step 输出 `$MY_VAR`（期望 job_value）。独立 job 无覆盖，输出 `$MY_VAR`（期望 workflow_value）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: MY_VAR=step_value | COVERED | step 级 env 覆盖后 `$MY_VAR` 解析为 step_value |
| 2 | run_logs | positive | must_contain: JOB_VAR=job_value | COVERED | 无 step 覆盖时 `$MY_VAR` 回退到 job 级 job_value |
| 3 | run_logs | positive | must_contain: WF_VAR=workflow_value | COVERED | 独立 job 无 job 级覆盖，`$MY_VAR` 继承 workflow 级 workflow_value |
