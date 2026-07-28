# COMP-JOB-01-067

- **标题**: job 可选字段 env if timeout-minutes needs 验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 job 可选字段 `env`、`if`、`timeout-minutes`、`needs` 均被平台接受并生效。

## 做了什么
两个 job：prepare 输出 `prepare_done`；verify 设置 `needs: prepare`、`if: ${{ true }}`、`timeout-minutes: 30`、`env: JOB_VAR=job_value`，step 输出 `$JOB_VAR` 和 `optional_ok`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: prepare_done | COVERED | needs 依赖确保 prepare job 先执行输出 |
| 2 | run_logs | positive | must_contain: JOB_VAR=job_value | COVERED | job 级 env 变量在 step 中通过 `$JOB_VAR` 解析 |
| 3 | run_logs | positive | must_contain: optional_ok | COVERED | echo 直接产生 marker |
