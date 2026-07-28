## 失败分诊 · USE-DOC-01-001 · stages 与 post 概念在迁移文档中具备可发现性

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例为文档可发现性审查 — LLM 评判迁移文档中 stages/post 概念是否有入口链接 + GitCode 差异标注，属于纯文档审查
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: documentation
    eval: llm_assisted
    rubric: "文档中关于 stages/post 的说明必须在迁移相关或快速入门类页面中有入口链接，且说明包含 GitCode 特有/GitHub 无此概念等显式差异标注"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例为文档可发现性 LLM 审查，`workflow: null` + `eval: llm_assisted` 明确表示非代码执行范畴

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可通过 LLM 离线审查文档入口链路
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此文档可发现性场景
- **综合**: 纯文档审查，LLM 可离线完成，但无自动化流程集成
- **是否有规避手段**: 是 — LLM 离线审查文档，但当前 Phase 02 无文档审查流水线

**建议**:
- Phase 02 开发文档审查流水线：自动抓取文档 → LLM 评判可发现性 → 生成报告
- 平台明确 stages/post 概念的唯一权威文档页面
