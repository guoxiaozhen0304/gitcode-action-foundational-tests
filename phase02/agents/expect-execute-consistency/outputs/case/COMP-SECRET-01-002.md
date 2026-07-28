# COMP-SECRET-01-002

- **标题**: secret 原始值不应以明文出现在标准日志中
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证通过多种方式引用 secret 时，原始值均不出现在日志中。

## 做了什么
Step: env 变量 MY_SECRET 引用 `${{ secrets.TEST_SECRET }}`，然后 `echo "env secret is $MY_SECRET"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret TEST_SECRET | COVERED | secret 通过 env 注入并使用，must_not_contain_secret 是真实安全断言（Rule 4） |
