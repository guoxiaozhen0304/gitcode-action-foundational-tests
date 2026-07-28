## 失败分诊 · USE-DIR-01-002 · .github/workflows/ 下 workflow 未被识别时应给出目录差异提示

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例验证平台在 `.github/workflows/` 下有 workflow 但无法识别时，是否给出 `.gitcode/workflows` 对照提示 — 需要平台 UI 交互或控制台消息采集
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: system_message
    eval: llm_assisted
    rubric: "提示信息必须同时包含 .github/workflows 与 .gitcode/workflows 对照字样"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例依赖平台 UI/控制台系统消息采集 + LLM 评判，不在当前 Phase 02 脚本化能力范围内

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可手动触发并截图由 LLM 评判
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此目录提示场景
- **综合**: `eval: llm_assisted` + `target: system_message` 表明无法通过代码断言自动化
- **是否有规避手段**: 是 — 手动操作 + 截图 + LLM 评判，但非全自动

**建议**:
- Phase 02 扩展 harness：集成浏览器自动化（Playwright）用于平台 UI 消息采集
- 或平台提供系统消息/通知 API
