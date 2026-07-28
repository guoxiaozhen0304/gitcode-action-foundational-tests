# REL-NEST-01-024
- **标题**: workflow_call 嵌套越界——3 层嵌套调用应被拒绝
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
A→B→C→D(3层嵌套)应失败，日志含嵌套超限提示，不应死循环。

## 做了什么
主workflow通过uses调用level1_deep.yml(内含2层调用链)。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=completed(failure) | COVERED | 文本"运行状态=failure"精确对应 |
| 2 | run_logs | positive | contains=嵌套 | COVERED | 文本"日志明确提示嵌套超限"对应(contains中文"嵌套") |
| 3 | (文本负向) 不应死循环或挂起 | — | — | MISSING | 文本"不应死循环或挂起"在YAML中无独立negative断言 |
