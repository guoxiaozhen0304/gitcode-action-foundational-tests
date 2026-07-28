## 失败分诊 · USE-TYPE-01-002 · 使用 GitHub types 命名 opened/synchronize 时应给出可理解提示

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
      types:
        - opened
        - synchronize

  # 应改为（GitCode 命名规范）:
  on:
    pull_request:
      types:
        - open
        - update
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 12: 平台仅允许指定 types。`pull_request` 的 types 使用 GitCode 命名 `open` / `reopen` / `update` / `merge`，而非 GitHub 的 `opened` / `synchronize` / `reopened`。规则表中 `merge_requests` types 的对照（`open` 非 `opened`）佐证了这一命名差异。

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 types 值不支持错误
- **影响面**: 所有从 GitHub 迁移并使用 `opened` / `synchronize` / `reopened` 命名的工作流
- **综合**: `opened` / `synchronize` 是 GitHub 命名，GitCode 使用 `open` / `update`
- **是否有规避手段**: 是 — 替换为 GitCode 命名 `open` / `update` / `reopen` / `merge`

**建议**:
- 将 `opened` → `open`，`synchronize` → `update`；保持与 GitCode 命名规范一致
