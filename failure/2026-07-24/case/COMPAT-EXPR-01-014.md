## 失败分诊 · COMPAT-EXPR-01-014 · always() 带括号与不带括号的兼容性差异

**判定结果**: INVALID（平台 Schema 校验拒绝）
**根因初判**: `if: ${{ always }}` 裸关键字被平台拒绝，平台只认 `${{ always() }}` 带括号形式
**责任人**: Phase 01（合约生成需适配平台限制）

**证据**:

- **违反的规则**: 规则 4（`if:` 表达式 — 裸 `always` 关键字被拒，必须 `always()`）
- **具体的 YAML 差异**: 
  ```yaml
  # 当前 YAML（无效）:
        - name: Step without parens
          if: ${{ always }}              # ❌ 平台拒绝裸关键字
  
  # 应改为（正向上通过）:
        - name: Step with parens
          if: ${{ always() }}            # ✅ 平台接受带括号
  ```
  
- **对照 VALIDATION-RULES.md** `phase01/schema/VALIDATION-RULES.md`:
  - 规则 4: "`if: ${{ always() }}` — ✅ 接受（目前唯一确认可用的状态函数）"
  - 规则 4: "`if: ${{ always }}`（文档写法·裸）— ❌ 拒绝：`表达式：always 第1位出现不支持的关键字`"

**置信度**: 高（平台实测确认裸 `always` 被拒，`always()` 通过）

**影响**:
- **阻塞性**: 🔴阻塞 — 无法通过平台 YAML 校验
- **静默性**: 🟢明确报错 — 平台返回 `不支持的关键字`
- **影响面**: 所有使用裸关键字形式的状态函数调用
- **综合**: 裸关键字 `always` 不被平台接受，但 `always()` 可规避
- **是否有规避手段**: 是 — 将 `${{ always }}` 改为 `${{ always() }}`

**建议**:
- 将 `if: ${{ always }}` 改为 `if: ${{ always() }}`（带括号）
- 此用例可改为仅测 `always()`（确认通过），移除 `always` 裸关键字测试
