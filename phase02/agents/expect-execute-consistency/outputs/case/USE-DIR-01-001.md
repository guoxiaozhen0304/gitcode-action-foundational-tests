# USE-DIR-01-001
- **标题**: workflow 放置于 .gitcode/workflows/ 下可正常触发
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
.gitcode/workflows/ 下的 workflow 被正常识别并触发运行。

## 做了什么
workflow 由 push 触发（branches: main），执行 `echo "workflow triggered from .gitcode/workflows/"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | COMPLETED | COVERED | push 事件触发，平台运行状态直接可观测 |

