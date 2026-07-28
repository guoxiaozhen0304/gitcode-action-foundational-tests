## 失败分诊 · COMPAT-FIELD-01-003 · 未知顶层字段不应被静默忽略而应给出警告

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 顶层 `custom_field` 不在平台 Schema 中，报 `unknown property`
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 22（未知顶层字段拒绝）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    on:
      workflow_dispatch:
    custom_field: value                 # 未知顶层字段
    jobs:
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 22: "GitCode 校验器拒绝任何不在 schema 中的顶层字段（如拼写错误的 `on` 变体、GitHub 专有字段等），报 `unknown_field: unknown property`"

**置信度**: 高（平台 Schema 明确拒绝未知顶层字段）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `custom_field: unknown property`
- **影响面**: 所有含用户自定义顶层字段的 workflow
- **综合**: 负向用例验证未知字段被拒绝，平台行为与预期一致
- **是否有规避手段**: 是 — 删除 `custom_field: value`

**建议**:
- 删除 `custom_field: value`
- 此用例为预期被拒绝的负向测试，标注为 `expected_rejection`
