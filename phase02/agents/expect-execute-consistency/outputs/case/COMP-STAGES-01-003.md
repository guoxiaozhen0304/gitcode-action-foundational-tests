# COMP-STAGES-01-003

- **标题**: post.run_always true 时 workflow 失败仍执行 post
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 main job 失败后（exit 1），post 阶段因 run_always: true 仍然执行。

## 做了什么
main job: `exit 1`（故意失败）。post.run_always: true + `echo "post executed"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals failure | COVERED | `exit 1` 故意失败，run_status=failure 非必然结果 |
| 2 | post_logs | positive | contains post executed | COVERED | post 阶段 run_always: true 确保 post step 执行 |
