# COMPAT-DIR-01-003
- **标题**: .github/workflows 目录不应被识别且应给出迁移提示   - **维度**: 兼容性   - **评级**: 断言一致
## 想测什么
验证 .github/workflows 下 workflow 不被触发时系统应给出迁移提示（说明应使用 .gitcode/workflows/）。
## 做了什么
push 事件触发，step echo `hello`。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
| 1 | run_status | negative | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；.github 下不应被触发 |
| 2 | error_message | positive | eval: llm_assisted | LLM_DEPENDENT→COVERED | 校准9；系统应给出迁移提示 |
说明：与 COMPAT-DIR-01-002 互补，强调"迁移提示"维度。若 workflow 未被触发，则无 run_logs 产生，迁移提示可能存在于平台 UI/API 而非运行日志中。 |
