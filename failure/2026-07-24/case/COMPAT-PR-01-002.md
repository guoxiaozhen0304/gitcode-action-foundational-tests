## 失败分诊 · COMPAT-PR-01-002 · pull_request types 命名差异 - GitHub 风格 types 应报错

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `on.pull_request.types` 使用了 GitHub 风格命名（`opened`、`closed`、`reopened`），GitCode 使用不同命名（`open`、`close`、`reopen`）
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 12（`on.<event>.types` 允许值 — `opened`/`closed`/`reopened` 不在允许值中）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    on:
      pull_request:
        branches: [main]
        types: [opened, closed, reopened]   # GitHub 风格命名
  
  # 应改为（GitCode 兼容）:
        types: [open, close, reopen]        # GitCode 风格命名
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 12: "`merge_requests` 允许 types: `close`, `merge`, `open`, `reopen`, `update`"
  - GitHub 风格 `opened` / `closed` / `reopened` 不是 GitCode 合法值

**置信度**: 高（GitHub vs GitCode types 命名差异已文档化）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 types 值不合法
- **影响面**: 所有使用 GitHub 风格 pull_request types 命名的 workflow
- **综合**: 负向用例验证 GitHub types 命名被拒绝，平台应给出清晰指引
- **是否有规避手段**: 是 — 使用 GitCode 兼容命名：`open`, `close`, `reopen`, `update`

**建议**:
- 将 `types: [opened, closed, reopened]` 改为 `types: [open, close, reopen]`
- 此用例重点在验证平台对 GitHub 命名的报错信息是否清晰可操作
- 标注为 `expected_rejection` 或改为 GitCode 兼容命名后重新提交
