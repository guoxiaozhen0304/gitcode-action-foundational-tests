# REL-NEST-01-023
- **标题**: workflow_call 嵌套边界——2 层嵌套调用应成功执行
- **维度**: 稳定性
- **评级**: 部分不符

## 想测什么
主workflow→level1→level2(2层嵌套)，3个workflow均success，参数每层正确传递。

## 做了什么
主workflow通过uses调用level1.yml(level1内部再调用level2.yml)。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals=completed(success) | COVERED | 文本"最外层运行状态=success"对应 |
| 2 | (文本) 所有子运行均success | — | — | MISSING | 文本"所有子运行均success"在YAML中无独立子运行断言 |
| 3 | (文本) 输入参数每层正确传递 | — | — | MISSING | YAML workflow无参数传递逻辑 |
