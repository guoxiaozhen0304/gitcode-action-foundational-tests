## 失败分诊 · SEC-RUN-01-003 · 自托管 Runner 跨项目残留必须被隔离

**判定结果**: FAIL

**失败断言**:
- assertions[0] (negative, run_logs, leak): 期望 `plaintext 'cross project leak' 0 hits`，实际 `0` — **通过**（但为空洞通过，见下文）
- assertions[1] (positive, run_logs, value): 期望 `log contains 'isolated as expected'`，实际 `absent`

**根因初判**: 环境问题

**责任人**: Phase 02 — 自托管 runner（`runs-on: [self-hosted, x64, large]`）不可用或未连接，导致两 job 均未执行任何 step，日志仅含调度检查信息

**证据**:

- **Job 日志全量**（仅 3 行，无任何 step 执行痕迹）:
  ```
  [2026/07/28 12:45:26.667 GMT+08:00] [INFO] Job(1531643747278528512_1531643747244974087) duration check: true

  [2026/07/28 12:45:26.678 GMT+08:00] [INFO] Job(1531643747278528512_1531643747244974089) duration check: true
  ```
  两 job（project-a / project-b）均仅输出 `duration check: true`，无 `No shell specified`、无 `::debug::Script file created`、无 `::debug::Executing: bash`——即**无任何 step 被调度执行**。duration 仅 46 秒，与正常 job 执行时长不匹配。

- **预期行为**（Phase 01 文本用例 SEC-RUN-01-003，P0，安全性）:
  - 操作步骤 1: "项目 A 的 workflow 写入临时文件和环境变量"
  - 操作步骤 2: "项目 B 的 workflow 在同一 runner 上检查残留"
  - 前置条件: "自托管 runner 被多个项目共享"
  - 预期结果: "项目 B 的 job 绝不应读取到项目 A 残留的敏感文件或环境变量"
  - 验证点: "[正向] 项目 B 的 job 日志包含 isolated as expected"

- **实际行为**:
  - 两 job 均未执行任何 step（零 shell 输出、零 step 创建痕迹）
  - run_status=FAILED，大概率因 runner 不可达或标签不匹配导致 job 调度失败
  - assertions[0]（"cross project leak" 漏检）通过是空洞的——因为没有日志可供检查，并非证明了隔离存在
  - **本用例的被测功能（跨项目隔离）实际上未被测试到**——runner 不可用导致所有 step 未执行

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/runner-management/using-self-hosted-runners.md`:
  - 第 86-95 行：`runs-on: [self-hosted, euler, x64, gpu]` 示例，标签必须完全匹配
  - 第 106 行：`runs-on 中列出的所有标签必须同时存在于 Runner 的标签集合中，才视为匹配成功`
  - 第 80-82 行：Runner 状态验证——脚本执行后返回页面确认 Runner 状态为**在线**（绿色），离线则检查网络
  - 测试 YAML 中 `runs-on: [self-hosted, x64, large]` 的标签组合符合规格约定，但无可用 runner 匹配

- **环境前置条件验证**:
  - 测试 YAML 使用 `repo_fixture: self-hosted-shared`，期望 harness 提供已注册的共享自托管 runner
  - 日志中无 `config_probe` 步骤确认 runner 已就绪
  - 无任何 step 执行痕迹 → 判定 runner 不可用或标签 [self-hosted, x64, large] 无匹配（`large` 规格需申请，不是默认可用）

**置信度**: 高（日志仅 3 行，零 step 输出是环境不可用的直接证据；duration 46s 远低于正常 job 执行时间）

**影响**:
- **阻塞性**: ⚪无影响 — 不是平台缺陷，是测试环境前置条件未满足
- **静默性**: 🟡可察觉 — run_status=FAILED 可被注意到，但原因不明确
- **影响面**: 🟢单用例 — 仅影响依赖此 runner 标签组合的测试
- **综合**: 无平台影响——环境问题（自托管 runner 不可用），被测隔离功能未实际执行；需 Phase 02 确认 `[self-hosted, x64, large]` runner 是否已注册并在线
- **是否有规避手段**: 是——确认自托管 runner 在线后重跑；或改用托管 runner 标签组合（如 `[ubuntu-latest, x64, small]`）并调整测试逻辑（单 job 内验证而非跨 job）

**建议**:
- Phase 02 确认 `repo_fixture: self-hosted-shared` 对应的 runner 是否已在平台注册且状态为在线
- 若 `large` 规格的自托管 runner 不可用，考虑降级为 `small`/`medium` 或使用 Kubernetes Runner 替代
- 测试 YAML 缺少 `config_probe` 步骤验证 runner 可用性——建议在所有依赖自托管 runner 的用例中加入 runner 可达性检查
- 相关用例: 所有使用 `runs-on: [self-hosted, ...]` 的用例
