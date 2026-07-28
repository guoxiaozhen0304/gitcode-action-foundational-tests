## 失败分诊 · COMP-EXPR-01-054 · 字符串函数 contains startsWith endsWith 边界行为

**判定结果**: FAIL
**失败断言**:
- assertions[1] (positive, run_logs) — 期望 log contains 'startswith_passed'，实际 absent
- assertions[3] (positive, run_logs) — 期望 log contains 'CASE_MATCH=false'，实际 absent
- assertions[0] (positive, run_logs) — 期望 log contains 'contains_passed'，实际 present（PASS）
- assertions[2] (positive, run_logs) — 期望 log contains 'endswith_passed'，实际 present（PASS）

**根因初判**: 产品缺陷（startswith 失败因 atomgit.ref 源数据问题）+ 产品缺陷/需人工判断（CASE_MATCH 步骤未执行）

**责任人**: startswith 失败 → 平台方；CASE_MATCH 缺失 → 需人工判断（平台方和 Phase 02 联合分析）

**证据**:

- **Job 日志全文**（共 11 行）:
  ```
  contains_passed            (行 5)
                              (行 6 空)
                              (行 7 空)
                              (行 8-10: 新的脚本)
  endswith_passed            (行 11)
  ```
  `contains_passed` 出现（contains 函数本身正常），`endswith_passed` 出现（endsWith 函数本身正常），但**没有 `startswith_passed` 也没有 `CASE_MATCH`**。

- **预期行为**（用例 YAML COMP-EXPR-01-054，P1，维度 completeness）:
  - `contains(atomgit.ref_name, 'main')` → step 执行 → 输出 `contains_passed`
  - `startsWith(atomgit.ref, 'refs/heads/')` → step 执行 → 输出 `startswith_passed`
  - `endsWith(atomgit.ref_name, 'ain')` → step 执行 → 输出 `endswith_passed`
  - `contains('main', 'MAIN')`（大小写测试） → step 执行 → 输出 `CASE_MATCH=false`

- **实际行为**:
  - **startswith 失败根因**：`atomgit.ref` 返回 `main`（短格式），`startsWith(atomgit.ref, 'refs/heads/')` 结果为 false → `if` 条件不满足 → 步骤被跳过。**`startsWith` 函数本身工作正常，失败原因是输入源 `atomgit.ref` 格式与文档不符**
  - **CASE_MATCH 缺失**：该步骤**没有 `if` 条件**（YAML 第 33-35 行），理论上应无条件执行。日志中完全没有任何该步骤的脚本创建或执行痕迹。可能原因为：① 步骤因前序步骤的某种错误被跳过；② 编译后的 workflow YAML 与该步骤不同；③ 步骤因未知原因未执行

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/expressions.md`:
  - 第 41 行：`startsWith(search, prefix)` 承诺为判断字符串前缀 — 函数本身工作正常（对输入 `main` 返回 false 是正确的）
  - 第 56 行：`startsWith/endsWith` 明确标注"区分大小写"
  - 第 55 行：`contains(search, item)` 承诺为子串匹配 — 经验证正常工作

**置信度**: startswith → 高（明确是 `atomgit.ref` 源数据问题）；CASE_MATCH → 低（无法从日志中确定步骤未执行的原因）

**影响**:
- **阻塞性**: 🟡非阻塞 — Workflow 可跑完，函数本身工作正常
- **静默性**: 🟡可察觉 — startswith 的 `if` 条件导致步骤被跳过是预期行为（结果为 false），但用户可能不理解为何 `atomgit.ref` 不匹配 `refs/heads/` 前缀
- **影响面**: 🔴跨维度 — `startsWith` 搭配 `atomgit.ref` 的用法在所有 GitHub Actions 文档中广泛存在，`atomgit.ref` 格式错误导致所有此类条件判断失效
- **综合**: 非阻塞但可察觉且跨维度，根因在 `atomgit.ref` 格式而非 startsWith 函数
- **是否有规避手段**: 是 — 可用 `startsWith(atomgit.ref_name, '')` 或硬编码调整前缀，但会破坏跨平台兼容性

**建议**:
- 优先修复 `atomgit.ref` 返回格式（与 COMP-ATOMGIT-01-047 同源缺陷）
- 排查 CASE_MATCH 步骤为何未执行 — 该步骤无 `if` 条件，其缺失异常
- 相关用例: COMP-ATOMGIT-01-047（源缺陷）/ COMP-EXPR-01-055, COMP-EXPR-01-056（同维度表达式边界测试）
