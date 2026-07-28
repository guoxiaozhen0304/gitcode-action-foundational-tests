## 失败分诊 · SEC-SUPPLY-01-002 · commit hash 不匹配时第三方 Action 应被拒绝执行

**判定结果**: FAIL

**失败断言**:
- assertions[0] (negative, run_logs, leak): 期望 `plaintext 'success' 0 hits`，实际 `0` — **通过**（平台确实未让 action 成功执行）
- assertions[1] (positive, run_logs, value): 期望 `log contains 'action_not_found_or_sha_mismatch'`，实际 `absent`

**根因初判**: 产品缺陷

**责任人**: 平台方 — 平台正确拒绝了无效 SHA 引用（run_status=FAILED，符合负向断言），但未在日志中给出任何可诊断的错误信息（静默失败），用户无法知晓失败原因

**证据**:

- **Job 日志全量**（仅 1 行，无任何 step 执行或错误消息）:
  ```
  [2026/07/28 12:46:36.243 GMT+08:00] [INFO] Job(1531644039122522112_1531644039097356295) duration check: true
  ```
  无 `No shell specified`、无 `::debug::Script file created`、无任何错误文本——即**平台在 action 解析阶段拒绝了引用，但未输出任何诊断**

- **预期行为**（Phase 01 文本用例 SEC-SUPPLY-01-002，P0，安全性，母意图 SEC-SUPPLY-01-001）:
  - 操作步骤 1: "提交一个 workflow，使用一个不存在的 commit SHA 引用 Action"
  - 操作步骤 2: "触发 workflow"
  - 预期结果: "job 进入失败状态或明确拒绝执行"、"系统不应静默回退到分支 HEAD"
  - 验证点: "[负向] 错误 commit SHA 绝不应执行 Action"、"[正向] 返回明确的 Action 未找到或 SHA 不匹配错误"

- **实际行为**:
  - 平台正确拒绝了 action（run_status=FAILED，log 中未出现 "success"）→ 满足负向验证（assertions[0] 通过）
  - 但平台**完全未给出任何错误信息**——日志中无 "action not found"、无 "sha mismatch"、无 "invalid reference"、无任何说明失败原因的文本
  - 用户面对一个 FAILED job + 空白日志，无法判断是 action 引用问题、runner 问题还是其他原因
  - **静默失败**：平台行为正确（拒绝），但错误报告完全缺失

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/using-actions.md`:
  - 第 93-100 行：文档列出四种引用方式（Tag / 完整版本 / 分支 / SHA），均标注为可用
  - 第 97 行：`@v4`（Tag）标注为"推荐"；第 98 行：`@v4.1.0`（完整版本）标注为"安全性最高"
  - 第 100 行：`@a1b2c3d`（SHA）标注为"生产环境推荐"
  - **文档未说明无效引用时平台的行为**——是否会报错、报什么错、错误文本格式等——这是文档缺口
  - 测试 YAML 中 `uses: docker/build-push-action@0000000000000000000000000000000000000000`（全零 SHA）的写法与文档 `@SHA` 模式对应，且全零 SHA 在语义上明确无效

- **与 SEC-SUPPLY-01-001 的关联**:
  - SEC-SUPPLY-01-001 使用非零模拟 SHA，SEC-SUPPLY-01-002 使用全零 SHA——两用例均产生完全相同的 1 行空日志
  - 两者的共性：**平台在 action 解析失败时不产生任何诊断日志**——无论是"无法解析 SHA"还是"SHA 不存在"，用户都看不到任何信息
  - 这表明错误报告机制本身（而非特定 SHA 解析逻辑）存在产品缺陷

**置信度**: 高（日志直接证据：1 行，零错误消息；行为正确（拒绝）但报告缺失；两起 SUPPLY 用例表现一致）

**影响**:
- **阻塞性**: 🟡非阻塞 — 平台行为正确（拒绝了无效引用），不影响正确 action 引用的 workflow
- **静默性**: 🔴静默错误 — job FAILED 但用户**完全无法从日志中判断原因**，必须盲猜或联系平台支持
- **影响面**: 🟡同维度 — 任何 action 引用解析失败（SHA 错误、tag 不存在、owner/repo 拼错等）均可能遇到同样的静默失败
- **综合**: 非阻塞但静默——行为层面无安全风险（无效引用被正确阻止），但用户体验严重受损：面对 FAILED job + 空白日志，调试成本极高
- **是否有规避手段**: 否——用户无法从日志中获取任何诊断信息，无法自行排查

**建议**:
- **平台方必须在 action 引用解析失败时输出可诊断的错误信息**，至少包含：失败的 action 引用字符串、失败原因（如 "SHA not found" / "invalid reference format"）
- 参照 GitHub Actions 的错误报告模式：`Unable to resolve action 'docker/build-push-action@0000...', repository not found or SHA does not exist`
- 文档补充说明无效引用场景下平台的错误行为格式
- 相关用例: SEC-SUPPLY-01-001（SHA 引用支持）、COMP-ACT-01-001/002（未知 action 引用）
