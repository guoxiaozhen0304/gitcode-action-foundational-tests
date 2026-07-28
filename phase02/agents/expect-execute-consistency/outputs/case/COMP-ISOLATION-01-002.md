# COMP-ISOLATION-01-002

- **标题**: 环境变量不跨 job 泄漏
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 job1 通过 `ATOMGIT_ENV` 设置的环境变量不会泄漏到 job2。

## 做了什么
job1 写入 `ISOLATION_VAR=leak` 到 `$ATOMGIT_ENV`；job2 检查 `$ISOLATION_VAR` 是否设置：若为空输出 "env not leaked as expected"，若非空输出 "env leaked: $ISOLATION_VAR" 并 exit 1。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | 隔离正确 → job2 不 exit 1 → workflow 成功 |
| 2 | run_logs | negative | must_not_contain: env leaked | COVERED | "env leaked" 仅在隔离失效时出现；不出现 = 隔离生效 |
