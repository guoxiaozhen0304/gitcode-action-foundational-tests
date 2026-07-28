## 失败分诊 · USE-ACT-01-003 · 官方短名 Action 清单与 actions-market 插件目录的映射一致性

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例为文档一致性质检 — 将文档短名集合与市场目录插件名集合做 diff 映射，属于静态文档审查，无需 workflow dispatch
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: documentation
    eval: "deterministic"
    criterion: "文档短名集合与市场目录插件名集合建立映射；cache 与 AtomgitCache 等大小写或连字符不一致且文档未明示映射规则即不合格"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例为静态文档一致性扫描，不属于 gitcode workflow 可执行范畴

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可通过独立文档扫描脚本执行（非 workflow dispatch）
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此文档映射一致性场景
- **综合**: 文档 diff 扫描可通过 Phase 02 独立脚本工具完成，不依赖 workflow 触发
- **是否有规避手段**: 是 — 可开发独立文档映射扫描脚本，但当前 Phase 02 无此工具链

**建议**:
- Phase 02 开发文档扫描工具链：拉取官方文档 → 解析短名清单 → diff actions-market 插件目录
- 将此类纯文档质检用例归类为"离线文档审核"而非"workflow 执行"
