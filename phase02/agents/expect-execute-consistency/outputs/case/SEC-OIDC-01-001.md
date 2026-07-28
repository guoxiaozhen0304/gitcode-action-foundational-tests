# SEC-OIDC-01-001
- **标题**: OIDC/短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案
- **维度**: 安全性
- **优先级**: P1
- **评级**: 部分不符（2026-07-28 优化后重评）

## 修复内容
原 workflow 仅 echo 占位文字（VACUOUS）。改为真实探测运行时环境 OIDC 信号（ATOMGIT_ID_TOKEN_REQUEST_URL 等平台注入变量），输出 OIDC_ENDPOINT_PRESENT/ABSENT 供文档描述与实际行为比对；文档断言保留 llm 并注释。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | platform_docs | negative | llm_assisted | 🔶 LLM_DEPENDENT | 文档内容判读（不应推荐长期凭据） |
| 2 | platform_docs | positive | llm_assisted | 🔶 LLM_DEPENDENT | 文档内容判读（OIDC 状态与替代方案标注） |

### 残留问题
文档内容检查本质不可确定化，保留 llm_assisted；workflow 已从占位 echo 升级为真实环境探测（评级由完全不符升为部分不符）。
