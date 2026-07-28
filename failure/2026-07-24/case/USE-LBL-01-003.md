## 失败分诊 · USE-LBL-01-003 · runs-on 标签写法跨文档形态扫描（不应出现三种以上互斥形态）

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例为文档一致性质检 — 对 gitcode-spec 全文 grep `runs-on:` 归纳形态数，形态数 > 2 且无等价关系说明即不合格，属于跨文档扫描而非 workflow 执行
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
  assertions:
    target: documentation
    eval: "deterministic"
    criterion: "对 gitcode-spec 全文 grep runs-on: 归纳形态数；形态数大于 2 且文档未在任何一处集中说明等价关系即不合格"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例为跨文档 pattern 扫描 + 形态归纳，不依赖 gitcode workflow 触发

**置信度**: 高

**影响**:
- **阻塞性**: 🟡可绕过 — 可通过 grep + 形态归纳脚本离线完成
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此 runs-on 文档形态一致性场景
- **综合**: `eval: deterministic` + `target: documentation` 可通过独立文档扫描脚本实现
- **是否有规避手段**: 是 — 可开发文档 pattern 扫描脚本，当前 Phase 02 未集成

**建议**:
- Phase 02 开发文档 pattern 扫描工具：全文 grep runs-on → 形态归纳 → 等价关系检测
- 平台统一 runs-on 写法规范并标注等价关系
