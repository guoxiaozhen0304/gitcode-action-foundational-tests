# COMPAT-YAML-01-001
- **标题**: YAML 1.1 on 键布尔陷阱与 env 中 yes/no/on/off 字面量的解析行为
- **维度**: 兼容性
- **评级**: 断言一致
## 想测什么
验证 GitCode 的 YAML 解析器能正确处理 `on` 键（不将其解析为布尔值导致触发器失效），以及 env 中 on/off 字面值的行为。
## 做了什么
提交标准的 `on: push` workflow，在 env 中放置未加引号的 `on` 字面值，观察解析和触发行为。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive | must_contain=ON_KEY_OK | COVERED | 确认 workflow 被正确解析并触发执行 |
| 2 | run_list | negative | llm_assisted 判断push后不应静默不触发 | LLM_DEPENDENT | eval=llm_assisted，需人工确认 push 后 workflow 运行列表 |
| 3 | run_logs | positive | llm_assisted 判断DEBUG_FLAG取值与GitHub比对 | LLM_DEPENDENT | eval=llm_assisted，需人工比对解析行为 |
