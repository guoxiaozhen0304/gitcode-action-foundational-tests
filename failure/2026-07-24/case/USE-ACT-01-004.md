## 失败分诊 · USE-ACT-01-004 · 文档短名与市场名两种写法解析一致性验证

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 4b — `uses:` Action 引用格式 · step 级别仅支持插件/Action，不支持 `.yml` 工作流路径
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  - name: use cache market name
    uses: AtomgitCache

  # 应改为（使用裸官方插件名）:
  - name: use cache
    uses: cache
    with:
      path: ~/.cache
      key: probe-cache-key
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 4b: "官方插件就是裸名（checkout / setup-node / cache...）。云集成类插件 exact 名称以 GitCode 插件市场为准；未确认前用 hyphen 命名并登记 spec-gap，勿臆造。" `AtomgitCache` 是臆造的驼峰命名，不匹配任何官方插件注册名，平台返回 `格式错误：pluginname@version` 无法解析该插件名。

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回插件名无法解析错误
- **影响面**: job `market-name` 中的 `uses: AtomgitCache` 直接导致 YAML 校验失败
- **综合**: 臆造的驼峰命名 `AtomgitCache` 不匹配官方插件名 `cache`，报格式错误
- **是否有规避手段**: 是 — 改为官方裸名 `uses: cache`

**建议**:
- 将 `uses: AtomgitCache` 替换为 `uses: cache`；短名与市场名对比测试需先确认各插件的市场注册名称
