# SEC-OIDC-01-001
- **标题**: OIDC/短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案   - **维度**: 安全性   - **评级**: 完全不符
## 想测什么
文档应明确标注OIDC支持状态与限制，不支持时应给出替代方案；若支持应说明token短时效与一次性。
## 做了什么
YAML workflow仅含echo "Checking OIDC support documentation"占位步骤，不执行任何功能性操作。两个断言均为llm_assisted，target platform_docs。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | platform_docs | negative | 文档不应将长期凭据作为默认推荐 | UNVERIFIABLE | eval:llm_assisted，目标为文档内容非workflow步骤 |
| 2 | platform_docs | positive | 文档应标注OIDC状态与限制 | UNVERIFIABLE | eval:llm_assisted，目标为文档内容非workflow步骤 |
