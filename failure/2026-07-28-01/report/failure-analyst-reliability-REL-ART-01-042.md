## 失败分诊 · REL-ART-01-042 · artifact 大小上限探测——2GB 上传应完整成功（MD5 一致）或上传阶段明确拒绝

**判定结果**: FAIL
**失败断言**: assertions[0] (value, positive, run_logs) — 期望 log contains 'md5_match=true_if_upload_success'，实际 absent

**根因初判**: 编译缺口 / 产品缺陷（平台做对了、编译器没接住）

**责任人**: Phase 01 — 合约编译器未支持条件性断言值（`equals: "true_if_upload_success"` 被编译为简单日志搜索，丢失了"仅在上传成功时"的条件语义）; 协同平台方（artifact 上限 2 GiB 未在任何文档中公开声明）

**证据**:

- **Job 日志摘录**（32 行，关键段）:
  ```
  第 5-7 行 (generate): 2048+0 records in / 2048+0 records out / 2147483648 bytes (2.1 GB) copied
  第 10 行 (upload): Uploading artifact "big-artifact-2gb" from paths: .../big-artifact.bin
  第 25-26 行 (zip): Zip archive creation still in progress... Zip archive created: ... (~2049 MB, 2148138864 bytes)
  第 27 行 (create): Creating artifact "big-artifact-2gb" (size: 2148138864 bytes)...
  第 29 行: [Twirp] error trace-id: dc573a9173b7b56a82700e1b91b544b5
  第 31 行: ::error::Upload artifact failed: Artifact size 2148138864 exceeds max allowed 2147483648, repoId=10431336, workflowId=4f467dbcc61445ec841451184c4ea192, artifactName=big-artifact-2gb
  ```
  - 上传阶段：平台明确拒绝——zip 压缩后制品大小为 2,148,138,864 bytes (~2.0006 GiB)，超过平台上限 2,147,483,648 bytes（精确 2 GiB）。错误信息包含了上限值、repoId、workflowId、artifactName——错误消息清晰完备。
  - 失败传导链：upload job FAILED（artifact 上传被拒）→ download job IGNORED（`needs: upload` 依赖未满足）→ md5 校验未执行 → 日志中不存在 `md5_match=true_if_upload_success` 字符串。

- **预期行为**（Phase 01 文本用例 `phase01/runs/2026-07-27-01/cases/text/REL-ART-01-042.md`，优先级 P2，维度 stability）:
  - 前置条件: "平台 max_artifact_size 未公开（探测型用例）"
  - 操作步骤 3: "若上传被拒，记录错误信息是否含上限值；实测上限回写 platform-config"
  - 预期结果: "上传完整成功且下载 MD5 一致；或上传阶段明确拒绝并给出上限值"
  - 验证点 [正向]: "上传成功 ↔ 下载 MD5 匹配；上传失败 ↔ 上传阶段明确报错"
  - 验证点 [非功能]: "实测 artifact 上限值记录完整"

- **实际行为**:
  - 平台行为完全符合"上传阶段明确拒绝并给出上限值"——错误消息清晰包含 `max allowed 2147483648`。这与测试 YAML 断言 `upload_outcome = "success_or_explicit_rejection_with_limit"` 完全匹配。
  - 问题是 `md5_match` 断言被编译为简单日志内容搜索（`log contains 'md5_match=true_if_upload_success'`），未保留原 YAML 中 `equals: "true_if_upload_success"` 的条件语义——"若上传成功则 MD5 应匹配"（条件性断言）。上传被拒后 MD5 校验从未执行，"日志中没有 md5_match 标记"是自然结果而非平台缺陷。
  - 此外，artifact 上限 2 GiB 在 GitCode 官方文档中未被任何页面声明——测试用例中 `intent_ref: INTENT-REL-078` 的设计意图本就是"探测 + 记录实测上限"，而非断言平台一定支持 2GB。

- **对照 GitCode 规格**:
  - `phase01/inputs/gitcode-spec/writing-pipelines/upload-download-artifacts.md`：全文未声明 artifact 大小上限；第 10 行前提条件仅写"已确认制品大小不超过限制"但未给出限制数值。
  - `phase01/inputs/gitcode-spec/core-concepts/artifacts-and-cache.md`：全文未提及大小上限。
  - 结论：平台行为（2 GiB 限制 + 明确拒绝 + 含上限值的错误消息）与文档**无矛盾**——文档本就没有做出具体大小承诺。平台甚至在错误消息中明确给出了限制数值，属于良好实践。
  - 测试 YAML 断言 `upload_outcome = "success_or_explicit_rejection_with_limit"`：平台行为满足此断言（明确拒绝 + 上限值），但该断言未出现在 assertion_results 中——可能是编译器丢弃了或作为独立断言通过了。

- **编译层面分析**:
  - 原 YAML 断言 `md5_match` 的 equals 值为 `"true_if_upload_success"`——这是一个条件性质的值（"如果上传成功，则为 true"），而非直接搜索目标。
  - 编译器将此编译为 `kind: value, target: run_logs, expected: "log contains 'md5_match=true_if_upload_success'"`——退化为了简单日志 grep。
  - 条件语义丢失导致：上传被拒时 MD5 校验未执行 → 日志无该字符串 → 断言误判为 FAIL。
  - 若编译器保留了条件语义，此断言在上传失败时应评估为"不适用/跳过"，或自动满足（vacuous truth）。

**置信度**: 高（日志证据直接——平台给出了明确的 "exceeds max allowed 2147483648" 错误，这是正确的"明确拒绝"行为；编译结果 JSON 中断言 kind 变为简单的 value/log search，与 YAML 原始条件语义不一致）

**影响**:
- **阻塞性**: ⚪无影响 — 平台行为正确（明确拒绝并给出上限），该 FAIL 是因编译器未处理条件断言导致的假阳性
- **静默性**: 🟢明确报错 — 平台拒绝上传时给出了清晰错误消息，含上限值、repoId、workflowId，用户可立即理解原因
- **影响面**: 🟢单用例 — 仅影响本探测用例的判定结果，不影响平台实际功能；实际 artifact 上限（2 GiB）已在本次探测中成功记录
- **综合**: 无实质性平台缺陷——上传阶段明确拒绝 2GB+ artifact 并给出上限值，行为符合文档（文档未承诺具体上限）；FAIL 来源于编译器将条件断言编译为简单日志搜索
- **是否有规避手段**: 是 — 可在 Phase 01 侧修复编译器以支持条件断言值（如 `true_if_upload_success` 模式）；本次探测的实测上限值（2 GiB = 2,147,483,648 bytes）可回写至 platform-config

**建议**:
- Phase 01 编译器需支持条件性断言值——当 equals 值为 `X_if_CONDITION` 模式时，不应编译为简单日志搜索，而应先评估条件再决定断言预期
- 实测 artifact 上限（2 GiB precision）已记录：`max allowed 2147483648 bytes`，可用于回写 `platform-config/instance-config.md`
- 平台方建议：将 artifact 上限值写入文档（`upload-download-artifacts.md` 或 `artifacts-and-cache.md`），避免用户盲测。当前 2 GiB 对于大多数构建产物是充足的，但未在文档中声明会造成用户困惑
- 相关用例: 无——本用例为探测型，同类条件断言编译问题可能影响其他含条件性预期的用例
