# COMP-CTX-01-051

- **标题**: 上下文在 workflow job step 各级注入验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `atomgit`、`env`、`job` 上下文在 workflow 级 env、job 级 env、step 级 run 中均可正常解析并注入。

## 做了什么
workflow 级 env 使用 `${{ atomgit.ref }}`，job 级 env 使用 `${{ env.WF_REF }}`，step 级 run 使用 `${{ job.status }}` 和 `${{ atomgit.ref }}` 并 echo 输出。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: WF_REF=refs/ | COVERED | workflow 级 env 中 `${{ atomgit.ref }}` 求值后在 step echo 输出 |
| 2 | run_logs | positive | must_contain: JOB_REF=refs/ | COVERED | job 级 env 中 `${{ env.WF_REF }}` 向下传递后在 step echo 输出 |
| 3 | run_logs | positive | must_contain: JOB_STATUS= | COVERED | step 级 `${{ job.status }}` 实时求值后 echo 输出 |
