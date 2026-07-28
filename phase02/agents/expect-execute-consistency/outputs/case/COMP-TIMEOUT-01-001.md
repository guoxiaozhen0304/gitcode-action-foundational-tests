# COMP-TIMEOUT-01-001

- **标题**: 未声明 timeout-minutes 的 job 在 360 分钟内正常完成
- **维度**: 完备性
- **评级**: 部分不符

---

## 想测什么
验证默认 timeout 下 job 成功完成，耗时远小于 360 分钟。

## 做了什么
Step: `echo "done"`（字面量 echo）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | STATUS_GUARANTEED | step 仅 echo，无条件失败路径 |
| 2 | run_duration | nonfunctional | less_than_minutes: 360 | LLM_DEPENDENT | 需人工检验运行时长 |
