# REL-IGNORE-01-004
- **标题**: concurrency IGNORE 策略——超上限运行应直接执行
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
concurrency max=2 exceed-action=IGNORE 时同时触发 4 次，验证 4 个 run 全部 completed(success)、不出现 queued 状态。
## 做了什么
YAML 定义 concurrency max:2 exceed-action:IGNORE，sleep 30，harness 同时触发 4 次 dispatch。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals completed(success) | COVERED | YAML sleep 30 + IGNORE 策略，platform 日志确认 4 个 run 全部成功 |
| 2 | run_status | negative | equals queued | COVERED | YAML 负向断言不应出现 queued，对应文本"无 queued 状态" |
