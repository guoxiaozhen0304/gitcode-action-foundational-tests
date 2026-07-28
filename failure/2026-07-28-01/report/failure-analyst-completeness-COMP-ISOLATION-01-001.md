## 失败分诊 · COMP-ISOLATION-01-001 · 同一 workflow 先后 job 的文件系统相互隔离

**判定结果**: FAIL
**失败断言**:
- assertions[0] (positive, run_status) — 期望 COMPLETED，实际 FAILED
- assertions[2] (positive, run_logs) — 期望 log contains 'file not found as expected'，实际 absent
- assertions[3] (positive, run_logs) — 期望 log contains 'PAYLOAD=shared payload'，实际 absent
- assertions[4] (positive, run_logs) — 期望 log contains 'artifact_read_ok'，实际 absent
- assertions[1] (negative, run_logs, leak) — 期望 plaintext 'secret data' 0 hits，实际 0 hits（PASS）

**根因初判**: 环境问题

**责任人**: Phase 02 — 测试执行环境 bug（artifact 名称冲突，前次运行残留未清理）

**证据**:

- **Job 日志关键行**（共 28 行，以下为失败直接证据）:
  ```
  [Twirp] error trace-id: 0d247fc2cb7d9956a16c0f14fab5f833  (行 24)
  ::error::Upload artifact failed: Artifact with name already exists: shared-file, repoId=10431319, workflowId=90a05f99cac34afa9945264b4f501210  (行 26)
  ```
  job1 (Write file) 上传制品时因名称冲突失败，日志第 26 行明确指出 `Artifact with name already exists`。

- **预期行为**（用例 YAML COMP-ISOLATION-01-001，P0，维度 completeness）:
  - job1：创建文件 + 上传制品 `shared-file`
  - job2：尝试读取 `/tmp/isolation_test.txt`，预期 `file not found as expected`（文件系统隔离成立）
  - job3：下载制品 `shared-file`，预期输出 `PAYLOAD=shared payload` 和 `artifact_read_ok`
  - 整体预期 run_status success

- **实际行为**:
  - job1 制品上传失败（名称冲突），job1 整体 FAILED
  - 失败传导链: job1 FAILED → job2/job3 因 `needs: job1` 依赖跳过或无法正常执行 → 整个 workflow FAILED
  - 被阻断的功能：job2 的文件隔离验证、job3 的制品下载验证均未被测试到

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/upload-download-artifacts.md`:
  - 第 30-34 行给出 `upload-artifact` 用法示例，测试 YAML 的 job1 写法（`uses: upload-artifact` + `with: name: shared-file`）与文档一致
  - 制品上传本身是平台支持的功能，失败原因明确为**名称冲突**（`Artifact with name already exists`），这正是文档中未专门强调但与运行环境直接相关的清理问题

**置信度**: 高（日志证据直接，错误信息明确指向 artifact 名称冲突）

**影响**:
- **阻塞性**: 🔴阻塞 — job1 制品上传失败导致整个 workflow 无法完成，job2/job3 的验证点（文件隔离、制品下载）均未被执行
- **静默性**: 🟡可察觉 — 平台输出了 `::error::` 明确报错，用户可定位到是制品名称冲突
- **影响面**: 🟢单用例 — 仅影响本测试用例，是环境残留而非平台系统性缺陷
- **综合**: 阻塞但可察觉，artifact 名称冲突阻断 workflow，但错误信息明确
- **是否有规避手段**: 是 — 每次运行前清理前次 artifacts，或使用唯一化名称（如加时间戳后缀）

**建议**:
- Phase 02 harness 应在每次触发测试前确保 artifact 命名空间干净（例如使用 `run_id` 作为 artifact name 后缀以避免跨 run 冲突）
- 若制品残留清理是 Phase 02 harness 的已知能力缺口，应将本用例从环境问题改录为 harness 缺陷
