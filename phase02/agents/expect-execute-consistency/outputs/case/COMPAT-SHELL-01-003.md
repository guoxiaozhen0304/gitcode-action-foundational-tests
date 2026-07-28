# COMPAT-SHELL-01-003
- **标题**: Windows runner 默认 shell 差异
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode Windows Runner 默认 shell 行为——若默认 shell 不是 powershell，应给出明确说明。
## 做了什么
创建 `runs-on: [windows-latest, x64, small]` 的工作流，不声明 shell，执行 `echo %OS%`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | llm_assisted 判断默认shell正确执行Windows命令 | LLM_DEPENDENT | eval=llm_assisted |
| 2 | run_logs | positive | llm_assisted 判断非powershell时给出说明 | LLM_DEPENDENT | eval=llm_assisted |
