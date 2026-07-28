## 失败分诊 · COMPAT-ENVIRON-01-001 · 含 environment 字段的 job 应被报错或警告

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `jobs[id].environment` 字段不被平台支持，报 `unknown property`
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 16（`environment` 不支持）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    jobs:
      test:
        name: Test environment field
        runs-on: [ubuntu-latest, x64, small]
        environment: production          # 平台不支持
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 16: "GitCode 平台不支持 `jobs[id].environment` 字段，报 `jobs[id].environment: unknown property`"

**置信度**: 高（平台 Schema 明确拒绝 `environment` 字段）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，但用例本身预期此行为
- **静默性**: 🟢明确报错 — 平台返回 `jobs.test.environment: unknown property`
- **影响面**: 所有使用 `jobs[].environment` 的 workflow
- **综合**: 负向用例验证 environment 字段被拒绝，平台行为与预期一致
- **是否有规避手段**: 否 — 此用例目的即为验证 environment 被拒绝，正因平台正确拒绝才被分入 INVALID

**建议**:
- 此用例为预期被拒绝的负向测试，平台行为正确
- 标注为 `expected_rejection`，记录平台返回 `unknown property`
- 标记为 SKIP
