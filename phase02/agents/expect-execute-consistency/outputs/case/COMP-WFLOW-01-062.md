# COMP-WFLOW-01-062
- **标题**: workflow env 与 defaults 字段验证   - **维度**: 完备性   - **评级**: 断言一致
## 想测什么
验证 workflow 级 env 对所有 job/step 可见，defaults.run.shell 可被 step 级覆盖。
## 做了什么
workflow_dispatch 触发，定义 GLOBAL_VAR=global_value，defaults shell=bash，step1 echo `GLOBAL=$GLOBAL_VAR`，step2 override shell=sh echo `shell_override`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | must_contain: GLOBAL=global_value | GENUINE→COVERED | `$GLOBAL_VAR` 为真实 env 引用 |
| 2 | run_logs | positive | must_contain: shell_override | GENUINE→COVERED | step 级 shell 覆盖为真实平台行为探测 |
