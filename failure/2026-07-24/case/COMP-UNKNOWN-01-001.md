## 失败分诊 · COMP-UNKNOWN-01-001 · 包含未知顶层字段的 workflow 触发 YAML 校验失败

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 顶层包含 `unknown_field` 字段，平台拒绝任何不在 Schema 中的顶层字段
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 22（未知顶层字段拒绝）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    unknown_field: true
    on:
      workflow_dispatch:
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 22: "GitCode 校验器拒绝任何不在 schema 中的顶层字段，报 `unknown_field: unknown property`"

**置信度**: 高（平台 Schema 明确拒绝未知顶层字段）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，但用例本身预期此行为
- **静默性**: 🟢明确报错 — 平台返回 `unknown_field: unknown property`
- **影响面**: 所有含未知顶层字段的 workflow
- **综合**: 负向用例验证未知字段被拒绝，平台行为与预期一致
- **是否有规避手段**: 否 — 此用例目的即为验证 unknown field 被拒绝，正因平台正确拒绝才被分入 INVALID

**建议**:
- 此用例为预期被拒绝的负向测试，平台行为正确
- 将用例标注为 `expected_rejection`，记录平台错误信息（`unknown_field: unknown property`）
- 标记为 SKIP，校验期拒绝行为已由 API 返回值验证
