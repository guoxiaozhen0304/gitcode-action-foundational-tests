## 失败分诊 · COMP-STAGES-01-005 · list 形式 stages 的实际处理裁定记录

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `stages` 使用了数组/list 格式 `[{...}]`，平台仅支持 map 格式
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 17（`stages` 必须是 map，不是数组）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    stages:
      - name: build-stage
        jobs:
          build: ...
  
  # 应改为（若希望通过校验）:
    stages:
      default:
        jobs:
          build: ...
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 17: "GitCode 的 `stages` 字段必须是 map 格式（`stages: {default: {jobs: {...}}}`），不支持数组格式 `stages: [{...}]`。数组格式报 `Cannot deserialize Map from Array value`"

**置信度**: 高（平台 Schema 明确拒绝数组格式 stages）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，但用例本身预期此行为
- **静默性**: 🟢明确报错 — 平台返回 `Cannot deserialize Map from Array value`
- **影响面**: 所有使用数组格式 stages 的配置
- **综合**: 负向用例验证 list 格式被拒绝，平台行为与预期一致
- **是否有规避手段**: 否 — 此用例目的即为验证 list 格式被拒绝，正因平台正确拒绝才被分入 INVALID

**建议**:
- 此用例为预期被拒绝的负向测试，平台行为正确
- 将用例标注为 `expected_rejection`（预期校验拒绝），记录平台错误信息
- 若需正向验证 list 格式改为 map 后的执行行为，参考 COMP-STAGES-01-004
