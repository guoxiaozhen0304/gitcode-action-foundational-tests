## 失败分诊 · COMPAT-PR-01-004 · PR types 含 merge 时不触发与 GitHub 行为差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `on.pull_request` 使用了 `types: [open, merge]` — `merge` 不是 `pull_request` 事件的合法 type，仅属于 `merge_requests` 事件
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 12（`on.<event>.types` 允许值 — `merge` 不在 `pull_request` 允许 types 中）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    on:
      pull_request:
        types: [open, merge]             # merge 不是 pull_request 合法 type
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 12: "`merge_requests` 允许 types: `close`, `merge`, `open`, `reopen`, `update`"
  - `merge` 属于 `merge_requests` 事件，不属于 `pull_request` 事件

**置信度**: 高（`merge` 不在 `pull_request` 的 types 允许枚举中）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 types 值不合法
- **影响面**: 所有在 `pull_request` 事件中尝试使用 `merge` type 的配置
- **综合**: `pull_request` 与 `merge_requests` types 不互通
- **是否有规避手段**: 是 — 移除 `merge` 或改用 `merge_requests` 事件：
  ```yaml
  on:
    merge_requests:
      types: [open, merge]
  ```

**建议**:
- 将事件从 `pull_request` 改为 `merge_requests` 以使用 `merge` type
- 或移除 `types: [open, merge]`，不指定 types 使用默认行为
