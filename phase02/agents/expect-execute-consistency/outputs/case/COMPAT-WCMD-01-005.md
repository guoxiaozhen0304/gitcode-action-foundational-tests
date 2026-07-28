# COMPAT-WCMD-01-005
- **标题**: debug 命令默认可见性与 GitHub ACTIONS_STEP_DEBUG 门控差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
确定 `::debug::` 命令在无门控配置时的默认可见性，与GitHub的ACTIONS_STEP_DEBUG/RUNNER_DEBUG门控差异文档化。

## 做了什么
step输出 `echo "::debug::demo debug message"` + `echo "DEBUG_PROBE_DONE"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive must_contain | "DEBUG_PROBE_DONE" | COVERED | echo直接覆盖(R1 GENUINE) |
| 2 | run_logs | positive llm | "确认debug message默认可见性，结论文档化" | COVERED | echo "::debug::..."为GENUINE(R1)；日志中该行可见/不可见直接确定默认行为；R5 LLM辅助记录结论 |
