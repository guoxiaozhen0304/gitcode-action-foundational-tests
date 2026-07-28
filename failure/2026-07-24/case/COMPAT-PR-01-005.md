## 失败分诊 · COMPAT-PR-01-005 · PR paths 过滤不工作时的兼容性差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `on.pull_request` 使用了 `paths` 过滤器但未指定 `branches`，平台可能要求 `pull_request` 事件必须指定 `branches` 或 `paths` 在 `pull_request` 事件上的行为与 GitHub 不同
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 11（`on.<event>` branches 限制 — `pull_request` 的 paths 可能需要搭配 branches）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    on:
      pull_request:
        paths: ['api/**']                # 有 paths 但无 branches
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 11: "`on.merge_requests` 和 `on.pull_request_target` 的 `branches` + `branches-ignore` 之和必须 ≥1 且 ≤32"
  - `pull_request` 事件可能也需要 `branches` 声明

**置信度**: 中（`pull_request` + `paths` 无 `branches` 可能触发平台拒绝）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 branches 必须声明或 paths 在 pull_request 上不支持
- **影响面**: 所有在 `pull_request` 上用 `paths` 无 `branches` 的配置
- **综合**: PR paths 过滤在 GitCode 上的行为与 GitHub 不同
- **是否有规避手段**: 是 — 添加 `branches` 声明或改用 `push` 事件配置 paths

**建议**:
- 添加 `branches: [main]` 到 `pull_request` 配置中
- 或改用 `push` 事件配置 `paths` 过滤器
- 在 spec-gap 中记录 `pull_request.paths` 的平台限制
