# USE-SECNAME-01-001
- **标题**: Secret 名称以 ATOMGIT_ 开头时应给出命名规则错误
- **维度**: 易用性/安全性
- **评级**: 部分不符

## 想测什么
验证引用 ATOMGIT_ 前缀的 secret 名称时平台应报错并给出 secret 命名规则提示，区分名称违规与未配置。

## 做了什么
workflow 引用 `${{ secrets.ATOMGIT_TOKEN }}`（ATOMGIT_ 前缀为保留前缀）。期望平台在校验或运行时给出命名规则错误。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | negative | 运行不应成功完成 | COVERED | 保留前缀 secret 应触发错误 → GENUINE |
| 2 | error_message | nonfunctional | 报错含 secret 名称规则和允许字符 | UNVERIFIABLE | eval: llm_assisted → LLM_DEPENDENT |
