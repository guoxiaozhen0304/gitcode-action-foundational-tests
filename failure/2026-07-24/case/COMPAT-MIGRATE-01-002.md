## 失败分诊 · COMPAT-MIGRATE-01-002 · GitHub 风格 run-name 语法迁移报错应给出可操作指引

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 顶层 `run-name` 字段 + 表达式 `${{ github.actor }}` 中使用了 `github` 上下文，两者均不被平台支持
**责任人**: Phase 01（合约生成需适配平台限制 — 负向用例预期报错）

**证据**:

- **违反的规则**: 规则 18（`run-name` 不支持）+ 平台不支持 `github` 上下文
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
    run-name: "Build by ${{ github.actor }}"   # run-name + github 上下文
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 18: "GitCode 平台不支持 `run-name` 字段（GitHub Actions 特性），报 `run-name: unknown property`"

**置信度**: 高（`run-name` 明确被拒，`github` 上下文不被 GitCode 支持）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `run-name: unknown property`
- **影响面**: 所有使用 `run-name` + `github.*` 上下文的 workflow
- **综合**: 负向用例验证 `run-name` + `github.actor` 被拒绝，平台行为与预期一致
- **是否有规避手段**: 是 — 删除 `run-name`，使用 `atomgit.*` 上下文替代 `github.*`

**建议**:
- 删除 `run-name: "Build by ${{ github.actor }}"` 整行
- GitCode 使用 `atomgit.actor` 而非 `github.actor`
- 此用例标注为 `expected_rejection`
