## 失败分诊 · USE-API-01-001 · API 字段值与事件类型命名同一概念分裂的对照检查

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例需要调用平台 REST API 获取 PR 状态值集合，与事件类型命名集合做同概念 diff（如 `opened` vs `open`），属于 API 面文档一致性审查
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: api_response
    eval: "deterministic"
    criterion: "API 返回的 PR 状态值集合与事件类型命名集合做同概念 diff"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例依赖平台 REST API + 文档字段对照，不在当前 Phase 02 脚本化能力范围内

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可通过独立 API 调用脚本完成
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此 API 命名一致性场景
- **综合**: `workflow: null` + `target: api_response` 表明需直接调用平台 API 而非 gitcode workflow
- **是否有规避手段**: 是 — 可开发独立 API 探查脚本，但需平台 API 文档 + token

**建议**:
- Phase 02 开发 API 探查工具：调用 REST API → 解析响应字段 → diff 文档事件命名
- 平台提供完整的 API 字段文档对照表
