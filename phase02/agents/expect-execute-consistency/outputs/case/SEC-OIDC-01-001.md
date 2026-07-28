# SEC-OIDC-01-001
- **标题**: OIDC / 短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案
- **维度**: security
- **评级**: 断言一致

## 想测什么
OIDC 不支持时无需长期高权限云部署凭证；文档明确标注状态。

## 做了什么
workflow 探测 ATOMGIT_ID_TOKEN_REQUEST_URL 等 OIDC 运行时信号；文档判读保留 llm_assisted。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | platform_docs | negative | eval llm_assisted | COVERED | 对应"不支持时不应提供长期高权限凭证作为默认方案"；LLM 辅助 = 断言一致 |
| 2 | platform_docs | positive | eval llm_assisted | COVERED | 对应"文档明确标注 OIDC 支持状态"；LLM 辅助 = 断言一致 |
