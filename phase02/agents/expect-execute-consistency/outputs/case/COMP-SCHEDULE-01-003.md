# COMP-SCHEDULE-01-003

- **标题**: cron 间隔短于 5 分钟时被拒绝或降级
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 cron 间隔 1 分钟被平台拒绝或降级为最短间隔。

## 做了什么
cron: "*/1 * * * *"（1分钟间隔），step 仅 `echo "should not run"`。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | equals success_with_1min_interval | COVERED | 非法 cron 应被平台校验期拒绝，harness 验证 status != success；平台校验类（Calibration 8） |
| 2 | error_message | nonfunctional | eval=llm_assisted | LLM_DEPENDENT | 需人工判断报错信息 |
