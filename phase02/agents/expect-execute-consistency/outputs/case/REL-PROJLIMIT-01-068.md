# REL-PROJLIMIT-01-068
- **标题**: 项目级 workflow 并发上限越界——201 条同时触发时至少一条进入排队   - **维度**: reliability   - **评级**: 断言一致
## 想测什么
验证项目级并发上限越界：201 条同时触发时，至少一条进入排队（queued），全部完成无丢失，失败数=0。
## 做了什么
在 60s 内通过 API 并发触发 201 次同一 workflow（每 job echo run_id + sleep 5）。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | completed_count | positive | equals "201" | COVERED | harness 统计完成数 |
| 2 | failed_count | positive | equals "0" | COVERED | harness 统计失败数 |
| 3 | queued_count | positive | ge "1" | COVERED | harness 统计排队数，超出 200 上限部分应排队 |
| 4 | total_duration_seconds | nonfunctional | le "3600" | COVERED | harness 测量总耗时 |
| 5 | lost_count | nonfunctional | equals "0" | COVERED | harness 对账确认无丢失 |
