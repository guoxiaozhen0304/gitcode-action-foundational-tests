## 失败分诊 · USE-PERM-01-002 · 使用 GitHub 权限域命名时报错应给出 GitCode 对照表

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 13 — `permissions` 不支持
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  permissions:
    contents: read
  on:
    workflow_dispatch:
  jobs:
    bad-perm:
      name: test github permission error
      runs-on: [ubuntu-latest, x64, small]
      steps: [...]

  # 应改为（删除 permissions 块）:
  on:
    workflow_dispatch:
  jobs:
    bad-perm:
      name: test github permission error
      runs-on: [ubuntu-latest, x64, small]
      steps: [...]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 13: "GitCode 平台**完全不支持** `permissions` 字段——无论是 workflow 级还是 job 级。报 `unknown property`（workflow 级）。" `contents: read` 是 GitHub 权限域命名，GitCode 使用 `repository` / `pr` / `issue` 等命名。

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `unknown property` 错误
- **影响面**: 所有使用 GitHub `contents` / `pull-requests` 等权限命名的工作流
- **综合**: workflow 级 `permissions` 不被平台支持，且 `contents` 是 GitHub 命名而非 GitCode 命名
- **是否有规避手段**: 是 — 删除整个 `permissions` 块

**建议**:
- 删除 workflow 级 `permissions: contents: read` 块
