# COMP-STATUS-01-001

- **标题**: 运行状态机 queued 到 completed 转换正确
- **维度**: 完备性
- **评级**: 部分不符

---

## 想测什么
验证状态转换序列 queued → in_progress → completed(success)。

## 做了什么
Step: `echo "running"`（字面量 echo）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status_sequence | positive | equals queued_in_progress_completed | COVERED | harness 轮询 API 观测状态转换序列，workflow 为 payload |
| 2 | run_status | positive | equals success | STATUS_GUARANTEED | step 仅 echo，无条件失败路径，必然 success |
