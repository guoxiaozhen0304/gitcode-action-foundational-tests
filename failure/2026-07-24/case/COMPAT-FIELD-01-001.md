## 失败分诊 · COMPAT-FIELD-01-001 · 含 run-name 字段的 workflow 应被报错或警告

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 顶层 `run-name` 字段不被 GitCode 平台支持，报 `unknown property`
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 18（`run-name` 不支持）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    run-name: Test Run Name             # 平台不支持 run-name 字段
    on:
      workflow_dispatch:
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 18: "GitCode 平台不支持 `run-name` 字段（GitHub Actions 特性），报 `run-name: unknown property`"

**置信度**: 高（平台 Schema 明确拒绝 `run-name` 字段）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `run-name: unknown property`
- **影响面**: 所有使用 `run-name` 字段的 workflow
- **综合**: 负向用例验证 `run-name` 被拒绝，平台行为与预期一致
- **是否有规避手段**: 是 — 删除 `run-name` 行；GitCode 默认使用 YAML 文件名或 workflow name 作为 run 标识

**建议**:
- 删除 `run-name: Test Run Name`
- 此用例为预期被拒绝的负向测试，标注为 `expected_rejection`
