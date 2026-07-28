# COMPAT-WCMD-01-001
- **标题**: ::add-mask:: 不被支持时应静默降级而非报错
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `::add-mask::` workflow命令不被支持时workflow不因该命令而失败。

## 做了什么
step输出 `echo "::add-mask::MY_SECRET_VALUE"` + `echo "MY_SECRET_VALUE"` + `echo "done"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive equals success llm | "workflow不因add-mask命令而失败" | COVERED | echo "::add-mask::..."为GENUINE(R1)；run_status可观测是否成功 |
| 2 | run_logs | negative llm | "add-mask不应导致workflow报错中断" | COVERED | run_logs中可观测该步骤是否报错(GENUINE R1平台日志) |
