## 失败分诊 · REL-RUNNER-01-050 · 架构标签调度正确性——x64 请求不得落到 arm64 节点（反之亦然）

**判定结果**: FAIL
**失败断言**: assertions[0] (status, run_status) — 期望 all job/step green，实际 job 'arm64 arch probe job' status=FAILED

**根因初判**: 产品bug

**责任人**: 平台方 — arm64 架构 Runner 在文档中声明可用，实际无法调度执行

**证据**:

- **Job 日志全量**（仅 7 行，仅含 x64 job 输出）:
  ```
  [2026/07/28 13:20:32.183 GMT+08:00] [INFO] Job(1531652578574217216_1531652578549051399) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: /home/slave1/runner/workers/0.0.4.4.version/_temp/8bf2b047-5569-4242-8942-cf73b3705bee.sh
  ::debug::Executing: bash -e /home/slave1/runner/workers/0.0.4.4.version/_temp/8bf2b047-5569-4242-8942-cf73b3705bee.sh
  declared=x64 actual=x86_64

  [2026/07/28 13:20:32.256 GMT+08:00] [INFO] Job(1531652578574217216_1531652578549051401) duration check: true
  ```
  - x64 job（1531652578574217216_1531652578549051399）：`uname -m` 输出 `x86_64`，与 `runs-on: [ubuntu-latest, x64, small]` 声明的架构一致——x64 调度正确。
  - arm64 job（1531652578574217216_1531652578549051401）：日志仅含 `duration check: true` 一行，无脚本创建、无 shell 执行痕迹——arm64 job 未在任何 Runner 上实际执行即 FAILED。
  - 结论：x64 标签正确调度到 x86_64 节点；arm64 标签找不到匹配 Runner。

- **预期行为**（Phase 01 文本用例 `phase01/runs/2026-07-27-01/cases/text/REL-RUNNER-01-050.md`，优先级 P1，维度 stability）:
  - 操作步骤 1: "分别触发 runs-on 声明 x64 与 arm64 的探针 job（job 内打印 uname -m）"
  - 操作步骤 3: "对无匹配架构空闲 runner 的场景观察排队/报错行为"
  - 预期结果: "x64 job 的 uname -m 输出=x86_64；arm64 job 输出=aarch64"
  - 验证点 [正向]: "arm64 探针输出=aarch64"
  - 验证点 [非功能]: "无对应架构空闲 runner 时状态=queued 或明确报错，而非错配执行"

- **实际行为**:
  - arm64 job 既未在 arm64 节点执行（无 `aarch64` 输出），也未进入排队/明确报错状态——直接 FAILED 且无任何诊断输出。
  - arm64 探针功能完全未被测试到。

- **对照 GitCode 规格**:
  - `phase01/inputs/gitcode-spec/runner-management/selecting-runner-labels.md` 第 11-14 行：标签类型对照表，`arch` 段位可选值明确包含 `arm64`，示例 `{ubuntu-24,x64,small}`。
  - `phase01/inputs/gitcode-spec/runner-management/using-hosted-runners.md` 第 17-21 行：官方托管 Runner 标签体系，`arch` 段位可选值明确包含 `arm64`；第 84-88 行给出多标签匹配示例 `runs-on: {ubuntu-24,arm64,medium}`。
  - `phase01/inputs/gitcode-spec/core-concepts/runner-and-environment.md` 第 14 行：官方资源池标签 `arch` 可选值 = `x64`、`arm64`。
  - 测试 YAML 中 `runs-on: [ubuntu-latest, arm64, small]` 与规格示例写法完全一致——平台文档确凿承诺 arm64 支持，测试用例严格按文档写法编写。

**置信度**: 高（x64 job 调度成功、arm64 job 无执行痕迹的直接对比证据；三处规格文档均明确列出 arm64 为有效标签；arm64 job 连 `::debug::Script file created` 都没有，证明 Runner 调度层面就失败了）

**影响**:
- **阻塞性**: 🔴阻塞 — arm64 架构 Runner 完全不可用，阻止所有需要 arm64 架构的 workflow
- **静默性**: 🔴静默错误 — arm64 job 直接 FAILED 且无任何诊断信息（无排队提示、无"无匹配 Runner"报错、无 `::error::` 日志），用户无法判断是"暂无可用的 arm64 Runner"还是"arm64 标签本身不被支持"
- **影响面**: 🔴跨维度 — arm64 是现代 CI 生态的关键架构（Apple Silicon 自托管 Runner、ARM 云原生构建、Docker 多架构镜像），缺失影响所有涉及 ARM 构建/测试的 pipeline
- **综合**: 阻塞且静默——arm64 Runner 按文档写法请求后直接 FAILED 无诊断，所有 ARM 架构 CI 场景受阻且用户无法自助排查
- **是否有规避手段**: 否 — 文档中 arm64 是唯一非 x64 的 CPU 架构选项，无替代方案

**建议**:
- 优先确认 GitCode 官方资源池是否实际部署了 arm64 Runner 节点：若未部署，需从文档中移除 arm64 标签声明（或标注"即将支持"）；若已部署，需修复 Runner 调度匹配逻辑，使 `runs-on: [ubuntu-latest, arm64, small]` 能正确分配到 arm64 节点
- arm64 job 失败时应有明确错误消息（如 `##[error] No runner matching labels [ubuntu-latest, arm64, small] is available`），而非静默 FAILED
- 相关用例: 所有声明 `runs-on` 含 arm64 标签的用例均受影响
