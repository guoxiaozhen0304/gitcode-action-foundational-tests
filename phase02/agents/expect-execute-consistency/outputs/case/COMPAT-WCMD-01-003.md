# COMPAT-WCMD-01-003
- **标题**: ::stop-commands:: 不被支持时应静默降级而非报错
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `::stop-commands::` / `::pause::` 不被支持时workflow不因此失败。

## 做了什么
step输出 `echo "::stop-commands::pause"` + `echo "::set-output name=K::V"` + `echo "::pause::"` + `echo "done"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive equals success llm | "workflow不因stop-commands而失败" | COVERED | echo "::stop-commands::..."为GENUINE(R1) |
| 2 | run_logs | negative llm | "stop-commands不应导致workflow报错中断" | COVERED | run_logs平台日志(GENUINE R1) |
