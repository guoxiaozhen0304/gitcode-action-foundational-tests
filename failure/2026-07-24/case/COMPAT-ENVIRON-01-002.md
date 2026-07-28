## 失败分诊 · COMPAT-ENVIRON-01-002 · environment 字段绑定 secrets 的行为差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `jobs[id].environment` 字段不被平台支持，报 `unknown property`
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 16（`environment` 不支持）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    jobs:
      test-environment:
        name: Test environment field
        runs-on: [ubuntu-latest, x64, small]
        environment: prod                # 平台不支持
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 16: "GitCode 平台不支持 `jobs[id].environment` 字段，报 `jobs[id].environment: unknown property`"

**置信度**: 高（平台 Schema 明确拒绝 `environment` 字段）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `unknown property`
- **影响面**: 所有使用 `environment` 字段绑定 secrets 的 workflow
- **综合**: `environment` + secrets 绑定场景同样被拒绝
- **是否有规避手段**: 是 — 删除 `environment: prod`，secrets 的可用性由项目/组织级别配置控制

**建议**:
- 删除 `environment: prod`
- 若需测试 environment 绑定 secrets 场景，标记为 SKIP（平台不支持此能力）
- 在 spec-gap 中记录 `environment` + secrets 能力缺失
