## 失败分诊 · COMPAT-ACTIONDEV-01-001 · action.yml 元数据校验与 GitHub 差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `uses: ./.github/actions/my-action` 引用本地 action，路径格式或 action.yml 元数据不被平台支持
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 4b（`uses:` Action 引用格式 — 本地 action 路径格式可能不被平台支持）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
        - name: Use local action
          uses: ./.github/actions/my-action
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 4b: "本仓 Action: `./path` 格式。例 `uses: ./.gitcode/actions/my-action`"
  - Note: 平台要求的本地 action 路径是 `./.gitcode/actions/...` 而非 `.github/actions/...`

**置信度**: 高（`.github/actions/` 是 GitHub 路径约定，GitCode 使用 `.gitcode/actions/`）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回路径错误或 action 未找到
- **影响面**: 所有引用 `.github/actions/` 路径的 workflow
- **综合**: GitHub 风格的 action 路径不被 GitCode 支持
- **是否有规避手段**: 是 — 将路径改为 `./.gitcode/actions/my-action`

**建议**:
- 将 `uses: ./.github/actions/my-action` 改为 `uses: ./.gitcode/actions/my-action`
- 如需测试 GitHub 路径是否报错（负向用例），标注为预期拒绝
