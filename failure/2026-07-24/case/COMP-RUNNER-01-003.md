## 失败分诊 · COMP-RUNNER-01-003 · 不存在的标签组合导致 job 排队或失败

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `runs-on` 标签 `nonexistent-os` 不是平台已知标签，平台在 Schema 校验阶段即拒绝未知标签
**责任人**: Phase 01（合约生成需适配平台限制，负向用例需标注预期 SKIP）

**证据**:

- **违反的规则**: 规则 1（Runner 标签格式 — 数组格式正确但标签值不在允许集合中）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
      runs-on: [nonexistent-os, x64, small]
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 1: "匹配逻辑：`runs-on` 中列出的所有标签必须同时存在于 Runner 的标签集合中"
  - 规则 1a: "不测 runs-on 时首选 `[ubuntu-latest, x64, small]`"

**置信度**: 高（`nonexistent-os` 不是平台已知标签，Schema 校验直接拒绝）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `unknown property` 或标签不匹配错误
- **影响面**: 所有使用不存在标签的 runs-on 配置
- **综合**: 负向测试用例（测非法标签）无法直接提交，需改为标注 SKIP 或使用平台允许的标签
- **是否有规避手段**: 否 — 此用例目的就是测试非法标签的行为，平台 Schema 层直接拒绝，无法在合法 YAML 中测试此项；需标 SKIP 并记录为 spec-gap

**建议**:
- 将此用例标记为 SKIP（平台 Schema 层拒绝非法标签，无法通过合法 YAML 提交验证）
- 在 spec-gap 中记录：平台标签校验发生在 YAML Schema 阶段而非运行阶段，无法测试非法标签的运行时行为
