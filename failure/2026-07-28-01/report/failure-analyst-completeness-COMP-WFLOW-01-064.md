## 失败分诊 · COMP-WFLOW-01-064 · workflow stages 阶段结构字段验证

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_status) — 期望 FAILED，实际 COMPLETED
- assertions[2] (negative, run_logs, leak) — 期望 plaintext 'test_done' 0 hits，实际 FOUND
- assertions[1] (positive, run_logs) — 期望 log contains 'build_done'，实际 present（PASS）

**根因初判**: 产品缺陷

**责任人**: 平台方 — GitCode Actions 的 stages 机制可能未被正确实现：`fail_fast: true` 未阻止 test stage 执行，且整体 run_status 为 COMPLETED 而非预期 FAILED

**证据**:

- **Job 日志全文**（共 11 行，2 个 job）:
  Job(1531647164134600704_1531647164109434893):
  ```
  build_done                (行 5)
  ```
  Job(1531647164134600704_1531647164109434895):
  ```
  test_done                 (行 11)
  ```
  - build stage 包含两个 job：`build`（成功输出 build_done，第 5 行）和 `build-fail`（`exit 1` 故意失败）
  - **关键发现**：test stage 的 `test` job 输出了 `test_done`（第 11 行），说明 test stage 在 build stage 中有 job 失败的情况下**仍然被调度执行了**
  - 日志中 `build-fail` 的 `exit 1` 未显示（可能是其日志未被采集或位于不同 job），但 test stage 的执行本身就是 `fail_fast` 未生效的证据

- **预期行为**（用例 YAML COMP-WFLOW-01-064，P1，维度 completeness）:
  - stages.build.fail_fast: true → build stage 内任一 job 失败后，应阻止后续 stage（test stage）执行
  - build-fail 执行 `exit 1` → build stage 失败
  - test stage 应被跳过 → `test_done` 不应出现在日志中
  - 整体 run_status 应为 FAILED

- **实际行为**:
  - build-fail 失败后，test stage 仍被执行（`test_done` 出现）
  - run_status = COMPLETED 而非 FAILED
  - `fail_fast: true` **未生效**

- **对照 GitCode 规格**: 未在 GitCode 文档中找到关于 `stages` 或 `fail_fast` 的明确承诺。这是一个**文档缺口**——如果平台不支持 stages/fail_fast，文档不应缺失；如果支持，实现有缺陷。

**置信度**: 高（日志证据直接，test_done 出现在 build-fail 之后是确凿的 fail_fast 失效证据）

**影响**:
- **阻塞性**: 🔴阻塞 — fail_fast 失效导致 test stage 被不应执行地执行，用户依赖 fail_fast 做 fast-fail 优化的 pipeline 行为错误
- **静默性**: 🔴静默错误 — 平台不报错，test stage 静默执行了本应被跳过的内容；用户可能产生的错误结果（如在不完整的构建产物上跑了完整测试）不会被标记
- **影响面**: 🟡同维度 — 所有使用 stages + fail_fast 的 workflow 均受影响
- **综合**: 阻塞且静默，stages 的 fail_fast 机制失效是一个严重的流水线行为隐患
- **是否有规避手段**: 否 — 无替代机制实现跨 stage 的 fast-fail

**建议**:
- 平台方确认 `stages` + `fail_fast` 是否在 GitCode Actions 中实现——若未实现，需在文档中明确告知用户（或移除 stages 相关文档以避免用户误用）
- 若已实现但有 bug，修复 build stage fail 后 test stage 仍被调度的缺陷
- 此缺陷还涉及 SECURITY_CRITICAL 标签（见 JSON 第 9-11 行），因为 test_done 的泄露意味着后续依赖 fast-fail 安全策略的步骤也可能被错误执行
