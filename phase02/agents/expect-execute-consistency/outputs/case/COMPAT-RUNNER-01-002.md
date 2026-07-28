# COMPAT-RUNNER-01-002
- **标题**: runner.arch 在 x86_64 Runner 上应返回 X64
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `${{ runner.arch }}` 在x64 Runner上返回"X64"（与GitHub一致），不返回"x86_64"。

## 做了什么
workflow_dispatch触发，step输出 `echo "runner_arch=${{ runner.arch }}"` + `echo "done"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive equals success | workflow成功执行 | COVERED | run_status平台可观测 |
| 2 | run_logs | positive llm | "runner_arch应等于X64，不应为x86_64" | COVERED | step输出${{ runner.arch }}为GENUINE(R1上下文变量)；与001同策略 |
