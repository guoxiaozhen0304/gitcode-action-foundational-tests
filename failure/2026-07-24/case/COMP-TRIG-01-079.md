## 失败分诊 · COMP-TRIG-01-079 · 触发事件 types 取值与过滤边界验证

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `on.push` 同时使用了 `paths` 和 `paths-ignore`，且在 `pull_request` 事件上使用 `types: [open, merge]` — `merge` 是 `merge_requests` 事件的合法 type，不是 `pull_request` 的合法 type
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 12（`on.<event>.types` 允许值）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    on:
      pull_request:
        types: [open, merge]    # merge 不是 pull_request 的合法 type
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 12: "`pull_request_comment` 允许 types: `created`, `deleted`, `edited`; `merge_requests` 允许 types: `close`, `merge`, `open`, `reopen`, `update`"
  - `pull_request` 事件未明确列出 types 枚举，但 `merge` 仅属于 `merge_requests` 事件

**置信度**: 中（`merge` 在 `merge_requests` 事件中合法，但在 `pull_request` 事件中不合法）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 types 值不合法
- **影响面**: 所有在 `pull_request` types 中使用 `merge` 的配置
- **综合**: `pull_request` 的 types 与 `merge_requests` 的 types 不互通
- **是否有规避手段**: 是 — 移除 `types: [open, merge]` 或使用默认不指定 types；如需测试 merge 触发，改用触发器 event 为 `pull_request`

**建议**:
- 移除 `types: [open, merge]`，或保持不指定 types（让平台使用默认类型）
- 如需验证特定 type 行为，仅在 `merge_requests` 事件上使用 `merge`
