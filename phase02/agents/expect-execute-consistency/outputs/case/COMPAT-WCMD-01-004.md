# COMPAT-WCMD-01-004
- **标题**: 注解命令 error/warning/notice 的不中断降级行为
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证 `::error::`/`::warning::`/`::notice::` 注解命令不导致step/workflow失败，后续命令正常执行。

## 做了什么
step1输出 `echo "::error::demo..."` + `echo "::warning::demo..."` + `echo "::notice::demo..."`；step2输出 `echo "AFTER_ANNOTATION_OK"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_status | positive equals success | workflow成功 | COVERED | run_status平台可观测 |
| 2 | run_logs | positive must_contain | "AFTER_ANNOTATION_OK" | COVERED | step2 echo直接覆盖(R1 GENUINE) |
| 3 | run_logs | negative llm | "注解命令行之后不应出现日志截断、乱码" | COVERED | run_logs平台日志可观测(GENUINE R1)；AFTER_ANNOTATION_OK出现即证明后续命令执行 |
