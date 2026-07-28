## 失败分诊 · COMPAT-EXPR-01-013 · success() 带括号与不带括号的兼容性差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `if: ${{ success() }}` 带括号的函数调用不被平台支持（平台拒绝 `success()`），`if: ${{ success }}` 裸关键字也被平台拒绝
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 4（`if:` 表达式 — `success()` 被拒，裸 `success` 也被拒）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
        - name: Step with parens
          if: ${{ success() }}           # ❌ 平台拒绝函数调用
        - name: Step without parens
          if: ${{ success }}             # ❌ 平台拒绝裸关键字
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 4: "`if: ${{ success() }}` — ❌ 拒绝：`表达式：success() 第1位出现不支持的函数`"
  - 规则 4: "`if: ${{ always }}`（文档写法·裸）— ❌ 拒绝：`表达式：always 第1位出现不支持的关键字`"

**置信度**: 高（平台实测确认 `${{ success() }}` 和裸 `${{ success }}` 均被拒绝）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `不支持的函数` 或 `不支持的关键字`
- **影响面**: 所有使用 `success()` / `failure()` 函数和裸 `success` / `failed` 关键字的 `if:` 表达式
- **综合**: 当前平台仅确认 `${{ always() }}` 可用，无其他状态函数可用
- **是否有规避手段**: 是 — 删除这些 `if:` 条件，或将状态判断移至 step 内 shell 脚本

**建议**:
- 移除 `if: ${{ success() }}` 和 `if: ${{ success }}` 条件
- 由于 step 默认就在 `success()` 状态下执行，无需额外条件；直接运行即可
- 此用例标注为 `expected_rejection`，验证平台拒绝非 `always()` 状态函数
