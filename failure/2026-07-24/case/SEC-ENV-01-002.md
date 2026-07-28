## 失败分诊 · SEC-ENV-01-002 · 环境级 secret 审批前 workflow 不可读取

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 16 — `environment` 不支持
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  jobs:
    env-secret-denied:
      name: Access env secret before approval
      runs-on: [ubuntu-latest, x64, small]
      environment: production
      steps: [...]

  # 应改为（删除 environment 字段）:
  jobs:
    env-secret-denied:
      name: Access env secret before approval
      runs-on: [ubuntu-latest, x64, small]
      steps: [...]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 16: "GitCode 平台不支持 `jobs[id].environment` 字段，报 `jobs[id].environment: unknown property`。"

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `unknown property` 错误
- **影响面**: 所有依赖环境审批与 secret 隔离的工作流
- **综合**: `environment` 字段不被平台支持，YAML 校验直接拒绝
- **是否有规避手段**: 是 — 删除 `environment` 字段

**建议**:
- 删除 `environment: production` 行
