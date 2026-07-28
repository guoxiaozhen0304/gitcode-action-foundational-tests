## 失败分诊 · COMPAT-CONCUR-01-001 · concurrency cancel-in-progress false 时应排队而非报错

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `concurrency.cancel-in-progress` 字段为非平台支持的字段名，GitCode 使用 `concurrency.preemption.events` 体系
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 19（`concurrency` 校验规则 — GitCode 的并发控制模型与 GitHub 不同）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    concurrency:
      group: test-group-compat-034
      cancel-in-progress: false           # GitHub 风格字段名
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 19: "`preemption.events` 仅允许 `[mr_id]`; `max` ≥ 1; `exceed-action` 不能为空"
  - GitCode 不支持 `cancel-in-progress` 字段，使用 `preemption` 模型

**置信度**: 高（`cancel-in-progress` 是 GitHub Actions 字段，GitCode schema 不支持）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `cancel-in-progress: unknown property`
- **影响面**: 所有使用 GitHub 风格 `cancel-in-progress` 的 concurrency 配置
- **综合**: GitCode 并发模型与 GitHub 不兼容，需迁移到 `preemption` 模型
- **是否有规避手段**: 是 — 使用 `concurrency.preemption` 替代 `cancel-in-progress`

**建议**:
- 将 `cancel-in-progress: false` 改为 GitCode 兼容的并发控制配置：
  ```yaml
  concurrency:
    group: test-group-compat-034
  ```
- 排队行为依赖平台默认，不需要显式 `cancel-in-progress` 字段
