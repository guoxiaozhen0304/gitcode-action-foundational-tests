## 失败分诊 · USE-EXPR-01-002 · 调用未知函数时报错应提示函数名错误与修正方向

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: 平台不支持该字段/写法
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 4 — `if:` 表达式：`${{ }}` 包裹 + `always()` 带括号
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
  - name: bad function
    if: ${{ unknownFunc() }}
    run: |
      echo "hello"

  # 应改为（使用平台支持的状态函数）:
  - name: conditional step
    if: ${{ always() }}
    run: |
      echo "hello"
  ```
- **对照 VALIDATION-RULES.md**:
  - 规则 4: "`if: ${{ success() }}` → ❌ 拒绝：`表达式：success() 第1位出现不支持的函数`。" `unknownFunc()` 同属平台不支持的函数调用，表达式校验器报 `第1位出现不支持的函数` 错误。

**置信度**: 高（平台 Schema 明确拒绝，规则明确）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验，用例无法提交执行
- **静默性**: 🟢明确报错 — 平台返回表达式函数不支持错误
- **影响面**: 所有使用自定义或 GitHub 特有函数的表达式
- **综合**: `unknownFunc()` 不在平台支持的函数列表中，表达式校验拒绝
- **是否有规避手段**: 是 — 改用 `${{ always() }}` 或 `atomgit.*` 上下文

**建议**:
- 将 `if: ${{ unknownFunc() }}` 改为 `if: ${{ always() }}`；未知函数报错测试转而验证平台对 `always()` 的正确接受
