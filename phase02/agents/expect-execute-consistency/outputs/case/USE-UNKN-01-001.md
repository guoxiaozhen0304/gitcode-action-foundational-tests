# USE-UNKN-01-001
- **标题**: 未知字段如 run-name 不应被静默忽略而应给出警告或错误
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
验证使用 GitHub 特有字段 `run-name` 时平台应给出警告或错误而非静默忽略，报错应包含字段名和不支持字样。

## 做了什么
workflow 声明 `run-name: Build by ${{ atomgit.actor }}`（GitHub 特有字段）。断言依赖 LLM 判断报错信息质量。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | nonfunctional | 报错含字段名和不支持字样；如识别为 GitHub 特有则追加迁移提示 | UNVERIFIABLE | eval: llm_assisted，全 LLM_DEPENDENT；Rule 9 → 断言一致 |
