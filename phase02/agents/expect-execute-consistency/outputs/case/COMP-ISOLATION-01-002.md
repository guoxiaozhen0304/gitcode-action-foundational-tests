# COMP-ISOLATION-01-002
- **标题**: 环境变量不跨 job 泄漏
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
job1 通过 ATOMGIT_ENV 设置的环境变量在 job2 中不可见。

## 做了什么
1. job1：`echo "ISOLATION_VAR=leak" >> "$ATOMGIT_ENV"`
2. job2 (needs: job1)：检查 `${ISOLATION_VAR:-}` 是否为空，空则输出 "env not leaked as expected"，否则 exit 1

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | COVERED | job2 期望 env 为空（不 exit 1） |
| 2 | run_logs | negative | must_not_contain: env leaked | COVERED | ISOLATION_VAR 为空时输出 "env not leaked as expected" 而非 "env leaked" |
