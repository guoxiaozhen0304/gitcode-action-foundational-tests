# COMPAT-RUNSON-01-006
- **标题**: Runner OS 多样性探测：macos-latest 的调度结局
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
探测 `runs-on: [macos-latest, x64, small]` 的调度结局——调度成功或明确报错并列出受支持OS。

## 做了什么
workflow_dispatch触发，runs-on指定macos-latest；step输出 `echo "MACOS_RUNNER_SCHEDULED"` 标记调度成功。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive llm | "macos-latest结局确定：调度成功或明确报错" | COVERED | echo "MACOS_RUNNER_SCHEDULED"为GENUINE(R1)；与005同策略 |
| 2 | run_status | negative llm | "不应无限queued且无提示" | COVERED | 负向验证，run_status持续观测 |
| 3 | run_status | nonfunctional llm | "与005结论合并确定支持的OS全集" | LLM_DEPENDENT | R5: nonfunctional；合并分析需人工/LLM |
