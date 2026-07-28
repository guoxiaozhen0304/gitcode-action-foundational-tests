## 失败分诊 · COMPAT-PR-01-008 · pull_request 不支持的 activity type（ready_for_review）不应静默不触发

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 12 — `on.<event>.types` 允许值
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  on:
    pull_request:
      types: [ready_for_review]

  # 应改为（GitCode 仅支持 open/reopen/update/merge）:
  on:
    pull_request:
      types: [open]
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 12: 平台仅允许指定 types 取值。`pull_request` 的 `types` 在 GitCode 侧只接受 `open` / `reopen` / `update` / `merge`；`ready_for_review` 是 GitHub Actions 专有值，GitCode 校验器拒绝并报 `types contains unsupported value`。

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回具体 Schema 错误信息
- **影响面**: 所有从 GitHub 迁移并使用 draft PR 就绪事件的工作流
- **综合**: `ready_for_review` 是 GitHub 专有 activity type，GitCode 不支持，YAML 遭 Schema 拒绝
- **是否有规避手段**: 是 — 替换为 GitCode 支持的 types（open/reopen/update/merge）

**建议**:
- 将 `types: [ready_for_review]` 替换为 GitCode 合法值 `types: [open, reopen, update, merge]`
