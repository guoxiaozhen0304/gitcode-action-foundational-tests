## 失败分诊 · COMP-UNKNOWN-01-005 · 顶层 inputs 与 manual_override 字段的实际处理记录

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 顶层 `inputs` 字段及 `manual_override: true` 不在平台 Schema 支持的字段中，报 `unknown property`
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 22（未知顶层字段拒绝 — `inputs` 不在顶层 Schema 中）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    inputs:
      branch_name:
        default: main
        manual_override: true
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 22: "GitCode 校验器拒绝任何不在 schema 中的顶层字段（如拼写错误的 `on` 变体、GitHub 专有字段等），报 `unknown_field: unknown property`"

**置信度**: 高（顶层 `inputs` 不是 GitCode workflow 标准字段，`manual_override` 也一样）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `unknown property`
- **影响面**: 所有使用顶层 `inputs` 字段的配置
- **综合**: 顶层 `inputs` 不被平台支持，平台使用 `workflow_dispatch.inputs` 在 `on` 块内定义参数
- **是否有规避手段**: 是 — 将 inputs 定义移至 `on.workflow_dispatch.inputs` 内

**建议**:
- 删除顶层 `inputs` 块
- 将参数定义移至 `on.workflow_dispatch.inputs:` 中（GitCode 标准方式）
- `manual_override` 标记为 spec-gap
