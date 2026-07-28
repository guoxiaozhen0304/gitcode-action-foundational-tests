# REL-PREEMPT-01-005
- **标题**: preemption events 边界值——配置 10 个应正常解析
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
concurrency.preemption.events 含10个事件，YAML校验通过、运行正常触发。

## 做了什么
workflow concurrency max=5 queue，preemption.events含10个标准事件。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=completed(success) | COVERED | 文本"workflow YAML校验通过"+"运行正常触发"→run_status=success覆盖 |
