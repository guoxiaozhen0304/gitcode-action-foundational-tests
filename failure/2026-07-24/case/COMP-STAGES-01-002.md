## 失败分诊 · COMP-STAGES-01-002 · fail_fast true 时 stage 内任一 job 失败终止同阶段其余 job

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `stages` 使用了数组格式 `[{...}]` 而非 map 格式 `{default: {...}}`，平台拒绝数组格式
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 17（`stages` 必须是 map，不是数组）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    stages:
      - name: test-stage
        fail_fast: true
        jobs:
          ...
      - name: deploy-stage
        jobs:
          ...
  
  # 应改为:
    stages:
      default:
        jobs:
          ...
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 17: "GitCode 的 `stages` 字段必须是 map 格式（`stages: {default: {jobs: {...}}}`），不支持数组格式 `stages: [{...}]`。数组格式报 `Cannot deserialize Map from Array value`"

**置信度**: 高（平台 Schema 明确拒绝数组格式 stages）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `Cannot deserialize Map from Array value`
- **影响面**: 所有使用 `stages: [{...}]` 数组格式的 workflow
- **综合**: `stages` 数组格式直接被平台拒绝，且平台不支持 `fail_fast` 字段
- **是否有规避手段**: 是 — 将 stages 改为 map 格式 `stages: {default: {jobs: {...}}}`，但 `fail_fast` 需确认平台是否支持

**建议**:
- 将 `stages` 从数组格式改为 map 格式
- 移除 `fail_fast: true` 字段（平台不一定支持），改用单个 stage 内 jobs 命名为 `fail-job` 和 `should-skip` 加 `needs` 依赖测试 fail-fast 语义
