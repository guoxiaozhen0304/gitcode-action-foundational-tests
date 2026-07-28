## 失败分诊 · COMP-EXPR-01-055 · hashFiles 函数边界行为

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_logs) — 期望 log contains 'SINGLE_HEX64=yes'，实际 absent
- assertions[1] (positive, run_logs) — 期望 log contains 'MULTI_HEX64=yes'，实际 absent
- assertions[2] (positive, run_logs) — 期望 log contains 'NONE_EMPTY=yes'，实际 absent

**根因初判**: 产品缺陷

**责任人**: 平台方 — GitCode Actions 未实现或未正确实现 `hashFiles` 函数

**证据**:

- **Job 日志全文**（共 9 行）:
  ```
  (行 1-4: 调度/脚本创建)
  /home/slave1/runner/workers/0.0.4.4.version/_temp/.../6a4c295b-.....sh: line 1: HASH_SINGLE=${{ hashFiles('package.json') }}: bad substitution  (行 5)
  ::error::Process exited with code 1  (行 6)
  ```
  第一个 step 的 shell 脚本在执行时直接报 `bad substitution` 错误并退出（code 1）。`${{ hashFiles('package.json') }}` 表达式在脚本生成阶段**未被 runner 求值**，表达式文本原样进入了生成的 .sh 文件，导致 bash 将其当作 shell 变量替换语法解析失败。

- **符合平台行为的预期行为**（用例 YAML COMP-EXPR-01-055，P1，维度 completeness）:
  - hashFiles 应返回文件的 SHA256 hex hash（64 字符），匹配 `^[0-9a-f]{64}$` → PASS 断言 `SINGLE_HEX64=yes`
  - 多 pattern hashFiles → PASS 断言 `MULTI_HEX64=yes`
  - 无匹配 hashFiles → 返回空字符串 → PASS 断言 `NONE_EMPTY=yes`

- **实际行为**:
  - Runner 在生成步骤 shell 脚本时**未对 `${{ hashFiles(...) }}` 进行表达式求值**
  - 表达式原样保留为 `${{ hashFiles('package.json') }}` 进入 bash 脚本
  - bash 尝试将 `{{ hashFiles('package.json') }}` 作为 shell 变量替换 → `bad substitution` 报错 → 进程退出
  - 失败传导链: Step 1 FAILED → 后续所有 step 未执行 → 全部断言失败

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/syntax-reference/expressions.md`:
  - 第 46 行：明确列出 `hashFiles(paths...)` 函数，说明为 "计算文件哈希值"，示例 `${{ hashFiles('src/**', 'package.json') }}`
  - 第 58 行：详细说明 `hashFiles` 为 "计算匹配路径文件的组合 SHA256 哈希，用于缓存 key 生成"
  - 测试 YAML 直接使用文档示例语法 `hashFiles('package.json')`，但 runner 未对其求值

**置信度**: 高（日志错误信息直接，`bad substitution` 是表达式未被求值的典型症状）

**影响**:
- **阻塞性**: 🔴阻塞 — 步骤因表达式未被求值而立即崩溃，整个 job FAILED，所有后续步骤停止
- **静默性**: 🟡可察觉 — 平台输出了 `::error::Process exited with code 1`，用户能从错误码中发现失败，但错误信息 `bad substitution` 不会直接指向"hashFiles 未实现"
- **影响面**: 🟡同维度 — 影响所有依赖 `hashFiles` 做缓存 key 生成或文件指纹的 CI pipeline
- **综合**: 阻塞且可察觉，`hashFiles` 表达式不被 runner 求值为致命功能缺失
- **是否有规避手段**: 否 — 无替代的内置函数实现文件哈希计算

**建议**:
- 平台方需实现 `hashFiles` 表达式的 runner 端求值（在生成 shell 脚本前将表达式替换为计算结果）
- 相关用例: COMP-EXPR-01-056（toJson 函数也疑似存在类似未求值问题）
