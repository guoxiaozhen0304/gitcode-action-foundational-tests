# REL-PREEMPT-01-006
- **标题**: preemption events 越界值——配置 11 个应被拒绝
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
事件数=11应被解析阶段拒绝，错误含超限提示，不应静默截断。

## 做了什么
workflow preemption.events含11个事件。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | yaml_validation | positive | equals=rejected | COVERED | 文本"系统在解析阶段报错"对应(yaml_validation=rejected) |
| 2 | (文本) 错误信息含events数量超限提示 | — | — | MISSING | 文本"错误信息包含events数量超限提示"在YAML中无对应断言 |
| 3 | (文本负向) 不应静默截断 | — | — | MISSING | 文本"不应静默截断"在YAML中无独立negative断言 |
