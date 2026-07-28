## 失败分诊 · COMPAT-PERM-01-003 · permissions 命名差异——GitHub contents 权限项应报错

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 顶层 `permissions` 字段不被 GitCode 平台支持，报 `unknown property`
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 13（`permissions` 不支持 — workflow 级 `permissions` 报 `unknown property`）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    permissions:                         # workflow 级 permissions 不支持
      contents: read
    jobs:
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 13: "GitCode 平台完全不支持 `permissions` 字段——无论是 workflow 级还是 job 级。报 `unknown property`（workflow 级）或 `jobs[id].permissions: unknown property`（job 级）"

**置信度**: 高（平台 Schema 明确拒绝 `permissions` 字段，与命名无关——整个字段被拒绝）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `permissions: unknown property`
- **影响面**: 所有使用 `permissions` 字段的 workflow，无论权限项命名
- **综合**: 负向用例验证 permissions 被拒绝，平台行为与预期一致
- **是否有规避手段**: 是 — 删除整个 `permissions` 块

**建议**:
- 删除 `permissions` 块
- 此用例为预期被拒绝的负向测试，标注为 `expected_rejection`
- 在 spec-gap 中记录 `permissions` 能力缺失
