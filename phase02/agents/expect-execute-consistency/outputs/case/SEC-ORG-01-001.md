# SEC-ORG-01-001
- **标题**: 可见范围外仓库的 workflow 绝不应读到组织级 secret 原值
- **维度**: security
- **评级**: 断言一致

## 想测什么
范围内仓库可引用组织级 secret；范围外仓库引用返回空或报错。

## 做了什么
workflow echo secrets.ORG_SHARED_KEY；trigger params 指定 repo 在可见范围外。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | must_not_contain_secret "ORG_SHARED_KEY" | COVERED | 对应"范围外仓库绝不应读到组织级 secret 原值"；platform→GENUINE |
| 2 | run_logs | positive | equals "empty_or_error_outside_scope" | COVERED | 对应"范围外仓库引用返回空或报错"；harness 检查 |
| 3 | visibility_change | nonfunctional | eval llm_assisted | COVERED | 对应"可见性变更即时生效"；LLM 辅助 = 断言一致 |
