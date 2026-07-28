## 失败分诊 · USE-DOC-01-007 · environment 字段能力描述存在而语法参考缺失及平台报错指引

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 16 — `environment` 不支持
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  jobs:
    deploy:
      name: job with environment field
      runs-on: [ubuntu-latest, x64, small]
      environment: production
      steps: [...]

  # 应改为（删除 environment 字段）:
  jobs:
    deploy:
      name: job with environment field
      runs-on: [ubuntu-latest, x64, small]
      steps: [...]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 16: "GitCode 平台不支持 `jobs[id].environment` 字段，报 `jobs[id].environment: unknown property`。"

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `unknown property` 错误
- **影响面**: 所有引用 `environment` 字段的工作流（文档描述存在但平台不支持）
- **综合**: `environment` 是 GitHub Actions 特性，GitCode 文档可能提及但平台 Schema 拒绝
- **是否有规避手段**: 是 — 删除 `environment` 字段

**建议**:
- 删除 `environment: production` 行；文档与 Schema 的不一致需作为 spec-gap 上报
