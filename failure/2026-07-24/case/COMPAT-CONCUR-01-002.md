## 失败分诊 · COMPAT-CONCUR-01-002 · concurrency 配置越界或不支持时应给出清晰报错

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `concurrency.group` 使用数组格式 `[invalid, array]`，平台期望 string 值 + `cancel-in-progress` 字段不支持
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 19（`concurrency` 校验规则）+ `concurrency.group` 应为 string 而非 array
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    concurrency:
      group: [invalid, array]          # group 应为 string，不是 array
      cancel-in-progress: false        # GitHub 字段，平台不支持
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 19: "`preemption.events` 仅允许 `[mr_id]`; `max` ≥ 1; `exceed-action` 不能为空"
  - `group` 字段应为字符串，数组格式导致类型错误

**置信度**: 高（数组格式的 `group` 值 + `cancel-in-progress` 双重重合）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回类型错误或 `unknown property`
- **影响面**: 所有使用 GitHub 风格 concurrency 配置的 workflow
- **综合**: `group` 类型错误 + `cancel-in-progress` 不兼容
- **是否有规避手段**: 是 — 将 `group` 改为 string，删除 `cancel-in-progress`

**建议**:
- 将 `group: [invalid, array]` 改为 `group: test-invalid-group`
- 删除 `cancel-in-progress: false`
- 若为负向测试预期报错，标注为 `expected_rejection`
