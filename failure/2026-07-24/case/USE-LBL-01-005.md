## 失败分诊 · USE-LBL-01-005 · runs-on 含资源池名写法的文档资源池清单 diff

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例为文档完整性审查 — 将样本资源池名集合（dedicate-hosted、codearts-hosted 等）与文档清单做 diff，每缺 1 个即一条缺陷，属于文档对照扫描
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: documentation
    eval: "deterministic"
    criterion: "样本资源池名集合（dedicate-hosted、codearts-hosted 等）应被文档清单包含；每缺 1 个即一条缺陷"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例为文档资源池清单对照，不依赖 gitcode workflow 触发

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可通过文档对照脚本离线完成
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此资源池清单完整性场景
- **综合**: `eval: deterministic` + `target: documentation` 可通过 diff 脚本实现
- **是否有规避手段**: 是 — 可开发文档清单 diff 脚本，当前 Phase 02 未集成

**建议**:
- Phase 02 开发文档资源池扫描工具：提取文档资源池清单 → diff 已知样本集合
- 平台统一 resource pool 文档并保持与实现同步
