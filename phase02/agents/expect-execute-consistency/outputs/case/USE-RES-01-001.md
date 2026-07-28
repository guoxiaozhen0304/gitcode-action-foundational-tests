# USE-RES-01-001
- **标题**: runtime-environment-variables.md 中不应出现未标注的 GitHub 专属变量名
- **维度**: 易用性
- **评级**: 断言一致

## 想测什么
检查 runtime-environment-variables.md 正文中是否残留未标注为 GitHub 对照的 GITHUB_ 前缀变量名（如 GITHUB_ACTION_PATH、GITHUB_ENV），独立环境变量示例应使用 ATOMGIT_ 前缀。

## 做了什么
纯文档检查用例（workflow: null）。LLM 辅助扫描文档中残留的 GITHUB_ 前缀。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | documentation | negative | 独立出现的 GITHUB_ 前缀（非引用/对照表场景）数量为 0 | UNVERIFIABLE | eval: llm_assisted，全 LLM_DEPENDENT；Rule 9 → 断言一致 |
