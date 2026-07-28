## 失败分诊 · COMPAT-PATHS-01-002 · paths 过滤器 301 条越界测试

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `on.push.paths` 包含 301 条路径，超出平台 paths 数量上限（预期上限为 300）
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: `on.push.paths` 条目数量超出平台限制
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    on:
      push:
        branches: [main]
        paths:                             # 301 条路径条目，超出上限
          - 'path/001.txt'
          ...
          - 'path/301.txt'
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 11: "`on.merge_requests` 和 `on.pull_request_target` 的 `branches` + `branches-ignore` 之和必须 ≥1 且 ≤32"（对路径数量无明确限制记录）
  - 平台对 paths 数量有未文档化上限，301 条超出限制

**置信度**: 中（301 条 paths 越界触发平台拒绝，但上限值未在规则中明确记录）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 paths 数量超限错误
- **影响面**: 所有 paths 条目超过上限的 workflow
- **综合**: 负向用例验证 301 条 paths 被拒绝，验证平台数量限制
- **是否有规避手段**: 是 — 将 paths 条目减至 300 或以下

**建议**:
- 此用例为预期被拒绝的负向测试
- 标注为 `expected_rejection`，记录平台 paths 数量上限
- 减少 paths 条目至合法范围内以通过校验
