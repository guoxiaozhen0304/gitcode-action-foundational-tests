# COMPAT-EXPR-01-002

- **标题**: success() 函数的处理行为差异
- **维度**: 兼容性
- **评级**: 部分不符

---

## 想测什么
验证 success() 依赖语义——job B（needs: job A）在 job A 成功后正常执行。

## 做了什么
job-a: checkout + echo "Job A done"；job-b: needs job-a, echo "Job B ran after Job A success"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | contains: Job B ran after Job A success | COVERED | run 步骤直接 echo 该字符串 |
| 2 | run_status | positive | equals: success | TRIVIAL | 两 job 均为 echo/checkout，无条件失败路径，必然成功 |
