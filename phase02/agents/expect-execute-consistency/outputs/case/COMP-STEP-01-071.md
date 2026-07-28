# COMP-STEP-01-071

- **标题**: step 执行控制 shell working-directory continue-on-error timeout-minutes 验证
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 shell、working-directory、continue-on-error、timeout-minutes 等 step 执行控制字段。

## 做了什么
Steps: shell: bash/sh 探针、`echo "PWD_NOW=$(pwd)"`（`$(pwd)` 真实命令替换）、continue-on-error: true + `exit 1`、后续 `echo "continue_ok"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | continue-on-error: true 允许 `exit 1` 后 job 继续 |
| 2 | run_logs | positive | must_contain bash_ok | COVERED | shell: bash 是平台真实特性，echo 是探针 |
| 3 | run_logs | positive | must_contain sh_ok | COVERED | shell: sh 是平台真实特性 |
| 4 | run_logs | positive | must_contain PWD_NOW=/tmp | COVERED | `$(pwd)` 真实命令替换 + working-directory 目录切换 |
| 5 | run_logs | positive | must_contain before_fail | COVERED | continue-on-error step 真实执行 echo + exit 1 |
| 6 | run_logs | positive | must_contain continue_ok | COVERED | continue-on-error 允许后续 step 执行 |
