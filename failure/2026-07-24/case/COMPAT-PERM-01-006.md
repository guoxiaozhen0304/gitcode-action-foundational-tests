## 失败分诊 · COMPAT-PERM-01-006 · job 级 permissions 字段的支持度与降级方式

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: workflow 级 `permissions` + job 级 `permissions` 双重违规，两个级别均不被平台支持
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 13（`permissions` 不支持 — workflow 级 + job 级均不支持）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    permissions:                         # workflow 级 permissions 不支持
      contents: read
    jobs:
      probe:
        permissions:                     # job 级 permissions 不支持
          contents: write
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 13: "GitCode 平台完全不支持 `permissions` 字段——无论是 workflow 级还是 job 级。报 `unknown property`（workflow 级）或 `jobs[id].permissions: unknown property`（job 级）"

**置信度**: 高（平台 Schema 明确拒绝所有级别的 `permissions` 字段）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 workflow 级 + job 级 `unknown property`
- **影响面**: 所有含 workflow 级和 job 级 permissions 的配置
- **综合**: 负向用例验证多级 permissions 被拒绝，GitCode 不支持任何级别的权限声明
- **是否有规避手段**: 是 — 删除所有 `permissions` 块

**建议**:
- 删除 workflow 级和 job 级 `permissions` 块
- 此用例为预期被拒绝的负向测试，标注为 `expected_rejection`
- 在 spec-gap 中记录 GitCode permissions 模型完全缺失
