## 失败分诊 · COMPAT-VARS-01-005 · vars 在条件表达式 if 中的可用性差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 7 — `vars` 上下文不支持
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  - name: Step conditional on vars
    if: ${{ vars.ENABLE_FEATURE == 'true' }}
    run: |
      echo "feature_enabled"

  # 应改为（使用 atomgit.* 或 secrets 替代）:
  - name: Step conditional
    if: ${{ atomgit.ref == 'refs/heads/main' }}
    run: |
      echo "condition_met"
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 7: "GitCode 平台不支持 `vars.*` 上下文。引用 `vars` 的用例标注 SKIP 或改用 `atomgit.*`。"

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回表达式上下文不可用错误
- **影响面**: 所有使用 GitHub `vars.*` 上下文的工作流
- **综合**: `vars.*` 上下文不被 GitCode 平台识别，条件表达式直接报错
- **是否有规避手段**: 是 — 改用 `atomgit.*` 上下文或 `secrets.*` 替代

**建议**:
- 将 `if: ${{ vars.ENABLE_FEATURE == 'true' }}` 替换为 `if: ${{ atomgit.ref == 'refs/heads/main' }}` 或使用 secrets 替代
