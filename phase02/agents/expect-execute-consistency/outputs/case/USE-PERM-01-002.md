# USE-PERM-01-002
- **标题**: 使用 GitHub 权限域命名时报错应给出 GitCode 对照表
- **维度**: 易用性/兼容性
- **评级**: 部分不符

## 想测什么
验证使用 GitHub 的 `permissions: contents: read` 时平台应报错并列出 GitCode 可用权限域（如 repository）及对照关系。

## 做了什么
workflow 声明 `permissions: contents: read`（GitHub 命名域），job 使用 checkout。期望平台在校验阶段拒绝并给出对照提示。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | 未知权限域应导致校验失败 → GENUINE |
| 2 | error_message | nonfunctional | 报错给出 GitHub 名 vs GitCode 名对照 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
