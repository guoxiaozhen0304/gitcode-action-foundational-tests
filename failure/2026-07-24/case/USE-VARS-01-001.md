## 失败分诊 · USE-VARS-01-001 · vars 上下文在文档与样本中的声明必须一致

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例为文档一致性审查 — LLM 评判文档与样本中对同一能力 `vars` 上下文的声明是否一致，纯文档对照
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: documentation
    eval: llm_assisted
    rubric: "文档与样本对同一能力 vars 上下文的声明必须一致；不一致即视为可理解性缺陷"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例为文档一致性 LLM 审查，`workflow: null` + `eval: llm_assisted` 明确表示非代码执行范畴

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可通过 LLM 离线审查文档与样本
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此 vars 上下文一致性的文档场景
- **综合**: LLM 可离线比对文档声明与样本用法，但无自动化流程集成
- **是否有规避手段**: 是 — LLM 离线审查，但当前 Phase 02 无集成流水线

**建议**:
- Phase 02 开发文档一致性审查流水线：LLM 对比文档声明与样本用法
- 平台文档系统应建立文档与样本代码的同步校验机制
