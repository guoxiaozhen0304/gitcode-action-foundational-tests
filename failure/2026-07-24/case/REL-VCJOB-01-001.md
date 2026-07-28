## 失败分诊 · REL-VCJOB-01-001 · vcjob（volcano job）格式任务解析与运行 — 回归用例

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例需要 Volcano 调度器部署 + 真实 vcjob YAML 提交流程，当前无 API 支持在 gitcode workflow 中解析和运行 volcano job
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: manual
    params:
      platform_op: vcjob_submit
  variables:
    volcano_deployed: "true"
    known_failure: "xlsx 实测不通过"
  assertions:
    target: vcjob_field_handling
    eval: llm_assisted
  ```
- **对照 VALIDATION-RULES.md**: 此类用例依赖 Volcano 调度器 + vcjob CRD + NPU 资源声明，不在当前 Phase 02 脚本化能力范围内

**置信度**: 高

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过 API 脚本化提交 vcjob
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此场景受限于 Volcano 部署
- **综合**: 需要 K8s + Volcano + NPU 三层基础设施，`workflow: null` 明确表示无法通过 gitcode workflow 执行
- **是否有规避手段**: 否 — 需平台提供 Volcano 集成测试环境

**建议**:
- Phase 02 扩展 harness：搭建 K8s + Volcano 测试环境
- 平台提供 vcjob 提交与状态查询 API
