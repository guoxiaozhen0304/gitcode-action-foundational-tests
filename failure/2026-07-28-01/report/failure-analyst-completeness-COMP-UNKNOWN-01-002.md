## 失败分诊 · COMP-UNKNOWN-01-002 · 不应静默忽略未知字段导致用户误以为配置生效

**判定结果**: FAIL
**失败断言**:
- assertions[0] (negative, run_status_not) — 期望 conclusion != success_with_unknown_field_silently_ignored，实际 COMPLETED

**根因初判**: 产品缺陷

**责任人**: 平台方 — GitCode Actions 平台对 workflow YAML 中的未知/无关字段采取了"静默接受并继续执行"的行为，而非拒绝或警告

**证据**:

- **Job 日志全文**（共 5 行）:
  ```
  (行 1-4: 调度/脚本创建)
  should not run            (行 5)
  ```
  虽然用例标题为"不应静默忽略未知字段"，但该用例的 workflow YAML 本身**没有注入任何未知字段**（YAML 仅包含标准的 `on: workflow_dispatch:` + `jobs.test.steps[0].run:`）。run_status 为 COMPLETED，日志中正常输出了 `should not run`。

  该用例的设计意图是通过 `fault_injection: null` + `assertions[0].target: run_status` + `equals: success_with_unknown_field_silently_ignored` 配合**负向断言**来判定：如果 workflow 被平台接受并成功执行（而平台本应拒绝未知字段），则 FAIL。

- **预期行为**（用例 YAML COMP-UNKNOWN-01-002，P1，维度 completeness）:
  - 若平台能在解析阶段发现并拒绝未知字段 → workflow 不执行 → run_status 不等于 COMPLETED → 断言 PASS
  - 若平台静默接受未知字段并成功执行 → run_status = COMPLETED → 断言 FAIL（即本用例的实际结果）

- **实际行为**:
  - **但关键问题：本用例的 workflow YAML 并未包含任何未知字段！** 查看 YAML 第 14-24 行，workflow 定义仅为标准字段（`on`, `jobs`, `runs-on`, `steps`, `run`）
  - 没有任何类似 `unknown_setting: value`、`obsolete_param: x` 等已知未知字段
  - 因此 run_status=COMPLETED 是**平台对合法 workflow 的正确行为**，而非平台静默忽略了未知字段
  - 这个断言 FAIL 有两个可能解释：① 用例设计本身有误（YAML 中未注入未知字段，导致无法触发平台的未知字段处理逻辑）；② 存在一个配套的 fault_injection 机制本应在编译阶段注入未知字段但未生效

- **对照 GitCode 规格**:
  - 暂无找到 GitCode 文档中关于"未知字段应被拒绝/警告/忽略"的明确承诺
  - 这是一个**文档缺口**本身——GitCode 未声明对未知字段的处理策略

**置信度**: 中 — 断言 FAIL 是事实，但原因更可能是**用例设计/编译未注入未知字段**而非平台实际存在"静默忽略"行为

**影响**:
- **阻塞性**: ⚪无影响 — 当前版本通过合法 workflow 验证，未暴露平台的实际未知字段处理行为
- **静默性**: 🟡可察觉 — 若用户实际遇到未知字段被静默忽略的场景，这是一个高风险的安全/正确性问题（用户以为配置生效但实际未生效）
- **影响面**: 🔴跨维度 — 如果平台确实静默忽略未知字段，这会是一个影响所有 workflow 的正确性隐患
- **综合**: 无影响（因用例未实际注入未知字段，无法判定平台行为），但未知字段处理策略的缺失是潜在的系统性风险
- **是否有规避手段**: 否 — 用户在编写 workflow 时无法主动发现自己的字段是否被平台识别

**建议**:
- Phase 01 检查 fault_injection 机制：本用例的 YAML 是否有配套的字段注入逻辑（如在编译阶段向 workflow YAML 添加 `unknown_setting: xxx`），若注入未生效则属于编译缺口
- 若确认该用例确无未知字段注入逻辑，则此 FAIL 是**用例设计缺陷**（负面测试未注入负面条件），需回流 Phase 01 修正
- 建议 Phase 01 设计明确注入已知未知字段（如 `non_existent_param: 123`）的 workflow YAML 变体，而非依赖运行时推断
