## 失败分诊 · REL-VCJOB-01-002 · 大规模 vcjob 并发提交（≥50）无丢失、无级联失败

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例需要向 Volcano 调度器并发提交 ≥50 个 vcjob 并对账（submitted==recorded==terminal==50），无平台 API 支持批量 vcjob 操作
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: manual
    params:
      platform_op: vcjob_batch_submit
      concurrency: 50
  # 注：本用例为平台操作型（vcjob 批量提交由 harness 编排，无 gitcode workflow），workflow 为 null 属用例设计。
  assertions:
    target: vcjob_terminal_reconciliation
    equals: "submitted==recorded==terminal==50"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例依赖 Volcano 批量提交 + 终态对账（≥50 并发），不在当前 Phase 02 脚本化能力范围内

**置信度**: 高

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过 API 脚本化批量提交 50 个 vcjob
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此场景受限于大规模 Volcano 并发操作
- **综合**: 需 Volcano 部署 + 批量提交编排 + 终态对账，YAML 明确注为"平台操作型"
- **是否有规避手段**: 否 — 需平台提供 vcjob 批量提交 API

**建议**:
- 平台提供 vcjob 批量提交与对账的 REST API
- Phase 02 扩展 harness：集成 Volcano 批量操作 + 终态采集能力
