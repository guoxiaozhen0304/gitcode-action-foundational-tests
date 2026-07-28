# COMPAT-RUNNER-01-003
- **标题**: self-hosted 标签不被支持时应明确报错
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `runs-on: [self-hosted, linux]` 在不支持的平台上应明确报错，而非无限排队。

## 做了什么
workflow配置 `runs-on: [self-hosted, linux]`，step输出 `echo "hello"`。预期平台在解析/调度阶段报错。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | error_message | positive llm | "系统对不支持的self-hosted标签给出明确报错" | COVERED | error_message为平台日志(GENUINE R1)；R5 LLM_DEPENDENT辅助理解报错内容 |
| 2 | run_status | negative llm | "不应无限排队且无提示" | COVERED | run_status可观测；无限queued状态可通过平台run状态持续观测判断 |
