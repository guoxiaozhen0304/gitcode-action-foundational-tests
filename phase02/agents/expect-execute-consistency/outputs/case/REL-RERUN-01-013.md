# REL-RERUN-01-013
- **标题**: rerun 6 小时年龄限制——超期运行不可重新运行
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
完成超6小时的运行，rerun被拒绝，不应创建新运行。

## 做了什么
harness在完成时间超过6小时后尝试rerun。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | rerun_request | positive | equals=rejected | COVERED | 文本"rerun请求被拒绝"精确对应 |
| 2 | new_run_created | negative | equals=true | COVERED | 文本"不应创建新运行"精确对应(negative+equals=true) |
