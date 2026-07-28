# COMPAT-RUNNER-01-006
- **标题**: Runner 未预装 Java 工具链与 GitHub 差异
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证GitCode Runner未预装Java工具链时系统的反馈行为——是否有明确提示并建议替代方案。

## 做了什么
step执行 `java -version || true` + `mvn -version || true` + `echo "done"`。通过 `|| true` 保证即使缺失也不中断。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive llm | "系统对缺失的Java工具链给出明确提示" | COVERED | java -version / mvn -version为真实命令(GENUINE R1)，其stderr输出在run_logs中可见 |
| 2 | error_message | positive llm | "提示应建议替代方案" | COVERED | error_message为平台日志(GENUINE R1) |
