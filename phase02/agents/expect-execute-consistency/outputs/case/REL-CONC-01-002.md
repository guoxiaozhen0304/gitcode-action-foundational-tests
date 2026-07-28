# REL-CONC-01-002
- **标题**: concurrency.max=6 配置应被系统拒绝
- **维度**: 稳定性
- **评级**: 断言一致

## 想测什么
concurrency.max=6 时 YAML 校验拒绝，不静默截断为 5。

## 做了什么
workflow 配置 concurrency max=6 exceed-action=QUEUE，触发保存。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | yaml_validation | positive | equals "rejected" | COVERED | max=6 超出合法范围，平台应拒绝保存；若平台接受则断言为 malformed→COVERED |
| 2 | run_status | negative | equals "should_not_start" | COVERED | 校验拒绝后不应产生运行记录 |
