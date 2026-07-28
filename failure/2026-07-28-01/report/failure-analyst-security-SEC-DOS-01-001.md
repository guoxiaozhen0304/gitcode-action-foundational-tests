## 失败分诊 · SEC-DOS-01-001 · 大 artifact / 大 cache 必须受配额与边界限制

**判定结果**: FAIL

**失败断言**:
- assertions[0] (negative, run_logs, leak, SECURITY_CRITICAL): 期望 `plaintext 'success' 0 hits`，实际 `FOUND`
- assertions[1] (positive, job_status): 期望 `job_status == FAILED`，实际 `Test size quota=COMPLETED`

**根因初判**: 用例问题

**责任人**: Phase 01 — 用例设计未考虑 artifact ZIP 压缩效应；使用全零文件导致 1.1GB 压缩后仅 ~1MB，未达平台任何可能存在的配额边界。另伴生：compile_asserts 将 `target: run_status must_not_equal: success` 编译为 `kind: leak, target: run_logs`（词法转换偏误），但非本 FAIL 主因。

**证据**:

- **Job 日志全量**（39 行，真实执行）:
  ```
  [2026/07/28 12:44:23.684] [INFO] Job(1531643483049959424_1531643483016404999) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: ...
  ::debug::Executing: bash -e ...
  1100+0 records in
  1100+0 records out
  1153433600 bytes (1.2 GB, 1.1 GiB) copied, 0.679354 s, 1.7 GB/s          ← 1.1GB 文件创建成功
  ...
  Uploading artifact "large-artifact" from paths: .../large.bin
  ...
  Zip archive created: ... (~1 MB, 1121217 bytes)                           ← 压缩后仅 ~1MB
  ...
  Artifact "large-artifact" uploaded successfully. ID: 207719914180608      ← 上传成功，未拒收
  ```

- **预期行为**（Phase 01 文本用例 SEC-DOS-01-001，P0，安全性）:
  - 操作步骤 1: "提交一个 workflow，尝试上传超大 artifact 或写入超大 cache"
  - 操作步骤 2: "触发 workflow 并查看上传结果"
  - 预期结果: "超过大小上限的 artifact/cache 上传绝不应成功写入（运行状态绝不应为 success）"
  - 验证点: "[负向] 超过大小上限的 artifact/cache 上传绝不应成功写入（run 状态绝不应为 success）"

- **实际行为**:
  - 1.1GB 全零文件经 ZIP 压缩后仅 ~1MB（1,121,217 bytes），平台正常完成上传，run_status=COMPLETED，job_status=COMPLETED
  - 用例设计假设 `dd if=/dev/zero bs=1M count=1100` 会生成一个"超大 artifact"，但忘掉了 artifact 上传流程自带 ZIP 压缩——全零数据压缩比极高（~1000:1），实际传输的 artifact 远低于任何合理配额
  - **本用例被测功能（artifact 大小配额）实际上未被测试到**——因为生成的 artifact 太小

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/upload-download-artifacts.md`:
  - 第 10 行前提条件明确：`已确认制品大小不超过限制`——文档承认存在大小限制
  - 但文档未给出具体限制值（多少 MB/GB），用户无法确认是否合规 → **文档缺口**
  - 测试 YAML 中的 `uses: upload-artifact` + `with: name/path` 写法与规格第 52-58 行示例完全对应

- **compile_asserts 偏误**（辅助发现，非主因）:
  - YAML 断言 `type: negative, target: run_status, must_not_equal: "success"` 被编译为 `kind: leak, target: run_logs, expected: plaintext 'success' 0 hits`
  - `target: run_status` → `kind: leak, target: run_logs` 的词法转换不精确——在日志中查找单词"success"不能可靠推断 run_status
  - assertions[1]（`target: job_status, equals: "failure"`）编译正确（`kind: job_status`），且独立验证了平台行为

**置信度**: 高（日志直接证据：ZIP 压缩行 "~1 MB, 1121217 bytes" + 上传成功行；全零文件压缩效应是确定性行为）

**影响**:
- **阻塞性**: ⚪无影响 — 用例设计问题，平台行为正常（接受了 ~1MB artifact）
- **静默性**: ⚪无影响 — 平台如实报告了上传成功
- **影响面**: 🟢单用例 — 仅影响本测试场景，artifact 配额功能本身未被有效测试
- **综合**: 无影响但测试无效——全零文件压缩效应导致 artifact 配额功能未被实际测试到；用例需改用不可压缩数据（如 `dd if=/dev/urandom` 或 `openssl rand`）
- **是否有规避手段**: 是——修改测试 YAML 使用随机数据源替代 `/dev/zero`，确保压缩后仍超过配额边界

**建议**:
- 修改用例生成逻辑：用 `/dev/urandom` 或 `openssl rand` 代替 `/dev/zero`，避免 ZIP 压缩效应掩盖配额检测
- 补充生成 2+ 个不同大小的文件（跨过已知/推测的配额线），确保至少有一条真正触达边界
- 向平台方索取 artifact 具体大小限制值并补充进 GitCode 规格文档
- 相关用例: 所有依赖 artifact 大小配额检测的安全/可靠性用例
