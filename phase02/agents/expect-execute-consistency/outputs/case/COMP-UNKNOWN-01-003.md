# COMP-UNKNOWN-01-003

- **标题**: 未声明 select 的 stage 与 job 默认被执行
- **维度**: 完备性
- **评级**: 部分不符

---

## 想测什么
验证未声明 select 字段的 job 默认执行（不会被跳过）。

## 做了什么
单个 job alpha，无 select 声明，run 步骤 echo "NO_SELECT_JOB_RAN"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | success | TRIVIAL | 仅有 echo 步骤，无条件失败路径，必然成功 |
| 2 | run_logs | positive | must_contain: NO_SELECT_JOB_RAN | COVERED | run 步骤直接 echo 该字符串 |
