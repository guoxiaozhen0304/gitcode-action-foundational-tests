# USE-UNKN-01-002
- **标题**: 未知字段报错若识别为 GitHub 特有应追加迁移提示
- **维度**: 易用性/兼容性
- **评级**: 断言一致

## 想测什么
验证使用 GitHub 特有的 `jobs.<id>.container` 字段时平台报错应追加"该字段为 GitHub Actions 特有"的迁移提示。

## 做了什么
workflow 在 job 下声明 `container: image: node:20`（GitHub 特有字段）。断言依赖 LLM 判断报错信息是否含迁移提示。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | error_message | nonfunctional | 报错含字段名和不支持字样；如识别为 GitHub 特有则追加迁移提示 | UNVERIFIABLE | eval: llm_assisted，全 LLM_DEPENDENT；Rule 9 → 断言一致 |
