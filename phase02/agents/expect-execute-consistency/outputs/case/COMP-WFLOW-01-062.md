# COMP-WFLOW-01-062

- **标题**: workflow env 与 defaults 字段验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 workflow 级 env 对所有 job/step 可见，defaults shell 被正确继承且 step 级 shell 可覆盖 defaults。

## 做了什么
顶层 env.GLOBAL_VAR=global_value 和 defaults.run.shell=bash，verify job 中 echo GLOBAL_VAR 并有一个 step 用 shell: sh 覆盖。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: GLOBAL=global_value | COVERED | run: echo "GLOBAL=$GLOBAL_VAR" 引用 workflow 级 env |
| 2 | run_logs | positive | must_contain: shell_override | COVERED | step 设 shell: sh，run echo "shell_override" |
