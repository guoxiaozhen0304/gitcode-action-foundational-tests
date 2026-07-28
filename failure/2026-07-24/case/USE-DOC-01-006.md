## 失败分诊 · USE-DOC-01-006 · syntax-reference 章节编号连续性扫描

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例为正则扫描文档章节编号（如 trigger-events.md 缺 1.7），属于静态文档结构审查，无需 workflow dispatch
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: documentation
    eval: "deterministic"
    criterion: "正则扫描 syntax-reference 各页二级编号并检测连续性；workflow-commands.md 缺 5.5、trigger-events.md 缺 1.7 且无说明即不合格"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例为文档章节编号正则扫描，属于静态审核，不依赖 gitcode workflow

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可通过正则扫描脚本离线完成
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此章节编号连续性场景
- **综合**: `eval: deterministic` + `target: documentation` 可通过独立脚本实现
- **是否有规避手段**: 是 — 可开发编号连续性正则扫描脚本

**建议**:
- Phase 02 开发文档编号连续性扫描工具：正则提取章节号 → 检测缺失 → 报告
- 平台文档系统应内置编号连续性校验
