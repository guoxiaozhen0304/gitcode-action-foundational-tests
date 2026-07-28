## 失败分诊 · COMPAT-CONCUR-01-003 · concurrency preemption enable 行为差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `concurrency.cancel-in-progress` 字段不被平台支持，GitCode 使用 `preemption` 模型
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 19（`concurrency` 校验规则 — `cancel-in-progress` 不是 GitCode 字段）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    concurrency:
      group: test-preemption
      cancel-in-progress: true          # GitHub 字段，平台不支持
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 19: "`preemption.events` 仅允许 `[mr_id]`; `max` ≥ 1; `exceed-action` 不能为空"
  - 规则 19a: "`preemption.events` 仅允许 `[mr_id]`"

**置信度**: 高（`cancel-in-progress` 是 GitHub Actions 字段，GitCode 不支持）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `cancel-in-progress: unknown property`
- **影响面**: 所有使用 `cancel-in-progress` 的 concurrency 配置
- **综合**: GitHub 并发取消模型不被 GitCode 支持
- **是否有规避手段**: 是 — 删除 `cancel-in-progress`，使用 `preemption.enable: true` + `preemption.events: [mr_id]`

**建议**:
- 删除 `cancel-in-progress: true`
- 改为 GitCode 兼容格式：
  ```yaml
  concurrency:
    group: test-preemption
    preemption:
      enable: true
      events: [mr_id]
  ```
