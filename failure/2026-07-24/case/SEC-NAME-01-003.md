## 失败分诊 · SEC-NAME-01-003 · 可遮蔽系统变量的 secret 命名创建时必须被拒

**判定结果**: SKIP（无法脚本化执行）
**根因初判**: 平台能力边界 — 当前测试 infrastructure 无法自动化此场景
**责任人**: 多方联合（Phase 02 扩充自动化能力 + 平台补全 API）

**证据**:

- **SKIP 原因**: 用例需要通过平台 secret 管理 API 尝试创建多种非法命名的 secret（ATOMGIT_TOKEN、my-secret、1SECRET）并验证拒绝，当前无标准化 secret 管理 API
- **具体阻塞点**:
  ```yaml
  # 当前 YAML 的特征:
  workflow: null
  trigger:
    event: workflow_dispatch
    params:
      invalid_names: ["ATOMGIT_TOKEN", "my-secret", "1SECRET"]
      valid_name: "DEPLOY_KEY"
  # 注：本用例为平台操作型——harness 通过 secret 管理 API 逐一尝试创建 invalid_names 与
  # valid_name，无 gitcode workflow，workflow 为 null 属用例设计。
  assertions:
    target: secret_mgmt_api
    must_not_equal: "invalid_name_accepted"
  ```
- **对照 VALIDATION-RULES.md**: 此类用例依赖平台 secret 管理 API，不在当前 Phase 02 脚本化能力范围内

**置信度**: 高

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过 API 脚本化创建/删除 secret 并验证命名规则
- **静默性**: 🟡可察觉 — 分类阶段明确标记为 SKIP
- **影响面**: 🟢单用例 — 仅此场景受限于 secret 命名校验
- **综合**: 需要平台 secret CRUD API 才能自动化验证命名约束
- **是否有规避手段**: 否 — 需平台提供 secret 管理 REST API

**建议**:
- 平台补全 secret 管理 API（创建/删除/列表）
- Phase 02 扩展 harness：集成 secret 管理 API 调用
