## 失败分诊 · USE-DOC-01-002 · stages 与 stages 内 jobs 字段语法跨文档四种形态互相矛盾的扫描

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例为跨文档一致性扫描 — grep 所有文档中 `stages:` 形态、形态组合数 > 1 且无等价关系说明即为不合格，属于文档审查而非 workflow 执行
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: documentation
    eval: "deterministic"
    criterion: "grep stages: 与 stages 内 jobs 形态；形态组合数大于 1 且文档未在任何一处说明等价关系即不合格"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例为跨文档 grep/pattern 扫描，属于静态文档审查，不依赖 gitcode workflow 触发

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可通过独立 grep 脚本离线完成
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此文档语法一致性场景
- **综合**: deterministic 判定可通过正则扫描实现，但当前 Phase 02 无文档扫描工具链
- **是否有规避手段**: 是 — 可开发 grep + pattern 扫描脚本，当前 Phase 02 未集成

**建议**:
- Phase 02 开发文档一致性扫描工具：全文 grep + 形态归纳 + 等价关系检测
- 平台指定单一权威文档页面定义 stages 语法
