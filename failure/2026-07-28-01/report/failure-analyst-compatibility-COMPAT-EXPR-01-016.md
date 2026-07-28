## 失败分诊 · COMPAT-EXPR-01-016 · format() 花括号转义与字符串字面量引号规则边界

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, value) — 期望 log contains 'PROBE_DONE'，实际 absent

**根因初判**: 产品缺陷

**责任人**: 平台方 — GitCode Actions 表达式求值管道未在 bash 执行前解析替换 `${{ format(...) }}` 表达式，原始表达式被直接传给 shell 导致语法错误

**证据**:

- **Job 日志全量**（8 行，workflow FAILED）:
  ```
  [2026/07/28 13:31:36.867 GMT+08:00] [INFO] Job(1531655366490337280_1531655366469365767) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../d3cc9bef.sh
  ::debug::Executing: bash -e .../d3cc9bef.sh
  /home/slave1/runner/workers/0.0.4.4.version/_temp/d3cc9bef.sh: line 1: FMT_BRACE=${{ format('{{{0}}}', 'x') }}: bad substitution
  ::error::Process exited with code 1
  ```
  - 第 2-4 行：平台正常创建了 bash 脚本并执行
  - 第 5 行：**关键证据** — bash 报错 "bad substitution"，错误行内容为 `FMT_BRACE=${{ format('{{{0}}}', 'x') }}`
  - 说明平台**未对 `${{ }}` 表达式求值**，原始表达式字符串直接被写入 shell 脚本传递给 bash
  - bash 收到 `${{ format('{{{0}}}', 'x') }}` 后尝试将其作为 shell 参数扩展解析，`{{ }}` 不是合法 bash 语法 → bad substitution
  - 第 6 行：进程 exit 1，后续步骤全部跳过

- **预期行为**（Phase 01 文本用例 COMPAT-EXPR-01-016，P2，兼容性）:
  - 操作步骤 1: 使用 `${{ format('{{{0}}}', 'x') }}` 测试花括号转义
  - 操作步骤 2: 使用 `${{ format('it''s {0}', 'ok') }}` 测试单引号转义
  - 预期结果: format 转义语义与 GitHub 对齐（双花括号→字面花括号），或文档声明不支持
  - 验证点: [正向] format 双花括号转义求值结果与 GitHub 对齐；[正向] 双单引号转义为字面单引号

- **实际行为**:
  - 表达式求值管道完全未工作——`${{ }}` 被原样写入 shell 脚本
  - bash 因语法错误退出，Step 1 即失败，Step 2 从未执行
  - 无法验证 GitCode 对 format() 转义语义的实现情况（因表达式求值本身不工作）

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/expressions.md`:
  - 第 5 行：文档明确声明 "AtomGit Action 使用 `${{ expression }}` 语法在工作流中编写表达式"，表达式在**平台侧**求值后替换
  - 第 43-44 行（函数表）：文档列出 `format(template, args...)` 为内置函数，说明为 "格式化字符串，0/1... 为占位符"，示例 `${{ format('Hello {0}, {1}!', name, role) }}`
  - 第 80-83 行（表达式示例）：文档给出 `${{ format('{0}:{1}', 'myimage', atomgit.sha) }}` 作为 env 赋值的标准用法
  - 测试 YAML 中 `${{ format('{{{0}}}', 'x') }}` 的写法与文档第 43 行 `format(template, args...)` 的函数签名完全对应——仅模板字符串更复杂（花括号转义），这是文档承诺的功能
  - 平台未能履行第 5 行承诺的基本表达式求值

**置信度**: 高（日志直接显示原始 `${{ }}` 未被求值即送入 bash，spec 第 5 行明确承诺表达式求值是平台职责）

**影响**:
- **阻塞性**: 🔴 阻塞 — 所有依赖 `${{ format() }}` 表达式的工作流均无法运行，步骤在第一步即因 shell 语法错误中断
- **静默性**: 🟡 可察觉 — bash 错误信息可见，但提示为 "bad substitution" 而非 "表达式不支持"，用户可能误以为是自己的语法问题
- **影响面**: 🔴 跨维度 — `${{ }}` 表达式求值是 GitCode Action 的核心引擎能力，此问题意味着所有使用表达式（不仅是 format）的场景都可能受影响；需进一步确认是否所有 `${{ }}` 均未被求值，或仅 complex format() 场景
- **综合**: 阻塞+跨维度——表达式求值管道未工作导致 format() 语法直接被送入 bash 产生 shell 语法错误，属于平台核心引擎缺陷；若影响面不仅限于 format() 则更为严重
- **是否有规避手段**: 否——表达式求值由平台引擎执行，用户无法绕过；只能跳过复杂 format() 调用，用其他方式构造字符串

**建议**:
- 优先排查表达式求值引擎的 `${{ }}` 解析-替换管道：确认是全局性故障还是仅 complex format 花括号转义解析失败
- 建议补充一个最小复现：`echo "${{ format('{0}', 'hello') }}"` 看简单 format 是否也失败——帮助平台缩小问题范围
- 相关用例: COMPAT-EXPR 系列所有依赖 `${{ }}` 表达式求值的用例
