# COMP-SCHEDULE-01-001

- **标题**: 合法 cron 在默认分支按时触发
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 schedule 事件按时触发，cron 表达式合法且 event 为 schedule。

## 做了什么
Step: `echo "SCHEDULED_RUN_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)"`（date 是真实命令）+ `echo "EVENT_NAME=${{ atomgit.event_name }}"`（`${{ }}` 表达式）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals success | COVERED | step 含真实命令 `date -u` + `${{ }}`，非必然成功 |
| 2 | run_event | positive | equals schedule | COVERED | trigger.event=schedule 与断言一致 |
| 3 | run_logs | positive | must_contain SCHEDULED_RUN_UTC= | COVERED | step 运行 `date -u` 真实命令产生时间戳 |
| 4 | trigger_time | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | 需人工对比时间戳与 cron 预期 |
