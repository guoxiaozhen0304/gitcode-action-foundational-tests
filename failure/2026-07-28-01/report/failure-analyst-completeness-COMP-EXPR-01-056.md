## 失败分诊 · COMP-EXPR-01-056 · toJson 函数边界行为

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_logs) — 期望 log contains 'EVENT_JSON={'，实际 absent（日志实际输出 `EVENT_JSON=null`）
- assertions[1] (positive, run_logs) — 期望 log contains 'ENV_JSON={'，实际 absent（日志报语法错误，步骤未完成）
- assertions[2] (positive, run_logs) — 期望 log contains 'TEST_KEY'，实际 absent
- assertions[3] (positive, run_logs) — 期望 log contains '"event":'，实际 absent

**根因初判**: 产品缺陷

**责任人**: 平台方 — `toJson` 函数实现存在缺陷：对 `atomgit.event` 返回 `null` 而非 JSON 对象；对 `env` 上下文序列化导致语法错误

**证据**:

- **Job 日志全文**（共 11 行）:
  ```
  EVENT_JSON=null                                      (行 5)
                                                       (行 6 空)
  (行 7-9: 第二个脚本)
  /home/slave1/runner/workers/.../4be930c6-.....sh: line 1: syntax error near unexpected token `(`  (行 10)
  ::error::Process exited with code 2                 (行 11)
  ```
  - Step 1: `toJson(atomgit.event)` 返回字符串 `null`（不是 JSON 对象），说明 `atomgit.event` 在 workflow_dispatch 下可能为 null/未初始化
  - Step 2: `toJson(env)` 导致 shell 语法错误 — env 上下文中可能包含括号等特殊字符，在 JSON 序列化时生成了非法的 shell 字符串，导致 bash 解析失败
  - Step 3: 因 step 2 失败未能执行，`toJson(atomgit)` 未测试

- **预期行为**（用例 YAML COMP-EXPR-01-056，P1，维度 completeness）:
  - `toJson(atomgit.event)` → 返回 JSON 字符串 → 断言含 `EVENT_JSON={`
  - `toJson(env)` → 返回 JSON 字符串 → 断言含 `ENV_JSON={` 和 `TEST_KEY`
  - `toJson(atomgit)` → 返回 JSON 字符串 → 断言含 `"event":`

- **实际行为**:
  - **`atomgit.event` 为 null/空**: workflow_dispatch 事件下 `atomgit.event` 上下文对象可能为空或未初始化
  - **`toJson(env)` 产生非法 shell 字符串**: env 上下文对象序列化后的 JSON 字符串包含括号等特殊字符，在 bash 变量赋值 `ENV_JSON=${{ toJson(env) }}` 时引起 shell 语法错误
  - 即使 `toJson` 函数本身产生了正确的 JSON 字符串，**将其结果直接嵌入 bash 脚本而不做引号转义**是不安全的

- **对照 GitCode 规格**:
  - `phase01/inputs/gitcode-spec/syntax-reference/expressions.md` 第 47 行：`toJson(value)` 承诺 "将对象序列化为 JSON 字符串" — 对 `atomgit.event` 返回 `null` 而非 JSON 字符串，偏离承诺
  - `phase01/inputs/gitcode-spec/syntax-reference/context.md` 第 34 行：`atomgit.event` 类型为 object，说明为 "事件完整 payload 对象" — 但实际为 null/未初始化
  - 第 103-107 行：`workflow_dispatch` 事件字段表中仅列出 `inputs`，对整个 `atomgit.event` 对象在 workflow_dispatch 下的行为未有明确承诺

**置信度**: 中 — `atomgit.event` 为 null 的原因需平台确认（是故意设计还是实现缺失）；`toJson(env)` 的语法错误有明确日志证据

**影响**:
- **阻塞性**: 🔴阻塞 — step 2 的语法错误导致步骤中断，job FAILED
- **静默性**: 🟡可察觉 — 平台报错 `syntax error near unexpected token`，用户可见
- **影响面**: 🟡同维度 — 影响所有使用 `toJson` 序列化上下文的 workflow
- **综合**: 阻塞且可察觉，`toJson` 对某些上下文的序列化行为有缺陷
- **是否有规避手段**: 部分 — 用户可手动构造 JSON 而不依赖 `toJson`，但对复杂对象极不现实

**建议**:
- 平台方确认 `atomgit.event` 在 workflow_dispatch 下是否设计为有值；若应为完整 payload 则修复；若设计为空则文档需明确标注
- 平台方修复 `toJson` 输出嵌入 shell 脚本时的转义处理（至少应对 JSON 结果做 shell 安全包裹）
- 相关用例: COMP-EXPR-01-054, COMP-EXPR-01-055（同维度表达式函数边界验证）
