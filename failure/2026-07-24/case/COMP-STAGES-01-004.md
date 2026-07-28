## 失败分诊 · COMP-STAGES-01-004 · map 形式 stages 按定义顺序串行执行（回归保护）

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `stages` 的 map 格式中使用了自定义 stage key（`build_stage`、`test_stage`），平台可能要求特定格式 `stages: {default: {jobs: {...}}}`
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 17（`stages` 必须是 map — 但 map 的 key 必须为 `default` 或平台允许值）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    stages:
      build_stage:
        jobs:
          build: ...
      test_stage:
        jobs:
          test: ...
  
  # 应改为:
    stages:
      default:
        jobs:
          build:
            name: Stage one job
            ...
          test:
            name: Stage two job
            needs: build
            ...
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 17: "GitCode 的 `stages` 字段必须是 map 格式（`stages: {default: {jobs: {...}}}`），不支持数组格式。数组格式报 `Cannot deserialize Map from Array value`"

**置信度**: 高（自定义 stage key 不在平台允许的 stage 名称集合中）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 stage 名称未知或格式错误
- **影响面**: 所有使用自定义 stage key 的 stages 配置
- **综合**: `stages` 需使用 `default` 作为 key，自定义 stage 名称不被接受
- **是否有规避手段**: 是 — 使用 `stages: {default: {jobs: {...}}}`，通过 `needs` 控制 job 间顺序实现串行执行

**建议**:
- 将 `stages.build_stage` 和 `stages.test_stage` 合并为 `stages.default.jobs`
- 使用 `needs: [build]` 实现 test job 在 build job 之后执行
