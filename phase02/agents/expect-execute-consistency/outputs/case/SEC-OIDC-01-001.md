# SEC-OIDC-01-001

- 标题: OIDC / 短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案
- 维度: 安全性 | 优先级: P1
- 评级: 部分不符

---

## 1. 想测什么（规格）

```
用例 ID:   SEC-OIDC-01-001
维度标签:   [security, compatibility]
维度:      安全性
优先级:    P1
溯源意图:  INTENT-SEC-034
参照来源:  inputs/gitcode-spec/
母意图:    —
标题:      OIDC / 短时凭据支持若缺失，必须明确标注为平台限制并提供替代安全方案

前置条件:
  - 仓库需要云部署凭据

操作步骤:
  1. 查阅 GitCode 文档，确认 OIDC 支持状态
  2. 若不支持，验证文档是否明确标注并提供替代方案

预期结果:
  - 不支持 OIDC 时，系统绝不应提供可长期复用的高权限云部署凭证作为默认方案
  - 文档中明确标注 OIDC 不支持，或 OIDC token 确实具备短时效与一次性

验证点:
  - [负向] 不支持 OIDC 时，系统绝不应提供可长期复用的高权限云部署凭证作为默认方案
  - [非功能] 若支持，应提供审计日志追踪 OIDC token 的签发与使用

清理:      无
```

## 2. 实际做了什么（实现）

| # | 步骤名 (job) | 关键内容 | 分类 |
|---|--------|------|------|
| 1 | Document check placeholder (oidc-check) | echo "Checking OIDC support documentation"  | VACUOUS |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| event | workflow_dispatch |
| as | maintainer |
| fault_injection | None |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| 不支持 OIDC 时，系统绝不应提供可长期复用的高权限云部署凭证作为默认方案 | 空洞 | no real logic, negative assertion may be vacuously true |
| 若支持，应提供审计日志追踪 OIDC token 的签发与使用 | 未覆盖 | 缺少非功能断言 |

### 断言逐条分析

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | platform_docs | negative |  | VACUOUS | no real logic, negative assertion may be vacuously true |
| 2 | platform_docs | positive | oidc_limitation_documented | VACUOUS | steps only echo literal strings |

### 问题

- 验证点 `不支持 OIDC 时，系统绝不应提供可长期复用的高权限云部署凭证作为默认方案` → 空洞: no real logic, negative assertion may be vacuously true

- 验证点 `若支持，应提供审计日志追踪 OIDC token 的签发与使用` → 未覆盖: 缺少非功能断言

- 断言 `[negative] platform_docs` → VACUOUS: no real logic, negative assertion may be vacuously true

- 断言 `[positive] platform_docs` → VACUOUS: steps only echo literal strings

---
