## 失败分诊 · USE-ONBD-01-001 · 新手快速开始路径端到端可复刻走查

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例需要真人/LLM 模拟新手按文档 00-overview → 01-quick-start 逐步操作并记录卡壳点，属于人为因素测试，`eval: llm_assisted` + 主观评判
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: documentation
    eval: "llm_assisted"
    rubric: "由无 GitCode 经验的评测者或 LLM 模拟新手按 00-overview 与 01-quick-start 逐步操作，记录每个卡壳点；卡壳点数量应为 0，全流程应不超过 30 分钟"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例为人因文档走查，需要人类判断或 LLM 模拟，不在脚本化自动化范畴

**置信度**: 高

**影响**:
- **阻塞性**: 🔴阻塞 — 需要真人或 LLM 模拟，无法纯代码自动化
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此新手引导流程
- **综合**: 人为因素测试，`"新手是否会卡需主观评判"` 明确标注不可自动化
- **是否有规避手段**: 否 — 需人类评测者或 LLM 模拟新手路径

**建议**:
- Phase 02 开发文档可用性测试流水线：LLM 模拟新手 → 逐步执行 → 记录卡壳点
- 仍无法完全替代真人可用性测试，建议作为定期手动复查项
