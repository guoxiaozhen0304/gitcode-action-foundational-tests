## 失败分诊 · COMPAT-EVENT-01-001 · GitHub 全量事件集中不受支持事件（release 等）的降级方式

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `on.release` 事件不在 GitCode 支持的事件集中，GitCode 不支持 GitHub 的 `release` 事件
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 8（`on` 触发事件枚举 — `release` 不在 GitCode 支持的事件中）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    on:
      release:                          # GitCode 不支持 release 事件
        types: [published]
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 8: "`on:` 必须是 map"（格式正确但事件名不合法）
  - 支持的触发事件枚举（规则 17）: `push | pr | pull_request | fork_pr | pull_request_target | pull_request_comment | manual | schedule | tag | workflow_dispatch | issue_comment`
  - `release` 不在枚举中

**置信度**: 高（`release` 事件不在 GitCode 支持的触发事件列表中）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回事件名不合法或 `unknown property`
- **影响面**: 所有使用 `release`、`deployment`、`workflow_run` 等 GitHub 专属事件的 workflow
- **综合**: 负向用例验证不受支持事件被拒绝，平台行为与预期一致
- **是否有规避手段**: 否 — 平台不支持 `release` 事件，无法通过任何合法配置触发

**建议**:
- 此用例为预期被拒绝的负向测试
- 标注为 `expected_rejection`，记录平台正确拒绝 `release` 事件
- 标记为 SKIP，在 spec-gap 中记录 `release` 事件缺失
