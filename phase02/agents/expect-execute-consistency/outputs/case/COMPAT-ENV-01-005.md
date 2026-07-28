# COMPAT-ENV-01-005
- **标题**: RUNNER_* 系列环境变量在 GitCode Runner 上的注入情况探测   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
逐字记录 RUNNER_OS/ARCH/NAME/TEMP/TOOL_CACHE/ENVIRONMENT 六个变量在 GitCode Runner 的注入情况。
## 做了什么
workflow_dispatch 触发，分两步 echo 六个 RUNNER_* 变量值，最后 echo `PROBE_DONE`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_logs | positive | must_contain: PROBE_DONE | GENUINE→COVERED | 多步真实 shell 变量读取，按 R6 GENUINE |
| 2 | run_logs | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；需 LLM 逐字记录六个变量取值 |
| 3 | run_logs | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；不应出现文档未声明的不一致注入 |
