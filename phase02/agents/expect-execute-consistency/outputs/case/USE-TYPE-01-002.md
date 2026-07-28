# USE-TYPE-01-002
- **标题**: 使用 GitHub types 命名 opened/synchronize 时应给出可理解提示
- **维度**: 易用性/兼容性
- **评级**: 部分不符

## 想测什么
验证在 pull_request 事件中使用 GitHub 的 types [opened, synchronize] 时平台应报错并列出 GitCode 支持的 types 取值及对应关系。

## 做了什么
workflow 监听 `on: pull_request: types: [opened, synchronize]`。期望平台在校验阶段报错并给出对照提示。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | 非法 types 值应导致校验失败 → GENUINE |
| 2 | error_message | nonfunctional | 报错列出 GitCode 支持的 types 并给出 GitHub 对应关系 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
