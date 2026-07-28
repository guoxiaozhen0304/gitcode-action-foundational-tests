## 失败分诊 · SEC-SUPPLY-01-003 · 第三方 Action 来源应具备信任边界（typosquatting 限制）

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 4b — `uses:` Action 引用格式
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  - name: Use typo action
    uses: checkout-action@v1

  # 应改为（裸插件名或 owner/repo@ref 格式）:
  - name: checkout source
    uses: checkout
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 4b: "官方插件就是裸名。`official_checkout` 不是合法语法，应写 `checkout`。" `checkout-action@v1` 不是合法的 action 引用格式——既不是裸官方插件名（`checkout`），也不是 `owner/repo@ref` 格式，step 级别不支持此类非标准引用。

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回 `格式错误：pluginname@version` 错误
- **影响面**: 所有使用非标准 action 命名的工作流
- **综合**: `checkout-action@v1` 不符合平台 step 级 uses 三种合法格式之一
- **是否有规避手段**: 是 — 改为官方裸名 `uses: checkout`

**建议**:
- 将 `uses: checkout-action@v1` 替换为 `uses: checkout`；typosquatting 测试需在平台插件市场注册正式名称后方可执行
