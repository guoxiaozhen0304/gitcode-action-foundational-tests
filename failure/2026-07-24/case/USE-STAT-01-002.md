## 失败分诊 · USE-STAT-01-002 · 使用 success() 带括号时报错应提示 GitCode 括号差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 4 — `if:` 表达式：`${{ }}` 包裹 + `always()` 带括号
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  - name: step with brackets
    if: ${{ success() }}
    run: |
      echo "hello"

  # 应改为（当前唯一确认可用的状态函数）:
  - name: step
    if: ${{ always() }}
    run: |
      echo "hello"
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 4: "`if: ${{ success() }}` → ❌ 拒绝：`表达式：success() 第1位出现不支持的函数`。" `success()` 是 GitHub 语法（带括号），GitCode 不支持该函数。

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回表达式函数不支持错误
- **影响面**: 所有使用 GitHub `success()` / `failure()` 状态函数的工作流
- **综合**: `success()` 是 GitHub 语法，GitCode 仅支持 `${{ always() }}`
- **是否有规避手段**: 是 — 改用 `if: ${{ always() }}`

**建议**:
- 将 `if: ${{ success() }}` 替换为 `if: ${{ always() }}`
