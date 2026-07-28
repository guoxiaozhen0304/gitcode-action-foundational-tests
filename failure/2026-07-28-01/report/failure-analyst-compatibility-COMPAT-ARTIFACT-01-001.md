## 失败分诊 · COMPAT-ARTIFACT-01-001 · upload/download-artifact 跨 job 传递等价性

**判定结果**: FAIL
**失败断言**: assertions[0] (positive, run_status) — 期望 completed_success，实际 FAILED

**根因初判**: 环境问题

**责任人**: Phase 02 — 测试执行环境 artifact 命名空间未跨运行隔离，前次运行的制品残留导致名称冲突

**证据**:

- **Job 日志全量**（27 行，仅 Upload 步骤执行，Download 步骤因上游失败跳过一次未执行）:
  ```
  === Upload artifact job ===
  [2026/07/28 13:00:57] [INFO] Job(1531647652804444160...) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: .../ed9216d6.sh
  ::debug::Executing: bash -e .../ed9216d6.sh
  ::debug::Using workspace directory: .../ComputingActionTest/gitcode-test-0
  Uploading artifact "cross-job-artifact" from paths: .../artifacts/marker.txt
  Found 1 file(s) to upload
  Creating zip archive from 1 file(s)...
  Zip archive created: /tmp/artifact-1785214871200-8dd8efa6.zip (~0 MB, 164 bytes)
  Creating artifact "cross-job-artifact" (size: 164 bytes, workflow: 4456b1d39f48433fb6ff4a5a5f1166db)...
  [Twirp] trace-id: 084de8b973d3bcc93dd74147580ca388
  [Twirp] error trace-id: 084de8b973d3bcc93dd74147580ca388
  ::debug::Temp zip file removed: /tmp/artifact-1785214871200-8dd8efa6.zip
  ::error::Upload artifact failed: Artifact with name already exists: cross-job-artifact, repoId=10431319, workflowId=4456b1d39f48433fb6ff4a5a5f1166db
  ```
  Upload 步骤创建了 zip（164 bytes）后，在向平台存储写入制品时被拒绝——名称 "cross-job-artifact" 已存在。Upload job FAILED → 下游 Download job（`needs: job-upload`）被 IGNORED，整个跨 job 传递链路从未真正执行。

- **预期行为**（Phase 01 文本用例 COMPAT-ARTIFACT-01-001，P1，兼容性）:
  - 操作步骤 1: job A 中使用 `uses: upload-artifact` 上传标记文件
  - 操作步骤 2: job B 中使用 `uses: download-artifact` 下载同一文件
  - 操作步骤 3: 验证 job B 能正确读取到 job A 上传的文件内容
  - 预期结果: upload-artifact 成功上传、download-artifact 成功下载、文件内容跨 job 一致、裸插件名写法等价
  - 验证点: [正向] upload-artifact 步骤成功；[正向] download-artifact 步骤成功

- **实际行为**:
  - upload-artifact 步骤执行并在前端完成打包，但在平台存储写入时被名称冲突拒绝
  - 失败传导链: Upload artifact job FAILED → Download and verify artifact job IGNORED（下游跨 job 传递功能未被测试到）
  - 跨 job artifact 传递整个路径因环境状态污染从未真正执行

- **对照 GitCode 规格** `phase01/inputs/gitcode-spec/writing-pipelines/upload-download-artifacts.md`:
  - 第 60-63 行（配置说明表格）：文档规定 `name` 参数为制品名称，"同一 workflow 中唯一"——仅承诺同一 workflow 内部唯一性，未声明跨运行隔离。
  - 第 13-45 行（快速示例）：文档给出完整跨 job 上传/下载示例，证明 `upload-artifact` + `download-artifact` 跨 job 传递是平台正式功能，写法（裸插件名 + `with: name/path`）为平台官方推荐。

**置信度**: 高（日志直接显示 name conflict 错误，spec 行为与用例写法完全对应，环境残留可复现）

**影响**:
- **阻塞性**: 🟡 非阻塞 — 制品名称冲突阻止了本次测试的跨 job 传递，但若前次制品被清理或用唯一名称可规避
- **静默性**: 🟡 可察觉 — 平台明确报错 "already exists"，用户能注意到失败
- **影响面**: 🟢 单用例 — 仅影响固定名称跨运行复用的特定场景；平台是否应自动隔离或清理制品属规范层面
- **综合**: 非阻塞可察觉的环境问题——artifact 名称跨运行冲突导致本次跨 job 传递测试无法执行，但平台给出了明确错误信息
- **是否有规避手段**: 是——每次测试使用唯一制品名称（如附加 run_id 后缀），或测试前清理旧制品

**建议**:
- 测试执行前增加 artifact 清理步骤，或制品名称引入 `${run_id}` 后缀以确保每次运行使用唯一名称
- 品质问题：平台文档仅承诺 "同一 workflow 中唯一" 但实现强制 repo 级唯一，可能是文档描述不足，需 ta 确认是否为预期行为
- 相关用例: COMPAT-ARTIFACT 系列所有用例（若均使用固定制品名称）
