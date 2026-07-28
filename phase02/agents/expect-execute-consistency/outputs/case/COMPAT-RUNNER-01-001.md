# COMPAT-RUNNER-01-001
- **标题**: runner.os 在 Linux Runner 上应返回 Linux
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `${{ runner.os }}` 在Linux Runner上返回"Linux"（首字母大写，与GitHub一致），不返回小写"linux"。

## 做了什么
workflow_dispatch触发，step输出 `echo "runner_os=${{ runner.os }}"` + `echo "done"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive equals success | workflow成功执行 | COVERED | run_status平台可观测 |
| 2 | run_logs | positive llm | "runner_os应等于Linux，不应为小写linux" | COVERED | step输出${{ runner.os }}为GENUINE(R1上下文变量)；LLM_DEPENDENT(R5)但断言覆盖runner.os真实值 |
