## 失败分诊 · COMPAT-FIELD-01-002 · 含 services 字段的 job 应被报错或警告

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `jobs[id].services` 字段不被 GitCode 平台支持，报 `unknown property`
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 20（`services` / `post.steps` 不支持）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    jobs:
      test:
        name: Test services field
        runs-on: [ubuntu-latest, x64, small]
        services:                        # 平台不支持 services
          redis:
            image: redis:latest
            ports:
              - 6379:6379
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 20: "GitCode 平台不支持 GitHub Actions 的 `jobs[id].services` 和 `post.steps`，均报 `unknown property`"

**置信度**: 高（平台 Schema 明确拒绝 `services` 字段）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `jobs.test.services: unknown property`
- **影响面**: 所有使用 `services` 字段启动 sidecar 容器的 workflow
- **综合**: 负向用例验证 services 被拒绝，GitCode 不支持 sidecar 容器
- **是否有规避手段**: 是 — 删除 `services` 块，sidecar 能力在 GitCode 中需通过其他方式（如 K8s runner）实现

**建议**:
- 删除 `services` 块
- 此用例为预期被拒绝的负向测试，标注为 `expected_rejection`
- 在 spec-gap 中记录 `services`（sidecar 容器）能力缺失
