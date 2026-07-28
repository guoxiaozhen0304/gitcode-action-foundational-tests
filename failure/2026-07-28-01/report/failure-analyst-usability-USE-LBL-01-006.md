## 失败分诊 · USE-LBL-01-006 · 含资源池名的 runs-on 写法平台识别验证

**判定结果**: FAIL

**失败断言**: assertions[0] (positive, run_status) — 期望 COMPLETED（等价于 YAML 约定的 `equals: "success"`），实际 FAILED。第二条断言（nonfunctional, target: documentation, eval: deterministic）进入 needs_review，未经引擎判定。

**根因初判**: 需人工判断

**责任人**: 多方联合 — Phase 02（环境侧确认 dedicated-hosted 资源池是否已就绪） + 平台方（确认 `[dedicate-hosted, x64, large]` 格式是否被平台识别） + Phase 01（确认前置条件是否真实满足）

**证据**:

- **Job 日志全量**（仅 1 行，无任何 shell 脚本输出）:
  ```
  [2026/07/28 13:27:04.853 GMT+08:00] [INFO] Job(1531654225249452032_1531654225224286215) duration check: true
  ```
  日志指纹 `56033effa17ea717`（非空 SHA），但仅含平台元信息行。Job duration_seconds = 103s，说明 job 被调度/等待了，但无任何步骤执行痕迹（无 `echo "scheduled on named pool"` 输出，无 `::debug::` 前缀行，无错误信息）。

- **预期行为**（Phase 01 文本用例 USE-LBL-01-006，P1，usability）:
  - 前置条件: "隔离测试实例配置了 dedicate-hosted 资源池"
  - 操作步骤 1: "以样本中的含资源池名写法声明 runs-on 并提交 workflow"
  - 操作步骤 2: "观察平台是否识别并进入对应资源池调度"
  - 预期结果: "平台应识别该写法并按资源池调度；识别结果回写文档一致性判定"
  - 验证点: "[正向] 平台应接受含资源池名的写法并成功调度"

- **实际行为**:
  - Job 终态 FAILED，无任何 shell 输出，无法确定是在调度阶段被拒、还是资源池无可用 runner、还是 runner 执行失败。
  - 用例 YAML 中无 `config_probe` 确认 dedicated-hosted 资源池已配置（setup.secrets 为空，setup.variables 为空），无法验证前置条件是否真实满足。

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/runner-management/selecting-runner-labels.md`:
  - 第 9-15 行「标签类型对照」表列出三种合法格式: 官方托管三段式 `{os},{arch},{spec}`、`default`、自托管 `self-hosted + labels`。**未提及 `dedicate-hosted` 或 `codearts-hosted` 等具名资源池作为第一段标签。**
  - 第 19-31 行「匹配规则」仅展示 `[self-hosted, linux, x64]` / `[self-hosted, npu, cann]` 形式的自托管示例，及 `default` 等价规则。
  - GitCode 规格 `phase01/inputs/gitcode-spec/writing-pipelines/configure-jobs.md` 第 33-41 行同样只描述三段式 `{os}-{version},{arch},{flavor}` 格式，无四段式含资源池名写法。
  - 综上，GitCode 文档**未承诺**支持 `[dedicate-hosted, x64, large]` 格式。

- **对照 INTENT-USE-040** (`phase01/runs/2026-07-27-01/intents/usability.md` 第 385-414 行):
  - 意图明确指出: "样本大量使用 `runs-on: [codearts-hosted, ubuntu-latest, x64, large]` 或 `[dedicate-hosted, arm64, xlarge]` 这种把「资源池名」作为第一段...的写法"，且"文档只讲三段式...未提官方池之外还有 dedicate-hosted 等具名资源池"。
  - Oracle 来源: 真实样本 (cann/*.yml / testorg/*.yaml) vs selecting-runner-labels.md diff。
  - 该意图是**探索性测试**: 验证内部样本中使用的格式是否对普通用户可用。

**置信度**: 低（日志证据严重不足——仅 1 行平台元信息，无法区分「平台不支持该格式」「资源池未配置」「runner 不可用」三种可能原因。前置条件无法验证。）

**影响**:
- **阻塞性**: 🔴阻塞 — 测试用例的 workflow 未能成功运行，无法完成预期验证。
- **静默性**: 🔴静默错误 — Job FAILED 但无任何错误信息或诊断输出，用户无法自行定位原因。
- **影响面**: 🟢单用例 — 当前仅影响 `[dedicate-hosted, x64, large]` 这一种写法；但若其他具名资源池（codearts-hosted 等）同样不可用，影响面将扩大。
- **综合**: 阻塞且静默——`[dedicate-hosted, x64, large]` 格式导致 Job 静默 FAILED，无诊断信息。无法判断是平台不支持、还是环境缺口。
- **是否有规避手段**: 否 — 若需使用 dedicate-hosted 资源池，无其他合法写法可用。

**建议**:
- 请 Phase 02 运维确认测试实例的 dedicate-hosted 资源池是否已实际配置并有可用 runner。
- 若资源池已配置，建议使用 `config_probe` 在 workflow 中明确验证（例如 echo runner 上下文信息），重新执行。
- 若资源池确认已就绪但格式仍 FAIL，则表明平台不支持该格式 → 转为「产品缺陷 / 文档缺口」（文档未列出可用资源池名，用户只能从内部样本学习）。
- 若资源池未配置 → 归类为「环境问题」。
- 相关用例: USE-LBL-01-005（同一 INTENT-USE-040 的文档 diff 用例）。
