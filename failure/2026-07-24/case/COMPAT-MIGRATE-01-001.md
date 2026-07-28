## 失败分诊 · COMPAT-MIGRATE-01-001 · GitHub 风格 permissions 块迁移报错应给出可操作指引

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `jobs[id].permissions` 字段不被 GitCode 平台支持，报 `unknown property`
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 13（`permissions` 不支持 — job 级 `permissions` 报 `unknown property`）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    jobs:
      migrate-permissions:
        name: Test permissions block error
        runs-on: [ubuntu-latest, x64, small]
        permissions:                     # job 级 permissions 不支持
          contents: read
          pull-requests: write
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 13: "GitCode 平台完全不支持 `permissions` 字段——无论是 workflow 级还是 job 级。报 `unknown property`（workflow 级）或 `jobs[id].permissions: unknown property`（job 级）"

**置信度**: 高（平台 Schema 明确拒绝 `permissions` 字段）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `jobs[migrate-permissions].permissions: unknown property`
- **影响面**: 所有使用 job 级 `permissions` 的 workflow
- **综合**: 负向用例验证 permissions 被拒绝，GitCode 不支持 GitHub 权限模型
- **是否有规避手段**: 是 — 删除 `permissions` 块；GitCode 使用项目级别的权限模型

**建议**:
- 删除 job 级 `permissions` 块
- 此用例为预期被拒绝的负向测试，标注为 `expected_rejection`
- 在 spec-gap 中记录 `permissions` 能力缺失
