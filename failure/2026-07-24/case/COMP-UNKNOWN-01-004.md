## 失败分诊 · COMP-UNKNOWN-01-004 · select 与 selected_by_default 声明时的实际行为记录

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `stages` 使用了自定义 key `gated_stage`，且 stage 和 job 级别使用了 `select: selected_by_default` 字段，这些均为 platform-unknown 字段
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 17（`stages` 必须是 map，且 key 须为平台允许值）+ 规则 22（未知字段拒绝 — `select` 不是已知字段）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    stages:
      gated_stage:                    # 非 default key
        select: selected_by_default   # 未知字段
        jobs:
          beta:
            select: selected_by_default # 未知字段
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 17: "`stages` 必须是 map 格式（`stages: {default: {jobs: {...}}}`）"
  - 规则 22: "GitCode 校验器拒绝任何不在 schema 中的顶层字段"

**置信度**: 高（`select` 字段和 `selected_by_default` 值均不在平台 Schema 中）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `unknown property`
- **影响面**: 所有使用 `select` / `selected_by_default` 字段的配置
- **综合**: `select` 和 `selected_by_default` 不是平台已知的 stage/job 字段
- **是否有规避手段**: 是 — 删除 `select` 字段，使用 `stages: {default: {jobs: {...}}}`

**建议**:
- 删除 stage 和 job 级别的 `select: selected_by_default`
- 将 `gated_stage` 改为 `default`
- `select` 语义标记为 spec-gap，平台无此能力
