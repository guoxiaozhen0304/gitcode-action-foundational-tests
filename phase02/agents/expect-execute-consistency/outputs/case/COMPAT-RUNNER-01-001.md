# COMPAT-RUNNER-01-001
- **标题**: runner.os 在 Linux Runner 上应返回 Linux
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 Linux Runner 上 `runner.os` 上下文返回 "Linux"（首字母大写，与 GitHub 一致），而非小写 "linux"。
## 做了什么
通过 `${{ runner.os }}` 输出运行器 OS 值，触发 workflow 后检查日志。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive | equals=success | COVERED | 标准运行状态检查，Harness 可直接验证 |
| 2 | run_logs | positive | llm_assisted 判断runner_os=Linux | LLM_DEPENDENT | eval=llm_assisted，需人工确认 OS 值大小写 |
