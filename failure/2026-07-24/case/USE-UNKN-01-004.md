## 失败分诊 · USE-UNKN-01-004 · 未文档化字段 select/manual_override/code-update/顶层 inputs 的文档集合 diff

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例为文档完整性审查 — 将样本 YAML key 集合与文档合法 key 集合做 diff，检测 `select`、`manual_override`、`code-update`、顶层 `inputs` 等未文档化字段，属于文档对照扫描
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: documentation
    eval: "deterministic"
    criterion: "样本 YAML key 集合与文档合法 key 集合 diff；select、manual_override、code-update、顶层 inputs 等样本独有 key 数量应为 0"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例为文档完整性对照扫描，`workflow: null` + `target: documentation` 表示不依赖 gitcode workflow 触发

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可通过 diff 脚本离线完成
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此未文档化字段场景
- **综合**: `eval: deterministic` + `target: documentation` 可通过正则提取 + diff 脚本实现
- **是否有规避手段**: 是 — 可开发文档 key 扫描 + diff 脚本，当前 Phase 02 未集成

**建议**:
- Phase 02 开发文档 key 集对照工具：提取文档合法字段 → 提取样本实际字段 → diff → 报告未文档化字段
- 平台文档系统应与代码实现字段同步更新
