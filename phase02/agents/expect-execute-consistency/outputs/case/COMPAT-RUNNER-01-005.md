# COMPAT-RUNNER-01-005
- **标题**: 内网环境 Runner 不支持时的差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `runs-on: [intranet, x64]` 内网环境标签不被支持时，系统应明确报错，不应无限排队。

## 做了什么
workflow配置 `runs-on: [intranet, x64]`，step输出 `echo "hello"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | error_message | positive llm | "系统对内网环境Runner标签给出明确报错" | COVERED | error_message为平台日志(GENUINE R1) |
| 2 | run_status | negative llm | "不应无限排队" | COVERED | run_status可通过平台持续观测；负向验证不出现永久queued状态 |
